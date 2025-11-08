import json

def save_data(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully!")
    except Exception as e:
        print("Error saving data:", e)

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found, returning empty list.")
        return []

data = load_data("users.json")
data.append({"name": "Alice", "score": 95})
save_data("users.json", data)
