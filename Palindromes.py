
'''

Author: Tangudu Avinash
Posted: Github
Topic: Data Structures through Python

'''

import string

def sanitize(sentence):
        array = sentence.lower()
        array = array.strip()
        array = array.strip(string.punctuation)
        return array

def check_if_palindrome(array):
        if len(array) < 2:
            return True
        
        if array[0] == array[-1]:
                return check_if_palindrome(array[1:-1])
        else:
            return False

def check_if_palindrome_iter(array):        
    i, j = 0, len(array)-1
    
    while i <= j:
        if array[i] != array[j]:
            return False
        i += 1
        j -= 1
        
    return True
    
    
if __name__ == '__main__':
    sentence = 'Namste Everyone'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == False)
    assert(check_if_palindrome_iter(array) == False)
    
    sentence = ''
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)
    
    sentence = 'Hey..'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)
    
    sentence = 'This is Palindrome'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)
        
    sentence = 'Welcome to Palindromes'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)