import string

def main():
    
    # Read the file and store its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Split contents into words and count them
    words = file_contents.split()
    print(len(words))
    
    # Count the frequency of each letter
    char_count = {}
    for char in file_contents:
        lower_case = char.lower()
        if lower_case.isalpha(): # Skip non-letter characters
            if lower_case not in char_count:
                char_count[lower_case] = 1 # First occurence of letter
            else:
                char_count[lower_case] += 1 # Increment existing count
    print(char_count)

main()