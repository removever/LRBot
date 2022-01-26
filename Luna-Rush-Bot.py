from ast import While
import pyautogui
from check_function import *


from tkinter import *
from check_function import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import os
import threading
event = threading.Event()
root = Tk()
root.geometry("400x300")
root.title(" LR Bot By removesver")

lb1 = Label(text="เวลาทำงาน (นาที)")
work_time = Text(root, height=1,
                 width=25,
                 bg="light yellow")
work_time.insert(END, '90')
Output = Text(root, height=3,
              width=25,
              bg="light cyan")
Display = Button(root, height=1,
                 width=10,
                 text="Run",
                 command=lambda: read_input())
Output.insert(END, "รอทำงาน")

lb1.pack()
work_time.pack()
Display.pack()
Output.pack()


def setup_windows():
    windows = []
    window_list = pyautogui.getWindowsWithTitle('Luna Rush')
    size_all = pyautogui.size()
    x_all = size_all[0]
    count_x = x_all/650
    curent_x = 0
    curent_y = 0
    for w in window_list:
        x = curent_x*650
        y = curent_y*550
        if curent_x >= count_x:
            curent_x = 0
            curent_y = curent_y+1
            x = curent_x*650
            y = curent_y*550
        curent_x += 1
        active = {
            "window": w,
            "login": 0,
            "heroes": 0,
            "new_map": 0,
            "refresh_heroes": 0,
            'current_page': 0,
            "x": x,
            "y": y,
        }
        windows.append(active)
        cp_resize(w, active)
    return windows


def run_bot(input_work_time):
    root.update()
    windows = setup_windows()
    show_time = 0
    work_time = input_work_time
    while True:
        for active in windows:
            w = active["window"]
            cp = current_page(w)
            if cp == 'login':
                login(w, active)
                time.sleep(5)
            my_break = False
            while my_break == False:
                my_break = work_all(w)
            time.sleep(2)
            time.sleep(1)
            # ทำงาน
        for x in range(work_time*60):
            show_time += 1
            # if (show_time % 120) == 1 and show_time > 120:
            #     for active in windows:
            #         w = active["window"]
            #         remap(w, active)
            time.sleep(1)
            Output.delete("1.0", END)
            Output.insert(END, "WORK : ")
            Output.insert(END, show_time)
            root.update()
        show_time = 0


def stop():
    event.set()
    print("stop")
    os._exit(0)


keyboard.add_hotkey("esc", stop)

run_loop = False


def read_input():
    work_val = work_time.get("1.0", "end-1c")
    Output.delete("1.0", END)
    Output.insert(END, "ทำงาน")
    run_bot(int(work_val))


mainloop()
