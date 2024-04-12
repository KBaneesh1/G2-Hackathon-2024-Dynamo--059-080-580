import json

# Open the JSON Lines file for reading
count = 0 
with open('sui.jsonl', 'r', encoding='utf-8') as file:
    # Iterate through each line in the file
    for line in file:
        # Parse the JSON object from the line
        data = json.loads(line)
        
        # Now you can work with the JSON data as a Python dictionary
        # For example, print the value of a specific key
        count += 1
        print(count)
