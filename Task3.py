import dearpygui.dearpygui as dpg
from GUI.Graphics import *

clck_point=dict()
clck_point['x']=100
clck_point['y']=35

frame_point=dict()
frame_point['x']=100
frame_point['y']=85
frame_flag = False

ad_point=dict()
ad_point['x1']=100
ad_point['y1']=165
ad_flag= False


cbe_point = dict()
cbe_point['x1']=100
cbe_point['y1']=245
cbe_flag=False


irdy_point=dict()
irdy_point['x']=100
irdy_point['y']=325
irdy_flag=False

trdy_point=dict()
trdy_point['x']=100
trdy_point['y']=405
trdy_flag=False


dsl_point=dict()
dsl_point['x']=100
dsl_point['y']=460
dsl_flag = False

def task3_callback(sender,app_data):
    start_x = 100
    start_y = 35
    dpg.push_container_stack(dpg.add_window(id='draw',label="Task 3 window", width=1050, height=800, pos=[150, 0]))
    dpg.push_container_stack(dpg.drawlist(label='drawlist', width=1050, height=600,pos=[150,0]))
    dpg.push_container_stack( dpg.draw_text(text='CLOCK', pos=[25, 15],size=18))
    dpg.push_container_stack(dpg.draw_text(text='FRAME#', pos=[25, 80],size=18))
    dpg.push_container_stack( dpg.draw_text(text='AD', pos=[25, 160], size=18))
    dpg.push_container_stack(dpg.draw_text(text='C/BE#', pos=[25, 240], size=18))
    dpg.push_container_stack(dpg.draw_text(text='IRDY#', pos=[25, 320], size=18))
    dpg.push_container_stack(dpg.draw_text(text='TRDY#', pos=[25, 400], size=18))
    dpg.push_container_stack(dpg.draw_text(text='DEVSEL', pos=[25,450], size=18))



    dpg.push_container_stack(dpg.add_window(id='controls',label='Controls',width=1050,height=200,
                   pos=[150,570],
                   no_resize=True,
                   no_move=True,
                   ))
    dpg.push_container_stack( dpg.add_button(label="+CLCK",callback=add_clck,parent='controls',width=55,height=100))
    dpg.push_container_stack( dpg.draw_line(p1=(60,5),p2=(60,150),thickness=0.5,parent='controls'))
    dpg.push_container_stack(dpg.add_button(label="Set frame",callback=set_frame,parent='controls',width=80,height=30,pos=[85,35]))
    dpg.push_container_stack(dpg.add_button(label="Cont frame",callback=cont_frame,parent='controls',width=80,height=30,pos=[85,95]))
    dpg.push_container_stack( dpg.draw_line(p1=(170,5),p2=(170,150),thickness=0.5,parent='controls'))
    dpg.push_container_stack(dpg.add_button(label="Set adress",callback=set_adress,parent='controls',width=80,height=30,pos=[200,35]))
    dpg.push_container_stack(dpg.add_button(label="Cont adress",callback=cont_adress,parent='controls',width=80,height=30,pos=[200,95]))
    dpg.push_container_stack(dpg.draw_line(p1=(290, 5), p2=(290, 150), thickness=0.5, parent='controls'))
    dpg.push_container_stack(
        dpg.add_button(label="Set C/BE#", callback=set_cbe, parent='controls', width=80, height=30, pos=[315, 35]))
    dpg.push_container_stack(
        dpg.add_button(label="Cont C/BE#", callback=cont_cbe, parent='controls', width=80, height=30,
                       pos=[315, 95]))
    dpg.push_container_stack(dpg.draw_line(p1=(400, 5), p2=(400, 150), thickness=0.5, parent='controls'))

    dpg.push_container_stack(
        dpg.add_button(label="Set IRDY#", callback=set_irdy, parent='controls', width=80, height=30, pos=[430, 35]))
    dpg.push_container_stack(
        dpg.add_button(label="Cont IRDY#", callback=cont_irdy, parent='controls', width=80, height=30,
                       pos=[430, 95]))

    dpg.push_container_stack(dpg.draw_line(p1=(520, 5), p2=(520, 150), thickness=0.5, parent='controls'))
    dpg.push_container_stack(
        dpg.add_button(label="Set TRDY#", callback=set_trdy, parent='controls', width=80, height=30, pos=[545, 35]))
    dpg.push_container_stack(
        dpg.add_button(label="Cont TRDY#", callback=cont_trdy, parent='controls', width=80, height=30,
                       pos=[545, 95]))

    dpg.push_container_stack(dpg.draw_line(p1=(640, 5), p2=(640, 150), thickness=0.5, parent='controls'))
    dpg.push_container_stack(
        dpg.add_button(label="Set DEVSEL#", callback=set_dsl, parent='controls', width=80, height=30, pos=[660, 35]))
    dpg.push_container_stack(
        dpg.add_button(label="Cont DEVSEL#", callback=cont_dsl, parent='controls', width=80, height=30,
                       pos=[660, 95]))



def add_clck(sender,app_data):
    global clck_point
    clck_point=draw_clck_period(clck_point)

def set_frame(sender,data):
    global frame_point
    global frame_flag
    if frame_flag == False:
        frame_point=set_position(frame_point)
        frame_flag=True
    else:
        frame_point=unset_position(frame_point)
        frame_flag=False

def cont_frame(sender,data):
    global frame_point
    global frame_flag
    if frame_flag == False:
        frame_point=upper_position(frame_point)
    else:
        frame_point=down_position(frame_point)

def set_adress(sender,data):
    global ad_point
    global ad_flag

    if ad_flag == False:
        ad_point=st_hexagon_ad(ad_point)
        ad_flag=True
    else:
        ad_point=end_hex_ad(ad_point)
        ad_flag=False

def cont_adress(sender,data):
    global ad_point
    global ad_flag

    if ad_flag == False:
        ad_point=cont_line(ad_point)
    else:
        ad_point=cont_hex_ad(ad_point)

def set_cbe(sender,data):
    global cbe_point
    global cbe_flag

    if cbe_flag == False:
        cbe_point = st_hexagon_cbe(cbe_point)
        cbe_flag = True
    else:
        cbe_point = end_hex_cbe(cbe_point)
        cbe_flag = False

def cont_cbe(sender,data):
    global cbe_point
    global cbe_flag

    if cbe_flag == False:
        cbe_point=cont_line(cbe_point)
    else:
        cbe_point=cont_hex_cbe(cbe_point)

def set_irdy(sender,data):
    global irdy_point
    global irdy_flag
    if irdy_flag == False:
        irdy_point = set_position(irdy_point)
        irdy_flag = True
    else:
        irdy_point = unset_position(irdy_point)
        irdy_flag = False

def cont_irdy(sender,data):
    global irdy_point
    global irdy_flag
    if irdy_flag == False:
        irdy_point = upper_position(irdy_point)
    else:
        irdy_point = down_position(irdy_point)

def set_trdy(sender,data):
    global trdy_point
    global trdy_flag
    if trdy_flag == False:
        trdy_point = set_position(trdy_point)
        trdy_flag = True
    else:
        trdy_point = unset_position(trdy_point)
        trdy_flag = False

def cont_trdy(sender,data):
    global trdy_point
    global trdy_flag
    if trdy_flag == False:
        trdy_point = upper_position(trdy_point)
    else:
        trdy_point = down_position(trdy_point)

def set_dsl(sender,data):
    global dsl_point
    global dsl_flag
    if dsl_flag == False:
        dsl_point = set_position(dsl_point)
        dsl_flag=True
    else:
        dsl_point=unset_position(dsl_point)
        dsl_flag=False

def cont_dsl(sender,data):
    global dsl_point
    global dsl_flag
    if dsl_flag == False:
        dsl_point = upper_position(dsl_point)
    else:
        dsl_point = down_position(dsl_point)


