# Task 1: Read a File and Handle Errors 

try:
    with open('sample.txt', 'r') as file:
        counter=1
        print("Reading file content:")
        while True:
            read_file = file.readline()
            if not read_file:
                break
            read_file = read_file.strip()
            print(f"Line {counter}: {read_file}")
            counter += 1
    print(read_file)
except FileNotFoundError:
    print("Error: The file sample.txt does was not found.")
