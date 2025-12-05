import sys

def count_words(text):
    """Count the number of words in the text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Count the frequency of each character (case-insensitive)."""
    char_count = {}
    lowered_text = text.lower()
    
    for char in lowered_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def sort_char_dict(char_dict):
    """Convert character dictionary to sorted list of dictionaries."""
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list

def generate_report(book_path, text):
    """Generate and print a report about the book."""
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_chars = sort_char_dict(char_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in sorted_chars:
        char = item['char']
        count = item['count']
        print(f"{char}: {count}")
    
    print("--- End report ---")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command-line arguments
    book_path = sys.argv[1]
    
    try:
        with open(book_path) as f:
            file_contents = f.read()
        
        generate_report(book_path, file_contents)
    
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
