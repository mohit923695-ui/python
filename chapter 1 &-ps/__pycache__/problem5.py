#understanding comments
import os

# Specify the directory path
path = "."

# Display the contents of the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)