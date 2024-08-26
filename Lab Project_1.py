def main():

    my_list = [1, 2, 3, 4, 5]

    print("Accessing elements:")
    for element in my_list:
        print(element)

    print("\nAccessing a specific element:")
    index = 2
    print(f"Element at index {index}: {my_list[index]}")

    print("\nSlicing the list:")
    start_index = 1
    end_index = 4
    sliced_list = my_list[start_index:end_index]
    print(f"Sliced list from index {start_index} to {end_index - 1}: {sliced_list}")

    new_element = int(input("Enter the Element to append :"))
    my_list.append(new_element)
    print("\nList after appending an element:")
    print(my_list)

    insert_index = int(input("Enter the index to insert the element :"))
    insert_value = int(input(f"\nEnter the Element to enter at {insert_index} :"))
    my_list.insert(insert_index, insert_value)
    print(f"\nList after inserting {insert_value} at index {insert_index}:")
    print(my_list)

main()
