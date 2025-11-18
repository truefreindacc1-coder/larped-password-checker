import random
import string
import re
txt = ".txt"
pwlength = 16
chars = string.ascii_letters + string.digits + string.punctuation
def pwstr(pw):
    return (len(pw) >= 8 and
            re.search(r'[A-Z]', pw) and
            re.search(r'[a-z]', pw) and
            re.search(r'\d', pw) and
            re.search(r'\W', pw))  

while True:
    check1 = input("1: Make A secure password.\n2. Check password.\n3. Check Password strength.\nQ. Exits the program\n").lower()

    if check1 == "1":

       randompw = ''.join(random.choice(chars) for _ in range(pwlength))
       print(randompw)
       ask = input("Do you want to save this password to a file? Y/N: ").lower()
       if ask == "y":
          with open(randompw + txt, "x") as file:
             file.write(randompw)
       elif ask == "n":
          print("ok vro")

    if check1 == "2":
       with open("rockyou.txt","r",encoding="latin-1") as file:
        passwords = set(line.strip() for line in file) 

        check = input("Password: ").strip()

        if check in passwords:
            print("Password is insecure use a diffrent one.")
        else:
            print("No password matches. You are safe")
    if check1 == "3":
        check = input("Enter password to check strength: ").strip()
        if pwstr(check):
            print("password is kinda strong")
        else:
            print("pw is weak asf gang\n\n")
    if check1 == "q":
       print("quitting :(")
       break