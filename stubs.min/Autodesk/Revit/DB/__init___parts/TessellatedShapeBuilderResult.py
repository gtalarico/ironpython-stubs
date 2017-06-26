class TessellatedShapeBuilderResult(object, IDisposable):
    """
    Describes what TessellatedShapeBuilder has
       construct.
    """
    def Dispose(self):
        """ Dispose(self: TessellatedShapeBuilderResult) """
        pass

    def GetGeometricalObjects(self):
        """
        GetGeometricalObjects(self: TessellatedShapeBuilderResult) -> IList[GeometryObject]
        
            When called the first time, returns geometrical objects which were built.
           
             Later calls will throw exceptions.
        
            Returns: Geometrical object which were built.
        """
        pass

    def GetIssuesForFaceSet(self, setIndex):
        """
        GetIssuesForFaceSet(self: TessellatedShapeBuilderResult, setIndex: int) -> IList[TessellatedBuildIssue]
        
            Returns the array of issues encountered while processing
           a face set with 
             index 'setIndex'.
        
        
            setIndex: Index of the face set.
            Returns: Array of issues encountered while processing a face set
           with index 
             'setIndex'.
        """
        pass

    def GetNumberOfFaceSets(self):
        """
        GetNumberOfFaceSets(self: TessellatedShapeBuilderResult) -> int
        
            Gets number of face sets for which 'this' result was obtained.
            Returns: The number of face sets.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TessellatedShapeBuilderResult, disposing: bool) """
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

    AreObjectsAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shows whether 'issues' still contains the original data or whether
   these data have already been relinquished by 'getGeometricalObjects'.
   The former is true, the later is false.

Get: AreObjectsAvailable(self: TessellatedShapeBuilderResult) -> bool

"""

    HasInvalidData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether there were any inconsistencies in the face sets,
   stored in the tessellated shape builder while building
   geometrical objects.

Get: HasInvalidData(self: TessellatedShapeBuilderResult) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TessellatedShapeBuilderResult) -> bool

"""

    Outcome = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """What kinds of geometrical objects were built.

Get: Outcome(self: TessellatedShapeBuilderResult) -> TessellatedShapeBuilderOutcome

"""


