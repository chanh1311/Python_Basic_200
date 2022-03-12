# import operator

# count_key = {}
# key = []
# values = []
# string = input().split()
# for x in string:
#     count_key[x] = string.count(x)

# print(count_key)
# print(count_key.items())  # chuyen dict thanh list cac tuple
# # sap xep theo thu thu tu cai
# count_key_sorted = sorted(count_key.items())
# for x, y in count_key_sorted:
#     print("{}:{}".format(x, y))
##############################################
freq = {}  # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word, 0) + 1
    # Bài tập Python 25 Code by Quantrimang.com
words = sorted(freq.keys())  # sap xep cac khoa, dau ra la list cac key
print(words)
for w in words:  # duyet cac key va hien thi
    print("%s:%d" % (w, freq[w]))
