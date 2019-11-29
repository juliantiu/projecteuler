/* 
Julian Tiu
Project Euler #4

Compilation:
    $ g++ jt_pe4.cpp -o jt_pe4

Running:
    $ time ./jt_pe4
    or
    $ ./jt_pe4

Answer:
    906609

Why I chose this problem:
    As I am new to Project Euler, I thought I would test the waters with the first few problems.
    Problems 1-3 proved to be rather trivial. When I sorted by "solved by" I noticed that Problem 4
    was the first problem usually skipped, and that's why I chose problem 4 as warm up. Problem 4
    is also the first problem ranked "medium" in Hackerrank's Project Euler+.

Quick Summary:
    - Find the palindromes starting from 999*999
    - Decrement through and determine if that value is divisble by a 3-digit number
    - If it is, determine if both the multiplier and multiplicand are 3-digit numbers
        - If so, return that number


********************************************* NOTES
FINAL ATTEMPT

The final attempt is different from the other 
attempts due to the function returning
right when it finds the first large palindrome 
that can be factored by two 3-digit numbers rather 
than generating a product between each possible 
3-digit numbers and checking if each product is 
a palindrome.

Moreover, the nested loop only runs when the 
large number is a palindrome.

Using the Unix/Linux time command confirms that the
final implementation is faster than the first two
**************************************************/

#include <iostream>

using namespace std;

// returns true if the number is a palindrome
bool isPalindrome(int num) {
    int digit = 0;
    int reversedNum = 0;
    int originalNum = num;
    
    while(originalNum != 0) {
        digit = originalNum%10;
        reversedNum = (reversedNum*10) + digit;
        originalNum /= 10;
    }

    return num == reversedNum;
}

// returns the largest palindrome divisible by two 3-digit numbers
int findLargestPalDiv3Digits() {
    const int STARTING_3_DIGIT_NUM = 100;
    const int ENDING_3_DIGIT_NUM = 1000;
    const int LARGEST_MULT_3_DIGIT_NUM = 999*999;
    const int SMALLEST_MULT_3_DIGIT_NUM = 100*100;
    int i, j;

    // start from the largest possible product of two 3-digit numbers 
    // all the way to the lowest possible product of two 3-digit numbers
    for(i = LARGEST_MULT_3_DIGIT_NUM; i > SMALLEST_MULT_3_DIGIT_NUM - 1; i--) {
        if(isPalindrome(i)) {
            for(j = STARTING_3_DIGIT_NUM; j < ENDING_3_DIGIT_NUM; j++) {

                // check if i is divisble by a 3-digit number and
                // check if its multiplicand is also a 3-digit number
                if((i%j == 0) && (i/j < ENDING_3_DIGIT_NUM)) {
                    return i;
                }
            }
        }
    }

    return 0;
}

int main(int argc, char * argv[]) {
    cout << findLargestPalDiv3Digits() << endl;
    return 0;
}

/******************************************** NOTES
FIRST ATTEMPT

Natural intuition calls for multiplying two 
3-digit numbers one by one and checking each 
product to see if it is a palindrome and then
comparing which is the largest palindrome.

This would cause a running time of O(n^2) 
where n is the count of all the possible 
3-digit numbers
**************************************************

#include <limits> // For numeric_limits<int>::min()
#include <iostream>

using namespace std;

// returns true if the number is a palindrome
bool isPalindrome(int num) {
    int digit = 0;
    int reversedNum = 0;
    int originalNum = num;
    
    while(originalNum != 0) {
        digit = originalNum%10;
        reversedNum = (reversedNum*10) + digit;
        originalNum /= 10;
    }

    return num == reversedNum;
}

// returns the largest palindrome divisible by two 3-digit numbers
int findLargestPalDiv3Digits() {
    const int STARTING_3_DIGIT_NUM = 100;
    const int ENDING_3_DIGIT_NUM = 1000;
    int i, j;
    int product;
    int max = numeric_limits<int>::min();

    for(i = STARTING_3_DIGIT_NUM; i < ENDING_3_DIGIT_NUM; i++) {
        for(j = STARTING_3_DIGIT_NUM; j < ENDING_3_DIGIT_NUM; j++) {
            product = i*j;

            // When multiplying i and j, determine if it is a palindrome
            // and if it is larger than the previous large palindrome product
            if(isPalindrome(product) && product > max) {
                max = product;
            }
        }
    }

    return max;
}

int main(int argc, char * argv[]) {
    cout << findLargestPalDiv3Digits() << endl;
    return 0;
} */

/******************************************** NOTES
SECOND ATTEMPT

From the first attempt, I noticed that a lot 
of multipliers and multipicands are symmetric 
and yields the same product; i.e. (1*2) and 
(2*1). There's no need to do both. Therefore
start the j index at i
***************************************************

#include <limits> // For numeric_limits<int>::min()
#include <iostream>

using namespace std;

// returns true if the number is a palindrome
bool isPalindrome(int num) {
    int digit = 0;
    int reversedNum = 0;
    int originalNum = num;
    
    while(originalNum != 0) {
        digit = originalNum%10;
        reversedNum = (reversedNum*10) + digit;
        originalNum /= 10;
    }

    return num == reversedNum;
}

// returns the largest palindrome divisible by two 3-digit numbers
int findLargestPalDiv3Digits() {
    const int STARTING_3_DIGIT_NUM = 100;
    const int ENDING_3_DIGIT_NUM = 1000;
    int i, j;
    int product;
    int max = numeric_limits<int>::min();

    for(i = STARTING_3_DIGIT_NUM; i < ENDING_3_DIGIT_NUM; i++) {
        for(j = i; j < ENDING_3_DIGIT_NUM; j++) {
            product = i*j;

            // When multiplying i and j, determine if it is a palindrome
            // and if it is larger than the previous large palindrome product
            if(isPalindrome(product) && product > max) {
                max = product;
            }
        }
    }

    return max;
}

int main(int argc, char * argv[]) {
    cout << findLargestPalDiv3Digits() << endl;
    return 0;
} */

