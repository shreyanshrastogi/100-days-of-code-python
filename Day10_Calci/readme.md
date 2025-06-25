# 🧮 Python Calculator

This is a simple calculator I built using Python. It runs in the terminal and handles basic operations like addition, subtraction, multiplication, and division.

The main idea was to avoid long if-else chains and instead use a dictionary to map operators to functions — worked out pretty nicely.

---

## Features

- Supports `+`, `-`, `*`, `/`
- Lets you keep calculating with the last result
- Uses function references inside a dictionary
- Handles basic input errors
- Clean and modular code

---

## How it Works

Each operator (`+`, `-`, etc.) is linked to its corresponding function like this:

```python
operators = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
