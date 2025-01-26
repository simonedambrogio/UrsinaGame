from ursina import *
from panda3d.core import WindowProperties
from functions.settings import *

window.size = size

def adjust_window():
    props = WindowProperties()
    props.set_size(*size)
    props.set_origin(*origin)  # Assuming 1920 is the width of your primary monitor
    # base.win.request_properties(props)

