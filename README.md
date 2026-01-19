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
└── 02_files_and_exceptions/
    ├── log_reader.py
    ├── file_writer.py
    ├── json_writer.py
    └── json_reader.py
```
## 01_oop_and_modules / users

This section focuses on object-oriented design in Python, including:
- class design and initialization
- inheritance vs composition
- state management inside objects
- modularization across files with clean imports

Start with `demo.py` to see how the components interact.

## 02_files_and_exceptions

This section focuses on working with files and structured data in Python, including:

- reading and writing text files
- handling missing files and basic exceptions
- serializing and deserializing JSON data
- separating file I/O logic from application logic

These patterns are foundational for automation, log processing, and security tooling.
