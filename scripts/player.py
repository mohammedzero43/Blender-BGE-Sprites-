####################################################################
# This is the player File , the class script is in the other file
# You need to Import spriter.py to your script
###############
# Your sprites should be added as separate objects and named as :
# SPR_NAME.Frame , For example Sprite.01
###############
# Class Variables you can access:
#   spr_name 
#   spr_frame
#   spr_speed
#   spr_loop
###############  
#   1 - 2 : change the Sprite (by changing the name)  Monster / Dragon 
#   q - w : change the current frame -1/+1 
#   a - d : change the speed to  0 (0 frame/sec )/1 (60 frame /sec)  *FrameRate changes depending on you game settings
#   z - x : change the Looping to  0 (no loop) / 1(loop)
###############
# If you have new Ideas please contact me :
#   Mohammedzero43@hotmail.com  
#
#       ^^  Please , Give Credits if used . Enjoy ^^
#                        MohammedZero 
####################################################################



import spriter
import bge
cont = bge.logic.getCurrentController()
own = cont.owner

#Initialize the class
spriters = spriter.sprite(own["spr_name"],own["spr_frame"],own["spr_speed"],own["spr_loop"])

def update():
   #Update Class Variables (Write Only) - Note : You can use Variables directly , but this will not let other objects contact with this object's sprite properties
    spriters.spr_frame = own["spr_frame"] 
    spriters.spr_name = own["spr_name"] 
    spriters.spr_speed = own["spr_speed"]
    spriters.spr_loop = own["spr_loop"] 
    #sprite and properties refresh 
    spriters.update()
    #used to contact with other Objects (Read Only)
    own["spr_frame"] = spriters.spr_frame
    own["spr_name"] = spriters.spr_name
    own["spr_speed"] = spriters.spr_speed
    own["spr_looop"] = spriters.spr_loop
