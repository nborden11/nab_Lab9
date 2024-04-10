#Nicholas Borden
def encoder(password):
    encodedPassword = ""
    for i in range(len(password)):
        num = str(int(password[i]) + 3)
        encodedPassword += num
    return encodedPassword


# Josh Daniels
def decoder(decoded):
    decoded_password = ""
    for i in range(len(decoded)):
        num = str(int(decoded[i])-3)
        decoded_password += num
    return decoded_password


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
    # Josh Daniels
    elif option == 2:
        decoded_final = decoder(encodedPassword)
        print(f'The encoded password is: {encodedPassword} and the original password is {decoded_final}\n')
    elif option == 3:
        break
