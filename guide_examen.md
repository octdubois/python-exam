# Ultimate Guide for the Practical Exam (Goal: < 30 min)

This guide provides templates categorized by data structures and concepts. The goal is to provide ready-to-use "recipes" so you can mentally copy-paste them and adapt them to any problem.

---

## 🌟 The Interactive Menu (`while True`)
**When to use:** Whenever an exercise asks for a program that "runs continuously" and gives choices to the user.

```python
# Always initialize your main structures BEFORE the loop
my_list = []
my_dictionary = {}

while True:
    print("\n--- Main Menu ---")
    print("1- See all items")
    print("2- Add an item")
    print("3- Delete an item")
    print("q- Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Call display function
        pass
    elif choice == "2":
        # Call add function
        pass
    elif choice == "3":
        # Call delete function
        pass
    elif choice == "q" or choice == "":
        print("Exiting program.")
        break # <-- Essential to exit the loop
    else:
        print("Invalid choice! Try again.")
```

---

## 1. 📦 Lists (`[]`)
**When to use:** To store an ordered collection of simple items (e.g., a history of user names, a list of IP addresses).

### Example 1.1: Managing a simple list (Add, Display, Count)
```python
def add_to_list(my_list, new_element):
    # Validation: don't allow empty strings
    if new_element == "":
        print("Error: Empty string not allowed.")
        return

    # Validation: prevent duplicates
    if new_element in my_list:
        print(f"Error: '{new_element}' already exists in the list.")
    else:
        my_list.append(new_element)
        print(f"'{new_element}' successfully added!")

def display_list(my_list):
    if len(my_list) == 0:
        print("The list is currently empty.")
        return

    print(f"There are {len(my_list)} items in the list:")
    for item in my_list:
        print(f"- {item}")

def find_in_list(my_list, item_to_find):
    if item_to_find in my_list:
        print(f"Yes, '{item_to_find}' is in the list.")
    else:
        print(f"No, '{item_to_find}' is not in the list.")
```

### Example 1.2: Filtering a list based on a condition
```python
def count_long_words(my_list):
    # Example: Count words with more than 4 characters
    count = 0
    for item in my_list:
        if len(item) > 4:
            count += 1
    print(f"There are {count} words with more than 4 characters.")
```

---

## 2. 📖 Dictionaries (`{}`)
**When to use:** When you need to associate two related pieces of data (Key -> Value), or when you need to COUNT occurrences of items.

### Example 2.1: Key-Value Associations (e.g., Name -> Phone Number)
```python
def add_contact(contacts_dict, name, number):
    if name in contacts_dict:
        print(f"Error: Contact '{name}' already exists.")
    elif number == "":
        print("Error: Phone number cannot be empty.")
    else:
        contacts_dict[name] = number
        print("Contact added!")

def view_number(contacts_dict, name):
    if name in contacts_dict:
        print(f"The number for {name} is {contacts_dict[name]}")
    else:
        print(f"Error: Contact '{name}' does not exist.")

def delete_contact(contacts_dict, name):
    if name in contacts_dict:
        del contacts_dict[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Error: Contact not found.")

def view_all_contacts(contacts_dict):
    for name, number in contacts_dict.items():
        print(f"Name: {name} | Number: {number}")
```

### Example 2.2: Counting Occurrences (e.g., Words in a sentence)
```python
def count_words(sentence):
    words_list = sentence.split() # Split string into a list
    word_counts = {}

    for word in words_list:
        if word in word_counts:
            # Word already exists in dictionary, increment count
            word_counts[word] = word_counts[word] + 1
        else:
            # Word seen for the first time, set count to 1
            word_counts[word] = 1

    for word, count in word_counts.items():
        print(f"The word '{word}' appears {count} times.")
```

---

## 3. ⚙️ Functions (`def`)
**When to use:** ALWAYS use them to extract logic out of your `while True` loop to keep the code clean and readable.

### General Function Principles:
- **Don't use `return` if modifying Lists or Dicts:** In Python, passing a list or dictionary to a function and modifying it with `.append()` or `dict[key] = val` changes the original object directly.
- **Do use `return` for calculations:**
```python
def validate_ip_address(num1, num2, num3, num4):
    """Returns True if valid, False otherwise."""
    if (0 <= num1 <= 255) and (0 <= num2 <= 255) and (0 <= num3 <= 255) and (0 <= num4 <= 255):
        return True
    return False

# Usage in loop:
# if validate_ip_address(n1, n2, n3, n4):
#     ip_string = f"{n1}.{n2}.{n3}.{n4}"
```

---

## 4. 🧬 Object-Oriented Programming (Classes)
**When to use:** When the problem describes "things" with multiple specific attributes (e.g., "A Course has a code, a title, and students").

### Example 4.1: A Basic Class with `__str__`
```python
class Car:
    def __init__(self, brand, year):
        # Initialize attributes
        self.brand = brand
        self.year = year

    # The __str__ method dictates how the object looks when you print() it.
    def __str__(self):
        return f"Car: {self.brand} (Year: {self.year})"

# Creating and displaying:
my_car = Car("Mazda", 2010)
print(my_car) # Output: Car: Mazda (Year: 2010)
```

### Example 4.2: A Class containing a List (Advanced)
```python
class Course:
    def __init__(self, course_code, course_title):
        self.code = course_code
        self.title = course_title
        # Initialize an empty list INSIDE the object
        self.enrolled_students = []

    def enroll_student(self, student_name):
        self.enrolled_students.append(student_name)
        print(f"{student_name} enrolled in {self.code}.")

    def view_students(self):
        print(f"Students in {self.title}:")
        for student in self.enrolled_students:
            print(f"- {student}")

    def __str__(self):
        return f"Course {self.code} - {self.title}"

# Usage:
math_class = Course("MATH101", "Introduction to Math")
math_class.enroll_student("Alice")
math_class.enroll_student("Bob")
math_class.view_students()
```

---

## 🎯 Quick Exam Strategy Checklist:
1. **Read the prompt:** Identify the main data structure (List for a sequence, Dictionary for Key-Value/Counting, Class for complex objects).
2. **Setup the Loop:** Copy the `while True` template.
3. **Write Functions:** Create a `def` for every menu option (Add, Display, Delete, Search).
4. **Validations are easy points:** Always check `if element in list:` or `if key in dict:` before adding or deleting.
5. **Use f-strings for output:** `print(f"Variable is {var}")` is faster and less prone to errors than concatenating strings with `+`.