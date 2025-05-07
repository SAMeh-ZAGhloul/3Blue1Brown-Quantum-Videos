from manim_imports_ext import *

class Ket(VMobject):
    def __init__(self, content=None, **kwargs):
        super().__init__(**kwargs)
        
        # Create the ket notation
        left_ket = Tex(r"|")
        right_ket = Tex(r"\rangle")
        
        # Add the content between ket symbols
        if content is not None:
            if isinstance(content, Mobject):
                content_mob = content
            else:
                content_mob = Tex(str(content))
            
            # Assemble the ket
            self.add(left_ket, content_mob, right_ket)
            self.arrange(RIGHT, buff=0.05)
        else:
            self.add(left_ket, right_ket)
            right_ket.next_to(left_ket, RIGHT, buff=0.5)

class GlowDot(VGroup):
    def __init__(self, point=ORIGIN, radius=0.2, color=YELLOW, **kwargs):
        super().__init__(**kwargs)
        
        # Create the main dot
        dot = Dot(point=point, radius=radius)
        dot.set_fill(color, 1)
        
        # Create the glow effect with multiple dots of decreasing opacity
        glow_dots = VGroup()
        for i in range(5):
            glow = Dot(point=point, radius=radius * (1 + 0.3 * i))
            glow.set_fill(color, 0.8 / (i + 1))
            glow_dots.add(glow)
        
        self.add(glow_dots, dot)

class LineBrace(Brace):
    def __init__(self, line, direction=DOWN, buff=0.1, **kwargs):
        """
        A brace specifically designed for lines
        """
        super().__init__(line, direction, buff=buff, **kwargs)

class Checkmark(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create a checkmark shape
        self.set_points_as_corners([
            LEFT, 
            LEFT + DOWN, 
            RIGHT + UP
        ])
        self.scale(0.5)
        self.set_stroke(GREEN, 3)

class Exmark(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create an X mark shape
        self.set_points_as_corners([
            UP + LEFT, 
            DOWN + RIGHT,
            ORIGIN,
            UP + RIGHT,
            DOWN + LEFT
        ])
        self.scale(0.5)
        self.set_stroke(RED, 3)

class Laptop(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create the base of the laptop
        base = Rectangle(height=0.2, width=1.5)
        base.set_fill(GREY_D, 1)
        base.set_stroke(GREY_B, 1)
        
        # Create the screen of the laptop
        screen_back = Rectangle(height=1, width=1.5)
        screen_back.set_fill(GREY_D, 1)
        screen_back.set_stroke(GREY_B, 1)
        
        screen_front = Rectangle(height=0.9, width=1.4)
        screen_front.set_fill(BLACK, 1)
        screen_front.set_stroke(GREY_B, 1)
        
        # Position the elements
        screen_back.next_to(base, UP, buff=0)
        screen_front.move_to(screen_back)
        
        # Add all elements to the group
        self.add(base, screen_back, screen_front)
        
        # Rotate to look like a laptop
        self.rotate(80 * DEGREES, RIGHT)

# Add any other classes or functions needed for state vectors
