import random


def create_anagram(string):
    str2chr = []
    str2chr += string
    str2chr_random = ''.join(random.sample(str2chr, len(string)))
    return str2chr_random


def sort_bubble(string):
    for i in range(len(string)):
        for j in range(len(string) - 1 - i):
            temp = string[j + 1]
            if string[j] > temp:
                temp = string[j]
                string[j] = string[j + 1]
                string[j + 1] = temp
    return string


def str2chr2int(string):
    str2chr = []
    str2chr += string
    chr2int = [ord(c) for c in str2chr]
    return chr2int


def int2chr2str(integer):
    int2chr = [chr(ch) for ch in integer]
    chr2str = ''.join(int2chr)
    return chr2str


def compare2str(str1, str2):
    if len(str1) == len(str2):
        s1_str2chr2int = str2chr2int(str1)
        s2_str2chr2int = str2chr2int(str2)

        s1_sort = sort_bubble(s1_str2chr2int)
        s2_sort = sort_bubble(s2_str2chr2int)

        str1 = int2chr2str(s1_sort)
        str2 = int2chr2str(s2_sort)

        if str1 == str2:
            print("Yes ,these strings are anagrams")
        else:
            print("No ,these strings are not anagrams")
    else:
        print("Two Strings Size Not Equal")


string_1 = ""
loop = 1
print("Please, enter two strings for comparing them that are anagram or not")
print("If the program is created an anagram string, you only enter first string")

while loop == 1:
    string_1 = input("First String: ")
    if string_1 == "":
        print("You can not enter first string as empty , please enter a proper string")
    else:
        loop = 0

string_2 = input("Second String: ")

if string_2 == "":
    string_2 = create_anagram(string_1)

print("First string: " + string_1)
print("Second string: " + string_2)

compare2str(string_1, string_2)
