def main():
    while True:
        print("\n ---String Processing Menu---")
        print("1. Replace Characters")
        print("2. Reverse a String")
        print("3. Check Palindrome")
        print("4. Count Character Frequencies")
        print("5. Count Word Frequencies")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1' :
            text = input("Enter the string: ")
            old_char = input("Enter the character to replace: ")
            new_char = input("Enter the new character: ")
            print("Result:", text.replace(old_char, new_char))

        elif choice == '2':
            text = input("Enter the string to reverse: ")
            print("Reversed string:", text[::-1])

        elif choice == '3':
            word = input("Enter the word to check: ").strip()
            if word.lower() == word.lower()[::-1]:
                print(f"'{word}' is a palindrome.")
            else:
                print(f"'{word}' is not a palindrome.")

        elif choice == '4':
            text = input("Enter text: ")
            char_count = {}
            for char in text:
                char_count[char] = char_count.get(char, 0) + 1
            print("Character Frequencies:",char_count)

        elif choice == '5':
            sentence = input("Enter a sentence: ")
            words = sentence.split()
            word_count = {}
            for word in words:
                clean_word = word.lower().strip(".,!?")
                word_count[clean_word] = word_count.get(clean_word, 0) + 1
            print("Word Frequencies:", word_count)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()