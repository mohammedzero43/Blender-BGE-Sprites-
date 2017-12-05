####################################################################
# Spriter for BGE :
#	Usage : 
#	Always Sensor (Pulse on) -> Python controller (module = "spriter3.1.py" or anything you name the script file as)
###############
# Your sprites should be added as separate objects and named as :
# SPR_NAME.Frame , For example Sprite.01
###############
# Properties to add:
#   spr_name 
#   spr_frame
#   spr_speed
#   spr_loop
###############  
# If you have new Ideas please contact me :
#   Mohammedzero43@hotmail.com  
#
#       ^^  Please , Give Credits if used . Enjoy ^^
#                        mohammedzero 
####################################################################


#initialization
import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scene= bge.logic.getCurrentScene()
Sobjects = scene.objects 

class sprite():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene= bge.logic.getCurrentScene()
    Sobjects = scene.objects 
    #passive vars
    _framer = 0
    _old = ""
    
    #public vars
    spr_name=""
    spr_frame=0
    spr_speed=0
    spr_loop=0
    
    def __init__(self,spr_name="",spr_frame=0,spr_speed=0,spr_loop=0):
        self.spr_name=spr_name
        self.spr_frame=spr_frame
        self.spr_speed=spr_speed
        self.spr_loop=spr_loop
        
    def update(self):
        
        #Sprite Attributes fix and update
        
        sprite_list = [] 
        if self.spr_speed >= 1:
            self.spr_speed = 1
        elif self.spr_speed <= 0 :
            self.spr_speed = 0       
            
        
        #Get sprite Objects
        for i in scene.objects:
            if i.name[:(len(self.spr_name)+1)]==self.spr_name+".":
                sprite_list.append(i.name)
        for i in scene.objectsInactive:
            if i.name[:(len(self.spr_name)+1)]==self.spr_name+".":
                sprite_list.append(i.name)
        sprite_list.sort()  
        sprite_tup = tuple(sprite_list)
        del(sprite_list)
        
        #Replaces the Sprites
        
        if  (self.spr_name != self._old) and self._old !="":
            self.spr_frame = 0
            sprite_list=[]
            for i in scene.objects:
                if i.name[:(len(self.spr_name)+1)]==self.spr_name+".":
                    sprite_list.append(i.name)
            for i in scene.objectsInactive:
                if i.name[:(len(self.spr_name)+1)]==self.spr_name+".":
                    sprite_list.append(i.name)        
            sprite_list.sort()
            sprite_tup = tuple(sprite_list)
            del(sprite_list)
            
        #looping              
        if self.spr_loop == True:
            if self.spr_frame > sprite_tup.__len__()-1:
                self.spr_frame = 0  
            if self.spr_frame < 0:
                self.spr_frame = sprite_tup.__len__()-1
        else :
            if self.spr_frame > sprite_tup.__len__()-1:
                self.spr_frame = sprite_tup.__len__()-1 
            
            if self.spr_frame < 0:
                self.spr_frame = 0
                    
                   
        #animating 
        for name in sprite_tup:
           if name in Sobjects:
               if str(Sobjects[name]) == str(sprite_tup[self.spr_frame]):
                   own.replaceMesh(Sobjects[name].meshes[0],1,1)
           if name in scene.objectsInactive:            
               if str(scene.objectsInactive[name]) == str(sprite_tup[self.spr_frame]):
                   own.replaceMesh(scene.objectsInactive[name].meshes[0],1,1)
        
        #Framing
        if (self._framer > 1):
            self._framer = 0
            self.spr_frame += 1
            
        self._framer += self.spr_speed
        self._old = self.spr_name     
             

def update():
    if ("spr_frame" not in own) and ("spr_name" not in own) and ("spr_speed" not in own) and ("spr_loop" not in own):
	return 0;
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
       
