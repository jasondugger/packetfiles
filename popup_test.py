"""
"""

import PySimpleGUI as sg

def create_window():
    sg.popup_get_text('Enter something on this window')

if __name__ == '__main__':
    create_window()