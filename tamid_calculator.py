def main():
    if __name__ == '__main__':
        main()
#welcome statement
print("Welcome to the TAMID Calculator!")

play = True #loop condition

while play: #calc loop
    start = str(input(("\nWould you like to calculate something (y/n): ")))
    
    if start == "y": #calculation 
        operand_1 = float(input("\nPlease enter the first number: "))
        operand_2 = float(input("Please enter the second number: "))

        function = str(input("Please enter your function: "))

        #calculation conditions
        if function == "+": #addition
            result = (operand_1 + operand_2)

        elif function == "-": #subtraction
            result = (operand_1 - operand_2)

        elif function == "*": #multiplication
            result = (operand_1 * operand_2)

        elif function == "/": #division
            if operand_2 == 0: #division by 0 error condition
                print("\nYou cannot divide by 0!")
                continue
            result = (operand_1 / operand_2)

        elif function == "%": #modulus
            operand_1 = int(operand_1)
            operand_2 = int(operand_2)
            result = (operand_1 % operand_2)

        print(f"\nThe result is:  {str(result)}") #output statement

    else: #exit conditions
        print("\nThanks for coming!")
        play = False

