import string
from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the file and remove punctuation
            text = file.read().translate(str.maketrans('', '', string.punctuation))

            # Tokenize the text into words and convert to lowercase
            words = text.lower().split()

            # Count occurrences of each word
            word_counts = Counter(words)

            # Sort by word frequency in descending order
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

            # Print the results
            for word, count in sorted_word_counts:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Get the file path from the user
        file_path = input("Enter the path to the .txt file: ").strip()

        # Check if the provided file has a .txt extension
        if file_path.endswith('.txt'):
            count_words(file_path)
        else:
            print("Error: Please provide a .txt file.")

    except KeyboardInterrupt:
        print("\nOperation aborted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
