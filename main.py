import os

art_file = input("Enter the name of the ASCII art file (ascii_art.txt or ascii_art2.txt): ")
if art_file == "ascii_art.txt" or art_file == "ascii_art2.txt":
    if os.path.exists(art_file):
        with open(art_file, "r") as f:
            art = f.read()
            print(art)
    else:
        print(f"Error: File '{art_file}' not found.")
else:
    print("Invalid file name. Please enter 'ascii_art.txt' or 'ascii_art2.txt'.")
    
