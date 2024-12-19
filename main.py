from nash_equilibrium import NashEquilibrium


def matrixInput(rows, columns):
    matrix = []
    print("\nAll cells must be entered in the form a,b where a is the payoff for player 1 and b is the payoff for player 2\n")
    
    for m in range(0, rows):
        row = []
        for n in range(0, columns):
            errorFlag = True
            while errorFlag:
                inputCell = input(f"Enter the values for cell {m + 1},{n + 1}: ")
                try:
                    newCell = list(map(float, inputCell.split(",")))
                except:
                    print("The entered cell contains a non allowed character")
                if len(newCell) == 2:
                    row.append(newCell)  
                    errorFlag = False
                else:
                    print("The entered cell is not in the correct format, try again")
        
        matrix.append(row)

    return matrix 


def main():
    typeResponse = input("Press any key to start or type exit to stop: ")
    inputResponse = ""

    while typeResponse != "exit" or inputResponse != "exit":
        print("_______________________________________________________")
        print("If you would like to calculate the Nash eqilibriums of a game press n")
        print("If you would like to exit simply type exit")
        typeResponse = input("Enter your choice: ")

        if typeResponse != "n" and typeResponse != "exit":
            print("Input is not a valid menu choice")
            continue
        print()

        if typeResponse == "exit":
            break


        while True:
            rows_input = input("Enter the number of strategies for player 1: ")
            if rows_input.isdigit() and int(rows_input) > 0:
                rows = int(rows_input)
                break
            else:
                print("Invalid input. Please enter a positive integer for Player 1 strategies.")

        while True:
            columns_input = input("Enter the number of strategies for player 2: ")
            if columns_input.isdigit() and int(columns_input) > 0:
                columns = int(columns_input)
                break
            else:
                print("Invalid input. Please enter a positive integer for Player 2 strategies.")

        matrix = matrixInput(rows, columns)

        if matrix == None:
            continue


        nash_game = NashEquilibrium(matrix)
        nash_game.print_mix_strategies()
        nash_game.print_pure_strategies()

        if inputResponse == "exit":
            break



main()