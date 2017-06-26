class ViewShapeBuilder(ShapeBuilder, IDisposable):
    """
    Builds and verifies a view-specific shape representation that would typically be stored in a DirectShape object.
       Currently limited to curve-based representations for plan and elevation views.
    
    ViewShapeBuilder(targetViewType: DirectShapeTargetViewType)
    ViewShapeBuilder()
    """
    def AddCurve(self, GCurve):
        """
        AddCurve(self: ViewShapeBuilder, GCurve: Curve)
            Add a curve to the GRep associated to this ViewShapeBuilder.
        
            GCurve: The curve to be added.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ShapeBuilder, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ShapeBuilder, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: ViewShapeBuilder)
            Clears the accumulated geometry and resets other ViewShapeBuilder parameters to 
             invalid values.
        """
        pass

    @staticmethod
    def ValidateCurve(GCurve, targetViewType=None):
        """
        ValidateCurve(self: ViewShapeBuilder, GCurve: Curve) -> bool
        
            Validates curve to be added to the view-specific shape being constructed. 
             Called by AddCurve() to validate input. Expects a valid view normal to be set 
             prior to the call.
        
        
            GCurve: Curve object to be validated.
            Returns: True is %GCurve% is acceptable as a part of view-specific shape representation 
             being built.
        
        ValidateCurve(GCurve: Curve, targetViewType: DirectShapeTargetViewType) -> bool
        
            Validates curve to be added to the view-specific shape being constructed. 
             Called by AddCurve() to validate input.
           This function may be used to 
             pre-validate the geometry being added to avoid AddCurve() throwing an 
             InvalidArgumentException
        
        
            GCurve: Curve object to be validated.
            targetViewType: View type for which this curve is intended.
            Returns: True is %GCurve% is acceptable as a part of view-specific shape representation.
        """
        pass

    @staticmethod
    def ValidateShape(shape, targetViewType):
        """ ValidateShape(shape: IList[GeometryObject], targetViewType: DirectShapeTargetViewType) -> bool """
        pass

    @staticmethod
    def ValidateViewType(targetViewType):
        """
        ValidateViewType(targetViewType: DirectShapeTargetViewType) -> bool
        
            Validates the incoming view type. As of today, the only allowed view type is 
             Plan.
        
            Returns: True if %targetViewType% is DirectShapeTargetViewType::Plan
        """
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
    def __new__(self, targetViewType=None):
        """
        __new__(cls: type, targetViewType: DirectShapeTargetViewType)
        __new__(cls: type)
        """
        pass

    ViewNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Normal of the view that will display the shape being built. Must be set explicitly before adding any geometry. Must be a unit vector.
   This is used to validate incoming geometry - it must be orthogonal to the viewNormal.

Get: ViewNormal(self: ViewShapeBuilder) -> XYZ

Set: ViewNormal(self: ViewShapeBuilder) = value
"""

    ViewType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """View type where the view-specific shape currently being built will be used

Get: ViewType(self: ViewShapeBuilder) -> DirectShapeTargetViewType

Set: ViewType(self: ViewShapeBuilder) = value
"""


