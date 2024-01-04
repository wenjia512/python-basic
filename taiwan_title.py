import turtle   #匯入turtle模組

window = turtle.Screen()    #畫面等於turtle模組視窗
window.setup(width=600,height=600)  #視窗大小(寬度600，高度600)

a1 = turtle.Turtle()    #a1等於turtle模組的小烏龜
a1.speed(0) #a1速度0，最快

a1.penup()  #a1抬起小烏龜畫筆
a1.goto(-280,200)  #a1移動到距離中心圓點往左280，往上200
a1.pendown()  #a1放下小烏龜畫筆
a1.begin_fill()  #a1開始塗滿顏色
for a in range(2) :  #a1進行迴圈2次
    a1.color("red")  #a1顏色紅色
    a1.forward(550)  #a1直走550
    a1.right(90)  #a1方向往右轉90
    a1.forward(355)  #a1直走355
    a1.right(90)  #a1方向往右轉90
a1.end_fill()  #a1結束塗滿顏色

a1.penup()  #a1抬起小烏龜畫筆
a1.goto(-280,200)  #a1移動到距離中心圓點往左280,往上200
a1.pendown()  #a1放下小烏龜畫筆    
a1.begin_fill()  #a1開始塗滿顏色
for a in range(2) :  #a1進行迴圈2次
    a1.color("blue")  #a1顏色藍色
    a1.forward(260)  #a1直走260
    a1.right(90)  #a1方向往右轉90
    a1.forward(170)  #a1直走170
    a1.right(90)  #a1方向往右轉90
a1.end_fill()  #a1結束塗滿顏色

a1.penup()  #a1抬起小烏龜畫筆
a1.goto(-90,98)  #a1移動到距離中心圓點往左90,往上98
a1.pendown()  #a1放下小烏龜畫筆
a1.begin_fill()  #a1開始塗滿顏色
for a in range(12) :  #a1進行迴圈12次
    a1.color("white")  #a1顏色白色
    a1.left(150)  #a1方向往左轉150
    a1.forward(128)  #a1直走128
a1.end_fill()  #a1結束塗滿顏色

a1.penup()  #a1抬起小烏龜畫筆
a1.goto(-155,85)  #a1移動到距離中心圓點往左155,上85
a1.pendown()  #a1放下小烏龜畫筆
a1.color("blue")  #a1顏色藍色
a1.width(5)  #a1寬度5
a1.circle(30)  #a1形狀是圓形且大小30

a1.hideturtle()  #a1隱藏小烏龜
window.exitonclick()  #要離開畫面請點擊任意一下