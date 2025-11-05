# File Handling

## Basic File Handling

### Write Data

```python
with open("file.txt", "w") as f:
    f.write("Hello World")
```

### Read Data

```python
with open("file.txt", "r") as f:
    data = f.read()
```

### Append Data (add without Overwriting)

```python
with open("file.txt", "a") as f:
    f.write("\nNew line added")
```

----

## Folder and File Management (using <strong>os</strong>)

### Get Current Directory

```python
import os
print(os.getcwd())
```

### Create New Folder

```python
os.mkdir("data")
```

### Change Directory

```python
os.chdir("data")
```

### List all files/folders

```python
print(os.listdir())
```

### Join Path (safe way)

```python
path = os.path.join("data", "info.json")
```

### Check if file/folder exists

```python
os.path.exists("data/info.json")
```

### Delete File

```python
os.remove("file.txt")
```

### Remove Empty Folder

```python
os.rmdir("data")
```

----

## <strong>JSON</strong> Handling (for lists & Dictionaries)

### Write Python Dict/List to File

```python
import json

data = {"name": "Rohan", "marks": [85, 90, 92]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### Read JSON file

```python
with open("data.json", "r") as f:
    info = json.load(f)
print(info)
```

### Convert Between Python and JSON (without file)

```python
json_string = json.dumps(data)      # dict → JSON string
python_dict = json.loads(json_string)  # JSON string → dict
```

----

## OS and JSON

```python
import os, json

# make sure folder exists
if not os.path.exists("storage"):
    os.mkdir("storage")

# data to store
user = {"name": "Rohan", "subjects": ["Math", "CS"]}

# store JSON file in folder
path = os.path.join("storage", "user.json")
with open(path, "w") as f:
    json.dump(user, f, indent=4)

# check and read back
if os.path.exists(path):
    with open(path, "r") as f:
        data = json.load(f)
    print(data)
```

----

&copy; 2025 All Rights Reserved

----

THANKYOU
