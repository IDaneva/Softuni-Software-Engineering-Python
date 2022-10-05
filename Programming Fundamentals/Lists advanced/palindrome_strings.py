words = input().split()
palindrome = input()

palindrome_strings = [current_word for current_word in words if current_word == current_word[::-1]]
print(palindrome_strings)
print(f"Found palindrome {palindrome_strings.count(palindrome)} times")