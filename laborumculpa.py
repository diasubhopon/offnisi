# Save the mapping as a dictionary in a file
import json

file_path = "june_2024_id_mapping.json"

# Save the mapping to a JSON file
with open(file_path, 'w') as file:
    json.dump(string_integer_mapping, file)

print(f"The string-integer ID mapping for June 2024 has been saved as a dictionary in the file: {file_path}")
