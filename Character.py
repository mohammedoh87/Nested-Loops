string = input("Enter a word: ")
char = input("Enter a character of your choice: ")

i = 0
count = 0

while(i < len(string)):
    if(string[i] == char):
        count += 1
    i = i + 1

print("The total number of times ", char, " has occurred ", string, " is ", count)