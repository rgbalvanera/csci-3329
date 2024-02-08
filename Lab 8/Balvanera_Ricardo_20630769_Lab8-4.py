# input message
x, y, z = map(int, input("Enter three integer numbers: ").split())

# find min and max
max_num = x
min_num = x

if y > max_num:
    max_num = y
elif y < min_num:
    min_num = y

if z > max_num:
    max_num = z
elif z < min_num:
    min_num = z

# output messages
print("Maximum is", max_num)
print("Minimum is", min_num)
