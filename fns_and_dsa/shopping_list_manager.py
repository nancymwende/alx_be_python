shopping_list = []

def display_list():
    if shopping_list :
        print("Current list:", shopping_list)
    else:
        print("The list is empty.")

def add_item(item):
    shopping_list.append(item)
    print(f'"{item}" has been added to the list.')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from the list.')
    else:
        print(f'"{item}" is not in the list.')

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
           
        elif choice == '2':
              item = input("Enter the item to remove: ")
              add_item(item)
            
      
        elif choice == '3':
            display_list()
           
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.Please try again.")

if __name__ == "__main__":
    main()         
