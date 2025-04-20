person["email"] = "alice@example.com"  # Add new key-value
person["age"] = 31  # Update existing key

del person["city"]  # Remove key
age = person.pop("age")  # Remove and return value
person.clear()  # Empty the dictionary