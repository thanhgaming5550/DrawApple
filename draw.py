from tkinter.messagebox import YESNOCANCEL
import pyautogui
import time

print("Vui long mo cua so mspaint, de full man hinh dong thoi set zoom=100% va set full draw area")
print("De con tro chuot o vi tri bat dau ve")
print("\n")
time.sleep(3)
print("Bat dau ve sau 5s")
time.sleep(1)
print("Bat dau ve sau 4s")
time.sleep(1)
print("Bat dau ve sau 3s")
time.sleep(1)
print("Bat dau ve sau 2s")
time.sleep(1)
print("Bat dau ve sau 1s")
time.sleep(1)
print("Dang ve...")
print("Dang thiet dat cong cu ve...")
current = pyautogui.position()
try: 
    pyautogui.click("brushes2.png")
except: 
    pyautogui.click("brushes1.png")
pyautogui.click("pen-click.png")
pyautogui.click("pen.png")
#############################################
print("Dang ve cuong...")
pyautogui.click("brown.png")
pyautogui.click("brown.png")
pyautogui.moveTo(current)
pyautogui.drag(0, -100, 0.5, button="left")
pyautogui.drag(15, 0, 0.3, button="left")
pyautogui.drag(0, 40, 0.2, button="left")
lacay = pyautogui.position()
pyautogui.drag(0, 60, 0.3, button="left")
current = pyautogui.position()
pyautogui.drag(-15, 0, 0.3, button="left")
endpoint = pyautogui.position()
pyautogui.click("fill.png")
pyautogui.moveTo(current) 
pyautogui.move(-3, -3, 0.1)
pyautogui.click()
print("Dang ve qua tao...")
pyautogui.click("pen.png")
pyautogui.click("red.png")
pyautogui.click("red.png")
pyautogui.moveTo(current)
#############################################
count=0
while (count!=10) :
    count=count+1
    pyautogui.drag(6, 1.5, 0, button="left")
count=0
while (count!=15) :
    count=count+1
    pyautogui.drag(4, 2, 0, button="left")
count=0
while (count!=20) :
    count=count+1
    pyautogui.drag(2, 5, 0, button="left")
#############################################
count=0
while (count!=20) :
    count=count+1
    pyautogui.drag(-2, 5, 0, button="left")
count=0
while (count!=15) :
    count=count+1
    pyautogui.drag(-4, 2, 0, button="left")
count=0
while (count!=10) :
    count=count+1
    pyautogui.drag(-6, 1.5, 0, button="left")
#############################################
count=0
while (count!=10) :
    count=count+1
    pyautogui.drag(-6, -1.5, 0, button="left")
count=0
while (count!=15) :
    count=count+1
    pyautogui.drag(-4, -2, 0, button="left")
count=0
while (count!=15) :
    count=count+1
    pyautogui.drag(-2, -5, 0, button="left")
#############################################
count=0
while (count!=12) :
    count=count+1
    pyautogui.drag(2, -10, 0, button="left")
count=0
while (count!=18) :
    count=count+1
    pyautogui.drag(4, -2, 0, button="left")
pyautogui.dragTo(endpoint)
#############################################
pyautogui.click("fill.png")
pyautogui.moveTo(endpoint)
pyautogui.move(3, 3)
pyautogui.click()
#############################################
print("Dang ve la...")
pyautogui.click("pen.png")
pyautogui.click("dark_green.png")
pyautogui.click()
pyautogui.moveTo(lacay)
pyautogui.drag(6, 0, 0, button="left")
count=0
while (count!=10):
    count=count+1
    pyautogui.drag(2, -1.6, 0, button="left")
count=0
while (count!=8):
    count=count+1
    pyautogui.drag(4, -1, 0, button="left")    
count=0
while (count!=8):
    count=count+1
    pyautogui.drag(5, 1, 0, button="left")    
count=0
while (count!=10):
    count=count+1
    pyautogui.drag(4, 2, 0, button="left")
count=0
while (count!=18):
    count=count+1
    pyautogui.drag(-3, 1, 0, button="left")  
count=0
while (count!=8):
    count=count+1
    pyautogui.drag(-4, -0.8, 0, button="left") 
count=0
while (count!=4):
    count=count+1
    pyautogui.drag(-6, -1, 0, button="left")     
pyautogui.dragTo(lacay)
pyautogui.click("fill.png")
pyautogui.moveTo(lacay)
pyautogui.move(10,3)
pyautogui.click()
print("Dang fill background...")
pyautogui.click("cyan.png")
pyautogui.click("cyan.png")
pyautogui.moveTo(lacay)
pyautogui.move(-30,0)
pyautogui.click()
print("Da ve xong!")