# Assignment 6 Problems 2-6
# CS 311
# Daniel Jensen

#calls all problem functions and passes any required inputs
def main():
    problem2()
    newLine(1)

    problem3()
    newLine(1)

    problem4()
    newLine(1)

    problem5()
    newLine(2)

    intList = [2, 4, 6, 8, 10, 12, 14]
    listSize = len(intList)
    num = 9
    problem6(intList, listSize, num)

#calculates total cost including tax of a router purchase
def problem2():
    print("Problem 2:")

    routerCost = 109.99
    tax = 0.12
    numRoutersSold = 5
    print("The cost of %s routers sold is : $%.2f" % (numRoutersSold, (routerCost * numRoutersSold * (1 + tax))))

#takes user score and returns received grade
def problem3():
    print("Problem 3:")

    #Asks user for score
    score = float(input("What score was received on the exam? (0-100):"))
    if(score >= 90 and score <= 100):
        grade = "A"
    elif(score >= 80 and score < 90):
        grade = "B"
    elif (score >= 70 and score < 80):
        grade = "C"
    elif (score >= 60 and score < 70):
        grade = "D"
    elif ( score < 60):
        grade = "F"
    else:
        print("Please enter a valid score between 0 and 100.")
        problem3()

    #Outputs the achieved score
    print("The grade achieved on the exam was: " + grade)

# calculates tip for a meal
def problem4():
    print("Problem 4:")
    #asks user for meal cost
    cost = float(input("How much did your meal cost? (ex. 45.89): "))

    #asks user for tip percentage
    percent = float(input("What percentage tip would you like to leave? (ex. 18): "))
    tipPercent = percent/100;
    percent = f"{tipPercent:.0%}"

    #outputs result
    print("A %s tip on a $%s meal is: %.2f" % (percent, cost, (cost * tipPercent)))

#given a list, multiply all values by 5
def problem5():
    print("Problem 5:")

    numList = [2, 4, 6, 8, 10, 12, 14]
    for x in numList:
        print(x * 5, end=' ')

#accepts an array, size of array, and a number. Prints all integers greater than the number
def problem6(intList, size, n):
    print("Problem 6:")

    for x in intList:
        if x > n:
            print(x, end=' ')


def newLine(x):
    i = 1
    while i <= x:
        print(' ')
        i += 1

if __name__ == '__main__':
    main()


