from ursina import *
import os 

basepath = "/Volumes/PROJECTS/Ongoing/game/minecraft-tutorial"

filepath = {
    "tree": [
		{
            "trunk": {
                "model"  : "models/trunk0",
                "texture": "textures/trunk0",
            },
            "crown": {
                "model"  : "models/crown0",
                "texture": "textures/crown0",
            }
        },

        {
            "trunk": {
                "model"  : "models/trunk1",
                "texture": "textures/trunk1",
            },
            "crown": {
                "model"  : "models/crown1",
                "texture": "textures/crown1",
            }
        }
    ]

}

# /Volumes/PROJECTS/Ongoing/game/minecraft-tutorial/assets/textures/BarkDecidious0143_5_S.jpg

# class Block(Entity):
#   def __init__(self, position, block_type):
#     super().__init__(
#       position=position,
#       model="assets/models/block_model",
#       scale=1,
#       origin_y=-0.5,
#       texture=block_textures.get(block_type),
#       collider="box"
#       )
#     self.block_type = block_type


def create_grouped_entities(models, textures, position=(0,0,0), scale=1, collider="box", parent=None):
    base_entity = Entity(position=position, parent=parent)
    entities = []
    for (i, model_name) in enumerate(models):
        entity = Entity(
           model=load_model(model_name), 
           texture= load_texture(textures[i]), 
           scale=scale, 
           position=position, 
           parent=base_entity,
           collider=collider
        )
        entities.append(entity)
    return base_entity, entities

def drawTree(typ, position=(0,0,0), scale=0.3, collider="box"):
    # typ indicates the type of tree
    tree, components = create_grouped_entities(
        models = [
            filepath["tree"][typ]["trunk"]["model"],
            filepath["tree"][typ]["crown"]["model"]
        ],
        textures = [
            filepath["tree"][typ]["trunk"]["texture"],
            filepath["tree"][typ]["crown"]["texture"]
        ],
        scale=scale,
        position=position,
        collider=collider
    )
    return tree, components


# def tree1():
#   tronco = Entity(
#     model = "assets/TreeSet2/tronco.obj",
#     scale=.3,
#     texture = '/Textures/BarkDecidious0143_5_S.jpg',
#     collider="box"
#   )
#   chioma = Entity(
#     model = "assets/TreeSet2/chioma.obj",
#     scale=.3,
#     texture = 'Textures/Leaves0120_35_S.png',
#   )
#   return tronco, chioma