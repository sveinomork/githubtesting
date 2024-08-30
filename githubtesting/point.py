from dataclasses import dataclass

@dataclass
class Point:
    x:float
    y:float
    z:float

    def translate(self,vx:float,vy:float,vz:float)->'Point':
        self.x+=vx
        self.y+=vy
        self.z+=vz
        return self
    
    
    


