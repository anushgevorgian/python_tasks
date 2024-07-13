import re
import random


# username validation
def validate_username(username):
  if len(username) < 5 or len(username) > 20:
    return "Username must be between 5 and 20 characters long."
  elif not username.isalnum():
    return "Username can only contain alphanumeric characters."
  elif username.lower() in ['admin', 'root']:
    return "Username cannot be a reserved name (e.g., 'admin', 'root')."
  return ""


# email validation
def validate_email(email):
  regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if not re.match(regex, email):
    return "Invalid email format."
  return ""


# phone number validation
def validate_phone(phone):
  if not re.match(r'^\+?\d{9,15}$', phone):
    return "Invalid phone number format. Must be +37499123456 or 099123456."
  return ""


# password validation
def validate_password(password):
  if len(password) < 8:
    return "Password must be at least 8 characters long."
  if not re.search(r'[A-Z]', password):
    return "Password must contain at least one uppercase letter."
  if not re.search(r'[a-z]', password):
    return "Password must contain at least one lowercase letter."
  if not re.search(r'[0-9]', password):
    return "Password must contain at least one digit."
  if not re.search(r'[!@#$%^&*]', password):
    return "Password must contain at least one special character (e.g., !@#$%^&*)."
  return ""


# password repeat validation
def validate_password_repeat(password, password_repeat):
  if password != password_repeat:
    return "Passwords do not match."
  return ""


list_of_people = []
number_of_users = int(input("Enter number of users: "))

for _ in range(number_of_users):
  while True:
    username = input("Please insert your username: ")
    username_error = validate_username(username)
    if username_error:
      print(username_error)
      continue

    email = input("Please insert your email: ")
    email_error = validate_email(email)
    if email_error:
      print(email_error)
      continue

    phone = input("Please insert your phone number: ")
    phone_error = validate_phone(phone)
    if phone_error:
      print(phone_error)
      continue

    password = input("Please insert your password: ")
    password_error = validate_password(password)
    if password_error:
      print(password_error)
      continue

    password_repeat = input("Please repeat your password: ")
    password_repeat_error = validate_password_repeat(password, password_repeat)
    if password_repeat_error:
      print(password_repeat_error)
      continue

    break

  user_data = {
    "ID": random.randint(1, 10000),
    "Username": username,
    "Email": email,
    "Phone": phone,
    "Password": password
  }
  list_of_people.append(user_data)

print(list_of_people)

find_ID = input("Enter ID: ")
for person in list_of_people:
  if find_ID == str(person["ID"]):
    print(person)
    break
else:
  print("User not found.")
