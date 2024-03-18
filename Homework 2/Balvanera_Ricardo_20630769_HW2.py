import csv

class Car:
    def __init__(self, vin, car_type, brand, model, year, mileage, price, color, feature):
        self.vin = vin
        self.car_type = car_type
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.color = color
        self.feature = feature

    def display(self):
        print(f"{self.vin} {self.car_type} {self.brand} {self.model} {self.year} {self.mileage} {self.price} {self.color} {self.feature}")


class User:
    def __init__(self, user_id, password, first_name, last_name, email):
        self.user_id = user_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def display(self):
        print(f"{self.user_id} {self.first_name} {self.last_name} {self.email}")

# Subclasses for different types of users
class Customer(User):
    def __init__(self, user_id, password, first_name, last_name, email, cart=None):
        super().__init__(user_id, password, first_name, last_name, email)
        self.cart = cart if cart else []

    def display(self):
        super().display()
        print("Cart:", ', '.join(self.cart))

class Employee(User):
    def __init__(self, user_id, password, first_name, last_name, email, position):
        super().__init__(user_id, password, first_name, last_name, email)
        self.position = position

    def display(self):
        super().display()
        print("Position:", self.position)

class Inventory:
    def __init__(self):
        self.cars = []

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split()  # Split data by spaces
                if data:
                    vin, car_type, brand, model, year, mileage, price, color, feature = data
                    car = Car(vin, car_type, brand, model, year, mileage, price, color, feature)
                    self.cars.append(car)

    def display(self):
        print("VIN Type Brand Model Year Mileage Price Color Feature")
        for car in self.cars:
            car.display()

    def sort_inventory(self, key):
        self.cars.sort(key=lambda x: getattr(x, key))

    def add_car(self, car):
        self.cars.append(car)

    def delete_car(self, vin):
        self.cars = [car for car in self.cars if car.vin != vin]

    def update_car(self, vin, key, value):
        for car in self.cars:
            if car.vin == vin:
                setattr(car, key, value)
class Members:
    def __init__(self):
        self.users = []

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split()  # Split data by spaces
                if data and len(data) == 6:  # Ensure correct number of fields
                    user_id, password, first_name, last_name, email, position = data
                    user = Employee(user_id, password, first_name, last_name, email, position)
                    self.users.append(user)


    def display(self):
        print("ID F_Name L_Name Email Password Cart" if isinstance(self.users[0], Customer) else "ID F_Name L_Name Email Position")
        for user in self.users:
            user.display()

    def authenticate(self, user_id, password):
        for user in self.users:
            if user.user_id == user_id and user.password == password:
                return user
        return None

# Main application class
class Main:
    def __init__(self):
        self.inventory = Inventory()
        self.members = Members()
        self.inventory.load_from_file("inventory.txt")
        self.members.load_from_file("users.txt")
        self.current_user = None

    def start(self):
        while True:
            print("Welcome to Carmax in Mission, Texas!")
            print("1. Log in")
            print("2. Sign up")
            print("3. Exit")
            choice = input("Please input your choice: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.signup()
            elif choice == "3":
                self.close()
                break
            else:
                print("Invalid choice. Please try again.")

    def login(self):
        user_id = input("Please input your user id: ")
        password = input("Please input password: ")
        user = self.members.authenticate(user_id, password)
        if user:
            self.current_user = user
            print(f"Welcome, {user.first_name} {user.last_name}!")
            if isinstance(user, Customer):
                self.customer_menu()
            else:
                self.employee_menu()
        else:
            print("Invalid user id or password.")

    def signup(self):
        print("Sign up as:")
        print("1. Employee")
        print("2. Customer")
        choice = input("Enter your choice: ")

        user_id = input("Please input user id: ")
        password = input("Please input password: ")
        first_name = input("Please input your first name: ")
        last_name = input("Please input your last name: ")
        email = input("Please input your email: ")

        if choice == "1":
            manager_code = input("Enter the manager code: ")
            if manager_code != "1234":
                print("Invalid manager code. Sign up failed.")
                return
            position = input("Please input your position: ")
            new_user = Employee(user_id, password, first_name, last_name, email, position)
        elif choice == "2":
            new_user = Customer(user_id, password, first_name, last_name, email)
        else:
            print("Invalid choice.")
            return

        self.members.users.append(new_user)
        print("Thank you for your sign up!")

    def customer_menu(self):
        while True:
            print("1. Display Inventory")
            print("2. Sort Inventory")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Empty Cart")
            print("6. Log out")
            choice = input("Please input your choice: ")

            if choice == "1":
                self.inventory.display()
            elif choice == "2":
                self.sort_inventory()
            elif choice == "3":
                self.add_to_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.empty_cart()
            elif choice == "6":
                print("Bye!")
                break
            else:
                print("Invalid choice.")

    def sort_inventory(self):
        print("1. Sort by VIN")
        print("2. Sort by Type")
        print("3. Sort by Brand")
        print("4. Sort by Model")
        print("5. Sort by Year")
        print("6. Sort by Mileage")
        print("7. Sort by Price")
        print("8. Sort by Color")
        print("9. Sort by Feature")
        choice = input("Please input your choice: ")
        keys = ['vin', 'car_type', 'brand', 'model', 'year', 'mileage', 'price', 'color', 'feature']
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            key = keys[int(choice) - 1]
            self.inventory.sort_inventory(key)
            self.inventory.display()
        else:
            print("Invalid choice.")

    def add_to_cart(self):
        vin = input("Please input a VIN: ")
        car = next((car for car in self.inventory.cars if car.vin == vin), None)
        if car:
            self.current_user.cart.append(car.vin)
            print(f"Successfully {car.brand} {car.model} has been added to your cart!")
        else:
            print("Invalid VIN.")

    def view_cart(self):
        print("VIN Type Brand Model Year Mileage Price Color Feature")
        for vin in self.current_user.cart:
            car = next((car for car in self.inventory.cars if car.vin == vin), None)
            if car:
                car.display()

    def empty_cart(self):
        self.current_user.cart = []
        print("Your cart is empty.")

    def employee_menu(self):
        while True:
            print("1. Display Inventory")
            print("2. Add Car")
            print("3. Delete Car")
            print("4. Update Car")
            print("5. Display Customers")
            print("6. Display Employees")
            print("7. Logout")
            choice = input("Please input: ")

            if choice == "1":
                self.inventory.display()
            elif choice == "2":
                self.add_car()
            elif choice == "3":
                self.delete_car()
            elif choice == "4":
                self.update_car()
            elif choice == "5":
                self.members.display()
            elif choice == "6":
                self.members.display()
            elif choice == "7":
                print("Bye!")
                break
            else:
                print("Invalid choice.")

    def add_car(self):
        vin = input("VIN: ")
        car_type = input("Type: ")
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Year: ")
        mileage = input("Mileage: ")
        price = input("Price: ")
        color = input("Color: ")
        feature = input("Feature: ")
        new_car = Car(vin, car_type, brand, model, year, mileage, price, color, feature)
        self.inventory.add_car(new_car)
        print(f"Successfully {brand} {model} has been added.")

    def delete_car(self):
        vin = input("Please input VIN to delete: ")
        self.inventory.delete_car(vin)
        print("Successfully this car has been deleted.")

    def update_car(self):
        vin = input("Please input VIN: ")
        print("1. Update brand")
        print("2. Update model")
        print("3. Update year")
        print("4. Update mileage")
        print("5. Update price")
        print("6. Update color")
        print("7. Update feature")
        choice = input("Please select option: ")
        if choice.isdigit() and 1 <= int(choice) <= 7:
            keys = ['brand', 'model', 'year', 'mileage', 'price', 'color', 'feature']
            key = keys[int(choice) - 1]
            value = input(f"Please input {key}: ")
            self.inventory.update_car(vin, key, value)
            print("It has been updated. Thank you.")
        else:
            print("Invalid choice.")

    def close(self):
        with open("inventory.txt", "w") as file:
            writer = csv.writer(file)
            for car in self.inventory.cars:
                writer.writerow([car.vin, car.car_type, car.brand, car.model, car.year, car.mileage, car.price, car.color, car.feature])

        with open("users.txt", "w") as file:
            writer = csv.writer(file)
            for user in self.members.users:
                if isinstance(user, Customer):
                    writer.writerow([user.user_id, user.password, user.first_name, user.last_name, user.email] + user.cart)
                else:
                    writer.writerow([user.user_id, user.password, user.first_name, user.last_name, user.email, user.position])

# Entry point
if __name__ == "__main__":
    app = Main()
    app.start()
