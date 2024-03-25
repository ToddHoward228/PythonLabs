print("\tЗавдання 1")
#      1   5    10        ⩔20
str = "Python is a high-level, general-purpose programming language. \
Its design philosophy emphasizes code readability with the use of significant indentation."

slice_str = str[19:-1]

print(slice_str)

print("\tЗавдання 2")

word = "внутрішньоконтинентальний"

max_count = 0
cur_count = 0
character = 'w'

for char in word:
    cur_count = 0
    for j in range(0, len(word)):
        if(word[j] == char):
           cur_count += 1
    if(cur_count > max_count):
        max_count = cur_count
        character = char
        
print("Буква - ", character, "кількість - ", max_count)

print("\tЗавдання 3")

str = "Чашка стояла на столі коли він зайшов і сказав привіт"
words = str.split(' ')

for word in words:
    if(word != "привіт"):
      
