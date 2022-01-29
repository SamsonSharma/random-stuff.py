#change the dirictory to the install of your chrome driver
from pynput import keyboard
import time
from pynput.keyboard import Key, Controller
from selenium import webdriver
keyboard = Controller()
browser = webdriver.Chrome('C:/Users/samso/Documents/chromedriver')
browser.get('https://www.youtube.com/watch?v=oHg5SJYRHA0')
keyboard.press(Key.space)
keyboard.release(Key.space)