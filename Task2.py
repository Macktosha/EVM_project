import dearpygui.dearpygui as dpg
import sys
import time
from PCI_classes.model2 import model2

#functions for int callback
def insertion_sort(list1):

    for i in range(1, len(list1)):

        value = list1[i]
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1

def int_transfer(sender,app_data):
    tac=time.perf_counter()
    val = dpg.get_value(sender)
    res = [int(t) for t in str(val)]
    arr = model2(res)
    arr = insertion_sort(arr)
    tic=time.perf_counter()
    dpg.push_container_stack(dpg.add_spacer(height=5))
    dpg.push_container_stack(dpg.add_text(f"You entered: {val}, it was transfered by the BUS as {res},"
                                          f" then it was sorted and we got: {arr}\n"
                                          f"It's Size: {sys.getsizeof(arr)}\n"
                                          f"Elapsed time {tic-tac:0.10f} seconds"))

def int_callback(sender,app_data):
   dpg.push_container_stack(dpg.add_window(label="Task 2",width=1050,height=800,pos=[150,0]))
   dpg.push_container_stack(dpg.add_input_int(label="Enter value to be transfered on the BUS and sorted as an array",on_enter=True,max_value=1000000000,
                                              callback=int_transfer,
                                              width=345))

#functions for str callback

def str_transfer(sender,app_data):
    tac = time.perf_counter()
    val = dpg.get_value(sender)
    str(val)
    arr = model2(val)
    count = 0
    for vowel in 'AEIOUaeiou':
        count += arr.count(vowel)
    tic = time.perf_counter()
    dpg.push_container_stack(dpg.add_spacer(height=5))
    dpg.push_container_stack(dpg.add_text(f"You entered: \"{val}\", it was transfered by the BUS as an array,"
                                          f" then we counted vowels in the string and we got: {count} vowels\n"
                                          f"It's Size: {sys.getsizeof(arr)}\n"
                                          f"Elapsed time {tic - tac:0.10f} seconds"))


def str_callback(sender,app_data):
    dpg.push_container_stack(dpg.add_window(label="Task 2", width=1050, height=800, pos=[150, 0]))
    dpg.push_container_stack(dpg.add_input_text(label="Enter value to be transfered on the BUS and edited as a string",
                                                on_enter=True,
                                                height=25,width=500,
                                                default_value='Enter your string right here :)',
                                                callback=str_transfer))


def task2_callback(sender,app_data):
    with dpg.window(label="Task 2 window",width=1050,height=800,pos=[150,0]):
         dpg.add_checkbox(label="Work with integer values",callback=int_callback)
         dpg.add_spacer(height=25)
         dpg.add_checkbox(label="Work with string values", callback=str_callback)
