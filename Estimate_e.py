class Estimate_e:
    # main method
    def main():

        # take in a number from the user to be used in the sumation
        num = int(input("What bound do you want for the sum of e? "))

        # display the result
        print ("e =" , sumation(num))

    # find the factorial of a number
    def factorial(n):

        # if you reached 1 return 1 because if you return 0
        # your answer will be 0
        if (n == 1):
            return 1
        # otherwise return n times the result of n - 1
        else:
            return (n * factorial(n - 1))

    # estimate e using a sumation
    def sumation(n):

        # estimate e based on the sumation bound you inputed
        # e = 1 + (1/1!) + (1/2!) + (1/3!) + ...
        i = 0
        e = 1.0
        while (i < n):
            e = e + (1/factorial(n))
            i = i + 1
            
        return e
