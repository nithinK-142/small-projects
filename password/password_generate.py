def generate_password():

    from random import sample

    password = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]}\{|/?<>.,"

    while True:
        try:
            pass_len = int(input("Enter Password Length: "))

            # Validate the password length
            if pass_len <= 0 or pass_len > len(password):
                print("Invalid password length. Please enter a valid value.")
            else:
                # Generate a random password by sampling characters from the password string
                generated_password = "".join(sample(password, pass_len))
                print(f"Generated Password is : {generated_password}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer value for password length.")

def secure_password():

    unsecured = input("Enter the Password: ")

    secure = (('s', '$'), ('a', '@'), ('o', '0'), ('i', '1'), ('e', '3'),
             ('l', '|'), ('t', '+'), ('g', '9'), ('b', '8'), ('z', '2'),
             ('A', '4'), ('B', '6'), ('E', '5'), ('I', '!'), ('O', '7'))

    generate = unsecured 

    # Iterate over secure list and replace characters in the password
    for a, b in secure:
        generate = generate.replace(a, b)

    # Check if any replacements were made
    if generate == unsecured:
        print("No Characters to Replace!!")
    else:
        print(f"Secured password is {generate}")


while True:
    try:
        user_input = int(input("1. Password Generation\n2. Securing Password\n3. Exit\nEnter 1, 2 or 3 : "))

        match user_input:
            case 1:
                generate_password()
                break
            case 2:
                secure_password()
                break
            case 3:
                break

    except ValueError:
        print("Invalid input. Please enter an integer.")
