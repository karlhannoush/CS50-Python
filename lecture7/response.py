import validator_collection

adress = input("Email: ")

try:
    valid = validator_collection.email(adress,allow_empty = True)
except validator_collection.errors.InvalidEmailError:
    print("Invalid")
else:
    print("Valid")