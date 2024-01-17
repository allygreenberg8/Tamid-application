def main():
    if __name__ == '__main__':
        main()

my_list = ["TAMID", "IS", "THE", "COOLEST"] #example list

longest = 0
for word in my_list: #find the longest word in the list
    if len(word) > longest:
        longest = len(word)

longest += 5 #add to the longest word - accounts for the asterisks and spaces

print("*" * (longest-1)) #top border

#loops through the list prints words and asterisks with the correct spacing
for word in my_list:
    print(f"* {word}{' ' * (longest - len(word) - 4)}*")

print("*" * (longest-1)) #bottom border