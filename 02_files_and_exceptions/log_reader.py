from pathlib import Path

path = Path('examples/sample_log.txt')
contents = path.read_text().rstrip()
print(contents)
