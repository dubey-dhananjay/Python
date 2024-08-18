contacts = [
    {"name": "Prashant", "number": "1234567890"},
    {"name": "Nikhil", "number": "1112131415"},
    {"name": "Swaraj", "number": "1617181920"}
]

name = input("Enter Name: ")

for person in contacts:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}")