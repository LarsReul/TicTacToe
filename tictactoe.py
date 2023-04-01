import random
import fieldClass
import players


if __name__ == "__main__":

    while True:
        choice = input("please enter exit to stop the game, or start and the two players to start the game").split()
        if choice[0] == "exit" and len(choice) == 1:
            break
        elif choice[0] == "start" and len(choice) == 3:
            if choice[1] == "user":
                player1 = players.User()
            elif choice[1] == "easy":
                player1 = players.ComputerEasy()
            elif choice[1] == "medium":
                player1 = players.ComputerMedium()
            elif choice[1] == "hard":
                player1 = players.ComputerHard()
            else:
                print("Bad parameters!")
                continue

            if choice[2] == "user":
                player2 = players.User()
            elif choice[2] == "easy":
                player2 = players.ComputerEasy()
            elif choice[2] == "medium":
                player2 = players.ComputerMedium()
            elif choice[2] == "hard":
                player2 = players.ComputerHard()
            else:
                print("Bad parameters!")
                continue
        else:
            print("Bad parameters!")
            continue

        field = fieldClass.Field()
        field.printField()
        while True:
            player1.makeMove(field)
            field.printField()
            if field.checkField() != 0:
                field.printWinner()
                break

            player2.makeMove(field)
            field.printField()
            if field.checkField() != 0:
                field.printWinner()
                break


