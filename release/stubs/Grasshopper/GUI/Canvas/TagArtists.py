# encoding: utf-8
# module Grasshopper.GUI.Canvas.TagArtists calls itself TagArtists
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_TagArtist(object, IGH_TagArtist):
    # no doc
    def Paint(self, canvas, channel):
        """ Paint(self: GH_TagArtist, canvas: GH_Canvas, channel: GH_CanvasChannel) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, id: Guid) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ID(self: GH_TagArtist) -> Guid

"""



class GH_TagArtist_WirePainter(GH_TagArtist, IGH_TagArtist):
    """ GH_TagArtist_WirePainter(source: IGH_Param, target: IGH_Param, colour: Color, width: int) """
    def Paint(self, canvas, channel):
        """ Paint(self: GH_TagArtist_WirePainter, canvas: GH_Canvas, channel: GH_CanvasChannel) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source, target, colour, width):
        """ __new__(cls: type, source: IGH_Param, target: IGH_Param, colour: Color, width: int) """
        pass

    WirePainter_ID = None


class IGH_TagArtist:
    # no doc
    def Paint(self, canvas, channel):
        """ Paint(self: IGH_TagArtist, canvas: GH_Canvas, channel: GH_CanvasChannel) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ID(self: IGH_TagArtist) -> Guid

"""



