def create_list():
    n = int(input("Enter the number of elements in the list: "))
    lst = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i+1)))
        lst.append(element)
    return lst

def reverse_list(lst):
    return lst[::-1]

def find_smallest_number(lst):
    return min(lst)

def find_largest_number(lst):
    return max(lst)

def multiply_list_items(lst):
    result = 1
    for item in lst:
        result *= item
    return result

# Main function
def main():
    user_list = create_list()
    reversed_user_list = reverse_list(user_list)
    smallest_number = find_smallest_number(user_list)
    largest_number = find_largest_number(user_list)
    product = multiply_list_items(user_list)

    print("\nOriginal list:", user_list)
    print("Reversed list:", reversed_user_list)
    print("Smallest number in the list:", smallest_number)
    print("Largest number in the list:", largest_number)
    print("Product of all items in the list:", product)

if __name__ == "__main__":
    main()
