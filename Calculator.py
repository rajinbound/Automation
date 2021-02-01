import math

while True:
    print("Choose the math operation:  \n\n0 - Addition\n1 - Subtractions\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    oper = input("\nYour option from the menu: ")
    #Sum of two value addition
    if oper == "0":
        val1 = float(input(("\nFirst Value: ")))
        val2 = float(input(("\nSecond Value: ")))

        print("\nThe Result is: " + str(val1 + val2 ) + "\n")

        back = input("\nGo back to the main menu? (y/n): ")
        if back =="y":
            continue
        else:
            break
    #substraction
    elif oper == "1":
        val1 = float(input(("\nFirst Value: ")))
        val2 = float(input(("\nSecond Value: ")))

        print("\nThe Result is: " + str(val1 - val2 ) + "\n")

        back = input("\nGo back to the main menu? (y/n): ")
        if back =="y":
            continue
        else:
            break
    #Multiplication
    elif oper == "2":
        val1 = float(input(("\nFirst Value: ")))
        val2 = float(input(("\nSecond Value: ")))

        print("\nThe Result is: " + str(val1 * val2) + "\n")

        back = input("\nGo back to the main menu? (y/n) : ")
        if back == "y":
            continue
        else:
            break
    #Divitision
    elif oper == "3":
        val1 = float(input(("\nFirst Value: ")))
        val2 = float(input(("\nSecond Value: ")))

        print("\nThe Result is: " + str(val1 / val2) + "\n")

        back = input("\nGo back to the main menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #Modulo
    elif oper == "4":
        val1 = float(input(("\nFirst Value ")))
        val2 = float(input(("\nSecond Value ")))

        print("\nThe Result is: " + str(val1 % val2 ) + "\n")

        back = input("\nGo back to the main menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #Raising to a power
    elif oper == "5":
        val1 = float(input(("\nFirst Value ")))
        val2 = float(input(("\nSecond Value ")))

        print("\nThe Result is: " + str(math.pow(val1, val2)) + "\n")

        back = input("\nGo back to the main menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #Squar root
    elif oper == "6":
        val1 = float(input(("\nEnter the value for extracting the square root ")))

        print("\nThe Result is: " + str(math.sqrt(val1)) + "\n")

        back = input("\nGo back to the main menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #logarithm
    elif oper == "7":
        val1 = float(input(("\nFirst The value for calculating the logarithm  to base of 2: ")))

        print("\nThe Result is: " + str(math.log(val1, 2)) + "\n")

        back = input("\nGo back to the main6 menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #Sine
    elif oper == "8":
        val1 = float(input(("\nFirst The value (in degree)for calculating the sine ")))

        print("\nThe Result is: " + str(math.sin(math.radians(val1))) + "\n")

        back = input("\nGo back to the main6 menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #COSINE
    elif oper == "9":
        val1 = float(input(("\nFirst The value (in degree)for calculating the cosine ")))

        print("\nThe Result is: " + str(math.cos(math.radians(val1))) + "\n")

        back = input("\nGo back to the main6 menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #Tangent
    elif oper == "9":
        val1 = float(input(("\nFirst The value (in degree)for calculating the cosine ")))

        print("\nThe Result is: " + str(math.tan(math.radians(val1))) + "\n")

        back = input("\nGo back to the main6 menu? (y/n): ")
        if back == "y":
            continue
        else:
            break
    #handling invalid options
    else:
        print("\nInvalid option!")
        continue