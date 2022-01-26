import dearpygui.dearpygui as dpg

#clck func
def draw_clck_period(point):
    dpg.draw_line(p1=(point['x'],point['y']),p2=(point['x']+30,point['y']),thickness=1.5,parent='draw')
    dpg.draw_line(p1=(point['x']+30,point['y']),p2=(point['x']+45,point['y']-25),thickness=1.5,parent='draw')
    dpg.draw_line(p1=(point['x']+45,point['y']-25),p2=(point['x']+45,720),parent='draw',thickness=0.5,color=(112,128,144,255))
    dpg.draw_line(p1=(point['x']+45,point['y']-25), p2=(point['x'] + 70, point['y']-25), thickness=1.5, parent='draw')
    dpg.draw_line(p1=(point['x']+70,point['y']-25), p2=(point['x'] + 85, point['y']), thickness=1.5, parent='draw')
    x=point['x']+85
    point['x']=x
    return point


def st_hexagon_ad(point):
    dpg.push_container_stack(dpg.draw_line(p1=(point['x1'],point['y1']),p2=(point['x1']+15,point['y1']-15), thickness=1.5, parent='draw'))
    dpg.push_container_stack(dpg.draw_line(p1=(point['x1'],point['y1']),p2=(point['x1']+15,point['y1']+15), thickness=1.5, parent='draw'))

    r_point=dict()
    x1 = point['x1'] + 15
    y1 = point['y1'] - 15
    x2 = point['x1'] + 15
    y2 = point['y1'] + 15
    r_point['x1'] = x1
    r_point['y1'] = y1
    r_point['x2'] = x2
    r_point['y2'] = y2
    return r_point

def cont_hex_ad(point):
    dpg.draw_line(p1=(point['x1'],point['y1']),p2=(point['x1']+35,point['y1']),thickness=1.5, parent='draw')
    dpg.draw_line(p1=(point['x2'], point['y2']), p2=(point['x2'] + 35, point['y2']),thickness=1.5, parent='draw')
    r_point= dict()
    r_point['x1']=point['x1']+35
    r_point['y1'] = point['y1']
    r_point['x2'] = point['x2'] + 35
    r_point['y2'] = point['y2']
    return r_point

def end_hex_ad(point):
    dpg.draw_line(p1=(point['x1'], point['y1']), p2=(point['x1'] + 15, point['y1'] + 15), thickness=1.5, parent='draw')
    dpg.draw_line(p1=(point['x2'], point['y2']), p2=(point['x2']+ 15, point['y2'] - 15), thickness=1.5, parent='draw')
    point['x1']=point['x1'] + 15
    point['y1']=165
    return point

def cont_line(point):
    dpg.draw_line(p1=(point['x1'],point['y1']),p2=(point['x1']+15,point['y1']),thickness=1.5, parent='draw')
    x = point['x1'] + 15
    point['x1'] = x
    return point

def st_hexagon_cbe(point):
    dpg.push_container_stack(
        dpg.draw_line(p1=(point['x1'], point['y1']), p2=(point['x1'] + 15, point['y1'] - 15), thickness=1.5,
                      parent='draw'))
    dpg.push_container_stack(
        dpg.draw_line(p1=(point['x1'], point['y1']), p2=(point['x1'] + 15, point['y1'] + 15), thickness=1.5,
                      parent='draw'))

    x1 = point['x1'] + 15
    y1 = point['y1'] - 15
    x2 = point['x1'] + 15
    y2 = point['y1'] + 15
    point['x1'] = x1
    point['y1'] = y1
    point['x2'] = x2
    point['y2'] = y2
    return point

def cont_hex_cbe(point):
    dpg.draw_line(p1=(point['x1'], point['y1']), p2=(point['x1'] + 35, point['y1']),thickness=1.5, parent='draw')
    dpg.draw_line(p1=(point['x2'], point['y2']), p2=(point['x2'] + 35, point['y2']),thickness=1.5, parent='draw')
    r_point = dict()
    r_point['x1'] = point['x1'] + 35
    r_point['y1'] = point['y1']
    r_point['x2'] = point['x2'] + 35
    r_point['y2'] = point['y2']
    return r_point

def end_hex_cbe(point):
    dpg.draw_line(p1=(point['x1'], point['y1']), p2=(point['x1'] + 15, point['y1'] + 15), thickness=1.5, parent='draw')
    dpg.draw_line(p1=(point['x2'], point['y2']), p2=(point['x2'] + 15, point['y2'] - 15), thickness=1.5, parent='draw')
    point['x1'] = point['x1'] + 15
    point['y1'] = 245
    return point
#cbe end

def set_position(point):
    dpg.draw_line(p1=(point['x'], point['y']), p2=((point['x'] + 15, point['y'])), thickness=1.5, parent='draw')
    dpg.draw_line(p1=(point['x'] + 15, point['y']), p2=(point['x'] + 30, point['y'] + 20), thickness=1.5, parent='draw')
    x=point['x'] + 30
    y=point['y'] + 20
    point['x'] = x
    point['y'] = y
    return point

def down_position(point):
    dpg.draw_line(p1=(point['x'], point['y']), p2=(point['x'] + 30, point['y']), thickness=1.5, parent='draw')
    x = point['x'] + 30
    point['x']=x
    return point

def upper_position(point):
    dpg.draw_line(p1=(point['x'], point['y']), p2=(point['x'] + 30, point['y']), thickness=1.5, parent='draw')
    x = point['x'] + 30
    point['x'] = x
    return point

def unset_position(point):
    dpg.draw_line(p1=(point['x'], point['y']), p2=(point['x'] + 15, point['y'] -20), thickness=1.5, parent='draw')
    x = point['x'] + 15
    y = point['y'] -20
    point['x'] = x
    point['y'] = y
    return point

