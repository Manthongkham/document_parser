"""
1. Recreate L5K file
    - read the file backward
    - put each line into a stack
    - popping the stack into new file

"""


def read_l5k_file_backwards(file_path):
    stack = []  

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in reversed(file.readlines()):
            stack.append(line)

    with open('new_l5k.txt', 'w', encoding='utf-8') as new_file:
        while stack:
            line = stack.pop()
            new_file.write(line)




if __name__ == "__main__":
    file_path = 'HENDERSON_WINDER.L5K'
    read_l5k_file_backwards(file_path)
