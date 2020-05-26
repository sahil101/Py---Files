# def exchange(str1):
#     s = str1[0]
#     s1 = str1[len(str1)-1]
#     s2 = ''
#     s2 = s2 + s1
#     for char in range(1,len(str1)-1):
#         s2 = s2 + str1[char]
#     s2 =  s2 + s
#     return s2
# print(exchange("12345"))



#count number of characters frequency in a string



# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google'))


# Write a Python program to remove the nth index character from a nonempty string
# def remove_char(str, n):
#     first_part = str[:n]
#     last_pasrt = str[n + 1:]
#     return first_part + last_pasrt
#
#
# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))



# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


#  Write a Python program to count the occurrences of each word in a given sentence
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('the quick brown fox jumps over the lazy dog.'))