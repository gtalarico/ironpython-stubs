class RebarShapeDefinitionByArc(RebarShapeDefinition, IDisposable):
    """
    Definition of a shape whose size and position can determined by a single arc.
    
    RebarShapeDefinitionByArc(doc: Document, height: float, pitch: float, baseFinishingTurns: int, topFinishingTurns: int)
    RebarShapeDefinitionByArc(doc: Document, type: RebarShapeDefinitionByArcType)
    """
    def AddConstraintArcLength(self, paramId):
        """
        AddConstraintArcLength(self: RebarShapeDefinitionByArc, paramId: ElementId)
            Specify a parameter to drive the arc length of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        """
        pass

    def AddConstraintChordLength(self, paramId):
        """
        AddConstraintChordLength(self: RebarShapeDefinitionByArc, paramId: ElementId)
            Specify a parameter to drive the chord length (the straight-line distance 
             between the endpoints of the arc).
        
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        """
        pass

    def AddConstraintCircumference(self, paramId, arcRefType):
        """
        AddConstraintCircumference(self: RebarShapeDefinitionByArc, paramId: ElementId, arcRefType: RebarShapeArcReferenceType)
            Specify a parameter to drive the circumference of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            arcRefType: Specify along which circle the circumference is measured--to the interior
           
             of the bar, the centerline, or the exterior.
        """
        pass

    def AddConstraintDiameter(self, paramId, arcRefType):
        """
        AddConstraintDiameter(self: RebarShapeDefinitionByArc, paramId: ElementId, arcRefType: RebarShapeArcReferenceType)
            Specify a parameter to drive the diameter of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            arcRefType: Specify how the diameter should be measured--to the interior of the bend, the 
             centerline of the bar, or the exterior.
        """
        pass

    def AddConstraintRadius(self, paramId, arcRefType):
        """
        AddConstraintRadius(self: RebarShapeDefinitionByArc, paramId: ElementId, arcRefType: RebarShapeArcReferenceType)
            Specify a parameter to drive the radius of the shape.
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        
            arcRefType: Specify how the radius should be measured--to the interior of the bend, the 
             centerline of the bar, or the exterior.
        """
        pass

    def AddConstraintSagittaLength(self, paramId):
        """
        AddConstraintSagittaLength(self: RebarShapeDefinitionByArc, paramId: ElementId)
            Specify a parameter to drive the sagittal
           length (the height of the 
             circular segment, measured
           perpendicular to the chord).
        
        
            paramId: Id of a parameter to drive the constraint.
           To obtain the id of a shared 
             parameter,
           call RebarShape.GetElementIdForExternalDefinition().
        """
        pass

    def Dispose(self):
        """ Dispose(self: RebarShapeDefinition, A_0: bool) """
        pass

    def GetConstraints(self):
        """
        GetConstraints(self: RebarShapeDefinitionByArc) -> IList[RebarShapeConstraint]
        
            Retrieve the list of constraints associated with this definition.
            Returns: The list of constraints.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeDefinition, disposing: bool) """
        pass

    def SetArcTypeSpiral(self, height, pitch, baseFinishingTurns, topFinishingTurns):
        """
        SetArcTypeSpiral(self: RebarShapeDefinitionByArc, height: float, pitch: float, baseFinishingTurns: int, topFinishingTurns: int)
            Set the RebarShapeDefinitionByArc.Type property to Spiral.
        
            height: The height of the spiral (assuming the spiral is vertical).
            pitch: The pitch, or vertical distance traveled in one rotation.
            baseFinishingTurns: The number of finishing turns at the lower end of the spiral.
            topFinishingTurns: The number of finishing turns at the upper end of the spiral.
        """
        pass

    def SetConstraints(self, constraints):
        """ SetConstraints(self: RebarShapeDefinitionByArc, constraints: IList[RebarShapeConstraint]) """
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

    @staticmethod # known case of __new__
    def __new__(self, doc, *__args):
        """
        __new__(cls: type, doc: Document, height: float, pitch: float, baseFinishingTurns: int, topFinishingTurns: int)
        __new__(cls: type, doc: Document, type: RebarShapeDefinitionByArcType)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Among those rebar shapes defined by an arc, specify which kind.

Get: Type(self: RebarShapeDefinitionByArc) -> RebarShapeDefinitionByArcType

Set: Type(self: RebarShapeDefinitionByArc) = value
"""


