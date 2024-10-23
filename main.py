from encoder import encode
def main():
    while True:
        print("Menu")
        print("---------------")
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Enter an option: ")
        if choice == "1":
            value = input("Please enter your passwrod to encode: ")
            print("Your password has been encoded and stored!")
            
        elif choice == "2":
            print(f"The encoded password is {encoder(value)}, and the original password is {value}.")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()


if __name__ == "__main__":
    main()
