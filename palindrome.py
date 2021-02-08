mot = input("Ecrivez un mot : ")


def is_palindrome(mot):
    for i in range(len(mot) // 2):
        if mot[i] != mot[-i - 1]:
            return False
    return True


if is_palindrome(mot):
    print("C'est un Palindrome")
else:
    print("Ce n'est pas un palindrome")

# correction
# word = input('Votre mot: ')
# my_range = range(len(word))
# is_palindrome = True

# for i in my_range:
#     if word[i] == word[-1-i]:
#         "cas d'un palindrome"
#     else:
#         "ce n'est pas un palindrome"
#         is_palindrome = False
#
# print(is_palindrome)