'''
===============================================================

    A simple class with diverse methods of check palindrome.
    Just a little fun.

===============================================================
'''



class CheckPalindrome:
    def __init__(self, input_word: str):
        self.__users_word = input_word

    def is_palindrome_first_way(self) -> bool:
        words_len = len(self.__users_word)
        for i in range(words_len):
            if self.__users_word[i] != self.__users_word[words_len - 1 - i]:
                return False
        return True

    def is_palindrome_second_way(self) -> bool:
        return self.__users_word == self.__users_word[::-1]

    def is_palindrome_third_way(self) -> bool:
        return self.__users_word == ''.join(reversed(self.__users_word))

