def read_and_write_file():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the filename to read: ")

        # Attempt to open the file for reading
        with open(input_filename, 'r') as file:
            content = file.readlines()

        # Modify the content (example: add line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

        # Ask for the output filename
        output_filename = input("Enter the filename to write to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified content successfully written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"An IOError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
