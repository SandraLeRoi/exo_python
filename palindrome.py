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
word = input('Votre mot: ')


my_range = range()
