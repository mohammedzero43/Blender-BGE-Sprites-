####################################################################
# Advanced Sprites for BGE :
#	Usage : 
#	Always Sensor (Pulse on) -> Python controller (script = "spriterUV.py" or anything you name the script file as)
###############
#
###############
# Properties to add:
# int     sprite_index  : sub-frame inside a sprite_image  (X-Axis)
# int     image_index   : sprite it self                   (Y-Axis)
# int     sprite_len    : Number of sub-frames in a row    (Length of X-Axis)
# double  sprite_speed  : Number of frames/sec (1 = game speed ;Default BGE = 60 fps)
# bool    spr_loop      : Looping of Sub-frames
###############  
#       ^^  Please , Give Credits if used . Enjoy ^^
#                mohammedzero43 /or/ Xtremezero
####################################################################


import bge
cont = bge.logic.getCurrentController()
own  = cont.owner
scene= bge.logic.getCurrentScene()

mesh = own.meshes[0]
m_index = mesh.materials[0]
v0 = mesh.getVertex(0,0)
v1 = mesh.getVertex(0,1)
v2 = mesh.getVertex(0,2)
v3 = mesh.getVertex(0,3)

#first locations of UV coordinations
if not 'v0_o' in own: 
    own['v0_o']= v0.getUV()
    own['v1_o']= v1.getUV()
    own['v2_o']= v2.getUV()
    own['v3_o']= v3.getUV()

v0_o= own['v0_o']
v1_o= own['v1_o']
v2_o= own['v2_o']
v3_o= own['v3_o']



#offsets calculations
if not 'x_offset' in own:
    own['x_offset'] =v1_o[0]-v0_o[0]  #x1-x0
    own['y_offset'] =v3_o[1]-v0_o[1]  #y3-y0
x_offset=own['x_offset'] 
y_offset=own['y_offset'] 

#Variables / properties (init)
if not "sprite_index" in own:
    own["sprite_index"]=0

    
if not "sprite_len" in own:
    own["sprite_len"]=0

    
if not "sprite_speed" in own:
    own["sprite_speed"]=1.0


if not "image_index" in own:
    own["image_index"]=1


if not "spr_loop" in own:
    own["spr_loop"]=True


if not "image_index_pre" in own:
    own["image_index_pre"]=own["image_index"]


if not "timer" in own:
    own["timer"]=0.0


#Variables/Properties Read 
sprite_index= own["sprite_index"]
sprite_len= own["sprite_len"]
sprite_speed=own["sprite_speed"]
image_index = own["image_index"]
loop = own["spr_loop"]
image_index_pre = own["image_index_pre"]
timer =  own["timer"]
#Reseting on image change
if image_index != image_index_pre:
    sprite_index = 0
image_index_pre=image_index

#Looping
if sprite_index>=sprite_len: 
    if loop:
        sprite_index = 0
    else: 
        sprite_index = sprite_index-1

#Animating
v0.setUV([v0_o[0]+(x_offset*sprite_index),v0_o[1]-(y_offset*image_index)])
v1.setUV([v1_o[0]+(x_offset*sprite_index),v1_o[1]-(y_offset*image_index)])
v2.setUV([v2_o[0]+(x_offset*sprite_index),v2_o[1]-(y_offset*image_index)])
v3.setUV([v3_o[0]+(x_offset*sprite_index),v3_o[1]-(y_offset*image_index)])

#Prep. for next frame
#Framing
if timer > 1:
    timer = 0
    sprite_index += 1
    


timer += sprite_speed * (1/bge.logic.getLogicTicRate()) * 10
image_index_pre=image_index

   
#Properties/lVariables Write
own['timer']= timer
own['image_index_pre']= image_index
own["sprite_index"]=sprite_index
own["sprite_len"]=sprite_len
own["image_index"]=image_index
own["loop"]=loop
