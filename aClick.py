''' Author: Luong Huyen Thuong
	Date: 14-08-2024
	Version: 1.3
	Usage: Users can give value to parameter like time between sleep in minute or changing tabs in second, path to sound file and positions of mouse (CLI). 9 Tabs on left handside, 14 Tabs on right handside. 
'''

class MyException(Exception): pass

import time, sys
import click
import playsound
from pynput.mouse import Button, Controller
from pynput import keyboard

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--minutes', type=int, default=5, help='die Periode zwischen automatischen Klicks')  
@click.option('--tab', type=int, default=5, help='? Sekunden dann Tab wechseln')  
@click.option('--monitorL1', nargs=3, default=(120,20,1), help="1.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option('--monitorL2', nargs=3, default=(300,20,2), help="2.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option('--monitorL3', nargs=3, default=(480,20,1), help="3.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option("--monitorL4", nargs=3, default=(660,20,0), help="4.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option("--monitorL5", nargs=3, default=(850,20,1), help="5.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option("--monitorL6", nargs=3, default=(1050,20,1), help="6.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option("--monitorL7", nargs=3, default=(1230,20,1), help="7.Plaetz der Maus zum Klicken auf linkem Monitor") 
@click.option("--monitorL8", nargs=3, default=(1410,20,0), help="8.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option("--monitorL9", nargs=3, default=(1600,20,0), help="9.Plaetz der Maus zum Klicken auf linkem Monitor")
@click.option('--monitorR1', nargs=3, default=(2010,20,0), help="1.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option('--monitorR2', nargs=3, default=(2130,20,1), help="2.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option('--monitorR3', nargs=3, default=(2250,20,2), help="3.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR4", nargs=3, default=(2370,20,1), help="4.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR5", nargs=3, default=(2490,20,0), help="5.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR6", nargs=3, default=(2610,20,0), help="6.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR7", nargs=3, default=(2730,20,0), help="7.Plaetz der Maus zum Klicken auf rechtem Monitor") 
@click.option("--monitorR8", nargs=3, default=(2850,20,1), help="8.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR9", nargs=3, default=(2970,20,0), help="9.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR10", nargs=3, default=(3090,20,2), help="10.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR11", nargs=3, default=(3200,20,0), help="11.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR12", nargs=3, default=(3320,20,0), help="12.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR13", nargs=3, default=(3440,20,0), help="13.Plaetz der Maus zum Klicken auf rechtem Monitor")
@click.option("--monitorR14", nargs=3, default=(3560,20,1), help="14.Plaetz der Maus zum Klicken auf rechtem Monitor") 
@click.option("--file", type=str, default='mouse-click.mp3', help='Dateiname von Klingel (im aktuellen Ordner')
@click.version_option(version='1.3')
def autorun(monitorl1,monitorl2,monitorl3,monitorl4,monitorl5,monitorl6,monitorl7,monitorl8,monitorl9, monitorr1,monitorr2,monitorr3,monitorr4,monitorr5,monitorr6,monitorr7,monitorr8,monitorr9,monitorr10,monitorr11,monitorr12,monitorr13,monitorr14, minutes, tab, file):
    """
    Sau khi cai python 3.12 can cai them 1 so module ghi o phan import phia tren
    de them/bot tab chi can them/bot may dong @click.option("--monitor... o tren cho phu hop, sau do kich hoat moi truong (trong windows tai thu muc chua file aClick.py chay lenh Scrips/activate
    roi go vd: python aClick.py --monitorL1 100 20 3 --minutes=11 --file=warning.mp3 --tab=5
    voi --monitor (man hinh) L (trai) hoac R (phai) STT tab toa_do_x toa_do_y so_lan_an_pageDOWN/UP
    --file duong_dan_tuong_doi_den_file_nhac_chuong
    --minutes thoi_gian_nghi_giua_nhung_lan_xem_tab
    --tab so_giay_cho_giua_2_tab
    chay ok co the xuat ra file .exe de chay tren cac may khong co cai python
    Can cai module PyInstaller sau do xuat ra file exe voi lenh python -m PyInstaller -F aClick.py
    """
    monitorL = [monitorl1,monitorl2,monitorl3,monitorl4,monitorl5,monitorl6,monitorl7,monitorl8,monitorl9] #[(270,20,3),(430,20,0),(610,20,0),(780,20,2),(1030,20,2),(1230,20,0),(1420,20,0)]
    monitorR = [monitorr1,monitorr2,monitorr3,monitorr4,monitorr5,monitorr6,monitorr7,monitorr8,monitorr9,monitorr10,monitorr11,monitorr12,monitorr13,monitorr14] #[(2230,20,0),(2410,20,0),(2610,20,0),(2780,20,3),(2960,20,0),(3140,20,2),(3320,20,0)]
    try:
        while True:
            playsound.playsound(file)
            fetch(monitorL,monitorR,tab)
            time.sleep(minutes*60)
    except KeyboardInterrupt:
        click.echo('\nDung tu dong click')

def fetch(positionsL,positionsR,tab):
    c=0
    for position in positionsL:
        x = position[0]
        y = position[1]
        s = position[2]
        x1 = positionsR[c][0]
        y1 = positionsR[c][1]
        s1 = positionsR[c][2]
        m.position=(x,y)
        m.press(Button.left)
        m.release(Button.left)
        time.sleep(tab)
        if s != '0':
            i=0
            while (i<s):
                k.press(keyboard.Key.page_down)
                time.sleep(4)
                i+=1
            i=0
            while (i<s):
                k.press(keyboard.Key.page_up)
                i+=1
        m.position=(x1,y1)
        m.press(Button.left)
        m.release(Button.left)
        time.sleep(tab)
        if s1 != '0':
            i=0
            while (i<s1):
                k.press(keyboard.Key.page_down)
                time.sleep(4)
                i+=1
            i=0
            while (i<s1):
                k.press(keyboard.Key.page_up) 
                i+=1
        c=c+1
    if len(positionsR) > len(positionsL):
        for i in range(len(positionsL), len(positionsR)):
            x = positionsR[i][0]
            y = positionsR[i][1]
            s = positionsR[i][2]
            m.position=(x,y)
            m.press(Button.left)
            m.release(Button.left)
            time.sleep(tab)
            if s != '0':
                i=0
                while (i<s):
                    k.press(keyboard.Key.page_down)
                    time.sleep(4)
                    i+=1
                while (i>0):
                    k.press(keyboard.Key.page_up)
                    i-=1

if __name__ == '__main__':
    m = Controller()
    k = keyboard.Controller()
    try:
        autorun() 
    except MyException as e:
        print('Loi:').format(e.args[0])
