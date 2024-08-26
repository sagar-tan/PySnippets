import json

def dictionary_function(dictionary, key, value, filename):
#main dict func
    if key in dictionary:
        print(f"Key '{key}' already exists with value '{dictionary[key]}'.")
        update_choice = input("Do you want to update the value? (yes/no): ")
        if update_choice.lower() == 'yes':
            dictionary[key] = value
            print("Value updated successfully.")
            # Update the file
            with open(filename, 'w') as file:
                json.dump(dictionary, file)
    else:
        dictionary[key] = value
        print("Key-value pair added successfully.")
        # Update the file
        with open(filename, 'w') as file:
            json.dump(dictionary, file)


def view_dictionary(dictionary, filename):
#function to view data by seeing the file
    key_to_view = input("Enter the key you want to view: ")
    if key_to_view in dictionary:
        print(f"The value for key '{key_to_view}' is: {dictionary[key_to_view]}")
    else:
        print("Key not found in the dictionary.")
        # Prompt to read from file
        read_choice = input("Do you want to read from the file? (yes/no): ")
        if read_choice.lower() == 'yes':
            try:
                with open(filename, 'r') as file:
                    data = json.load(file)
                    dictionary.update(data)
                    if key_to_view in dictionary:
                        print(f"The value for key '{key_to_view}' is: {dictionary[key_to_view]}")
                    else:
                        print("Key not found in the file.")
            except FileNotFoundError:
                print("File not found.")
    return dictionary


def edit_dictionary(dictionary, filename):
#function to edit data in a existing key
    key_to_edit = input("Enter the key you want to edit: ")
    if key_to_edit in dictionary:
        new_value = input(f"Enter the new value for key '{key_to_edit}': ")
        if dictionary[key_to_edit] == new_value:
            print("New value is same as the existing value.")
            return
        confirmation = input(f"Are you sure you want to change the value of key '{key_to_edit}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            dictionary[key_to_edit] = new_value
            print("Value updated successfully.")
            # Update the file
            with open(filename, 'w') as file:
                json.dump(dictionary, file)
    else:
        print("Key not found in the dictionary.")


if __name__ == "__main__":
    filename = "dictionary.json"
    
    try:
        with open(filename, 'r') as file:
            user_dict = json.load(file)
    except FileNotFoundError:
        user_dict = {}

    while True:
        print("\nInteractive Dictionary Operations:")
        print("1. Add a key-value pair")
        print("2. View value for a key")
        print("3. Edit a key-value pair")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            confirmation = input(f"Are you sure you want to add key '{key}' with value '{value}'? (yes/no): ")
            if confirmation.lower() == 'yes':
                dictionary_function(user_dict, key, value, filename)

        elif choice == '2':
            user_dict = view_dictionary(user_dict, filename)

        elif choice == '3':
            edit_dictionary(user_dict, filename)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
