list =[]
while True:
    print("List of Items")
    items = input("Enter Items: ")
    print("1. Append \t 2.Remove \t 3.Quit")
    choice = input(">")

    if choice == "1":
        list.append(items)
        print("New items:", list)
    elif choice == "2":
        list.remove(items)
        print("Remove items:", list)

    elif choice == "3":
        exit()
    else:
        print("Invalid Input!")



