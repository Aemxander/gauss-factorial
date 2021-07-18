#gauss factorial of a number n is defined as the product of all positive numbers <= n that are relatively prime to n

#project euler problem
#G(n) =
#n
#pi notation -> gauss factorial(i)
#i=1



def CheckIfPositivePrime(value):
    if value <= 0:
        return False
    if value == 1 or value == 2 or value == 3:
        return True
    else:
        if value % 2 == 0 or value % 3 == 0:
            return False
        else:
            return True



def FindFactors(value):
    if value <= 1:
        return []
    else:
        factorsArray = []

        for i in range(2, value):
            if value % i == 0:
                factorsArray.append(i)

        return factorsArray



def FindCoprimeNumbers(value):
    primeArray = []
    nonPrimeArray = []

    for i in range(1,value):
        if CheckIfPositivePrime(i) == True:
            primeArray.append(i)
        else:
            nonPrimeArray.append(i)

    factorsArray = FindFactors(value)
    coprimeArray = []

    for i in primeArray:
        if factorsArray.__contains__(i) == False:
            coprimeArray.append(i)

    for i in nonPrimeArray:
        factorsArrayForNonprime = FindFactors(i)
        hasSameFactors = False

        for j in factorsArrayForNonprime:
            if factorsArray.__contains__(j) == True:
                hasSameFactors = True

        if hasSameFactors == False:
            coprimeArray.append(i)

    return coprimeArray



def FindProductOfArray(values):
    if values == []:
        return

    product = values[0]

    for i in values:
        product *= i

    return product



def FindGaussFactorial(value):
    coprimeArray = FindCoprimeNumbers(value)
    product = FindProductOfArray(coprimeArray)

    return product



#gauss factorial of a number n is defined as the product of all positive numbers <= n that are relatively prime to n

#project euler problem
#G(n) =
#n
#pi notation -> gauss factorial(i)
#i=1



def AnswerProblem(n):
    gaussFactorialArray = []

    for i in range(1, n + 1):
        if FindGaussFactorial(i) != None:
            gaussFactorialArray.append(FindGaussFactorial(i))
    return FindProductOfArray(gaussFactorialArray)



#question is find G(10^8) mod 1 000 000 007
answer = AnswerProblem(10**8) % 1000000007



