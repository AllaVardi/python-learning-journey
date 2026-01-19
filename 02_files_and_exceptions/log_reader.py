from pathlib import Path

path = Path('sample_log.txt')
contents = path.read_text().rstrip()
print(contents)
