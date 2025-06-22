"""
1. Recreate input file
    - read the file backward
    - put each line into a stack
    - popping the stack into new file

"""
import re

def read_file_backwards(file_path):
    stack = []  
    queue = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    i = len(lines) - 1
    while i >= 0:
        line = lines[i]
        stack.append(line)
        i -= 1


    with open('secret/new_file.txt', 'w', encoding='utf-8') as new_file:
        while stack:
            new_file.write(stack.pop())
            



if __name__ == "__main__":
    file_path = 'secret/file.L5K'
    read_file_backwards(file_path)




