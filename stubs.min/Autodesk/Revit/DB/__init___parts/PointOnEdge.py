class PointOnEdge(PointElementReference):
    """
    Define a ReferencePoint relative to a referenceable edge or
    curve on another element.
    """
    def GetEdgeReference(self):
        """
        GetEdgeReference(self: PointOnEdge) -> Reference
        
            Get a copy of the edge or curve reference.
        """
        pass

    def SetEdgeReference(self, reference):
        """
        SetEdgeReference(self: PointOnEdge, reference: Reference)
            Change the edge or curve reference.
        """
        pass

    LocationOnCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point location on curve.

Get: LocationOnCurve(self: PointOnEdge) -> PointLocationOnCurve

"""


