# 这是一个自动回复的程序，应该会经过不断地修改与完善
# 开坑于2022.6.16
import pyautogui as gui
import pyperclip,time

gui.PAUSE = 0.5

# 载入预定消息
mylist=[]
mydict={}
def load_message():
    f=open('test.txt',"r",encoding='UTF-8')
    lines=f.readlines()

    for x in lines:#将文本处理为列表
        mylist.append(x.split(","))

    for a in mylist:
        print(a)
        mydict[a[0]]=a[1]
    print(mydict)



def open_qq():
    # 打开QQ
    qq_location=gui.locateCenterOnScreen("qq.png")
    print(qq_location)
    if qq_location is not None:
        gui.click(qq_location.x,qq_location.y)
    else:
        pass

def wait_message():
# 点击消息，进入聊天框
    while 1==1:
        situation=0
        gui.moveTo(100,100)
        message_location=gui.locateCenterOnScreen("message_tip.png",confidence=0.9)
        if message_location is not None:
            gui.moveTo(message_location.x,message_location.y)
            gui.doubleClick(message_location.x-50,message_location.y)
            print(message_location)
            situation=1
            break
        else:
            time.sleep(1)#等待1秒，防止过度占用内存

    return situation

def send_message(text):
    while 0==0:
        send_location=gui.locateCenterOnScreen("send2.png",confidence=0.9)
        print(send_location)
        if send_location is not None:
            gui.click(send_location.x,send_location.y-80)
            break
        else:
            pass
    pyperclip.copy(mydict[text])
    gui.keyDown('ctrl')
    gui.keyDown('v')
    gui.click(send_location.x,send_location.y)

load_message()
open_qq()
wait_message()
send_message('for_the_first')
print("end")


print(mydict)










