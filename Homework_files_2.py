import os

if os.path.exists("exclusive_mode.txt"):
    print("File already exists.")
else:
    file = open("exclusive_mode.txt", 'x')
    file.write("some text")
    print("File created and text written successfully.")

    file.close()