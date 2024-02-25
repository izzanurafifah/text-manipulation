def text_tool():
    print("Welcome to the Text Manipulation Tool.")
    print("1. Count word occurrences")
    print("2. Reverse the text")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        word = input("Enter the word to count: ")
        text = input("Enter the text: ")
        count = count_word_occurrences(word, text)
        print(f"The word '{word}' occurs {count} times.")
    elif choice == "2":
        text = input("Enter the text to reverse: ")
        reversed_text = reverse_text(text)
        print("Reversed Text:", reversed_text)
    else:
        print("Invalid choice. Please enter 1 or 2.")

def count_word_occurrences(word, text):
    words = text.split()
    return words.count(word)

def reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    text_tool()