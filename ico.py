import os

def get_ico_files(directory):
    """Return a list of paths to .ico files in the specified directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.ico')]

def read_file(file_path):
    """Read and return the content of the specified file."""
    with open(file_path, 'rb') as file:
        return file.read()

def write_merged_file(output_path, contents):
    """Write the merged contents to the output file."""
    with open(output_path, 'wb') as output_file:
        for content in contents:
            output_file.write(content)

def main():
    directory = input("Please enter the directory containing .ico files: ")
    if not os.path.isdir(directory):
        print("Invalid directory. Please try again.")
        return

    ico_files = get_ico_files(directory)
    if not ico_files:
        print("No .ico files found in the directory.")
        return

    merged_contents = []
    separator = b'737373737' + b'3' * 100

    for ico_file in ico_files:
        content = read_file(ico_file)
        merged_contents.append(content)
        merged_contents.append(separator)

    # Remove the last separator
    if merged_contents:
        merged_contents.pop()

    output_file = os.path.join(directory, "merged.ico")
    write_merged_file(output_file, merged_contents)
    print(f"Merged file created at: {output_file}")

if __name__ == "__main__":
    main()
