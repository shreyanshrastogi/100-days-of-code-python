from art import logo
def addition(n1, n2):
    return n1 + n2
def substraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division (n1,n2):
    return n1/n2


operators={
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division
}

while True:
    print(logo)
    result=0
    n1 = int(input("Type first number: "))

    while True:
        operation = input("type operator +,-,*,/: ")
        n2 = int(input("Type next number: "))
        result = operators[operation](n1, n2)
        n1 = result
        print(result)
        continued = input("do you want to continue with same calculation yes or no?: ").strip().lower()
        if continued == "no":
            break




