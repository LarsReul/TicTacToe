class Field:
    def __init__(self, ticString: str = "_________"):
        self.field = self.initializeField(ticString)
        self.possibleMoves = self.createPossibleMoves()

    def initializeField(self, inputString) -> list:
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

    def printField(self):
        """
        Prints the tic tac toe field

        Parameters
        ----------
        field : list
            List in form of a matrix containing the tic tac toe field
        """
        print("---------")
        for row in self.field:
            print("| ", end="")
            for tic in row:
                if tic == "_":
                    print("  ", end="")
                else:
                    print(tic + " ", end="")
            print("|")
        print("---------")

    def getColumn(self, column: int) -> list:
        return [row[column] for row in self.field]

    def checkField(self) -> int:
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
        outcomes = self.getAllOutcomes()

        # check for winning conditions
        win_x = ["X", "X", "X"]
        win_O = ["O", "O", "O"]

        if win_x in outcomes:
            return 1

        if win_O in outcomes:
            return 2

        for row in self.field:
            if "_" in row:
                # print("Game not finished")
                return 0

        return 3

    def printWinner(self):
        check = self.checkField()
        if check == 1:
            print("X wins")
        if check == 2:
            print("O wins")
        if check == 3:
            print("Draw")

    def getAllOutcomes(self):
        outcomes = []
        # add all rows
        for row in self.field:
            outcomes.append(row)

        # add all columns
        for i in range(len(self.field[0])):
            outcomes.append(self.getColumn(i))

        # add diagonals
        row = []
        for i in range(len(self.field)):
            row.append(self.field[i][i])
        outcomes.append(row)

        row = []
        length = len(self.field)
        for i in range(length):
            length -= 1
            row.append(self.field[length][i])
        outcomes.append(row)

        return outcomes

    def countOccurrences(self) -> list:
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

        for row in self.field:
            for entry in row:
                if entry == "X":
                    countX += 1
                elif entry == "O":
                    countO += 1
                else:
                    count_ += 1

        return [countX, countO, count_]

    def createPossibleMoves(self) -> set:
        moves = []
        for i in range(3):
            for j in range(3):
                moves.append((i + 1, j + 1))

        return set(moves)

    def getEmptyPositions(self):
        emptyPositions = []
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == "_":
                    emptyPositions.append((i+1, j+1))
        return emptyPositions

    def currentPlayer(self):
        occurrences = self.countOccurrences()
        if occurrences[0] <= occurrences[1]:
            return "X"
        else:
            return "O"

    def winningPlayer(self):
        if self.checkField() == 1:
            return "X"
        if self.checkField() == 2:
            return "0"
        return None

    def minimax(self):
        pass

    def setTic(self, coordinates: list):
        occurrences = self.countOccurrences()
        if occurrences[0] <= occurrences[1]:
            self.field[coordinates[0] - 1][coordinates[1] - 1] = "X"
        else:
            self.field[coordinates[0] - 1][coordinates[1] - 1] = "O"

    def clearTic(self, coordinates: list):
        self.field[coordinates[0] - 1][coordinates[1] - 1] = "_"


if __name__ == "__main__":
    field = Field("X_O__OXOX")
    print(field.currentPlayer())