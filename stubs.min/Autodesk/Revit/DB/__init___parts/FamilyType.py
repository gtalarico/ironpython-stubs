class FamilyType(APIObject, IDisposable):
    """ The family type object provides read access to the values of family parameters for this type. """
    def AsDouble(self, familyParameter):
        """
        AsDouble(self: FamilyType, familyParameter: FamilyParameter) -> Nullable[float]
        
            Provides access to the double precision number of the given family parameter.
            Returns: The double value contained in the parameter. Returns ll
        if the storage type of 
             the input argument is not double type or this parameter has no value.
        """
        pass

    def AsElementId(self, familyParameter):
        """
        AsElementId(self: FamilyType, familyParameter: FamilyParameter) -> ElementId
        
            Provides access to the Autodesk::Revit::DB::ElementId^ stored in the given 
             family parameter.
        
            Returns: The Autodesk::Revit::DB::ElementId^ contained in the parameter.Returns an 
             invalid element id
        if the storage type of the input argument is 
             Autodesk::Revit::DB::ElementId^ type or this parameter has no value.
        """
        pass

    def AsInteger(self, familyParameter):
        """
        AsInteger(self: FamilyType, familyParameter: FamilyParameter) -> Nullable[int]
        
            Provides access to the integer number of the given family parameter.
            Returns: The integer value contained in the parameter. Returns ll
        if the storage type 
             of the input argument is not integer type or this parameter has no value.
        """
        pass

    def AsString(self, familyParameter):
        """
        AsString(self: FamilyType, familyParameter: FamilyParameter) -> str
        
            Provides access to the string contents of the given family parameter.
            Returns: The string contained in the parameter. Returns ll if the storage type of the 
             input
        argument is not string type or this parameter has no value.
        """
        pass

    def AsValueString(self, familyParameter):
        """
        AsValueString(self: FamilyType, familyParameter: FamilyParameter) -> str
        
            Provides access to value as a string with unit in the given family parameter.
            Returns: The string that represents the parameter value with unit.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def HasValue(self, familyParameter):
        """
        HasValue(self: FamilyType, familyParameter: FamilyParameter) -> bool
        
            Indicates if this family parameter has an assigned value or not.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the family type.

Get: Name(self: FamilyType) -> str

"""


