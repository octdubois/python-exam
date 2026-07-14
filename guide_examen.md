# Ultimate Guide for the Practical Exam (Goal: < 30 min)

This guide is based on your teacher's examples. The goal is to provide you with ready-to-use "recipes" (templates) so you don't have to think during the exam. You can mentally copy-paste these structures and adapt them to the problem.

## 🌟 Most Used Principle: The Interactive Menu (`while True`)
**Why use it?** Almost all exercises require a program that "runs continuously" and interacts with the user.
**How to use it?**
```python
# 1. Always initialize your data structures BEFORE the loop
my_list = []
my_dictionary = {}

# 2. The infinite loop
while True:
    print("1- Option 1")
    print("2- Option 2")
    print("q- Quit (or press Enter)")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Action 1
        pass
    elif choice == "2":
        # Action 2
        pass
    elif choice == "q" or choice == "":
        print("End of program.")
        break # <-- Very important to exit the loop
    else:
        print("Invalid choice!")
```

---

## 1. Functions (To simplify the code)
**Why?** The teacher wants the code inside the `while` loop to be clean. Instead of putting 15 lines in an `elif`, we call a function.

**Classic Model (Display, Add, Search):**
```python
def display_options():
    print("1- Display, 2- Add, etc.")

# Lists and dictionaries are modified directly (no need for 'return')
def add_user(user_list, new_user):
    # Always check if the element already exists to avoid duplicates
    if new_user in user_list:
        print("Error: User already exists.")
    else:
        user_list.append(new_user)
        print(f"{new_user} added successfully!")

def display_all(my_list):
    if len(my_list) == 0:
        print("The list is empty.")
        return # Exit the function if it's empty
    for element in my_list:
        print(element)
```

---

## 2. Lists (To store and iterate)
**Why?** To keep a history (e.g., created IP addresses) or a list of simple elements (user names).

**Quick Operations:**
- **Create:** `my_list = []`
- **Add:** `my_list.append(element)`
- **Count:** `count = len(my_list)`
- **Iterate:**
```python
for item in my_list:
    print(item)
```

---

## 3. Dictionaries (Key -> Value)
**Why?** To associate two pieces of information (e.g., Name -> Phone number) or COUNT elements (e.g., words in a sentence).

**Recipe 1: Associating information (e.g., Contacts)**
```python
contacts = {}

# Add / Modify
contacts["Alice"] = "514-123-4567"

# Search and Display
name = "Alice"
if name in contacts:  # Always check if the key exists!
    print(f"The number is {contacts[name]}")
else:
    print("Contact not found.")

# Delete
if name in contacts:
    del contacts[name]
```

**Recipe 2: Counting occurrences (VERY FREQUENT)**
```python
# Example: counting words in a sentence
sentence = "cat dog cat"
word_list = sentence.split() # Splits the sentence into a list of words
counter = {}

for word in word_list:
    if word in counter:
        counter[word] = counter[word] + 1 # Increment if the word already exists
    else:
        counter[word] = 1 # Initialize to 1 if it's the first time

# Display results
for key, value in counter.items():
    print(f"{key} --- {value}")
```

---

## 4. Object-Oriented Programming (OOP)
**Why?** To group attributes under a single entity (e.g., Car, Student, Course).

**The perfect template to copy-paste and adapt:**
```python
class ClassName:
    # 1. The constructor (initialize attributes)
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.internal_list = [] # Sometimes we have an empty list initially (e.g., enrolled students)

    # 2. An action method (optional, depending on the question)
    def do_action(self, element):
        self.internal_list.append(element)

    # 3. The magic __str__ method (FOR DISPLAYING)
    # The teacher ALWAYS asks to do this.
    def __str__(self):
        return f"{self.attribute1} - {self.attribute2}"

# Object creation
object1 = ClassName("Value1", "Value2")
object2 = ClassName("ValueA", "ValueB")

# Direct display (thanks to __str__)
print(object1)
print(object2)
```

---

## 🎯 Strategy to finish in < 30 minutes:
1. **Read the question:** Are they asking for a "continuous program"? -> **Copy-paste the Interactive Menu template (`while True`).**
2. **Identify the data structure:**
   - Are we just storing names or history? -> **List (`[]`)**
   - Are we associating two things or counting? -> **Dictionary (`{}`)**
   - Are we creating things with multiple characteristics (brand, year, color)? -> **Class (OOP)**
3. **Make functions:** Extract complex logic (e.g., validation, adding) outside the `while True` using `def`.
4. **Always validate:**
   - Before reading/deleting in a dict: `if key in dict:`
   - Before adding to a list without duplicates: `if element not in list:`
5. **Display clearly:** Use f-strings: `print(f"The result is {variable}")`.