from ursina import *

app=Ursina()

animated_model = FrameAnimation3d('models/imported/obj-wolf/wolf', fps=24, loop=True, autoplay=True)


EditorCamera()
app.run()