import json


def sort_json(obj):
    """
    Recursively sort a JSON object by its keys.

    :param obj: The JSON object or any nested part of it.
    :return: A new object with all dictionaries sorted by key.
    """
    if isinstance(obj, dict):
        # Sort the dictionary by key, and recursively sort its values
        return {k: sort_json(obj[k]) for k in sorted(obj)}
    elif isinstance(obj, list):
        # Recursively sort each item in the list
        return [sort_json(item) for item in obj]
    else:
        # Return the item itself if it's neither a dict nor a list
        return obj


# Load the JSON data from the uploaded file
file_path = '5.json'

with open(file_path, 'r') as file:
    json_data = json.load(file)

# Apply the sorting function to the entire JSON data
sorted_json_data = sort_json(json_data)

# Convert the sorted JSON data back into a string for display or use
sorted_json_str = json.dumps(sorted_json_data, indent=4)
print(sorted_json_str)
