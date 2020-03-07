string = str(input("Words: "))
l = len(string)

for i in range(l // 2):
    if string[i] != string[-1-i]:
        print("It's not palindrome")
        quit()
print("It's palindrome") 





