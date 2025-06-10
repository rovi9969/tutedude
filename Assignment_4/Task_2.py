# Task 2: Write and Append Data to a File

file_path = "output.txt"
with open(file_path, 'w') as file:
    # Write user input to the file
    write_data = input("Enter text to write to the file: ")
    file.write(write_data)
    print(f"Data successfully written to {file_path}.\n")

with open(file_path, 'a') as file:
    # Append user input to the file
    append_data = input("Enter additional text to append: ")
    file.write('\n' + append_data)
    print(f"Data successfully appended.\n")

with open(file_path, 'r') as file:
    read_file = file.read()
    print(f"Final content of output.txt:\n{read_file}")
