from pathlib import Path
import json

path =  Path('examples/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
