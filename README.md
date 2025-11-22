# SOLID Principles and Design Patterns

This repository contains exercises and examples from a course on SOLID principles and Design Patterns.

## Project Structure

```
patterns/
├── oop_refresher/          # Object-Oriented Programming refresher exercises
│   ├── contracts.py        # Abstract classes and interfaces
│   └── book_authorship.py  # Class relationships and composition
├── .flake8                 # Flake8 linting configuration
├── .gitignore              # Git ignore rules
├── Makefile                # Common development tasks
└── README.md               # This file
```

## Requirements

- Python 3.7+
- flake8 (for linting)

## Installation

```bash
# Install dependencies
make install
```

Or manually:
```bash
pip install flake8
```

## Usage

### Running Exercises

Each exercise file can be run directly:

```bash
# Run contracts exercise
python oop_refresher/contracts.py

# Run book authorship exercise
python oop_refresher/book_authorship.py
```

### Linting

Check code style with flake8:

```bash
make lint
```

### Formatting

Format code (if you have black installed):

```bash
make format
```

## Available Make Commands

- `make install` - Install project dependencies
- `make lint` - Run flake8 linting
- `make format` - Format code with black (if installed)
- `make clean` - Remove Python cache files
- `make help` - Show all available commands

## Course Topics

This repository covers:

- **SOLID Principles**
  - Single Responsibility Principle
  - Open/Closed Principle
  - Liskov Substitution Principle
  - Interface Segregation Principle
  - Dependency Inversion Principle

- **Design Patterns**
  - Creational Patterns
  - Structural Patterns
  - Behavioral Patterns

## Notes

This is a learning repository for tracking exercises and examples from the SOLID principles and Design Patterns course.

