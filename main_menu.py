import dearpygui.dearpygui as dpg
from GUI.Task1 import task1_callback
from GUI.Task2 import task2_callback
from GUI.Task3 import task3_callback


def init_window():
    dpg.create_context()
    dpg.setup_dearpygui()
    dpg.create_viewport(title='PCI project', width=1215, height=800,x_pos=150,y_pos=-10,large_icon="icon.png")
    with dpg.window(id='Menu window',label='Menu',width=150,height=800,no_close=True,no_resize=True,no_move=True,no_collapse=True):
         dpg.add_text('Choose the task')
         dpg.push_container_stack(dpg.add_button(label='Task 1', callback=task1_callback,indent=5,width=70,height=50,pos=[125,50]))
         dpg.add_button(label='Task 2', callback=task2_callback,indent=5,width=70,height=50,pos=[125,150])
         dpg.push_container_stack(dpg.add_button(label='Task 3', callback=task3_callback,indent=5,width=70,height=50,pos=[125,250]))


    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
