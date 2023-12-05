import os, sys

def get_input(choice):
    current_directory = os.path.dirname(os.path.abspath(__file__))

    file_name = ''
    if choice == '0':
        file_name = 'input.txt'
    elif choice == '1':
        file_name = 'sample.txt'
    else:
        print('Incorrect file descriptor')
        sys.exit(1)
    
    file_path = os.path.abspath(os.path.join(current_directory, '..', 'inputs', file_name))

    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
        return lines