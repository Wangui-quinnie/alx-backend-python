Python - Variable Annotations

Here's a brief overview of how to use type annotations in Python:

Variable Annotations: You can annotate variables using a colon (:) followed by the type. For example:
x: int = 5
Function Annotations: You can annotate function parameters and return types using the arrow (->) syntax. For example:
def add(x: int, y: int) -> int:
    return x + y
Optional and Default Values: You can specify optional parameters and their types using Optional from the typing module and default values. For example:
from typing import Optional

def greet(name: str, age: Optional[int] = None) -> str:
    if age:
        return f"Hello, {name}! You are {age} years old."
    else:
        return f"Hello, {name}!"
Duck Typing: Python follows the principle of duck typing, which means that the type of an object is determined by its behavior, not its explicit type. However, type annotations provide a way to document expected behavior.

Validating with Mypy: Mypy is a static type checker for Python that analyzes your code and detects type-related errors. You can install Mypy using pip (pip install mypy), and then run it on your Python files to check for type errors:

mypy your_file.py
Mypy will report any type errors it finds based on the annotations you've provided.

Overall, type annotations in Python provide a way to add clarity and consistency to your code, and tools like Mypy can help you catch potential errors early in the development process.

0. Basic annotations - add
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

1. Basic annotations - concat
Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string

2. Basic annotations - floor
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.

3. Basic annotations - to string
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.

4. Define variables
Define and annotate the following variables with the specified values:

a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton”

5. Complex types - list of floats
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.

6. Complex types - mixed list
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

7. Complex types - string and int/float to tuple
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

8. Complex types - functions
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

9. Let's duck type an iterable object
Annotate the below function’s parameters and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
10. Duck typing - first element of a sequence
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
11. More involved type annotations
Given the parameters and the return values, add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
12. Type Checking
Use mypy to validate the following piece of code and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
