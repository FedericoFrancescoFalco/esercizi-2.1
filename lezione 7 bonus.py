#Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included).
# The numbers should be stored in a list and returned as output.


def find_numbers():
    result = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5!= 0:
            result.append(num)
    return result

print(find_numbers())
print("\n\n")




#Write a function to calculate the factorial of a number given as input. The number should be returned as output. For example:
    #Input: 8
    #Output: 40320

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
print("\n\n")


 #Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. The list is given as input to the function. 
 #All factorials should be returned as output. For example:
#Input: [2, 5, 8, 10]
#Output: [2, 120, 40320, 3628800]


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def compute_factorials(numbers):
    return [factorial(num) for num in numbers]

numbers = [7, 14, 17, 21]
print("Factorials of", numbers, "are", compute_factorials(numbers))

print("\n\n")





#Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output. For example:
#Input: 8
#Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def dictionary_numbers(n):
    return {i: i*i for i in range(1, n+1)}

n= 5
print(dictionary_numbers(n))











#Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a comma-separated sequence after sorting them alphabetically. For example:
        #Input: without,hello,bag,world
        #Output: bag,hello,without,world
















#Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising all sentence characters. For example:
        #Input: Practice makes perfect
        #Output: PRACTICE MAKES PERFECT












    #Write a function accepting an input string defined with whitespace-separated words and returning it after removing all duplicates and sorting each word alphanumerically. For example:
        #Input: hello world and practice makes perfect and hello world again
        #Output: again and hello makes perfect practice world











    #Write a function to check whether a string is a pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once.
        #Input: The quick brown fox jumps over the lazy dog
        #Output: True











    #Write a function to check whether a number is "Perfect" or not. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). For example:
        #Input: 6
        #Output: True










    #Using the code implemented in Exercise 8, write a function that, given a number n as input, computes all "Perfect" numbers between 1 and n. For example:
        #Input: 500
        #Output: [6, 28, 496]









    #Write a function to sort the (name, age, height) input list of tuples by ascending order where name is string, age and height are numbers. The function should return a list of tuples of strings. The priority is that name > age > score. Namely, the sort criteria are:
        #Sort based on name;
        #Then, sort based on age;
        #Then, sort by score.

        #Input: [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]
        #Output:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]       