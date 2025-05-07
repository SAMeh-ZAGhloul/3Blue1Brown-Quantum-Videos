from manim_imports_ext import *

def get_quantum_computer_symbol(height=1.0):
    """
    Creates a quantum computer symbol (stylized Q)
    """
    try:
        q_symbol = SVGMobject("quantum_q")
        if q_symbol.has_no_points():
            raise Exception("SVG has no points")
    except:
        # Fallback if SVG is not available
        q_symbol = Text("Q", font="Arial")

    q_symbol.set_fill(TEAL, 1)
    q_symbol.set_height(height)
    return q_symbol

def get_classical_computer_symbol(height=1.0):
    """
    Creates a classical computer symbol
    """
    try:
        c_symbol = SVGMobject("classical_computer")
        if c_symbol.has_no_points():
            raise Exception("SVG has no points")
    except:
        # Fallback if SVG is not available
        c_symbol = Text("C", font="Arial")

    c_symbol.set_fill(BLUE, 1)
    c_symbol.set_height(height)
    return c_symbol

def get_blackbox_machine(height=2.0, label_tex="f"):
    """
    Creates a black box machine with a label
    """
    box = Rectangle(height=height, width=height*0.8)
    box.set_fill(GREY_D, 1)
    box.set_stroke(WHITE, 2)

    if label_tex:
        label = Tex(label_tex)
        label.set_height(height * 0.4)
        label.move_to(box)
        return VGroup(box, label)

    return VGroup(box)

class BitString(VGroup):
    def __init__(self, value=0, length=4, **kwargs):
        super().__init__(**kwargs)

        if isinstance(value, str):
            # If value is a string, use it directly
            bits = value
        else:
            # Convert integer to binary string of specified length
            bits = bin(value)[2:].zfill(length)
            bits = bits[-length:]  # Take only the last 'length' bits

        # Create individual bit mobjects
        for bit in bits:
            bit_mob = Text(bit)
            self.add(bit_mob)

        # Arrange bits horizontally
        self.arrange(RIGHT, buff=0.1)

    def get_value(self):
        """Returns the integer value of the bit string"""
        bits = ''.join(bit.text for bit in self)
        return int(bits, 2)

class KetGroup(VGroup):
    def __init__(self, content, height_scale_factor=1.0, **kwargs):
        super().__init__(**kwargs)

        # Create the ket notation
        left_ket = Tex(r"|")
        right_ket = Tex(r"\rangle")

        # Add the content between ket symbols
        if isinstance(content, Mobject):
            content_mob = content
        else:
            content_mob = Tex(str(content))

        # Assemble the ket
        self.add(left_ket, content_mob, right_ket)
        self.arrange(RIGHT, buff=0.05)

        # Scale height if needed
        if height_scale_factor != 1.0:
            self.scale(height_scale_factor)
