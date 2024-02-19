#call the function header that will use the algorithm to find the number of infected computers
def total_infected(computers, connections, infected):
#sreate a set to keep track of infected computers
    infected_computers = set()
#initialize a stack with the initially infected computer
    stack = [infected]
#iterate until the stack is empty
    while stack:
#pop a computer from the stack
        current_computer = stack.pop()       
#check if the current computer is not already infected
        if current_computer not in infected_computers:
#mark the current computer as infected
            infected_computers.add(current_computer)           
#if the current computer has connections, add its uninfected neighbors to the stack
            if current_computer in connections:
                for neighbor in connections[current_computer]:
                    if neighbor not in infected_computers:
                        stack.append(neighbor)
#return the total number of infected computers
    return len(infected_computers) - 1

#open both the input and output files 
input_file = open("input.txt", "r")
output_file = open("output.txt", "a")
#get the number of computers from the file 
total_computers = int(input_file.readline().strip())
#get the number of edges from the file
total_edges = int(input_file.readline().strip())
#initialize an empty dictionary to store connections between computers
connections = {}
#use total_edges to get the connections between the two computers
for i in range(total_edges):
    comp1, comp2 = map(int, input_file.readline().strip().split())
    if comp1 in connections:
        connections[comp1].append(comp2)
    else:
        connections[comp1] = [comp2]
    if comp2 in connections:
        connections[comp2].append(comp1)
    else:
        connections[comp2] = [comp1]
#get the number of the infected computer
infected_computer = int(input_file.readline().strip())
#call the function to get the total # of infected computers
x = total_infected(total_computers, connections, infected_computer)
#output the value to the file
output_file.write(str(x)+ "\n")
#close the files
input_file.close()
output_file.close()