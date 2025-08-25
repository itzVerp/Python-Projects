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
# Replace multiple spaces with one.
# Remove special characters.
# Remove duplicates.
import re

with open("text.txt", "r", encoding="utf-8") as infile:  
    lines = infile.readlines()

cleaned_lines = []
for line in lines:
    
    line = line.strip()
    
    if not line:
        continue
    
    # Remove extra spaces
    line = re.sub(r" +", " ", line).strip()
    cleaned_lines.append(line + "\n")

with open("cleaned_file.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(cleaned_lines)
