'''Write a Python script that reads a text file named "sample.txt", counts the number of lines, words, 
and characters in the file, and prints these counts.'''
def count_file(filename):
    with open('filename', 'r') as f:
        content= f.read()
        lines = content.split('\n')
        ct_lines = len(lines)
        ct_words = len(content.split())
        ct_char = len(content)
filename = 'sample.txt'
count_file(filename)
