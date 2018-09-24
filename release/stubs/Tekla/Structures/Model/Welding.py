# encoding: utf-8
# module Tekla.Structures.Model.Welding calls itself Welding
# from Tekla.Structures.Model, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class WeldGeometry(object):
    # no doc
    Polygons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Polygons(self: WeldGeometry) -> ArrayList

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: WeldGeometry) -> WeldSeamPositionEnum

"""



class WeldSeamPositionEnum(Enum):
    """ enum WeldSeamPositionEnum, values: SEAM_ABOVE (1), SEAM_BELOW (2) """
    SEAM_ABOVE = None
    SEAM_BELOW = None
    value__ = None


