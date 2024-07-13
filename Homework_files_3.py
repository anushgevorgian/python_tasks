file = open("specific_position.txt", 'w')
file.write("some text")
file.close()

file = open("specific_position.txt", 'r+')
file.seek(5)
file.write("new text")
print("File created and text written successfully.")

file.close()