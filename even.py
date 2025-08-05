#filtering even numbers from a list:
list = [1, 4, 5, 6 ,7 ,8 ,10 ,11, 14, 112, 1111]
index = 0

while index < len(list):
    if list[index] % 2 == 0:
        print ("The list of even numbers:", list[index])
    index += 1
