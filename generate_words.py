import random
import re

def extract_words(filename, num_words=256):
    words = set()  # Use a set to store unique words
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Extract words, ignoring punctuation and numbers
            cleaned_words = re.findall(r'\b[a-zA-Z-]+\b', line.lower())
            words.update(cleaned_words)
    
    words = list(words)  # Convert set to list for random selection
    
    # Ensure we don't request more words than available
    num_words = min(num_words, len(words))
    
    return random.sample(words, num_words) if words else []

# Example usage
filename = 'words.txt'  # Replace with your actual file name
random_words = extract_words(filename)
print(random_words) 