import time
import sys
from PCI_classes.pci_Work import pci_Work
from PCI_classes.pci_properties import pci_Properties

#Bus model for task1
def pci_model(speed,freq,bitting,type,data_amnt):
    work1 = pci_Work(True, False, None, None, False, False, False, 0)
    propertiez1 = pci_Properties(freq, speed, bitting)
    i = 0
    cnt = 16
    adr = 0
    tmp=0
    if type=='char':
         data_var=1
    elif type == 'short':
        data_var = 32580
    elif type == 'int':
        data_var = 325184478981516084870000007940
        int(data_var)
    elif type =='long':
        data_var=10**17870
    else:
        ctypes.c_int(data_var)

    if speed==264:
        cnt=10
        data_amnt = data_amnt //cnt
    elif speed==528:
        cnt=6
        data_amnt = data_amnt // cnt
    else:
     cnt=16
     data_amnt = data_amnt

    tac = time.perf_counter()

    while (cnt >0):
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

            if work1.IRDY == True and work1.TRDY == True and work1.devsel == True and work1.adress!=None:
                x=data_var*data_amnt
                work1.data += x
                i += 1
                cnt -= 1
            else:
                i += 1
                cnt -= 1
                continue

    tic=time.perf_counter()
    perf=tic-tac
    print(f"Вычисление заняло {perf:0.10f} секунд")
    print(f"SIZEE:: {sys.getsizeof(work1.data)}")

    result = dict()
    result['time']= perf
    result['bytes']=sys.getsizeof(work1.data)


    return result
