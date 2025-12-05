def count_characters(text):
    """Count the frequency of each character in the text.
    
    Args:
        text: String to analyze
        
    Returns:
        Dictionary with characters as keys and counts as values
    """
    char_dict = {}
    lowered_text = text.lower()
    
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict


def sort_char_dict(char_dict):
    """Convert character dictionary to sorted list of dictionaries.
    
    Args:
        char_dict: Dictionary with characters as keys and counts as values
        
    Returns:
        List of dictionaries sorted by count (greatest to least)
    """
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Helper function to get the 'num' value for sorting
    def sort_on(dict_item):
        return dict_item["num"]
    
    # Sort from greatest to least
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
