from abc import ABC, abstractmethod
import random
import fieldClass
import minmax


class Player(ABC):
    @abstractmethod
    def makeMove(self, field: fieldClass.Field):
        pass


    def popRandomElement(self, mySet: set):
        randomInteger = random.randrange(len(mySet))
        element = list(mySet)[randomInteger]
        mySet.remove(element)
        return element


class User(Player):
    def makeMove(self, field: fieldClass.Field):
        self.setUserCoordinates(field)

    def getUserInput(self) -> list:
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

    def setUserCoordinates(self, field: fieldClass.Field) -> list:
        coordinates = []

        while not coordinates:
            coordinates = self.getUserInput()
            if not coordinates:
                continue

            if tuple(coordinates) in field.possibleMoves:
                field.setTic(coordinates)
                field.possibleMoves.remove(tuple(coordinates))
            else:
                coordinates = []
                continue


class ComputerEasy(Player):
    def makeMove(self, field: fieldClass.Field):
        print("Making move level 'easy'")
        coordinates = self.popRandomElement(field.possibleMoves)
        field.setTic(coordinates)


class ComputerMedium(Player):
    def makeMove(self, field: fieldClass.Field):
        print("Making move level 'Medium'")
        coordinates = self.evaluateMove(field)
        if coordinates:
            field.setTic(coordinates)
            field.possibleMoves.remove(coordinates)
        else:
            coordinates = self.popRandomElement(field.possibleMoves)
            field.setTic(coordinates)

    def evaluateMove(self, field):
        # evaluate rows
        for i in range(3):
            if (field.field[i].count("X") == 2 or field.field[i].count("O") == 2) and field.field[i].count("_") == 1:
                return i + 1, field.field[i].index("_") + 1

        # evaluate columns
        for i in range(3):

            if (field.getColumn(i).count("X") == 2 or field.getColumn(i).count("O") == 2) and field.getColumn(i).count("_") == 1:
                return field.getColumn(i).index("_") + 1, i + 1

        # evaluate diagonals
        row = []
        for i in range(len(field.field)):
            row.append(field.field[i][i])
        if (row.count("X") == 2 or row.count("O") == 2) and row.count("_") == 1:
            return row.index("_") + 1, row.index("_") + 1

        row = []
        length = len(field.field)
        lengthIterator = length
        for i in range(length):
            lengthIterator -= 1
            row.append(field.field[lengthIterator][i])
        if (row.count("X") == 2 or row.count("O") == 2) and row.count("_") == 1:
            return length - row.index("_"), row.index("_") + 1

class ComputerHard(Player):
    def makeMove(self, field: fieldClass.Field):
        print("Making move level 'hard'")
        coordinates = minmax.minimax(field, 0)["position"]
        field.setTic(coordinates)
        field.possibleMoves.remove(coordinates)