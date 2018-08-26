from turtle import*
turtle_list=[]
for _ in range (5):
    t= Turtle()
    turtle_list.append(Turtle())
n= len(turtle_list)
print("Bố mày có", n,"turtle")
position = int(input("Mày thik con nào"))
color_str = input("màu nào?")
cmd = input("cái j?")
turtle_list[position].color(color_str)
turtle_list[position].fd(100)
if cmd == "fd"
    t.fd(100)
elif cmd == "bd"
    t.bd(100)
elif cmd == "lt"
    t.lt(100)
elif cmd == "rt"
    t.rt(100)
mainloop()