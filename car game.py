from ursina import *

app = Ursina()
camera.orthographic = True
camera.fov = 10

car = Entity(
    model='quad',
    texture='assets\car',
    collider='box',
    scale=(2,1),
    rotation_z=-90

)

