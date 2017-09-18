# encoding: utf-8
# module Grasshopper.GUI.Equations calls itself Equations
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_EquationFragment(object, IGH_EquationFragment):
    # no doc
    def Layout(self, font):
        """ Layout(self: GH_EquationFragment, font: Font) -> bool """
        pass

    def Position(self, location):
        """ Position(self: GH_EquationFragment, location: PointF) -> bool """
        pass

    def Render(self, graphics, font, colour):
        """ Render(self: GH_EquationFragment, graphics: Graphics, font: Font, colour: Color) """
        pass

    def ToExpression(self):
        """ ToExpression(self: GH_EquationFragment) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: GH_EquationFragment) -> RectangleF

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_EquationFragment) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: GH_EquationFragment) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_EquationFragment) -> str

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pivot(self: GH_EquationFragment) -> PointF

Set: Pivot(self: GH_EquationFragment) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: GH_EquationFragment) -> SizeF

"""


    m_pivot = None
    m_size = None


class GH_SequenceFragment(GH_EquationFragment, IGH_EquationFragment):
    """ GH_SequenceFragment() """
    def Layout(self, font):
        """ Layout(self: GH_SequenceFragment, font: Font) -> bool """
        pass

    def Position(self, location):
        """ Position(self: GH_SequenceFragment, location: PointF) -> bool """
        pass

    def Render(self, graphics, font, colour):
        """ Render(self: GH_SequenceFragment, graphics: Graphics, font: Font, colour: Color) """
        pass

    def ToExpression(self):
        """ ToExpression(self: GH_SequenceFragment) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_SequenceFragment) -> str

"""

    Fragments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fragments(self: GH_SequenceFragment) -> List[IGH_EquationFragment]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_SequenceFragment) -> str

"""


    m_pivot = None
    m_size = None


class GH_TextFragment(GH_EquationFragment, IGH_EquationFragment):
    """ GH_TextFragment() """
    def Layout(self, font):
        """ Layout(self: GH_TextFragment, font: Font) -> bool """
        pass

    def Position(self, location):
        """ Position(self: GH_TextFragment, location: PointF) -> bool """
        pass

    def Render(self, graphics, font, colour):
        """ Render(self: GH_TextFragment, graphics: Graphics, font: Font, colour: Color) """
        pass

    def ToExpression(self):
        """ ToExpression(self: GH_TextFragment) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_TextFragment) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_TextFragment) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: GH_TextFragment) -> str

Set: Text(self: GH_TextFragment) = value
"""


    m_pivot = None
    m_size = None


class IGH_EquationFragment:
    # no doc
    def Layout(self, font):
        """ Layout(self: IGH_EquationFragment, font: Font) -> bool """
        pass

    def Position(self, location):
        """ Position(self: IGH_EquationFragment, location: PointF) -> bool """
        pass

    def Render(self, graphics, font, colour):
        """ Render(self: IGH_EquationFragment, graphics: Graphics, font: Font, colour: Color) """
        pass

    def ToExpression(self):
        """ ToExpression(self: IGH_EquationFragment) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: IGH_EquationFragment) -> RectangleF

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IGH_EquationFragment) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: IGH_EquationFragment) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IGH_EquationFragment) -> str

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pivot(self: IGH_EquationFragment) -> PointF

Set: Pivot(self: IGH_EquationFragment) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: IGH_EquationFragment) -> SizeF

"""



