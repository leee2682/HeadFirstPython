# nums = [1, 2, 3, 4]
# nums
# nums.remove(3)
# nums

# nums.pop()
# nums

# nums.pop(0)
# nums

# nums = [2]
# nums.extend([3,4])
# nums

# nums.insert(0,1)
# nums.insert(2,'two-and-a-half')
# nums

# phrase = "Dont't panic!"
# plist = list(phrase)
# phrase
# plist

# for i in range(4):
#     plist.pop()

# plist.pop(0)
# plist.remove("'")
# plist

# first = [1, 2, 3, 4, 5]
# first

# second = first
# second

# second.append(6)
# second
# first

# third = second.copy()
# third

# third.append(7)
# third
# second

# saying = "Don't panic!"
# letters = list(saying)

# letters

# letters[0]
# letters[-1]

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowels in found:
    print(vowels)