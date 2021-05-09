from manimlib import *
from big_ol_pile_of_manim_imports import *
import numpy as np  



class DrawField(ThreeDScene):
    CONFIG = {
        "plane_kwargs" : {
        "color" : RED_B
    },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)
        self.wait()
        field = VGroup(*[self.calc_field(x*RIGHT+y*UP+z*OUT) for x in np.arange(-5,5,1) for y in np.arange(-5,5,1) for z in np.arange(0,10,1)])
        
        self.play(ShowCreation(plane))
        self.play(ShowCreation(field))
        self.move_camera(phi=45*DEGREES,theta=-45*DEGREES,run_time=3)
        self.play(Rotating(field))
        
    
    def calc_field(self, point):
        x, y, z = point
        efield = np.array([-y,x,z])/math.sqrt(x**2+y**2+z**2)
        return Vector(efield).shift(point)

    
    


