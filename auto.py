#!/usr/bin/python3

import pyautogui
import subprocess
import argparse

#get current workspace
workspace = subprocess.run(['./workspace.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[0].split(')')[0].split('(')[1]
print('Curent Workspace: ' + workspace)

mouse_pos = pyautogui.position()

# Instantiate the parser
parser = argparse.ArgumentParser(description='A gui media controler')
parser.add_argument('action', type=str,
                    help='what action must i perform')
args = parser.parse_args()

if args.action == 'pp':
    #move work space
    pyautogui.hotkey('winleft', '1')
    pyautogui.moveTo(965, 50000) 
    pyautogui.moveRel(-10, -70) 
    pyautogui.click()

    pyautogui.hotkey('winleft', workspace)
    pyautogui.moveTo(mouse_pos)

if args.action == 'next':
    #move work space
    pyautogui.hotkey('winleft', '1')
    pyautogui.moveTo(965, 50000) 
    pyautogui.moveRel(32, -70) 
    pyautogui.click()

    pyautogui.hotkey('winleft', workspace)
    pyautogui.moveTo(mouse_pos)

if args.action == 'prev':
    #move work space
    pyautogui.hotkey('winleft', '1')
    pyautogui.moveTo(965, 50000)  
    pyautogui.moveRel(-52, -70) 
    pyautogui.click()

    pyautogui.hotkey('winleft', workspace)
    pyautogui.moveTo(mouse_pos)
