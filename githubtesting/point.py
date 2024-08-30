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
    
    
    def mirror_about_plane(self, a: float, b: float, c: float, d: float) -> 'Point':
        """
        Mirrors this point about a plane defined by the equation ax + by + cz + d = 0.

        :param a: Coefficient of x in the plane equation.
        :param b: Coefficient of y in the plane equation.
        :param c: Coefficient of z in the plane equation.
        :param d: Constant term in the plane equation.
        :return: New Point that is the mirror image of the original point.
        """
        # Calculate the distance from the point to the plane
        t = (a * self.x + b * self.y + c * self.z + d) / (a**2 + b**2 + c**2)

        # Calculate the mirrored point coordinates
        x_mirrored = self.x - 2 * a * t
        y_mirrored = self.y - 2 * b * t
        z_mirrored = self.z - 2 * c * t

        return Point(x_mirrored, y_mirrored, z_mirrored)


