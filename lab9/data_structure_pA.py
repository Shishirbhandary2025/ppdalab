def list_opertions():
    my_list=[]
    while True:
        print("\nLst Orations:")
        print("1.Insert an element")
        print("2.Delete an element")
        print("3.Find an element")
        print("4.Display list")
        print("5.Exit")
        choice=int(input("Enter your choice"))
        if choice == 1:
           element =input("Enter element to inset:")
           my_list.append(element)
           print(f"Element'{element}'inserted.")
        elif choice ==2:
            element = input ("Enter element to delete:")
            if element in my_list:
                my_list.remove(element)
                print(f"Element'{element}'not found.")
            else:
                print(f"element'{element}'not found.")
        elif choice==3:
            element=input("Enter element to find:")
            if element in my_list:
                print(f"Element'{element}'found.")
            else:
                print(f"Element'{element}'not found.")
        elif choice ==4:
            print(f"current list:{my_list}")
        elif choice ==5:
            break
        else:
           print("Invalid choice,please try again.")

list_opertions()
