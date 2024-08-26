def dictionary_function(dictionary, key, value):
#func to perform dict operations
    if key in dictionary:
        print(f"Key '{key}' already exists with value '{dictionary[key]}'.")
        update_choice = input("Do you want to update the value? (yes/no): ")
        if update_choice.lower() == 'yes':
            dictionary[key] = value
            print("Value updated successfully.")
    else:
        dictionary[key] = value
        print("Key-value pair added successfully.")


def view_dictionary(dictionary):
#func to view contents
    key_to_view = input("Enter the key you want to view: ")
    if key_to_view in dictionary:
        print(f"The value for key '{key_to_view}' is: {dictionary[key_to_view]}")
    else:
        print("Key not found in the dictionary.")


def edit_dictionary(dictionary):
#funct to edit the dict contents
    key_to_edit = input("Enter the key you want to edit: ")
    if key_to_edit in dictionary:
        new_value = input(f"Enter the new value for key '{key_to_edit}': ")
        dictionary[key_to_edit] = new_value
        print("Value updated successfully.")
    else:
        print("Key not found in the dictionary.")


if __name__ == "__main__":
    user_dict = {}
    while True:
        print("\nInteractive Dictionary Operations:")
        print("1. Add a key-value pair")
        print("2. View dictionary")
        print("3. Edit a key-value pair")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            dictionary_function(user_dict, key, value)

        elif choice == '2':
            view_dictionary(user_dict)

        elif choice == '3':
            edit_dictionary(user_dict)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
