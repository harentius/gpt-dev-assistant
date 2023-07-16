import os

class FileManager:
    def __init__(self):
        pass

    def read_file(self, file_name):
        # check if file exists
        if not os.path.exists(file_name):
            print(f"The file '{file_name}' does not exist.")
            return

        try:
            with open(file_name, 'r') as f:
                content = f.read()
            return content
        except IOError:
            print(f"An error occurred trying to read the file '{file_name}'.")

    def write_file(self, file_name, content):
        try:
            with open(file_name, 'w') as f:
                f.write(content)
            print(f"Content written successfully to '{file_name}'.")
        except IOError:
            print(f"An error occurred trying to write to the file '{file_name}'.")
