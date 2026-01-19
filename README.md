# Python Learning Journey

This repository documents my structured Python learning path, built deliberately over several months with a focus on reusable code, correct mental models, and small systems rather than one-off scripts.

Progression is intentional:

**structured learning > reusable code > small systems**

## Current structure
```
python-learning-journey/
├── 01_oop_and_modules/
│   └── users/
│       ├── user.py
│       ├── admin.py
│       ├── demo.py
│       └── login_attempts.py
├── 02_files_and_exceptions/
│   ├── file_writer.py
│   ├── json_reader.py
│   ├── json_writer.py
│   ├── log_reader.py
│   └── examples/
│       ├── numbers.json
│       ├── output.txt
│       └── sample_log.txt
└── README.md
    
```
## 01_oop_and_modules / users

This section focuses on object-oriented design in Python, including:
- class design and initialization
- inheritance vs composition
- state management inside objects
- modularization across files with clean imports

Start with `demo.py` to see how the components interact.

## 02_files_and_exceptions

This section focuses on working with files and exceptions in Python, including:

- reading and writing text files using `pathlib`
- serializing and deserializing data with JSON
- handling file paths and generated outputs
- separating executable code from example data

These patterns are foundational for automation, log processing, and security tooling.

Generated files are stored in the `examples/` subfolder.

