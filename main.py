import string

def main():
    
    # Read the file and store its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Split contents into words and count them
    words = file_contents.split()
    
    # Count the frequency of each letter
    char_count = {}
    for char in file_contents:
        lower_case = char.lower()
        if lower_case.isalpha(): # Skip non-letter characters
            if lower_case not in char_count:
                char_count[lower_case] = 1 # First occurence of letter
            else:
                char_count[lower_case] += 1 # Increment existing count

    char_list = []
    for char in char_count:
        char_list.append({"char" : char, "num" : char_count[char]}) # Append a dictionary with character and its count
    
    char_list.sort(key=lambda x: x["num"], reverse=True) # Sort the list of dictionaries by the 'num' key in descending order

    print(f"\n--- Begin report of books/frankenstein.txt ---\n")
    print(f"{len(words)} words found in the document\n") # Print the total number of words in the document

    for item in char_list: 
        print(f"The '{item['char']}' character was found {item['num']} times") # Print each character's frequency in a formatted string

    print("\n--- End Report ---\n")

main()