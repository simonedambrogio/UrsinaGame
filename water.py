from ursina import *

app = Ursina()

waterfall = Entity(
	model='models/blender/waterfall.obj',
	position=(0,-2,0),
	# texture_scale=(3,2),
	texture = f"textures/make-textures/0.png"
	# texture_rotation = (0, 90, 0)
	# scale=0.1
)

# plane = Entity(
# 	model='plane',
# 	position=(0,-2,0),
# 	scale=10,

# 	# rotation=(10, 180, 0),
#     texture_scale=(2,2),
# 	texture = "brick",
# 	# texture_rotation = (0, 90, 0)
# 	# scale=0.1
# )

cumtime, frameid = 0, 0
def update():
    global cumtime, frameid  # Declare cumtime and frameid as global
    
    cumtime += time.dt
    if cumtime > .1:
        cumtime = 0
        frameid += 1  # Increment frameid
        if frameid >= 34:
            frameid = 0
        waterfall.texture = f"textures/make-textures/{34-frameid}.png"


# for (n, e) in enumerate(waterfall.frames):
# 	e.texture = f"textures/make-textures/{n}.png"

EditorCamera()
app.run()
