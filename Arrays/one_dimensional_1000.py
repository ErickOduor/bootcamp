# Compose a program that creates a one-dimensional array a containing exactly 1000 integers and then attempt to access a[1000].
# what happens when you run the program?  
# a. 1000  
# b. value of the array at the start  
# c. value of the array at the end  
# d. indexing error

i = 0
while i <= 999:
    a = [i]
    while True:
        try:
            a.append(int(input("Key in integer value: ")))
            i += 1
            break
        except Exception:
            print('Invalid input, not an integer please try again')
            pass







