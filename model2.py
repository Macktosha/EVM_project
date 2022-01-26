import time
import sys
from PCI_classes.pci_Work import pci_Work
from PCI_classes.pci_properties import pci_Properties
#Bus model for task2

def model2(in_data):
    work1 = pci_Work(True, False, None, None, False, False, False, 0)
    i = 0
    j=0
    cnt = len(in_data)
    adr = 0
    work1.data=list()

    while (j!=cnt):
            work1.frame = True
            if i%2 == 0:
                work1.clck = True
            else:
                work1.clck = False

            if work1.clck == True and adr == 0:
                work1.adress = "Some adress"
                work1.IRDY = True
                work1.TRDY = True
                work1.devsel = True
                work1.CBE = 'Some command'
                adr = 1
                i+=1
                continue
            else:
                work1.IRDY = True
                work1.TRDY = True
                work1.devsel = True
                work1.CBE = 'Some command'

            if work1.IRDY == True and work1.TRDY == True and work1.devsel == True and work1.adress!=None and work1.clck==True:
                work1.data.append(in_data[j])
                i += 1
                j+=1
            else:
                i += 1
                continue
    print(work1.data)
    return work1.data