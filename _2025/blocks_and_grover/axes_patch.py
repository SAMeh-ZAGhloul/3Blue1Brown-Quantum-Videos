from manim_imports_ext import *

# Patch for ThreeDAxes to add the missing get_x_unit_size method
class PatchedThreeDAxes(ThreeDAxes):
    """
    Extended version of ThreeDAxes that adds the get_x_unit_size method
    required by VectorField.
    """
    
    def get_x_unit_size(self):
        """
        Returns the unit size of the x-axis.
        This method is required by VectorField.
        """
        return self.x_axis.get_unit_size()
    
    def get_y_unit_size(self):
        """
        Returns the unit size of the y-axis.
        """
        return self.y_axis.get_unit_size()
    
    def get_z_unit_size(self):
        """
        Returns the unit size of the z-axis.
        """
        return self.z_axis.get_unit_size()
