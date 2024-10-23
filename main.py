from encoder import encode
from decoder import decode
def main():
    while True:
        print("Menu")
        print("---------------")
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Enter an option: ")
        if choice == "1":
            value = input("Please enter your password to encode: ")
            encoded_password = encode(value)
            print("Your password has been encoded and stored!")
            
        elif choice == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()


if __name__ == "__main__":
    main()
