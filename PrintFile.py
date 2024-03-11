workflow_name = "WorkflowScripts::PrintFile"
source_url = "https://github.com/uaineteine/WorkflowScripts/"

print(f"{'=' * 40}")
print(f"{' ' * 10} {workflow_name}")
print(f"{'=' * 40}")
print(f"Source: {source_url}")
print(f"{'=' * 40}")

import sys

def read_and_print_file(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the file path.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit(1)

    file_path_argument = sys.argv[1]
    read_and_print_file(file_path_argument)
  
