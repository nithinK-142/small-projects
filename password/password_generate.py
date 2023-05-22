def secure_password():
    # Function to secure a password by replacing certain characters
    unsecured = input("Enter the Password: ")

    secure = (('s', '$'), ('a', '@'), ('o', '0'), ('i', '1'), ('e', '3'),
              ('l', '|'), ('t', '+'), ('g', '9'), ('b', '8'), ('z', '2'))

    generate = unsecured  # Initialize generate with unsecured password

    for a, b in secure:
        generate = generate.replace(a, b)

    if generate == unsecured:
        print("No Characters to Replace!!")
    else:
        print(f"Secured password is {generate}")


def generate_password():
    # Function to generate a random password based on user input
    import random

    password = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

    while True:
        try:
            pass_len = int(input("Enter Password Length: "))
            if pass_len <= 0 or pass_len > len(password):
                print("Invalid password length. Please enter a valid value.")
            else:
                generated_password = "".join(random.sample(password, pass_len))
                print(f"Generated Password is : {generated_password}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer value for password length.")


while True:
    try:
        user_input = int(input("Enter 1 or 2: "))

        match user_input:
            case 1:
                secure_password()  # Call secure_password function for securing a password
                break
            case 2:
                generate_password()  # Call generate_password function for generating a password
                break

    except ValueError:
        print("Invalid input. Please enter an integer.")
