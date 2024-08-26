'''Write a Python program to extract characters from various text files and puts them into a list '''
def extraction(filenames):
    all_char = []
    for filename in filenames:
        with open(filename, 'r') as file:
            content = file.read()
            all_char.extend(list(content))
    return all_char
filenames = ['file1.txt', 'file2.txt']
characters = extraction(filenames)
print(characters)
 