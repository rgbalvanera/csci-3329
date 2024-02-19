#define the function to calculate the years for all the civilizations to connect
def years(n, k, civs):
    civilizations = set(civs)
    connected = set()
    years = 0

    while civilizations:
        years += 1
        new_civs = set()
        for civ in civilizations:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_civ = (civ[0] + dx, civ[1] + dy)
                if new_civ in connected:
                    continue
                if new_civ[0] < 0 or new_civ[0] >= n or new_civ[1] < 0 or new_civ[1] >= n:
                    continue
                new_civs.add(new_civ)
                connected.add(new_civ)
        civilizations = new_civs
    return years
#open input and output files
input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
#get the n and k values from the first line of the file
n, k = map(int, input_file.readline().strip().split())
#create a list that will contain the xy coordinates of the civilizations
civilizations = []
#in the next k lines of the file obtain the xy coordinates for each civilization from the file
for i in range(k):
    #append the coordinates to the civilizations list
    civilizations.append(tuple(map(int, input_file.readline().strip().split())))
#call the function that will caculate the years for the civs to connect
total_years = years(n,k,civilizations)
#print the value to the output file
output_file.write(str(total_years) + "\n")
#close the files
input_file.close()
output_file.close()