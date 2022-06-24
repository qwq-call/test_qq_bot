import pyautogui


# 鼠标操作
print(pyautogui.size())   # 返回所用显示器的分辨率； 输出：Size(width=1920, height=1080)
width,height = pyautogui.size()
print(width,height)  # 1920 1080
pyautogui.moveTo(100,300,duration=1)#移动鼠标

# 点击鼠标
pyautogui.click(10,10)   # 鼠标点击指定位置，默认左键
pyautogui.click(10,10,button='left')  # 单击左键
pyautogui.click(1000,300,button='right')  # 单击右键
pyautogui.click(1000,300,button='middle')  # 单击中间

pyautogui.doubleClick(10,10)  # 指定位置，双击左键
pyautogui.rightClick(10,10)   # 指定位置，双击右键
pyautogui.middleClick(10,10)  # 指定位置，双击中键

pyautogui.mouseDown()   # 鼠标按下
pyautogui.mouseUp()    # 鼠标释放

pyautogui.dragTo(100,300,duration=1)   #鼠标拖动到指定位置

pyautogui.scroll(300)  # 向上滚动300个单位；

currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置

# 图像处理

im = pyautogui.screenshot()#返回屏幕的截图，是一个Pillow的image对象
im.getpixel((500, 500))#返回im对象上，（500，500）这一点像素的颜色，是一个RGB元组
pyautogui.pixelMatchesColor(500,500,(12,120,400))#是一个对比函数，对比的是屏幕上（500，500）这一点像素的颜色，与所给的元素是否相同；

# 图像识别（一个）
# btm = pyautogui.locateOnScreen('zan.png')
# print(btm)  # Box(left=1280, top=344, width=22, height=22)
#
# 图像识别（多个）
# btm = pyautogui.locateAllOnScreen('zan.png')
# print(list(btm))  # [Box(left=1280, top=344, width=22, height=22), Box(left=25, top=594, width=22, height=22)]

# pyautogui.center((left,top,right,height))  #找寻四个坐标点的中心

pyautogui.keyDown("a")#按下一个按键
pyautogui.keyUP("a")#模拟放开一个按键
pyautogui.press("a")#模拟按下并放开一个按键
pyautogui.typewrite("this",0.1)#第一个参数是输入内容，第二个参数是输入字符的间隔时间


