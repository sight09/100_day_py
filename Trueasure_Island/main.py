print ("welcome to Trueasure Island")
print ("Your mission is to find the treasure")

go =input("you are at a cross road, where do u wanna go ? left or right \n")
if (go == "left"):
    swim = input("you come to a lake, there is an island in the middle of the lake, what do u wanna do ? swim or wait \n")
    if (swim == "wait"):
        door = input("you arrive at the island unharmed, there is a house with 3 doors. one red, one yellow and one blue. which colour do u choose ? \n")
        if (door == "yellow"):
            print("you win")
        elif (door == "red"):
            print("burned by fire. game over")
        elif (door == "blue"):
            print("eaten by beasts. game over")
        else:
            print("game over")
    else:
        print("attacked by trout. game over")
