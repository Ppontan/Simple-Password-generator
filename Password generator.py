import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!%"

while 1:
    password_len = int(input("Length of password: "))
    password_count = int(input("how many passwords : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password     = password + password_char
        print(" passwrod : ", password)