class RebarShapeVertex(object, IDisposable):
    """ A bend between segments of a rebar shape definition. """
    def Dispose(self):
        """ Dispose(self: RebarShapeVertex) """
        pass

    def GetConstraints(self):
        """
        GetConstraints(self: RebarShapeVertex) -> IList[RebarShapeConstraint]
        
            Retrieve the list of constraints associated with this vertex.
            Returns: The list of constraints.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeVertex, disposing: bool) """
        pass

    def SetConstraints(self, constraints):
        """ SetConstraints(self: RebarShapeVertex, constraints: IList[RebarShapeConstraint]) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BendAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The range of permissible angles at this bend.

Get: BendAngle(self: RebarShapeVertex) -> RebarShapeBendAngle

Set: BendAngle(self: RebarShapeVertex) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RebarShapeVertex) -> bool

"""

    Turn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sense of the turn. The Turn property must be set to Left or Right on each internal vertex
   before the RebarShapeDefinitionBySegments is used.
   Default is permissible for the first and last vertex, since they do not correspond to bends.

Get: Turn(self: RebarShapeVertex) -> RebarShapeVertexTurn

Set: Turn(self: RebarShapeVertex) = value
"""


