import pywhatkit
import pyautogui
import time

phonenumber="+254720507316"
message="Oyaaah morio hii text imetumwa na Python"
pywhatkit.sendwhatmsg_instantly(phonenumber,message)

time.sleep(30)
pyautogui.press("enter")