#!/usr/bin/python3
"""Challenge 67 - Looping Vampires"""

def new_vampire_file(line):
    """new file for lines that have vampire"""

    line.rstrip("\n")

    with open("vampytimes.txt", "a") as vampire_file:
        vampire_file.write(line + "\n")

    return line

def main():
    """runtime"""

    count_dracula = 0;

    with open("dracula.txt") as dracula:
        for line in dracula:
            if "vampire" in line.lower():
                count_dracula += 1 
                print(line)
                
                new_vampire_file(line)

    print("Total number of lines witht the word vampire: ", count_dracula)

if __name__ == "__main__":
    main()
