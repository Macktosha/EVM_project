import dearpygui.dearpygui as dpg
from PCI_classes.pci_Work import pci_Work
from PCI_classes.pci_properties import pci_Properties
from PCI_classes.pci_model import pci_model


def emulate_transaction(sender,app_data):
    dpg.push_container_stack(dpg.add_window(label="Task1",width=1050,height=800,pos=[150,0]))
    amnt  = dpg.get_value(sender)
    d = pci_model(132,33,32,'char',amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 33MHz; 32-bit"))
    dpg.add_spacer(height=4)
    d = pci_model(132, 33, 32, 'int', amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 33MHz; 32-bit"))
    dpg.add_spacer(height=4)
    d = pci_model(132, 33, 32, 'long', amnt)
    dpg.push_container_stack(dpg.add_text( f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 33MHz; 32-bit"))

    dpg.add_spacer(height=45)
    dpg.draw_line(p1=(20,110),p2=(1000,110))

    d = pci_model(264, 33, 64, 'char', amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 33/66MHz; 64/32-bit"))
    dpg.add_spacer(height=4)
    d = pci_model(264, 33, 64, 'int', amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 33/66MHz; 64/32-bit"))
    dpg.add_spacer(height=4)
    d = pci_model(264, 33, 64, 'long', amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 33/66MHz; 64/32-bit"))

    dpg.add_spacer(height=45)
    dpg.draw_line(p1=(20, 240), p2=(1000, 240))

    d = pci_model(528, 66, 64, 'char', amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 66MHz; 64-bit"))
    dpg.add_spacer(height=4)
    d = pci_model(528, 66, 64, 'int', amnt)
    dpg.push_container_stack(dpg.add_text(f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 66MHz; 64-bit"))
    dpg.add_spacer(height=4)
    d = pci_model(528, 66, 64, 'long', amnt)
    dpg.push_container_stack(dpg.add_text( f"Bus obtained {d['bytes']} bytes in {d['time']:0.10f} seconds with PCI properties: frequency = 66MHz; 64-bit"))


def task1_callback(sender,app_data):
      dpg.push_container_stack(dpg.add_window(label="Task 1 window",width=1050,height=800,pos=[150,0]))
      dpg.push_container_stack(dpg.add_input_int(label="Enter amount of data",callback=emulate_transaction,on_enter=True,max_value=1000000000))



