import string
import random


def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters  # includes both lowercase and uppercase

    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters available to generate password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator 🔐")

    try:
        length = int(input("Enter desired password length: "))
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_digits, use_specials)
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for length.")


if __name__ == "__main__":
    main()
