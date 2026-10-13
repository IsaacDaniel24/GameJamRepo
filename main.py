from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)

        self.gun = Entity(parent=self.controller.camera_pivot,
                          scale = 0.1,
                          position = Vec3(0.7,-1,1.5),
                          rotation = Vec3(0,170,0),
                          texture = "images/PIST1.png",
                          visible = True)
        

app = Ursina(title=" After Hours", size=(1280, 720))

piso = Entity(
    model="plane",               
    scale=(20, 1, 20),                
    texture=load_texture("images/textures/floor.png"), 
    texture_scale=(10, 10), 
    unlit=True, 
    collider="mesh",        
)

caja = Entity(model="cube", color=color.red, position=(0, 0.5, 5))


player = Player(position=(0, 1, 0))


app.run()