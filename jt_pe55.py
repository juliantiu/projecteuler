# !/usr/local/bin/python3

""" 
Julian Tiu
Project Euler #55

Running (assuming python v 3.7.x):
    $ python jt_pe55.py

Answer:
    249

Why I chose this problem:
    One of the assignments I peer taught involved the 196-algorithm (also a common interview question). 
    I remember students having trouble with their algorithms when they reached the number 196. 
    Upon further research, I found out that 196 is a lychrel number and there are a lot of numbers 
    that share the same property. I chose this problem because it involves lychrel numbers--something 
    that intrigues me.

Quick Summary:
    For each number between 1 and 9999 inclusive, I checked if that number has already been discovered
    and known to be a lychrel number. If it is, then stop and add 1 to the count of lychrel numbers. 
    Otherwise keep adding that number to its reverse and stop when it is a palindrome. If it takes
    more than 50 iterations, then it is a lychrel number, then store the results for future reference.


######################################### NOTES

The brute force way of tackling this problem is 
running the 196-algorithm for all numbers from
1 to 9999. This can be achieved in a relatively
few lines of code in python.

Although my solution has more lines of code, it
is has a faster runtime than brute force 
because it uses a dynamic memory technique called 
memoization. Essentially, when the number has
already been visited, then there is no need to
perform the 196-algorithm on it. For instance, if
I know that 196 is a lychrel number, then 691
should also be a lychrel number. (196+691) and its 
reverse should also be a lychrel numbers, and so 
on and so forth.

This is done by using a hash map (python dictionary).
Hash maps data structures have a search speed 
of O(1) due to the mathematical properties of hashing.

############################################"""

# Palindrome check using the str() method in python
def isPalindrome(num):
    return str(num) == str(num)[::-1]

# Reverse number using the str() method in python
def reverse(num):
    return int(str(num)[::-1])

def countLychrelNumbers():
    num_lychrels = 0
    visited = {} # holds the previously discovered lychrel and non-lycrel numbers
    LIMIT_ITERATIONS = 50 # given in the problem statement

    for i in range(10000):
        try :
            # If the number is visited already, we check if it is known to be lychrel
            if visited[i] != 1:
                num_lychrels += 1
            
            # otherwise, it will produce a KeyError meaning the number hasn't been discovered yet
        except KeyError:
            not_palindromes = [] # holds all of the generated new_num's that are not palindromes
            new_num = i
            num_iterations = 0

            # check isPalindrom(new_num + reverse(new_num)) instead of isPalindrome(new_num), because 4994 itself is a lychrel number even though it is a palindrome
            while (not isPalindrome(new_num + reverse(new_num))) and (num_iterations < LIMIT_ITERATIONS):
                not_palindromes.append(new_num)
                new_num = new_num + reverse(new_num)
                num_iterations += 1
                
                try:
                    # checking if the new_num generated is already in the visited dictionary
                    if visited[new_num] != 1:
                        num_iterations = LIMIT_ITERATIONS + 1
                        break
                    else:
                        break
                except:
                    pass

            if num_iterations >= LIMIT_ITERATIONS:
                num_lychrels += 1

                # then all of the generated numbers in not_palindromes[] are lychrels
                for non_palim_num in not_palindromes:
                    visited[non_palim_num] = 0
                    visited[reverse(non_palim_num)] = 0
            else:
                # then all of the generated numbers in not_palindromes[] are non-lychrels
                for non_palim_num in not_palindromes:
                    visited[non_palim_num] = 1
                    visited[reverse(non_palim_num)] = 1
    
    return num_lychrels


if __name__ == "__main__":
    print(countLychrelNumbers())
