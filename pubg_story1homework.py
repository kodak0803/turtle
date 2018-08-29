player= {"NAME":"BOT ADAM","ATTACK": 10, "HP": 100,"DEFENSE":100}

cmd = input("Your command:")

if cmd == "stats":
    print("NAME:", player["NAME"])
    print("HP:", player["HP"])
    print("STRENGTH:", player["STRENGTH"])
    print("DEFENSE:", player["DEFENSE"])
elif cmd =="inventory":
    print(" You can choose a gun")
    print= (input("What gun do you choose?"))
    if gun == "akm" or "AKM":
        print("You choose AKM")
    elif gun == "m416" or "M416":
        print("You choose M416")
    elif gun == "awp"or "AWP":
        print ("You choose AWP")
    else:
        print(" Can't find gun")
elif cmd == "start"
