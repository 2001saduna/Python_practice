'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''

def plusOne(digits):

    s = [str(digit) for digit in digits]
    joined_digit = int("".join(s))
    result_digit = str(joined_digit+1)
    result_list = result_digit.split()
    result = [int(digit) for digit in result_list]
    print(result)

    
    


'''
-> convert to string numbers s = [str(i) for digit in digits]
-> join numbers joined_digit = int("".join(s))
-> convert it into an integer int(joined_digit)
-> add 1
-> convert the result integer into a string
-> split it into a list
-> convert the string back to ints s = [int(i) for digit in result_list]
-> join numbers
-> unjoin the numbers
'''

#Model solution
class Solution:
    def plusOne(self, digits):
        # converting the int list into one string number
        strings = ""
        # going through each number in the list of digits
        for number in digits:
            #converting each number to string and addign it to the strings variable
            strings += str(number)

        # made a temp variable to store the result of the calculation as a string
        temp = str(int(strings) +1)

        # return the numbers as a ints in the list
        return [int(temp[i]) for i in range(len(temp))]

