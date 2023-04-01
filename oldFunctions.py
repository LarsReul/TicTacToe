import random


def initializeField(inputString: str) -> list:
    """
    Initializes a 3 by 3 tic tac toe field, based on a given String

    Parameters
    ----------
    inputString : str
        A String with a length of exactly 9 characters,
        consisting only of the characters 'X', '0' and '_'

    Return
    ----------
    list
        a list in form of a 3 by 3 matrix
    """
    allowedSymbols = "XO_"

    if not (isinstance(inputString, str) and len(inputString) == 9 and all(
            char in allowedSymbols for char in inputString)):
        print("input has to be a string of length 9, containing only X, O and _")
        return []

    # create and populate the tic tac toe field as matrix
    field = []
    for i in range(3):
        field.append([])
        for j in range(3):
            field[i].append(inputString[3 * i + j])

    return field


def initializeEmptyField() -> list:
    return initializeField("_________")


def printField(field: list):
    """
    Prints the tic tac toe field

    Parameters
    ----------
    field : list
        List in form of a matrix containing the tic tac toe field
    """
    print("---------")
    for row in field:
        print("| ", end="")
        for tic in row:
            if tic == "_":
                print("  ", end="")
            else:
                print(tic + " ", end="")
        print("|")
    print("---------")


def getColumn(field: list, column: int) -> list:
    return [row[column] for row in field]


def checkField(field: list) -> int:
    """
    checks the given field for tic tac toe winning conditions

    Parameters
    ----------
    field : list
        List in form of a matrix containing the tic tac toe field

    Returns
    ----------
    int
        0 - if there are still open spaces and no winning condition is triggered
        1 - if X has three in a row
        2 - if 0 has three in a row
        3 - if no fields are open and no winning condition was reached
    """
    outcomes = []
    # add all rows
    for row in field:
        outcomes.append(row)

    # add all columns
    for i in range(len(field[0])):
        outcomes.append(getColumn(field, i))

    # add diagonals
    row = []
    for i in range(len(field)):
        row.append(field[i][i])
    outcomes.append(row)

    row = []
    length = len(field)
    for i in range(length):
        length -= 1
        row.append(field[length][i])
    outcomes.append(row)

    # check for winning conditions
    win_x = ["X", "X", "X"]
    win_O = ["O", "O", "O"]

    if win_x in outcomes:
        print("X wins")
        return 1

    if win_O in outcomes:
        print("O wins")
        return 2

    for row in field:
        if "_" in row:
            # print("Game not finished")
            return 0

    print("Draw")
    return 3


def countOccurrences(field: list) -> list:
    """
    counts the occurrences of 'X', 'O' and '_' characters in a matrix

    Parameters
    ----------
    field : list
        List in form of a matrix containing the tic tac toe field

    Returns
    ----------
    list
        contains number of X's, number of O's and number of _
    """
    countX = 0
    countO = 0
    count_ = 0

    for row in field:
        for entry in row:
            if entry == "X":
                countX += 1
            elif entry == "O":
                countO += 1
            else:
                count_ += 1

    return [countX, countO, count_]


def getUserInput() -> list:
    """
    prompts user to input two coordinates, which have to be two integers

    Returns
    ----------
    list
        the two coordinates as list
    """
    userInput = input("Enter the coordinates:").split()
    coordinates = []

    # if len(userInput) != 2:
    #     print("There should only be two coordinates separated by a space!")
    #     return []

    try:
        for coordinate in userInput:
            coordinates.append(int(coordinate))
    except ValueError:
        print("You should enter numbers!")
        return []

    if not (coordinates[0] in [1, 2, 3] and coordinates[1] in [1, 2, 3]):
        print("Coordinates should be from 1 to 3!")
        return []

    return coordinates


def setUserCoordinates(field: list, possibleMoves: set) -> list:
    coordinates = []

    while not coordinates:
        coordinates = getUserInput()
        if not coordinates:
            continue

        if tuple(coordinates) in possibleMoves:
            setTic(field, coordinates)
            possibleMoves.remove(tuple(coordinates))
        else:
            coordinates = []
            continue


def computerMove(field: list, possibleMoves: set):
    coordinates = popRandomElement(possibleMoves)
    setTic(field, coordinates)


def setTic(field: list, coordinates: list):
    occurrences = countOccurrences(field)
    if occurrences[0] <= occurrences[1]:
        field[coordinates[0] - 1][coordinates[1] - 1] = "X"
    else:
        field[coordinates[0] - 1][coordinates[1] - 1] = "O"


def createPossibleMoves() -> set:
    moves = []
    for i in range(3):
        for j in range(3):
            moves.append((i+1, j+1))

    return set(moves)


def popRandomElement(mySet: set):
    randomInteger = random.randrange(len(mySet))
    element = list(mySet)[randomInteger]
    mySet.remove(element)
    return element