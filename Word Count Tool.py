# Word Count Tool
import string

def count_words(text):
    # Remove punctuation and convert to lower case
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return len(words)

def get_text_from_user():
    text = input("Enter the text: ")
    if not text.strip():
        print("The input text is empty. Please enter some text.")
        return None
    return text

def get_text_from_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            text = file.read()
            if not text.strip():
                print("The file is empty. Please provide a file with text.")
                return None
            return text
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return None

def main():
    print("Welcome to the Word Count Tool!")
    while True:
        print("\nSelect input method:")
        print("1. Enter text manually")
        print("2. Load text from a file")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            text = get_text_from_user()
            if text:
                word_count = count_words(text)
                print(f"The number of words in the given text is: {word_count}")

        elif choice == '2':
            text = get_text_from_file()
            if text:
                word_count = count_words(text)
                print(f"The number of words in the given text is: {word_count}")

        elif choice == '3':
            print("Thank you for using the Word Count Tool. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

