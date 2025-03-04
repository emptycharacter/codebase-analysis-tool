import os

password = "123456"  # Hardcoded password (BAD PRACTICE)

def insecure_function(user_input):
    eval(user_input)  # Using eval() is dangerous!

with open("secret_key.txt", "w") as f:
    f.write("API_KEY=abcd1234")  # Hardcoded API Key
