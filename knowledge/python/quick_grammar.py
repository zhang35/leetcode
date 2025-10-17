# python3_cheatsheet_pythonic.py
# A detailed reference for Python 3, now including "Pythonic" best practices.

print("--- Python 3 Cheatsheet (with Pythonic Usages) ---")

# ==============================================================================
# 1. VARIABLES AND DATA TYPES
# ==============================================================================
print("\n## 1. Variables and Data Types ##")
# ... (Content from the previous detailed cheatsheet remains the same) ...
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# -- String Manipulation & Slicing --
sentence = " a pythonic example "
print(f"Stripped: '{sentence.strip()}'")
print(f"Title cased: '{sentence.title()}'")
words = sentence.split()
joined_string = "-".join(words)
print(f"Joined with '-': '{joined_string}'")

s = "abcdefgh"
print(f"Reversed string (s[::-1]): '{s[::-1]}'")


# ==============================================================================
# 2. DATA STRUCTURES
# ==============================================================================
print("\n## 2. Data Structures ##")

# -- Lists (Mutable, Ordered) --
fruits = ["apple", "banana", "cherry", "orange"]
print(f"\nOriginal List: {fruits}")
print(f"Is 'cherry' in the list? {'cherry' in fruits}")

# sorted() returns a new sorted list (Pythonic for not modifying original)
sorted_fruits = sorted(fruits)
print(f"New sorted list: {sorted_fruits}")

# -- Dictionaries (Mutable, Key-Value pairs) --
person = {"name": "Bob", "age": 25, "city": "New York"}
print(f"\nDictionary: {person}")

# Use .get() for safe access to avoid KeyErrors
occupation = person.get('occupation', 'Not specified')
print(f"Occupation: {occupation}")

# -- Sets (Mutable, Unordered, Unique elements) --
# Great for fast membership testing and removing duplicates.
numbers = {1, 2, 3, 4, 4, 5}
print(f"\nSet: {numbers}")


# ==============================================================================
# 3. CONTROL FLOW
# ==============================================================================
print("\n## 3. Control Flow ##")
# -- Conditional Expressions (Ternary Operator) --
# A concise, Pythonic way to write simple if-else statements.
is_adult = True if age >= 18 else False
print(f"Is a {age}-year-old an adult? {is_adult}")


# ==============================================================================
# 4. FUNCTIONS
# ==============================================================================
print("\n## 4. Functions ##")
# -- Function with Type Hinting --
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width
print(f"Area of 10x5 rectangle: {calculate_area(10, 5)}")


# ==============================================================================
# 5. PYTHONIC USAGES & IDIOMS
# ==============================================================================
print("\n## 5. Pythonic Usages & Idioms ##")
# Writing Python code the "right" way.

# -- Iterating Over Sequences --
my_list = ['a', 'b', 'c']

# Non-Pythonic (C-style)
print("\nNon-Pythonic iteration:")
for i in range(len(my_list)):
    print(my_list[i], end=' ')
print()

# Pythonic ✨
print("Pythonic iteration:")
for item in my_list:
    print(item, end=' ')
print()

# -- Iterating with an Index (enumerate) --
print("\nPythonic iteration with index (enumerate):")
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

# -- Iterating Over Dictionaries --
my_dict = {'a': 1, 'b': 2}
print("\nPythonic dictionary iteration (.items()):")
for key, value in my_dict.items():
    print(f"{key} -> {value}")

# -- Swapping Variables --
x, y = 10, 20
print(f"\nBefore swap: x={x}, y={y}")
# Pythonic tuple unpacking swap
x, y = y, x
print(f"After swap:  x={x}, y={y}")

# -- List Comprehensions (instead of loops) --
# Non-Pythonic
squares_loop = []
for i in range(5):
    squares_loop.append(i * i)

# Pythonic ✨
squares_comp = [i * i for i in range(5)]
print(f"\nSquares created with a loop: {squares_loop}")
print(f"Squares created with list comprehension: {squares_comp}")

# -- Joining Strings --
words = ["python", "is", "awesome"]
# Non-Pythonic (inefficient)
result_loop = ""
for word in words:
    result_loop += word + " "
result_loop = result_loop.strip()

# Pythonic ✨
result_join = " ".join(words)
print(f"\nString joined with a loop: '{result_loop}'")
print(f"String joined with .join(): '{result_join}'")

# -- "EAFP" vs "LBYL" --
# EAFP: Easier to Ask for Forgiveness than Permission (often more Pythonic)
# It means you just try the operation and handle the exception if it fails.
print("\nEAFP approach (try...except):")
my_dict = {'a': 1}
try:
    value = my_dict['b']
    print(f"Found value: {value}")
except KeyError:
    print("Key 'b' not found.")

# LBYL: Look Before You Leap
# Check if the key exists before trying to access it.
print("LBYL approach (if...in):")
if 'b' in my_dict:
    value = my_dict['b']
    print(f"Found value: {value}")
else:
    print("Key 'b' not found.")


# ==============================================================================
# 6. CLASSES AND OBJECTS
# ==============================================================================
print("\n## 6. Classes and Objects ##")
class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    # The __str__ method provides a user-friendly string representation.
    def __str__(self):
        return f"{self.name} the {self.breed}"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog)  # This automatically calls my_dog.__str__()


# ==============================================================================
# 7. FILE I/O (Context Managers)
# ==============================================================================
print("\n## 7. File I/O (Context Managers) ##")
# The 'with' statement is Pythonic because it automatically handles
# resource cleanup (e.g., closing the file) even if errors occur.
file_path = "pythonic_example.txt"
try:
    with open(file_path, "w") as f:
        f.write("Using 'with' is the Pythonic way!\n")
    print(f"Successfully wrote to {file_path}")

    with open(file_path, "r") as f:
        content = f.read()
        print(f"Read from file: '{content.strip()}'")
except IOError as e:
    print(f"File handling error: {e}")


# ==============================================================================
# 8. EXCEPTION HANDLING
# ==============================================================================
print("\n## 8. Exception Handling ##")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught a specific error: {e}")
finally:
    print("The 'finally' block always runs, for cleanup.")


print("\n--- End of Pythonic Cheatsheet ---")