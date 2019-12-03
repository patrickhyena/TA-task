fridge = ["oranges","milk","jam","the souls of the damned","the blood of innocents","rotten tomatoes","eggs"]

def store(x):
    fridge.append(x)
    print(x, "has been stored into the fridge.")

def retrieve(y):
        if y == 3:
            print("you just consumed", fridge[y])
            fridge.pop(y)
            print("Did you just... consume souls? You are a monster.")
        elif y == 5:
            print("you just consumed", fridge[y])
            fridge.pop(y)
            print("Why would you do that? It was rotten. You do you, I guess.")
        elif y == 4:
            print("you just consumed", fridge[y])
            fridge.pop(y)
            print("You are a horrible person.")
        else:
            print("you just consumed", fridge[y])
            fridge.pop(y)
            print("its gone forever now")

def update():
    print("Here's what's in your fridge currently:")
    print(fridge)

update()

store("banana")
store("jar of hearts")

retrieve(5)
retrieve(4)
retrieve(3)

update()