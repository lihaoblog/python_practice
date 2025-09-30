import pyautogui
import time


#基础设置
pyautogui.pause=1           #每次执行的间隔，用time.sleep(1)更好
pyautogui.FAILSAFE=True  #跑不动的情况下退出，防故障

# 判断屏幕大小
screenWidth,screenHeigh=pyautogui.size()
# print(screenWidth,screenHeigh)
# 获取当前鼠标的位置
currentPositionX,currentPositionY=pyautogui.position()

print(currentPositionX,currentPositionY)

# y移动鼠标,duration表示移动需要的时间
# pyautogui.moveTo(387,232,duration=2)
#
# #鼠标拖拽,设置的到地方自动按左键,即为拖拽
# pyautogui.dragTo(1610,175,button='left',duration=2)

#鼠标点击一下双击是doubleClick
# pyautogui.click(387,232,button='left')
#之所以两下是因为第一次要切到对应的文件上去,文件在被选中才能双击进去
# pyautogui.doubleClick(387,232,button='left')
#向上滚动10格
# pyautogui.scroll(500)

#键盘的操作
time.sleep(1)
pyautogui.click()
#敲一个hello再空格
pyautogui.typewrite('hello')
pyautogui.press('space')

#长按,会一直按
# time.sleep(3)
# pyautogui.keyDown('shift')
# pyautogui.press('4')

# 组合键,热键
pyautogui.hotkey('commend','c')
pyautogui.hotkey('commend','v')