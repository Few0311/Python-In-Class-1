bar = "="*15
print(f"{bar}\n | Main menu | \n{bar}")
#ใช่ ''' แทน \n 
print(''' 
1. Triangle
2. Triangle
3, Triangle
4. Triagle
5. Exit
''')

choice = input("Enter Choice : ")
match choice :
    case "1":
        print()
        u = int(input("Enter number of character : "))
        print()
        i = 1
        while i <= u:
            print("*"*i)
            i += 1
    case "2":
        print()
        u = int(input("Enter number of character : "))
        print()
        i = 1
        while i <= u:
            print("*"*(u-i+1))
            u -= 1
    case "3":
        print()
        u = int(input("Enter number of character : "))
        print()
        i = 1
        while i <= u:
            print(" " *(u - i)+"*"*i)
            i += 1
