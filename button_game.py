#!/usr/bin/python3
import math
import random
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class button_atr(Gtk.Button):
    def __init__(self, ind):
        Gtk.Button.__init__(self, label='XX')
        self.ind = ind

class GridWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Game")

        grid = Gtk.Grid()
        self.add(grid)
        self.n = 36 #число кнопок
        self.myArray = [] #massiv s knopkami
        self.a=None
        self.b=None
        self.but_ind_a=0
        self.but_ind_b=0
        self.arr = []
        self.arr = []
        for i in range(self.n // 2):
            self.arr.append(i)
        self.arr = self.arr + self.arr
        self.arr = random.sample(self.arr, self.n)
        print(self.arr)
        for x in range(0, self.n):

            self.button = button_atr(x)

            self.button.connect("clicked", self.on_click_me_clicked)
            self.myArray.append(self.button)
            if x==0:
                grid.add(self.button)
            elif x < round(math.sqrt(self.n)):
                grid.attach_next_to(self.myArray[x], self.myArray[x-1], Gtk.PositionType.RIGHT, 1, 1)
            else:
                grid.attach_next_to(self.button,self.myArray[x-round(math.sqrt(self.n))], Gtk.PositionType.BOTTOM, 1, 1)

    def on_click_me_clicked(self, button):


        if self.a != self.b and self.a != None and self.b != None and self.arr[int(self.a)] != self.arr[int(self.b)]:

            self.myArray[self.a].set_label('XX')
            self.myArray[self.b].set_label('XX')
            self.a = None
            self.b = None
        elif self.a == self.b == None:
            self.a = button.ind
            button.set_label(str(self.arr[button.ind]))
        elif self.b == None:
            self.b = button.ind
            button.set_label(str(self.arr[button.ind]))
        elif self.arr[int(self.a)] == self.arr[int(self.b)] and self.a != self.b:
            self.myArray[int(self.a)].set_sensitive(False)
            self.myArray[int(self.b)].set_sensitive(False)
            self.a = None
            self.b = None
        elif self.arr[int(self.a)] == self.arr[int(self.b)] and self.a == self.b:
            self.myArray[self.a].set_label('XX')
            self.myArray[self.b].set_label('XX')
            self.a = None
            self.b = None
win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
