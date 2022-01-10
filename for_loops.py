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