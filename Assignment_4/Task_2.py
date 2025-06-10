# Task 2: Write and Append Data to a File

with open('output.txt', 'w') as file:
    # Write user input to the file
    write_data = input("Enter text to write to the file: ")
    file.write(write_data)

with open('output.txt', 'a') as file:
    # Append user input to the file
    append_data = input("Enter additional text to append: ")
    file.write('\n' + append_data)

with open('output.txt', 'r') as file:
    read_file = file.read()
    print(f"Final content of output.txt:\n{read_file}")
