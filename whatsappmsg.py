import pywhatkit
import pyautogui
import time

phonenumber="+254720507316"
message="Pia hii imetumwa na Python"
pywhatkit.sendwhatmsg_instantly(phonenumber,message)
time.sleep(30)
pyautogui.press("enter")