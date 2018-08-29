#player = ["kodak", "Student",100, 7,1,8,20]
player ={"NAME": "MAD","HP":100, "STRENGTH":7, "DEFENSE":10, "LEVEL":1,  }
cmd = input("Your command:")
if cmd == "stats":
    print("NAME:",player["NAME"])
    print("HP:",player["HP"])
    print("STRENGTH:",player["STRENGTH"])
    print("DEFENSE:",player["DEFENSE"])
    print("LEVEL:",player["LEVEL"])
elif cmd == "here":
    print("Bạn đang ở trước của Techkids")
    print("Bạn có 2 lựa chọn")
    print("1. Về Techkids")
    print("2. Đi vào cánh rừng đối diện")
    option = input("Lựa chọn của bạn?")
    if option == "1":
        print("Xin lỗi, đã hết giờ làm việc")
        print("Nhập lại đê!!")
    elif option == "2":
        print("Bạn đã bước vào rừng")
        print("Bạn thấy một bình thủy dịch ở trên mặt đất")
        print("1.Bỏ qua")
        print("2.Nhặt lên uống")
        option= input("Lựa chọn của bạn")
        if option == "1":
            print("Bạn chết")
        elif option == "2":
            print("Game over")
            print("...")
            print("...")
            print("...")
            print("...")
            print("Từ Từ đã ...")
            print("Bạn chưa chết")
conđiên = { "NAME":"orc ", "HP":20,"STRENGTH":0, "DEFENSE":10, "LEVEL":1 }

        elif option == "3":
    print("Bạn đã gặp 1 con điên")
    print("1.bạn đánh nó")
    print("2.Bạn bỏ chạy")
    print("3.đối kháng tiếp")
    if option == "1":
        conđiên = {"NAME": "orc ", "HP": 20, "STRENGTH": 0, "DEFENSE": 10, "LEVEL": 1}
        damage = player["STRENGTH"] - org["DEF"]
        org["HP"] = org["HP"] - damage
        if damage > 0:
            org["HP"] = org["HP"]
            print("bạn vừa tát conđiên")
            print("Con điên mất ", damage, "HP")
            print("HP  của conđiên ", end=' ')

        print ("bạn chắc chắn chết bởi nó quá mạnh")
        print("Đen thôi đỏ quên đi")
    elif option == "2":
        print("bạn rất hay")
        print("bạn đã thoát khỏi cái chết nhưng...")
        print("Game muốn bạn chết")
        print("Game over")
    elif option == "3":
        print("Game đợi bạn quá lâu")
        print("Sập")
        print("Game over")
else:
    print("Game over")

#cmd = input("Your command?")
#if cmd == "stats"