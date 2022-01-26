from pickle import FALSE
from tkinter.constants import TRUE
from turtle import width
import pyautogui
import win32gui
import time
# ,region=(screen.left,screen.top,screen.width,screen.height)


def current_page(w):
    w.activate()
    w.activate()
    w.activate()
    pyautogui.sleep(1)
    start = pyautogui.locateCenterOnScreen(
        './img/connect_wallet.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'login'
    start = pyautogui.locateCenterOnScreen(
        './img/boss_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'home'
    start = pyautogui.locateCenterOnScreen(
        './img/title_boss_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'select_boss'
    start = pyautogui.locateCenterOnScreen(
        './img/title_hero.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'select_hero'


def work_all(w):
    cp = current_page(w)
    if cp == 'home':
        boss_hunt(w)
        pyautogui.sleep(1)
    boss_lvl = check_level_boss(w)
    print(boss_lvl)
    select_boss(w, boss_lvl)
    cp = current_page(w)
    if cp == 'select_hero':
        clear_hero(w)
    else:
        work_all(w)
    move_for_select_hero(w)
    my_break = select_hero(w)
    go = False
    while go == False :
        boss_hunt_click(w)
        cp = current_page(w)
        if cp != 'select_hero' :
            go = True
    pyautogui.sleep(6)
    pyautogui.click()
    success = False
    while success == False :
        pyautogui.sleep(1)
        success = check_success(w)
    return my_break
    # home_to_hero(w)
    # pyautogui.sleep(1)
    # work_all_click(w)
    # pyautogui.sleep(3)
    # hero_list_to_home(w)
    # pyautogui.sleep(1)
    # home_to_hunt(w)
def check_success(w):
    victory = pyautogui.locateCenterOnScreen(
        './img/victory.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    defeat = pyautogui.locateCenterOnScreen(
        './img/defeat.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if defeat != None :
        pyautogui.click()
        return True
    if victory != None :
        pyautogui.sleep(5)
        tap_to_open = pyautogui.locateCenterOnScreen('./img/tap_to_open.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
        pyautogui.moveTo(tap_to_open)
        pyautogui.click()
        pyautogui.sleep(5)
        pyautogui.click()
        return True
    return False

def boss_hunt_click(w):
    start = pyautogui.locateCenterOnScreen(
        './img/btn_boss_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    print(start)
    pyautogui.moveTo(start)
    pyautogui.click()

def select_hero(w):
    count_click = 0
    count_break = 0
    _break = False
    while count_click < 3:
        en_3 = pyautogui.locateCenterOnScreen(
            './img/en_3.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
        en_2 = pyautogui.locateCenterOnScreen(
            './img/en_2.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
        en_1 = pyautogui.locateCenterOnScreen(
            './img/en_1.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
        if en_3 != None:
            pyautogui.moveTo(en_3)
            pyautogui.click()
            count_click = count_click+1
        elif en_2 != None:
            pyautogui.moveTo(en_2)
            pyautogui.click()
            count_click = count_click+1
        elif en_1 != None:
            pyautogui.moveTo(en_1)
            pyautogui.click()
            count_click = count_click+1
        else:
            pyautogui.scroll(-100)
        time.sleep(1)
        count_break = count_break+1
        if count_break == 20:
            _break = True
            count_click = 3
    return _break



def move_for_select_hero(w):
    start = pyautogui.locateCenterOnScreen(
        './img/title_hero.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.moveTo((start[0], start[1]+50))


def clear_hero(w):
    ck_btn = True
    while ck_btn:
        start = pyautogui.locateCenterOnScreen(
            './img/btn_boss_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
        if start != None:
            ck_btn = False
    hero_3 = (start[0], start[1]-300)
    pyautogui.moveTo(hero_3)
    pyautogui.click()

    hero_2 = (hero_3[0]-250, hero_3[1])
    pyautogui.moveTo(hero_2)
    pyautogui.click()

    hero_1 = (hero_2[0]-250, hero_2[1])
    pyautogui.moveTo(hero_1)
    pyautogui.click()


def select_boss(w, boss_lvl):
    start = pyautogui.locateCenterOnScreen(
        './img/'+boss_lvl+'.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    print(start)
    pyautogui.moveTo(start)
    pyautogui.click()


def boss_hunt(w):
    start = pyautogui.locateCenterOnScreen(
        './img/boss_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()

# get boss


def check_level_boss(w):
    _level = pyautogui.locateCenterOnScreen('./img/boss_1_10.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
    if(_level == None):
        boss = pyautogui.locateCenterOnScreen('./img/boss_1.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
        if boss != None:
            return "boss_1"
    _level = pyautogui.locateCenterOnScreen('./img/boss_2_10.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
    if(_level == None):
        boss = pyautogui.locateCenterOnScreen('./img/boss_2.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
        if boss != None:
            return "boss_2"
    _level = pyautogui.locateCenterOnScreen('./img/boss_3_10.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
    if(_level == None):
        boss = pyautogui.locateCenterOnScreen('./img/boss_3.PNG', region=(w.left, w.top, w.width, w.height), grayscale=False, confidence=.9)
        if boss != None:
            return "boss_3"
    return "boss_4"

# def check_level_boss(w):
#     _level = pyautogui.locateCenterOnScreen(
#         './img/boss_3.PNG', region=(w.left, w.top, w.width, w.height), grayscale=FALSE, confidence=.9)
#     if(_level != None):
#         return "boss_3"
#     _level = pyautogui.locateCenterOnScreen(
#         './img/boss_4.PNG', region=(w.left, w.top, w.width, w.height), grayscale=FALSE, confidence=.9)
#     if(_level != None):
#         return "boss_3"


def cp_resize(w, active):
    w.restore()
    w.resizeTo(1000, 800)
    w.moveTo(0,0)


def login(w, active):
    w.maximize()
    pyautogui.sleep(2)
    start = pyautogui.locateCenterOnScreen('./img/connect_wallet.PNG',  grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()
    pyautogui.sleep(10)
    start = pyautogui.locateCenterOnScreen('./img/sign_btn.PNG',  grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()
    pyautogui.sleep(3)
    cp_resize(w, active)
