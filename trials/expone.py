import math

def exp(x):

    return sum([
        x**n / math.factorial(n)

        for n in range(0,100)
    ])

def main():

    k=int(input("Enter number:"))
    answer=exp(k)
    print(f"The answer is: {answer}")

if __name__=='__main__':
    main()