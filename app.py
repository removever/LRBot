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
root.title(" AutoBomb by Wara Multi v. By removesver")

lb1 = Label(text="เวลาทำงาน (นาที)")
work_time = Text(root, height=1,
                 width=25,
                 bg="light yellow")
work_time.insert(END, '10')
# lb2 = Label(text="เวลาพัก (นาที)")
# rest_time = Text(root, height=1,
#                  width=25,
#                  bg="light yellow")
# rest_time.insert(END, '3')
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
# lb2.pack()
# rest_time.pack()
Display.pack()
Output.pack()


# col = 4
# work_time = 5
# wait_time = 3
# ,region=(screen.left,screen.top,screen.width,screen.height)
def setup_windows():
    windows = []
    window_list = pyautogui.getWindowsWithTitle('Bombcrypto')
    size_all = pyautogui.size()
    x_all = size_all[0]
    count_x = x_all/550
    curent_x = 0
    curent_y = 0
    for w in window_list:
        index = window_list.index(w)
        x = curent_x*550
        y = curent_y*450
        if curent_x >= count_x:
            curent_x = 0
            curent_y = curent_y+1
            x = curent_x*550
            y = curent_y*450
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
            work_all(w)
            time.sleep(2)
            time.sleep(1)
            # ทำงาน
        for x in range(work_time*60):
            show_time += 1
            if (show_time % 120) == 1 and show_time > 120:
                for active in windows:
                    w = active["window"]
                    remap(w, active)
            time.sleep(1)
            Output.delete("1.0", END)
            Output.insert(END, "WORK : ")
            Output.insert(END, show_time)
            root.update()
        show_time = 0
        # #หยุดพัก
        # for y in range(wait_time*60):
        #     show_time += 1
        #     if (show_time % 120) == 1 and show_time > 120:
        #         for active in windows:
        #             w = active["window"]
        #             remap(w, active)
        #             cp_resize(w, active)
        #     time.sleep(1)
        #     Output.delete("1.0", END)
        #     Output.insert(END, "REST : ")
        #     Output.insert(END,show_time)
        #     root.update()
        # show_time = 0


def stop():
    event.set()
    print("stop")
    os._exit(0)


keyboard.add_hotkey("esc", stop)

run_loop = False


def read_input():
    work_val = work_time.get("1.0", "end-1c")
    # rest_time_val = rest_time.get("1.0", "end-1c")
    # print(work_val)
    # print(rest_time_val)
    Output.delete("1.0", END)
    Output.insert(END, "ทำงาน")
    run_bot(int(work_val))


mainloop()
