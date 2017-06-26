class FamilyParameter(APIObject, IDisposable):
    """ The family parameter object. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
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

    AssociatedParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameters from elements in the family which are associated to this parameter.

Get: AssociatedParameters(self: FamilyParameter) -> ParameterSet

"""

    CanAssignFormula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this parameter can be assigned a formula.

Get: CanAssignFormula(self: FamilyParameter) -> bool

"""

    Definition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The definition.

Get: Definition(self: FamilyParameter) -> Definition

"""

    DisplayUnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The display unit type.

Get: DisplayUnitType(self: FamilyParameter) -> DisplayUnitType

"""

    Formula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The formula.

Get: Formula(self: FamilyParameter) -> str

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The globally unique identifier

Get: GUID(self: FamilyParameter) -> Guid

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the family parameter.

Get: Id(self: FamilyParameter) -> ElementId

"""

    IsDeterminedByFormula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the parameter is determined by formula.

Get: IsDeterminedByFormula(self: FamilyParameter) -> bool

"""

    IsInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the parameter is instance or type.

Get: IsInstance(self: FamilyParameter) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the object is read-only or modifiable.

Get: IsReadOnly(self: FamilyParameter) -> bool

"""

    IsReporting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the parameter is a reporting parameter.

Get: IsReporting(self: FamilyParameter) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the parameter is a shared parameter.

Get: IsShared(self: FamilyParameter) -> bool

"""

    StorageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The storage type describes the type that is used internally within the parameter to store its value.

Get: StorageType(self: FamilyParameter) -> StorageType

"""

    UserModifiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the interactive user can modify the value of this parameter.

Get: UserModifiable(self: FamilyParameter) -> bool

"""


