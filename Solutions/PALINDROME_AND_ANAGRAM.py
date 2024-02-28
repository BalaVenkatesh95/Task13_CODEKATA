string01, string02 = map(str, input().split())
reversed_string01 = string01[::-1]
reversed_string02 = string02[::-1]
anagram_count = 0
palindrome_count = 0
if string01 == reversed_string01 and string02 == reversed_string02:
    palindrome_count = palindrome_count + 1
if sorted(string01) == sorted(string02):
    anagram_count = anagram_count + 1
if palindrome_count and anagram_count == 1:
    print(1)
else:
    print(0)
