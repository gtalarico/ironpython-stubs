class PointOnFace(PointElementReference):
    """ Define a ReferencePoint relative to a Face. """
    def GetFaceReference(self):
        """
        GetFaceReference(self: PointOnFace) -> Reference
        
            Get a copy of the face reference.
        """
        pass

    def SetFaceReference(self, reference):
        """
        SetFaceReference(self: PointOnFace, reference: Reference)
            Change the face reference.
        """
        pass

    UV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The location of the point in the surface's coordinate system.

Get: UV(self: PointOnFace) -> UV

Set: UV(self: PointOnFace) = value
"""


