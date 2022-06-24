import pyperclip,pyautogui,cv2

# f=open('test.txt',"r",encoding='UTF-8')
# lines=f.readlines()
# print(lines)
# mylist=[]
# for x in lines:
#     mylist.append(x.split(","))
# print(mylist)
# mydict={}
# for a in mylist:
#     print(a)
#     mydict[a[0]]=a[1]
# print(mydict)
# pyperclip.copy(mydict['状态'])

print('star')
while 0==0:
    print(1)
    send2=pyautogui.locateCenterOnScreen("send2.png",confidence=0.9)
    print(send2,2)
    if send2 is not None:
        pyautogui.moveTo(send2.x,send2.y)
        pyautogui.click(send2.x-100, send2.y-50)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown("v")
        pyautogui.click(send2.x, send2.y)
        # pyautogui.click(send_location.left-send_location.width+30,send_location.top+send_location.height+30)
        # pyautogui.moveTo(send_location.left-send_location.width+30,send_location.top+send_location.height+30)
    #     print(111)
        break



