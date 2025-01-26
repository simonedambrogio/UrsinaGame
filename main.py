from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from functions.setup import *
from functions.settings import *
from functions.utils import *

app = Ursina()


# Add a Sky dome with a preset texture
sky = Sky(texture='sky_sunset')

player = FirstPersonController(
    mouse_sensitivity=Vec2(100,100),
    position=Vec3(2, 30, -45),
    speed=15
)

cumtime, lakespeed, frameid, frameid1 = 0, 0, 0, 0
def update():
    global cumtime, frameid, lakespeed, frameid1  # Declare cumtime and frameid as global
    
    cumtime += time.dt
    lakespeed += time.dt

    if cumtime > .1:
      cumtime = 0
      frameid += 1  # Increment frameid
      if frameid >= 34:
          frameid = 0
      waterfall.texture = f"textures/make-textures/{34-frameid}.png"
      bwaterfall.texture = f"textures/make-textures/{34-frameid}.png"

    if lakespeed > 0.2:
      lakespeed=0
      frameid1 += 1  # Increment frameid
      if frameid1 >= 34:
          frameid1 = 0
      lakewaterfall.texture = f"textures/make-textures/{frameid1}.png"
        

waterfall = Entity(
	model='models/blender/wf.obj',
   scale=1.5,
   rotation=(5, 0, 0)
)
lakewaterfall = Entity(
	model='models/blender/lake-waterfall.obj',
   scale=1.5,
   rotation=(5, 0, 0)
)

stones = Entity(
	model='models/blender/stones.obj',
   texture="textures/RockTexture1",
   scale=1.5,
   rotation=(5, 0, 0)
)


bwaterfall = Entity(
	model='models/blender/bwf.obj',
   scale=1.5,
   rotation=(5, 0, 0)
)


cespugli = Entity(
	model='models/blender/cespugli.obj',
   texture="textures/crown0",
  scale=1.5,
  rotation=(5, 0, 0)
)

myground = Entity(
  model='models/blender/ground.obj',
  texture='models/blender/metarial',
  scale=1.5,
  collider="mesh",
  rotation=(5, 0, 0)
)

lake = Entity(
  model='models/lake',
  texture='sky_default',
  scale=1.5,
  rotation=(5, 0, 0)
)


# Sign ---
signwood = Entity(
  model='models/sign.obj',
  texture='textures/sign-wood',
  scale=1.5,
  collider="mesh",
  rotation=(5, 0, 0)
)

signleft = Entity(
  model='models/blender/stage1-left.obj',
  texture='textures/waterfall-sign-left',
  scale=1.5,
  collider="mesh",
  rotation=(5, 0, 0)
)

signright = Entity(
  model='models/blender/stage1-right.obj',
  texture='textures/waterfall-sign-right',
  scale=1.5,
  collider="mesh",
  rotation=(5, 0, 0)
)


crowns = Entity(
  model='models/blender/crowns.obj',
  texture='textures/crown0',
  scale=1.5,
  # collider="mesh",
  rotation=(5, 0, 0)
)

trunks = Entity(
  model='models/blender/trunks.obj',
  texture='textures/trunk0',
  scale=1.5,
  # collider="mesh",
  rotation=(5, 0, 0)
)


# for z in range( -30, 0, 4):
#   for x in [-2, 2]:
#     if np.random.rand()<0.8:
#       tree, components = drawTree(0, position = (x+np.random.rand()*0.3+0.2, 2, z+np.random.rand()*0.3+0.2))
    
# for z in range( -30, -5, 4):
#   for x in [-3.5, 3.5]:
#     if np.random.rand()<0.8:
#       if bool(np.random.binomial(1, 0.8)):
#         tree, components = drawTree(0, position = (x+np.random.rand(), 3, z+np.random.rand()))
#       else:
#         tree, components = drawTree(1, position = (x+np.random.rand(), 3, z+np.random.rand()))




# EditorCamera()
app.run()