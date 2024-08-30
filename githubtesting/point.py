from dataclasses import dataclass
import math
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
    
    def distance_to(self, other: 'Point') -> float:
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 +
                    (self.y - other.y) ** 2 +
                    (self.z - other.z) ** 2)
    

    


