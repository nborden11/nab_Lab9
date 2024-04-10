#Nicholas Borden
def encoder(password):
    encodedPassword = ""
    for i in range(len(password)):
        num = str(int(password[i]) + 3)
        encodedPassword += num
    return encodedPassword

# Nicholas Borden
while True:
       print("Menu")
       print("-------------")
       print("1. Encode")
       print("2. Decode")
       print("3. Quit\n")


       option = int(input("Please enter an option: "))
       if option == 1:
           password = input("Please enter your password to encode: ")
           encodedPassword = encoder(password)
           print("Your password has been encoded and stored!\n")
       if option == 3:
           break
