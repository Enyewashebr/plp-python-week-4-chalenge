# create a file named input.txt
with open("input.txt", "w") as file:
    file.write("file one\n")
    file.write("file two\n")
    file.write("file three\n")
    file.write("file four\n")
    file.write("file five\n")
    file.write("file five\n")
# Read the contents of input.txt.
with open("input.txt", "r") as file:
    content= file.read()
    print(content)
# Count the number of words in the file.
contents= content.split()
print(contents)
word_count=len(contents)
print("total number of word in input .txt is :", word_count)


# Convert all text to uppercase.
content_upper = content.upper()
print(content_upper)


# Write the processed text and the word count to a new file called output.txt.
with open("output.txt", "w") as file:
    file.write(content)
    


# This code opens a file named "example.txt" in read mode, reads its content, and prints it to the console.
# Ensure that the file exists in the same directory as this script or provide the correct path to
# the file if it is located elsewhere. If the file does not exist, an error will be raised.
# If you want to handle the case where the file might not exist, you can use a try-except block like this:
