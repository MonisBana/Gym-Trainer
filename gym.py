import serial
import numpy as np

import time
from datetime import datetime
from gpiozero import Buzzer
class Gym:
    error_count=0
    buzzer = Buzzer(17)
    anx=0
    any=0
    temp=0
    anz=0
    T=0
    i = 0
    result=[]
    L=np.zeros((3,),dtype='float')
    a=np.zeros((3,),dtype='float')
    ang=np.zeros((3,),dtype='float')
    ser = serial.Serial('/dev/rfcomm12', 115200)
    def one():
        while True:
            def convert(val):
                from bitstring import Bits
                temp = hex(val)
                a = Bits(hex=temp)
                return a.int


            result.insert(i, ord(ser.read()))
            if i == 0 and result[0] != 0x55:
                continue
            else:
                i = i + 1
                if i != 11:
                    continue
                else:
                    i = 0
                    x = np.array(
                        [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
                         result[9], result[10]], dtype='uint8')
                    if x[1] == 81:
                        L[0] = (convert(x[3] << 8 | x[2])) / 32768.0 * 16
                        L[1] = (convert(x[5] << 8 | x[4])) / 32768.0 * 16
                        L[2] = (convert(x[7] << 8 | x[6])) / 32768.0 * 16
                        # T = (x[9] << 8 | x[8]) / 340.0 + 36.25

                    elif x[1] == 82:
                        a[0] = (convert(x[3] << 8 | x[2])) / 32768.0 * 2000
                        a[1] = (convert(x[5] << 8 | x[4])) / 32768.0 * 2000
                        a[2] = (convert(x[7] << 8 | x[6])) / 32768.0 * 2000
                        # T = (x[9] << 8 | x[8]) / 340.0 + 36.25

                    else:
                        ang[0] = (convert(x[3] << 8 | x[2])) / 32768.0 * 180
                        ang[1] = (convert(x[5] << 8 | x[4])) / 32768.0 * 180
                        ang[2] = (convert(x[7] << 8 | x[6])) / 32768.0 * 180
                        # T = (result[9] << 8 | result[8]) / 340.0 + 36.25

                    if 85 < ang[0] < 102:
                        error_count += 1
                        print(error_count)
                        buzzer.on()
                    else:
                        buzzer.off()
                    # thewriter.writerow([(datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]),L[0],L[1],L[2],ang[0],ang[1],ang[2]])
                    # print((datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]),L,ang)
                    print(error_count)
    def two():
        while True:
            def convert(val):
                from bitstring import Bits
                temp = hex(val)
                a = Bits(hex=temp)
                return a.int


            result.insert(i, ord(ser.read()))
            if i == 0 and result[0] != 0x55:
                continue
            else:
                i = i + 1
                if i != 11:
                    continue
                else:
                    i = 0
                    x = np.array(
                        [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
                         result[9], result[10]], dtype='uint8')
                    if x[1] == 81:
                        L[0] = (convert(x[3] << 8 | x[2])) / 32768.0 * 16
                        L[1] = (convert(x[5] << 8 | x[4])) / 32768.0 * 16
                        L[2] = (convert(x[7] << 8 | x[6])) / 32768.0 * 16
                        # T = (x[9] << 8 | x[8]) / 340.0 + 36.25

                    elif x[1] == 82:
                        a[0] = (convert(x[3] << 8 | x[2])) / 32768.0 * 2000
                        a[1] = (convert(x[5] << 8 | x[4])) / 32768.0 * 2000
                        a[2] = (convert(x[7] << 8 | x[6])) / 32768.0 * 2000
                        # T = (x[9] << 8 | x[8]) / 340.0 + 36.25

                    else:
                        ang[0] = (convert(x[3] << 8 | x[2])) / 32768.0 * 180
                        ang[1] = (convert(x[5] << 8 | x[4])) / 32768.0 * 180
                        ang[2] = (convert(x[7] << 8 | x[6])) / 32768.0 * 180
                        # T = (result[9] << 8 | result[8]) / 340.0 + 36.25

                    if 85 < ang[0] < 102:
                        error_count += 1
                        print(error_count)
                        buzzer.on()
                    else:
                        buzzer.off()
                    # thewriter.writerow([(datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]),L[0],L[1],L[2],ang[0],ang[1],ang[2]])
                    # print((datetime.utcnow().strftime('%H:%M:%S.%f')[:-3]),L,ang)
                    print(error_count)
