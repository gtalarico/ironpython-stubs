class BooleanOperationsUtils(object, IDisposable):
    """ These utilities are applicable for the geometry created by GeometryCreationUtilities and the geometry of Revit model. """
    @staticmethod
    def CutWithHalfSpace(solid, plane):
        """
        CutWithHalfSpace(solid: Solid, plane: Plane) -> Solid
        
            Creates a new Solid which is the intersection of the input Solid with the 
             half-space on the positive side of the given Plane. The positive side of the 
             plane is the side to which Plane.Normal points.
        
        
            solid: The input Solid to be cut.
            plane: The cut plane.  The space on the positive side of the normal of the plane will 
             be intersected with the input Solid.
        
            Returns: The newly created Solid.
        """
        pass

    @staticmethod
    def CutWithHalfSpaceModifyingOriginalSolid(solid, plane):
        """
        CutWithHalfSpaceModifyingOriginalSolid(solid: Solid, plane: Plane)
            Modifies the input Solid preserving only the volume on the positive side of the 
             given Plane. The positive side of the plane is the side to which Plane.Normal 
             points.
        
        
            solid: The input Solid to be cut. This object cannot be obtained directly from a Revit 
             element.
           This means that Autodesk.Revit.DB.GeometryObject.IsElementGeometry 
             cannot be true.
        
            plane: The cut plane.  The space on the positive side of the normal of the plane will 
             be intersected with the input Solid.
        """
        pass

    def Dispose(self):
        """ Dispose(self: BooleanOperationsUtils) """
        pass

    @staticmethod
    def ExecuteBooleanOperation(solid0, solid1, booleanType):
        """
        ExecuteBooleanOperation(solid0: Solid, solid1: Solid, booleanType: BooleanOperationsType) -> Solid
        
            Perform a boolean geometric operation between two solids, and return a new 
             solid to represent the result.
        
        
            solid0: The first solid object. A copy will be taken of the input object, so any solid 
             whether obtained from a Revit element or not would be accepted.
        
            solid1: The second solid object. A copy will be taken of the input object, so any solid 
             whether obtained from a Revit element or not would be accepted.
        
            booleanType: boolean operation type.
            Returns: The result geometry.
        """
        pass

    @staticmethod
    def ExecuteBooleanOperationModifyingOriginalSolid(solid0, solid1, booleanType):
        """
        ExecuteBooleanOperationModifyingOriginalSolid(solid0: Solid, solid1: Solid, booleanType: BooleanOperationsType)
            Perform a boolean geometric operation between two solids, and modify the 
             original solid to represent the result.
        
        
            solid0: The original solid object. This object cannot be obtained directly from a Revit 
             element.
           This means that Autodesk.Revit.DB.GeometryObject.IsElementGeometry 
             cannot be true.
        
            solid1: The second solid object. A copy will be taken of the input object, so any solid 
             whether obtained from a Revit element or not would be accepted.
        
            booleanType: boolean operation type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BooleanOperationsUtils, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: BooleanOperationsUtils) -> bool

"""


