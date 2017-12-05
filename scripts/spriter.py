##############################
#Created By MohammedZero     #
#Mohammedzero43@hotmail.com  #
##############################

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
        elif self.spr_speed <= -1 :
            self.spr_speed = -1       
            
        
        #Get sprite Objects
        for i in scene.objects:
            if i.name[:(len(self.spr_name)+1)]==self.spr_name+".":
                sprite_list.append(i.name)
        for i in scene.objectsInactive:
            if i.name[:(len(self.spr_name)+1)]==self.spr_name+".":
                sprite_list.append(i.name)
        sprite_list.sort()  
        
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
                    
        #looping              
        if self.spr_loop == True:
            if self.spr_frame > len(sprite_list)-1:
                self.spr_frame = 0  
            if self.spr_frame < 0:
                self.spr_frame = len(sprite_list)-1
        else :
            if self.spr_frame > len(sprite_list)-1:
                self.spr_frame = len(sprite_list)-1 
            
            if self.spr_frame < 0:
                self.spr_frame = 0
             
        
                   
        #animating 
        for name in sprite_list:
           if name in Sobjects:
               if str(Sobjects[name]) == str(sprite_list[self.spr_frame]):
                   own.replaceMesh(Sobjects[name].meshes[0],1,0)
           if name in scene.objectsInactive:            
               if str(scene.objectsInactive[name]) == str(sprite_list[self.spr_frame]):
                   own.replaceMesh(scene.objectsInactive[name].meshes[0],1,0)
        
        #Framing
        if (self._framer > 1):
            self._framer = 0
            self.spr_frame += 1
            
        self._framer += self.spr_speed
        self._old = self.spr_name     
             
        
       