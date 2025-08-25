# Ask user for input filename.
# Open and read lines.
# Clean them.
# Save to new file.

# Cleaning process:
# Remove empty lines.
# Remove extra spaces.
# Lower case.
# Remove Punctuation.
# Remove digits.
# Remove special characters.
# Remove duplicates.
import re
import string

with open("file.txt", "r", encoding="utf-8") as infile:  
    lines = infile.readlines()

cleaned_lines = []
for line in lines:
    
    line = line.strip()
    
    # Remove empty lines
    if not line:
        continue
    
    # Remove extra spaces
    line = re.sub(r" +", " ", line).strip()
    
    # Lower case
    line = line.lower()
    
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    remove_punctuation = line.translate(translator)
    line = remove_punctuation
    
    # Remove digits
    translator = str.maketrans("","", string.digits)
    remove_digits = line.translate(translator)
    line = remove_digits
    
    # Remove special characters
    remove_special = re.sub(r"[^a-zA-Z0-9\s]", "", line)
    line = remove_special
    
    cleaned_lines.append(line + "\n")
    
    # Remove duplicates
    cleaned_lines = list(set(cleaned_lines))

with open("cleaned_file.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(cleaned_lines)
