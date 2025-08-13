password = input("Enter your password: ")
strength = 0

# Types of strength

length = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False

# Comparing strengths

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# Strength score
if length == True:
    strength+= 1

if has_upper == True:
    strength+= 1

if has_lower == True:
    strength+= 1

if has_digit == True:
    strength+= 1



# The final check

if strength == 4:
    print("Your password is really strong!")
elif strength == 3:
    print("Your password is strong!")
elif strength == 2:
    print("Your password is decent.")
elif strength == 1:
    print("Your password is very weak.")
else:
    print("Seriously?")