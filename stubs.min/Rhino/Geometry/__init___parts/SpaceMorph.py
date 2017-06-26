class SpaceMorph(object):
    # no doc
    @staticmethod
    def IsMorphable(geometry):
        """ IsMorphable(geometry: GeometryBase) -> bool """
        pass

    def MorphPoint(self, point):
        """ MorphPoint(self: SpaceMorph, point: Point3d) -> Point3d """
        pass

    PreserveStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveStructure(self: SpaceMorph) -> bool

Set: PreserveStructure(self: SpaceMorph) = value
"""

    QuickPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuickPreview(self: SpaceMorph) -> bool

Set: QuickPreview(self: SpaceMorph) = value
"""

    Tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tolerance(self: SpaceMorph) -> float

Set: Tolerance(self: SpaceMorph) = value
"""


