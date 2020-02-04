from psychopy import event, core, visual
import csv, os, ctypes




win_background = visual.Window(fullscr=True, screen=1,color=(-1,-1,-1), waitBlanking=True, colorSpace='rgb',winType='pyglet', allowGUI=False)

win_foreground = visual.Window(fullscr=True, screen=1,color=(1,1,1), waitBlanking=True, colorSpace='rgb',winType='pyglet', allowGUI=False)

core.wait(10)

win_foreground.close()

core.wait(10)

win_foreground = visual.Window(fullscr=True, screen=1,color=(1,1,1), waitBlanking=True, colorSpace='rgb',winType='pyglet', allowGUI=False)

core.wait(10)

win_foreground.close()

core.wait(10)

win_background.close()

