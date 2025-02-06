import os

directory = '/home/aous/Desktop/MIPT/project/yolo data/3D/lbl'  # Replace with the path to your directory

# Iterate through the files in the directory

# Iterate through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            content = file.read().splitlines()
            for line_number, line in enumerate(content, start=1):
                values = line.split()
                if len(values) != 32:
                    print(f"File: {filename} - Line: {line_number} does not contain exactly 32 values.")
                else:
                    try:
                        float_values = [float(value) for value in values]
                        zero_count = sum(1 for value in float_values if value == 0)
                        if zero_count > 7:
                            print(f"File: {filename} - Line: {line_number} has more than 7 occurrences of 0.")
                        if zero_count == 4:
                            print(f"File: {filename} - Line: {line_number} has 4 occurrences of 0.")
                    except ValueError:
                        print(f"File: {filename} - Line: {line_number} contains non-numeric values.")
        file.close()