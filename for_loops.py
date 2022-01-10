print("1. From individual words to a quoted string.")
words = ["Ich", "bin", "der", "Flash!"]
w_range = range(len(words))
string = ""

for w in w_range:
    if w < len(words):
        string += words[w] + " "
    else:
        string += words[w]
print(string)

print("2. reverse Flash!")
rev_str= ""
for w in w_range:
    w_rev = words[w][::-1]
    if w < len(words):
        rev_str += w_rev + " "
    else:
        rev_str += w_rev
print(rev_str)

print("3. Palindrome words.")
word = "revive"
palindrome = "is a PALINDROME!!!"

for w in range(len(word)//2):
    if word[w] != word[len(word)-w-1]:
        palindrome = "is not a palindrome!"
print(f"{word} {palindrome}")

print("4. string slicing.")
string2 = "impossible"

for s in range(len(string2)//2, len(string2)):
    print(string2[s])

print("5. output results in length of 3 substrings without the index\
 of 0, or -1.")
for t in range(1, len(string2)-3):
    print(string2[t:t+3])

print("6. working with symbols.")
for i in range(7):
    if i%2 == 0:
        print("@"*i)
    else:
        print("#"*i)

print("7. Count of a substring")
text = "impossible"
substr = "i"
counter = 0

for i in range(len(text)-len(substr)+1):
    if text[i:i+len(substr)] == substr:
        counter += 1
print(f"{substr}:{counter}")

print("8. Finding count of vowels in a string.")
string3 = 'armageddon'
vowels = 'aeiou'
vowel = 0

for i in range(len(string3)):
    if string3[i] in vowels:
        vowel += 1
print(f"There are {vowel} vowels in {string3}.")


