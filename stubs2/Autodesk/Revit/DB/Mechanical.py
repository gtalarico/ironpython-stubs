# encoding: utf-8
# module Autodesk.Revit.DB.Mechanical calls itself Mechanical
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ComponentClassification(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type lists all MEP component classification. This attribute describes the general purpose of the MEP part component, that is used for scheduling, tagging, filter, ODBC, and etc.
       One component classification may include more than one part type.
    
    enum ComponentClassification, values: Coupling (107), Cross (105), Duct (2), Elbow (101), Endcap (106), Flange (109), FlexDuct (12), FlexPipe (11), Hanger (113), Pipe (1), Sensor (112), Sleeve (114), Tap (103), Tee (102), Transition (104), Undefined (0), Union (108), Valve (111), Wye (110)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Coupling = None
    Cross = None
    Duct = None
    Elbow = None
    Endcap = None
    Flange = None
    FlexDuct = None
    FlexPipe = None
    Hanger = None
    Pipe = None
    Sensor = None
    Sleeve = None
    Tap = None
    Tee = None
    Transition = None
    Undefined = None
    Union = None
    value__ = None
    Valve = None
    Wye = None


class ConditionType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible condition types for a space object.
    
    enum ConditionType, values: Cooled (1), Heated (0), HeatedAndCooled (2), NaturallyVentedOnly (5), NoOfConditionTypes (6), Unconditioned (3), Vented (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Cooled = None
    Heated = None
    HeatedAndCooled = None
    NaturallyVentedOnly = None
    NoOfConditionTypes = None
    Unconditioned = None
    value__ = None
    Vented = None


class Duct(MEPCurve, IDisposable):
    """ A duct in the Autodesk Revit MEP product. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Duct
        
            Creates a new duct from two points.
        
            document: The document.
            systemTypeId: The id of the HVAC system type.
            ductTypeId: The id of the duct type.
            levelId: The level ElementId for the duct.
            startPoint: The start point of the duct.
            endPoint: The end point of the duct.
            Returns: The created duct.
        Create(document: Document, ductTypeId: ElementId, levelId: ElementId, startConnector: Connector, endPoint: XYZ) -> Duct
        
            Creates a new duct that connects to the connector.
        
            document: The document.
            ductTypeId: The ElementId of the new duct type.
            levelId: The level id for the new duct.
            startConnector: The first connector where the new duct starts.
            endPoint: The second point of the new duct.
            Returns: The created duct.
        Create(document: Document, ductTypeId: ElementId, levelId: ElementId, startConnector: Connector, endConnector: Connector) -> Duct
        
            Creates a new duct that connects to two connectors.
        
            document: The document.
            ductTypeId: The ElementId of the new duct type.
            levelId: The level ElementId for the new duct.
            startConnector: The first connector where the new duct starts.
            endConnector: The second point of the new duct.
            Returns: The created duct.
        """
        pass

    @staticmethod
    def CreatePlaceholder(document, systemTypeId, ductTypeId, levelId, startPoint, endPoint):
        """
        CreatePlaceholder(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Duct
        
            Creates a new placeholder duct.
        
            document: The document.
            systemTypeId: The id of the HVAC system type.
            ductTypeId: The id of the duct type.
            levelId: The level id for the duct.
            startPoint: The first point of the placeholder line.
            endPoint: The second point of the placeholder line.
            Returns: The created placeholder duct.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsDuctTypeId(document, ductTypeId):
        """
        IsDuctTypeId(document: Document, ductTypeId: ElementId) -> bool
        
            Checks if given type is valid duct type.
        
            document: The document.
            ductTypeId: ElementId of the duct type to check.
            Returns: True if duct type can used for this duct, false otherwise.
        """
        pass

    @staticmethod
    def IsHvacSystemTypeId(document, systemTypeId):
        """
        IsHvacSystemTypeId(document: Document, systemTypeId: ElementId) -> bool
        
            Checks if given type is valid HVAC system type.
        
            document: The document.
            systemTypeId: ElementId of the HVAC system type to check.
            Returns: True if the given systemTypeId is the HVAC system type, false otherwise.
        """
        pass

    @staticmethod
    def IsLevelId(document, levelId):
        """
        IsLevelId(document: Document, levelId: ElementId) -> bool
        
            Checks if given element id is valid level element.
        
            document: The document.
            levelId: ElementId of the level to check.
            Returns: True if given level id is valid, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetSystemType(self, systemTypeId):
        """
        SetSystemType(self: Duct, systemTypeId: ElementId)
            Updates the associated system type for the duct.
        
            systemTypeId: The ElementId of the hvac system type.
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

    DuctType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The duct type of this duct.

Get: DuctType(self: Duct) -> DuctType

Set: DuctType(self: Duct) = value
"""

    IsPlaceholder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the duct is a placeholder or not.

Get: IsPlaceholder(self: Duct) -> bool

"""



class DuctFittingAndAccessoryConnectorData(object, IDisposable):
    """ The input data used by external servers for calculation of the duct fitting and duct accessory coefficient. """
    def Dispose(self):
        """ Dispose(self: DuctFittingAndAccessoryConnectorData) """
        pass

    def GetCoordination(self):
        """
        GetCoordination(self: DuctFittingAndAccessoryConnectorData) -> Transform
        
            Gets the coordination of the connector
            Returns: The coordination of the connector
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctFittingAndAccessoryConnectorData, disposing: bool) """
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

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the angle of the fitting, Units:(rad).

Get: Angle(self: DuctFittingAndAccessoryConnectorData) -> float

"""

    Coordination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the coordination of the connector

Get: Coordination(self: DuctFittingAndAccessoryConnectorData) -> Transform

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector diameter, Units:(ft).

Get: Diameter(self: DuctFittingAndAccessoryConnectorData) -> float

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector flow, Units:(ft³/s)

Get: Flow(self: DuctFittingAndAccessoryConnectorData) -> float

"""

    FlowDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the flow direction of this connector, In or Out.

Get: FlowDirection(self: DuctFittingAndAccessoryConnectorData) -> FlowDirectionType

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector height, Units:(ft).

Get: Height(self: DuctFittingAndAccessoryConnectorData) -> float

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """return the index of this connector

Get: Index(self: DuctFittingAndAccessoryConnectorData) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctFittingAndAccessoryConnectorData) -> bool

"""

    LinkIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the index of the connector which is linked with this connector

Get: LinkIndex(self: DuctFittingAndAccessoryConnectorData) -> int

"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector profile.

Get: Profile(self: DuctFittingAndAccessoryConnectorData) -> ConnectorProfileType

"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector velocity pressure. Units: (kg/(ft·s²)).

Get: VelocityPressure(self: DuctFittingAndAccessoryConnectorData) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector width, Units:(ft).

Get: Width(self: DuctFittingAndAccessoryConnectorData) -> float

"""



class DuctFittingAndAccessoryData(object, IDisposable):
    """ The input data used by external servers for calculation of the duct fitting and duct accessory coefficient. """
    def Dispose(self):
        """ Dispose(self: DuctFittingAndAccessoryData) """
        pass

    def GetAllConnectorData(self):
        """
        GetAllConnectorData(self: DuctFittingAndAccessoryData) -> IList[DuctFittingAndAccessoryConnectorData]
        
            Gets the connector data of the pipe fitting or pipe accessory.
            Returns: All connector data.
        """
        pass

    def GetEntity(self):
        """
        GetEntity(self: DuctFittingAndAccessoryData) -> Entity
        
            Returns an Entity of the Schema of the serverGUID.
           or an invalid entity 
             otherwise.
        
            Returns: The Entity.
        """
        pass

    def GetFamilyInstanceId(self):
        """
        GetFamilyInstanceId(self: DuctFittingAndAccessoryData) -> ElementId
        
            Gets the Id of the fiting or accessory instance
            Returns: The element Id of the fiting or accessory instance.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctFittingAndAccessoryData, disposing: bool) """
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

    AirViscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The air viscosity of the duct fitting or duct accessory, Units: (kg/(ft·s)).

Get: AirViscosity(self: DuctFittingAndAccessoryData) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctFittingAndAccessoryData) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The origin position of the duct fitting or duct accessory.

Get: Origin(self: DuctFittingAndAccessoryData) -> XYZ

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The part type of the duct fitting or duct accessory.

Get: PartType(self: DuctFittingAndAccessoryData) -> PartType

"""

    ServerGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID of the duct fitting or duct accessory.

Get: ServerGUID(self: DuctFittingAndAccessoryData) -> Guid

"""

    SystemClassification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The system classification of the duct fitting or duct accessory.

Get: SystemClassification(self: DuctFittingAndAccessoryData) -> MEPSystemClassification

"""



class DuctFittingAndAccessoryPressureDropData(object, IDisposable):
    """ The input and output data used by external servers for calculation of the duct fitting and duct accessory pressure drop. """
    def Dispose(self):
        """ Dispose(self: DuctFittingAndAccessoryPressureDropData) """
        pass

    def GetDuctFittingAndAccessoryData(self):
        """
        GetDuctFittingAndAccessoryData(self: DuctFittingAndAccessoryPressureDropData) -> DuctFittingAndAccessoryData
        
            Returns the fitting and accessory information.
        """
        pass

    def GetPresureDropItems(self):
        """
        GetPresureDropItems(self: DuctFittingAndAccessoryPressureDropData) -> IList[DuctFittingAndAccessoryPressureDropItem]
        
            Returns the pressure drop items.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctFittingAndAccessoryPressureDropData, disposing: bool) """
        pass

    def SetDefaultEntity(self, defaultEntity):
        """
        SetDefaultEntity(self: DuctFittingAndAccessoryPressureDropData, defaultEntity: Entity)
            Stores the default entity in the data.
        
            defaultEntity: The Entity to be stored.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CalculationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculation type, a bitmask of FittingAndAccessoryCalculationType.

Get: CalculationType(self: DuctFittingAndAccessoryPressureDropData) -> int

"""

    IsCurrentEntityValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the current settings stored in the entity is valid.

Get: IsCurrentEntityValid(self: DuctFittingAndAccessoryPressureDropData) -> bool

Set: IsCurrentEntityValid(self: DuctFittingAndAccessoryPressureDropData) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctFittingAndAccessoryPressureDropData) -> bool

"""



class DuctFittingAndAccessoryPressureDropItem(object, IDisposable):
    """ A flow path of the duct/pipe fitting and accessory. It is defined by the begin connector and end connector. """
    def Dispose(self):
        """ Dispose(self: DuctFittingAndAccessoryPressureDropItem) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctFittingAndAccessoryPressureDropItem, disposing: bool) """
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

    BeginConnectorIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the begin connector of the flow path.

Get: BeginConnectorIndex(self: DuctFittingAndAccessoryPressureDropItem) -> int

"""

    Coefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The coefficient between the begin connector and end connector, Units: (kg/(ft·s²)).

Get: Coefficient(self: DuctFittingAndAccessoryPressureDropItem) -> float

Set: Coefficient(self: DuctFittingAndAccessoryPressureDropItem) = value
"""

    EndConnectorIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the end conector of the flow path.

Get: EndConnectorIndex(self: DuctFittingAndAccessoryPressureDropItem) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctFittingAndAccessoryPressureDropItem) -> bool

"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity pressure, for converting between coefficient and pressure drop on this flow path. Units: (kg/(ft·s²)).

Get: VelocityPressure(self: DuctFittingAndAccessoryPressureDropItem) -> float

"""



class DuctFlowConfigurationType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all duct flow configuration types for a connector.
    
    enum DuctFlowConfigurationType, values: Calculated (0), Preset (1), System (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Calculated = None
    Preset = None
    System = None
    value__ = None


class DuctInsulation(InsulationLiningBase, IDisposable):
    """ Represents insulation applied to the outside of a given duct , fitting or accessory. """
    @staticmethod
    def Create(document, ductOrContentElementId, ductInsulationTypeId, Thickness):
        """
        Create(document: Document, ductOrContentElementId: ElementId, ductInsulationTypeId: ElementId, Thickness: float) -> DuctInsulation
        
            Creates a new instance of duct insulation.
        
            document: The document.
            ductOrContentElementId: The duct , fitting or accessory ElementId to which insulation will be added.
            ductInsulationTypeId: The duct insulation type.
           If the input duct insulation type is 
             InvalidElementId, the default insulation type from the document will be used.
        
            Thickness: The thickness of the insulation.
            Returns: The newly created duct insulation.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class DuctInsulationType(ElementType, IDisposable):
    """ This class represents a duct insulation type in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class DuctLining(InsulationLiningBase, IDisposable):
    """ Represents Lining applied to the inside of a given duct, fitting or accessory. """
    @staticmethod
    def Create(document, ductOrContentElementId, ductLiningTypeId, Thickness):
        """
        Create(document: Document, ductOrContentElementId: ElementId, ductLiningTypeId: ElementId, Thickness: float) -> DuctLining
        
            Creates a new instance of duct lining.
        
            document: The document.
            ductOrContentElementId: The duct, fitting or accessory ElementId to which lining will be added.
            ductLiningTypeId: The duct lining type.
           If the input duct lining type is InvalidElementId, 
             the default lining type from the document will be used.
        
            Thickness: The thickness of the lining.
            Returns: The newly created duct lining.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class DuctLiningType(ElementType, IDisposable):
    """ This class represents a duct lining type in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsValidRoughness(self, roughness):
        """
        IsValidRoughness(self: DuctLiningType, roughness: float) -> bool
        
            Identifies if the input roughness is valid.
        
            roughness: The roughness to check.
            Returns: True if the value is acceptable, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Roughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The roughness of Duct Lining.

Get: Roughness(self: DuctLiningType) -> float

Set: Roughness(self: DuctLiningType) = value
"""



class DuctLossMethodType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all duct loss calculation methods for a connector.
    
    enum DuctLossMethodType, values: Coefficient (6), NotDefined (0), SpecificLoss (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Coefficient = None
    NotDefined = None
    SpecificLoss = None
    value__ = None


class DuctPressureDropData(object, IDisposable):
    """ The input and output data used by external servers for calculation of the duct pressure drop. """
    def Dispose(self):
        """ Dispose(self: DuctPressureDropData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctPressureDropData, disposing: bool) """
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

    CategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category id of duct curves. It will be OST_DuctCurves, OST_FlexDuctCurves, or OST_PlaceHolderDucts.

Get: CategoryId(self: DuctPressureDropData) -> ElementId

"""

    Coefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The coefficient of the duct.

Get: Coefficient(self: DuctPressureDropData) -> float

Set: Coefficient(self: DuctPressureDropData) = value
"""

    Density = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The density of the duct.Units: (kg/ft³).

Get: Density(self: DuctPressureDropData) -> float

"""

    EquivalentDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The equivalent diameter of the duct. Units: (ft).

Get: EquivalentDiameter(self: DuctPressureDropData) -> float

Set: EquivalentDiameter(self: DuctPressureDropData) = value
"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow of the duct. Units: (ft³/s).

Get: Flow(self: DuctPressureDropData) -> float

"""

    Friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The friction of the duct. Units: (kg/(ft²·s²)).

Get: Friction(self: DuctPressureDropData) -> float

Set: Friction(self: DuctPressureDropData) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the duct. If the duct is round, it will be equal to the diameter of the duct. Units: (ft).

Get: Height(self: DuctPressureDropData) -> float

"""

    HydraulicDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hydraulic diameter of the duct. Units: (ft).

Get: HydraulicDiameter(self: DuctPressureDropData) -> float

Set: HydraulicDiameter(self: DuctPressureDropData) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctPressureDropData) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the duct. Units: (ft).

Get: Length(self: DuctPressureDropData) -> float

"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculation level of the system.

Get: Level(self: DuctPressureDropData) -> SystemCalculationLevel

"""

    PressureDrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pressure drop of the duct. Units: (kg/(ft·s²)).

Get: PressureDrop(self: DuctPressureDropData) -> float

Set: PressureDrop(self: DuctPressureDropData) = value
"""

    ReynoldsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The reynolds number of the duct.

Get: ReynoldsNumber(self: DuctPressureDropData) -> float

Set: ReynoldsNumber(self: DuctPressureDropData) = value
"""

    Roughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The roughness of the duct. Units: (ft).

Get: Roughness(self: DuctPressureDropData) -> float

"""

    Shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The profile type of the duct.

Get: Shape(self: DuctPressureDropData) -> ConnectorProfileType

"""

    Velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity of the duct. Units: (ft/s).

Get: Velocity(self: DuctPressureDropData) -> float

Set: Velocity(self: DuctPressureDropData) = value
"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity pressure of the duct. Units: (kg/(ft·s²)).

Get: VelocityPressure(self: DuctPressureDropData) -> float

Set: VelocityPressure(self: DuctPressureDropData) = value
"""

    Viscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The viscosity of the duct. Units: (kg/(ft·s)).

Get: Viscosity(self: DuctPressureDropData) -> float

"""

    WidthOrDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The diameter of the duct with round profile, or the width of the duct with other profiles. Units: (ft).

Get: WidthOrDiameter(self: DuctPressureDropData) -> float

"""



class DuctSettings(Element, IDisposable):
    """ The duct setting class. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetDuctSettings(document):
        """
        GetDuctSettings(document: Document) -> DuctSettings
        
            Get the duct settings of the project.
        
            document: The document.
            Returns: The duct settings of the project.
        """
        pass

    def GetPressLossCalculationServerInfo(self):
        """
        GetPressLossCalculationServerInfo(self: DuctSettings) -> MEPCalculationServerInfo
        
            Get the MEPServerInfo of the current pipe pressure loss calculation server.
            Returns: The MEPServerInfo of the current pipe pressure loss calculation server
        """
        pass

    def GetSpecificFittingAngles(self):
        """
        GetSpecificFittingAngles(self: DuctSettings) -> IList[float]
        
            Gets the list of specific fitting angles.
            Returns: Angles (in degrees).
        """
        pass

    def GetSpecificFittingAngleStatus(self, angle):
        """
        GetSpecificFittingAngleStatus(self: DuctSettings, angle: float) -> bool
        
            Gets the status of given specific angle.
        
            angle: The specific fitting angle (in degree) that must be one of 90, 60, 45, 30, 22.5 
             or 11.25 degrees.
        """
        pass

    def IsValidSpecificFittingAngle(self, angle):
        """
        IsValidSpecificFittingAngle(self: DuctSettings, angle: float) -> bool
        
            Checks that the given value is a valid specific fitting angle. The specific 
             fitting angles are angles of 90, 60, 45, 30, 22.5 or 11.25 degrees.
        
        
            angle: The angle value (in degree).
            Returns: True if the given value is a valid specific fitting angle.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetPressLossCalculationServerInfo(self, serverInfo):
        """
        SetPressLossCalculationServerInfo(self: DuctSettings, serverInfo: MEPCalculationServerInfo)
            Set the MEPServerInfo of the current pipe pressure loss calculation server.
        """
        pass

    def SetSpecificFittingAngleStatus(self, angle, useInLayout):
        """
        SetSpecificFittingAngleStatus(self: DuctSettings, angle: float, useInLayout: bool)
            Sets the status of given specific angle.
        
            angle: The specific angle (in degree) that must be one of 60, 45, 30, 22.5 or 11.25 
             degrees.
        
            useInLayout: Status, true - using the given angle during the duct layout.
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

    AirDensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The air density.

Get: AirDensity(self: DuctSettings) -> float

Set: AirDensity(self: DuctSettings) = value
"""

    AirViscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The air dynamic viscosity.

Get: AirViscosity(self: DuctSettings) -> float

Set: AirViscosity(self: DuctSettings) = value
"""

    Centerline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Centerline (=) string.

Get: Centerline(self: DuctSettings) -> str

Set: Centerline(self: DuctSettings) = value
"""

    ConnectorSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The duct connector separator string.

Get: ConnectorSeparator(self: DuctSettings) -> str

Set: ConnectorSeparator(self: DuctSettings) = value
"""

    FittingAngleUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine how to use fitting angle during duct layout or modifying layout.

Get: FittingAngleUsage(self: DuctSettings) -> FittingAngleUsage

Set: FittingAngleUsage(self: DuctSettings) = value
"""

    FittingAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of fitting annotation size.

Get: FittingAnnotationSize(self: DuctSettings) -> float

Set: FittingAnnotationSize(self: DuctSettings) = value
"""

    FlatOnBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Flat On Bottom (FOB) string.

Get: FlatOnBottom(self: DuctSettings) -> str

Set: FlatOnBottom(self: DuctSettings) = value
"""

    FlatOnTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Flat On Top (FOT) string.

Get: FlatOnTop(self: DuctSettings) -> str

Set: FlatOnTop(self: DuctSettings) = value
"""

    OvalDuctSizeSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The oval duct size separator string.

Get: OvalDuctSizeSeparator(self: DuctSettings) -> str

Set: OvalDuctSizeSeparator(self: DuctSettings) = value
"""

    OvalDuctSizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The oval duct size suffix string.

Get: OvalDuctSizeSuffix(self: DuctSettings) -> str

Set: OvalDuctSizeSuffix(self: DuctSettings) = value
"""

    RectangularDuctSizeSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rectangular duct size separator string.

Get: RectangularDuctSizeSeparator(self: DuctSettings) -> str

Set: RectangularDuctSizeSeparator(self: DuctSettings) = value
"""

    RectangularDuctSizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rectangular duct size suffix string.

Get: RectangularDuctSizeSuffix(self: DuctSettings) -> str

Set: RectangularDuctSizeSuffix(self: DuctSettings) = value
"""

    RiseDropAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rise drop annotation size.

Get: RiseDropAnnotationSize(self: DuctSettings) -> float

Set: RiseDropAnnotationSize(self: DuctSettings) = value
"""

    RoundDuctSizePrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The round duct size prefix string.

Get: RoundDuctSizePrefix(self: DuctSettings) -> str

Set: RoundDuctSizePrefix(self: DuctSettings) = value
"""

    RoundDuctSizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The round duct size suffix string.

Get: RoundDuctSizeSuffix(self: DuctSettings) -> str

Set: RoundDuctSizeSuffix(self: DuctSettings) = value
"""

    SetDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Set Down (SD) string.

Get: SetDown(self: DuctSettings) -> str

Set: SetDown(self: DuctSettings) = value
"""

    SetUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Set Up (SU) string.

Get: SetUp(self: DuctSettings) -> str

Set: SetUp(self: DuctSettings) = value
"""

    UseAnnotationScaleForSingleLineFittings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether use annotation scale for single line fittings or not.

Get: UseAnnotationScaleForSingleLineFittings(self: DuctSettings) -> bool

Set: UseAnnotationScaleForSingleLineFittings(self: DuctSettings) = value
"""



class DuctShape(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerated type listing possible shapes for ducts.
    
    enum DuctShape, values: Oval (2), Rectangular (1), Round (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Oval = None
    Rectangular = None
    Round = None
    value__ = None


class DuctSizeIterator(object, IEnumerator[MEPSize], IDisposable, IEnumerator):
    """ An iterator to a set of MEP duct sizes from DuctSizes. """
    def Dispose(self):
        """ Dispose(self: DuctSizeIterator) """
        pass

    def GetCurrent(self):
        """
        GetCurrent(self: DuctSizeIterator) -> MEPSize
        
            Returns the current MEPSize.
            Returns: The current MEPSize.
        """
        pass

    def HasCurrent(self):
        """
        HasCurrent(self: DuctSizeIterator) -> bool
        
            Identifies if the iterator has a current item.
            Returns: True if there is a current item.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: DuctSizeIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: DuctSizeIterator) -> bool
        
            Increments the iterator to the next item.
            Returns: True if there is a next available item in this iterator.
           False if the 
             iterator has completed all available items.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctSizeIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: DuctSizeIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MEPSize](enumerator: IEnumerator[MEPSize], value: MEPSize) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item at the current position of the iterator.

Get: Current(self: DuctSizeIterator) -> MEPSize

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctSizeIterator) -> bool

"""



class DuctSizes(object, IEnumerable[MEPSize], IEnumerable, IDisposable):
    """ Class RbsDuctSizes being used to store the duct sizes """
    def Contains(self, nominalDiameter):
        """
        Contains(self: DuctSizes, nominalDiameter: float) -> bool
        
            Checks whether a duct size with the nominal diameter exists.
        
            nominalDiameter: Nominal diameter.
            Returns: True if a duct size with the nominal diameter exists.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DuctSizes) """
        pass

    def GetDuctSizeIterator(self):
        """
        GetDuctSizeIterator(self: DuctSizes) -> DuctSizeIterator
        
            Returns a DuctSizeIterator that iterates through the collection.
            Returns: A DuctSizeIterator object that can be used to iterate through key-value pairs 
             in the collection.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DuctSizes) -> IEnumerator[MEPSize]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctSizes, disposing: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MEPSize](enumerable: IEnumerable[MEPSize], value: MEPSize) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count of the items contained in the collection.

Get: Count(self: DuctSizes) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctSizes) -> bool

"""



class DuctSizeSettingIterator(object, IEnumerator[KeyValuePair[DuctShape, DuctSizes]], IDisposable, IEnumerator):
    """ An iterator to a set of items from DuctSizeSettings. Each item is a KeyValuePair(DuctShape::Enum, DuctSizes). """
    def Dispose(self):
        """ Dispose(self: DuctSizeSettingIterator) """
        pass

    def HasCurrent(self):
        """
        HasCurrent(self: DuctSizeSettingIterator) -> bool
        
            Identifies whether the iterator has a current item.
           There is no current 
             item if the iterator has not started yet or has been done.
        
            Returns: True if there is a current item.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: DuctSizeSettingIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: DuctSizeSettingIterator) -> bool
        
            Increments the enumerator to the next item.
            Returns: True if there is a next available item in this enumerator.
           False if the 
             enumerator has completed all available items.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DuctSizeSettingIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: DuctSizeSettingIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[DuctShape, DuctSizes]](enumerator: IEnumerator[KeyValuePair[DuctShape, DuctSizes]], value: KeyValuePair[DuctShape, DuctSizes]) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item at the current position of the iterator.

Get: Current(self: DuctSizeSettingIterator) -> KeyValuePair[DuctShape, DuctSizes]

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DuctSizeSettingIterator) -> bool

"""



class DuctSizeSettings(Element, IDisposable, IEnumerable[KeyValuePair[DuctShape, DuctSizes]], IEnumerable):
    """ Duct sizes settings """
    def AddSize(self, shape, sizeInfo):
        """
        AddSize(self: DuctSizeSettings, shape: DuctShape, sizeInfo: MEPSize)
            Inserts a new MEPSize in to the duct size settings. The duct shape determines 
             the location of the new size in the size table.
        
        
            shape: The shape of duct.
            sizeInfo: The new MEPSize to be added.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetDuctSizeSettingIterator(self):
        """
        GetDuctSizeSettingIterator(self: DuctSizeSettings) -> DuctSizeSettingIterator
        
            Returns a DuctSizeSettingIterator object that iterates through the collection.
            Returns: A DuctSizeSettingIterator object that can be used to iterate through key-value 
             pairs in the collection.
        """
        pass

    @staticmethod
    def GetDuctSizeSettings(aDoc):
        """
        GetDuctSizeSettings(aDoc: Document) -> DuctSizeSettings
        
            Get the duct size settings of the project.
        
            aDoc: The document.
            Returns: The duct size settings of the project.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DuctSizeSettings) -> IEnumerator[KeyValuePair[DuctShape, DuctSizes]]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetSizeCount(self, shape):
        """
        GetSizeCount(self: DuctSizeSettings, shape: DuctShape) -> int
        
            Get the size count of the duct size table. The duct shape determines the 
             location of the size in the size table.
        
        
            shape: The shape of duct.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveSize(self, shape, nominalDiameter):
        """
        RemoveSize(self: DuctSizeSettings, shape: DuctShape, nominalDiameter: float)
            Erase the existing MEPSize with this nominal diameter. The duct shape 
             determines the location of the size in the size table.
        
        
            shape: The shape of duct.
            nominalDiameter: Nominal diameter.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[DuctShape, DuctSizes]](enumerable: IEnumerable[KeyValuePair[DuctShape, DuctSizes]], value: KeyValuePair[DuctShape, DuctSizes]) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class DuctSystemType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible duct system types for a connector object.
    
    enum DuctSystemType, values: ExhaustAir (3), Fitting (28), Global (29), OtherAir (4), ReturnAir (2), SupplyAir (1), UndefinedSystemType (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ExhaustAir = None
    Fitting = None
    Global = None
    OtherAir = None
    ReturnAir = None
    SupplyAir = None
    UndefinedSystemType = None
    value__ = None


class DuctType(MEPCurveType, IDisposable):
    """ A duct type element. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class FlexDuct(MEPCurve, IDisposable):
    """ A flex duct in the Autodesk Revit MEP product. """
    @staticmethod
    def Create(document, systemTypeId, ductTypeId, levelId, *__args):
        """
        Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, points: IList[XYZ]) -> FlexDuct
        Create(document: Document, systemTypeId: ElementId, ductTypeId: ElementId, levelId: ElementId, startTangent: XYZ, endTangent: XYZ, points: IList[XYZ]) -> FlexDuct
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsFlexDuctTypeId(document, ductTypeId):
        """
        IsFlexDuctTypeId(document: Document, ductTypeId: ElementId) -> bool
        
            Checks if given type is valid flexible duct type.
        
            document: The document.
            ductTypeId: ElementId of the flexible duct type to check.
            Returns: True if flexible duct type can used for this duct, false otherwise.
        """
        pass

    @staticmethod
    def IsHVACSystemTypeId(document, systemTypeId):
        """
        IsHVACSystemTypeId(document: Document, systemTypeId: ElementId) -> bool
        
            Checks if given type is valid HVAC system type.
        
            document: The document.
            systemTypeId: ElementId of the HVAC system type to check.
            Returns: True if the given systemTypeId is the HVAC system type, false otherwise.
        """
        pass

    @staticmethod
    def IsLevelId(document, levelId):
        """
        IsLevelId(document: Document, levelId: ElementId) -> bool
        
            Checks if given element id is valid level element.
        
            document: The document.
            levelId: ElementId of the level to check.
            Returns: True if the given level id is valid, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    EndTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the tangent vector at the end of the curve. The invalid or zero vector is ignored when setting the tangent.

Get: EndTangent(self: FlexDuct) -> XYZ

Set: EndTangent(self: FlexDuct) = value
"""

    FlexDuctType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flex duct type of this flex duct.

Get: FlexDuctType(self: FlexDuct) -> FlexDuctType

Set: FlexDuctType(self: FlexDuct) = value
"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The points of the flex duct.

Get: Points(self: FlexDuct) -> IList[XYZ]

Set: Points(self: FlexDuct) = value
"""

    StartTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the tangent vector at the start of the curve. The invalid or zero vector is ignored when setting the tangent.

Get: StartTangent(self: FlexDuct) -> XYZ

Set: StartTangent(self: FlexDuct) = value
"""



class FlexDuctType(MEPCurveType, IDisposable):
    """ A flex duct type in the Autodesk Revit MEP product. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class IDuctFittingAndAccessoryPressureDropServer(IExternalServer):
    """ Interface class for external servers implementing duct fitting and duct accessory coefficient calculation. """
    def Calculate(self, data):
        """
        Calculate(self: IDuctFittingAndAccessoryPressureDropServer, data: DuctFittingAndAccessoryPressureDropData) -> bool
        
            Calculate the duct fitting and duct accessory coefficient.
        
            data: The input and output data of the calculation.
            Returns: True if calculation succeeds.
           False if calculation fails.
        """
        pass

    def GetDataSchema(self):
        """
        GetDataSchema(self: IDuctFittingAndAccessoryPressureDropServer) -> Schema
        
            Obtains the schema of the ESEntity.
            Returns: Null if the server has no data.
        """
        pass

    def IsApplicable(self, data):
        """
        IsApplicable(self: IDuctFittingAndAccessoryPressureDropServer, data: DuctFittingAndAccessoryPressureDropData) -> bool
        
            Check if the server is applicable for the duct fitting or duct accessory.
        
            data: The input data of the calculation.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDuctPressureDropServer(IExternalServer):
    """ Interface for external servers implementing duct pressure drop calculation. """
    def Calculate(self, data):
        """
        Calculate(self: IDuctPressureDropServer, data: DuctPressureDropData)
            Calculate the duct pressure drop.
        
            data: The input and output data of the calculation.
        """
        pass

    def GetHtmlDescription(self):
        """
        GetHtmlDescription(self: IDuctPressureDropServer) -> str
        
            The method that Revit will invoke to get an HTML formatted description of the 
             server.
        
            Returns: The HTML format description of the server.
        """
        pass

    def GetInformationLink(self):
        """
        GetInformationLink(self: IDuctPressureDropServer) -> str
        
            The method that Revit will invoke to obtain a URL address which provides more 
             information about the server.
        
            Returns: The URL providing server information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class MechanicalEquipment(MEPModel, IDisposable):
    """ Provides access to the Mechanical Equipment in Autodesk Revit MEP. """
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


class MechanicalFitting(MEPModel, IDisposable):
    """ A mechanical fitting in the Autodesk Revit MEP product. """
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

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The part type of the mechanical fitting.

Get: PartType(self: MechanicalFitting) -> PartType

"""



class MechanicalSystem(MEPSystem, IDisposable):
    """ A mechanical system element. """
    @staticmethod
    def Create(ADocument, typeId, name=None):
        """
        Create(ADocument: Document, typeId: ElementId) -> MechanicalSystem
        
            Creates a new instance of a mechanical system and adds it to the document.
        
            ADocument: The document where the element will be created and added.
            typeId: The identifier of this mechanical system element's type.
            Returns: The newly created mechanical system element.
        Create(ADocument: Document, typeId: ElementId, name: str) -> MechanicalSystem
        
            Creates a new instance of a mechanical system and adds it to the document.
        
            ADocument: The document where the element will be created and added.
            typeId: The identifier of this mechanical system element's type.
            name: The name of the mechanical system to be created.
            Returns: The newly created mechanical system element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def getElementsInNetwork(self, *args): #cannot find CLR method
        """ getElementsInNetwork(self: MEPSystem) -> ElementSet """
        pass

    def GetFlow(self):
        """
        GetFlow(self: MechanicalSystem) -> float
        
            Gets the flow of this mechanical system.
        """
        pass

    def getFlow(self, *args): #cannot find CLR method
        """ getFlow(self: MEPSystem, param: BuiltInParameter) -> float """
        pass

    def GetStaticPressure(self):
        """
        GetStaticPressure(self: MechanicalSystem) -> float
        
            Gets the static pressure of this mechanical system.
        """
        pass

    def getStaticPressure(self, *args): #cannot find CLR method
        """ getStaticPressure(self: MEPSystem, param: BuiltInParameter) -> float """
        pass

    def IsPressureDropServerMissing(self):
        """
        IsPressureDropServerMissing(self: MechanicalSystem) -> bool
        
            Indicates if any pressure drop server which was used in the mechanical system 
             is not available.
        
            Returns: True if there is any pressure drop server not available, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    BaseEquipmentConnector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector within the base equipment which is used to connect with the system.

Get: BaseEquipmentConnector(self: MechanicalSystem) -> Connector

Set: BaseEquipmentConnector(self: MechanicalSystem) = value
"""

    DuctNetwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ducts and fittings contained within the system.

Get: DuctNetwork(self: MechanicalSystem) -> ElementSet

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow of this piping system

Get: Flow(self: MechanicalSystem) -> float

"""

    IsWellConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the system is well connected or not.

Get: IsWellConnected(self: MechanicalSystem) -> bool

"""

    StaticPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The static pressure of this piping system

Get: StaticPressure(self: MechanicalSystem) -> float

"""

    SystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of this duct system.

Get: SystemType(self: MechanicalSystem) -> DuctSystemType

"""



class MechanicalSystemType(MEPSystemType, IDisposable):
    """ Base class for duct system types """
    @staticmethod
    def Create(ADoc, systemClassification, name):
        """
        Create(ADoc: Document, systemClassification: MEPSystemClassification, name: str) -> MechanicalSystemType
        
            Creates a new instance of a mechanical system type and adds it to the document.
        
            ADoc: The document where the element will be created and added.
            systemClassification: The classification for the mechanical system type to be created
            name: The name of the mechanical system type to be created.
            Returns: The newly created mechanical system type element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def ValidateRiseDropSymbolType(self, risedropType):
        """
        ValidateRiseDropSymbolType(self: MechanicalSystemType, risedropType: RiseDropSymbol) -> bool
        
            Confirms if the parameter is a valid HVAC rise/drop symbol type.
        
            risedropType: The type.
            Returns: True if the input is a valid HVAC rise/drop symbol type, false otherwise.
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

    RiseDropSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """indicates the rise/drop symbol given the system type

Get: RiseDropSettings(self: MechanicalSystemType) -> RiseDropSymbol

Set: RiseDropSettings(self: MechanicalSystemType) = value
"""



class MechanicalUtils(object):
    """ General utility methods in the Autodesk Revit MEP product. """
    @staticmethod
    def BreakCurve(document, ductId, ptBreak):
        """
        BreakCurve(document: Document, ductId: ElementId, ptBreak: XYZ) -> ElementId
        
            Breaks the duct curve into two parts at the given position.
        
            document: The document.
            ductId: The element id of the duct curve to break.
            ptBreak: The break point on the duct curve.
            Returns: The new duct curve element id if successful otherwise if a failure occurred an 
             invalidElementId is returned.
        """
        pass

    @staticmethod
    def ConnectAirTerminalOnDuct(document, airTerminalId, ductCurveId):
        """
        ConnectAirTerminalOnDuct(document: Document, airTerminalId: ElementId, ductCurveId: ElementId) -> bool
        
            Connects an air terminal to a duct directly (without the need for a tee or 
             takeoff).
        
        
            document: The document.
            airTerminalId: The air terminal id.
            ductCurveId: The duct curve id.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConnectDuctPlaceholdersAtCross(document, *__args):
        """
        ConnectDuctPlaceholdersAtCross(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool
        
            Connects a pair of placeholders that can intersect in a Cross connection.
        
            document: The document.
            placeholder1Id: The element id of the first duct placeholder.
            placeholder2Id: The element id of the second duct placeholder.
            Returns: True if connection succeeds, false otherwise.
        ConnectDuctPlaceholdersAtCross(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId, placeholder3Id: ElementId) -> bool
        
            Connects a trio of placeholders that can intersect in a Cross connection.
        
            document: The document.
            placeholder1Id: The element id of the first duct placeholder.
            placeholder2Id: The element id of the second duct placeholder.
            placeholder3Id: The element id of third duct placeholder.
            Returns: True if connection succeeds, false otherwise.
        ConnectDuctPlaceholdersAtCross(document: Document, connector1: Connector, connector2: Connector, connector3: Connector, connector4: Connector) -> bool
        
            Connects a group of placeholders that can intersect in a Cross connection.
        
            document: The document.
            connector1: The end connector of the first placeholder.
            connector2: The end connector of the second placeholder.
            connector3: The end connector of the third placeholder.
            connector4: The end connector of the fourth placeholder.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConnectDuctPlaceholdersAtElbow(document, *__args):
        """
        ConnectDuctPlaceholdersAtElbow(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool
        
            Connects a pair of placeholders that can intersect in an Elbow connection.
        
            document: The document.
            placeholder1Id: The element id of the first duct placeholder.
            placeholder2Id: The element id of the second duct placeholder.
            Returns: True if connection succeeds, false otherwise.
        ConnectDuctPlaceholdersAtElbow(document: Document, connector1: Connector, connector2: Connector) -> bool
        
            Connects a pair of placeholders that can intersect in an Elbow connection.
        
            document: The document.
            connector1: The end connector of the first placeholder.
            connector2: The end connector of the second placeholder.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConnectDuctPlaceholdersAtTee(document, *__args):
        """
        ConnectDuctPlaceholdersAtTee(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool
        
            Connects a pair of placeholders that can intersect in a Tee connection.
        
            document: The document.
            placeholder1Id: The element Id of the first duct placeholder.
            placeholder2Id: The element Id of the second duct placeholder.
            Returns: True if connection succeeds, false otherwise.
        ConnectDuctPlaceholdersAtTee(document: Document, connector1: Connector, connector2: Connector, connector3: Connector) -> bool
        
            Connects a trio of placeholders that can intersect in a Tee connection.
        
            document: The document.
            connector1: The end connector of the first placeholder.
            connector2: The end connector of second placeholder.
            connector3: The end connector of the third placeholder.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConvertDuctPlaceholders(document, placeholderIds):
        """ ConvertDuctPlaceholders(document: Document, placeholderIds: ICollection[ElementId]) -> ICollection[ElementId] """
        pass

    __all__ = [
        'BreakCurve',
        'ConnectAirTerminalOnDuct',
        'ConnectDuctPlaceholdersAtCross',
        'ConnectDuctPlaceholdersAtElbow',
        'ConnectDuctPlaceholdersAtTee',
        'ConvertDuctPlaceholders',
    ]


class MEPBuildingConstruction(ElementType, IDisposable):
    """ Construction definition for Project Information. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetBuildingConstruction(self, constructionType):
        """
        GetBuildingConstruction(self: MEPBuildingConstruction, constructionType: ConstructionType) -> Construction
        
            Gets the current Building Construction from the project information.
        
            constructionType: The Construction Type of Building Construction.
            Returns: The Building Construction of the Project Information.
        """
        pass

    def GetBuildingConstructionOverride(self, constructionType):
        """
        GetBuildingConstructionOverride(self: MEPBuildingConstruction, constructionType: ConstructionType) -> bool
        
            Gets the Building Construction override for a ConstructionType.
        
            constructionType: The ConstructionType override value to get.
            Returns: True if analytical construction properties specified in Constructions.xml are 
             used for the given ConstructionType, false otherwise.
        """
        pass

    def GetConstructions(self, constructionType):
        """
        GetConstructions(self: MEPBuildingConstruction, constructionType: ConstructionType) -> ICollection[Construction]
        
            Gets all the Building Constructions corresponding to the specific Construction 
             type.
        
        
            constructionType: The Construction Type of Building Construction.
            Returns: A collection containing Building constructions matching the construction type.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetBuildingConstruction(self, constructionType, buildingConstruction):
        """
        SetBuildingConstruction(self: MEPBuildingConstruction, constructionType: ConstructionType, buildingConstruction: Construction)
            Sets the Building Construction of the Project Information.
        
            constructionType: The Construction Type of Building Construction.
            buildingConstruction: The Building Construction to be set.
        """
        pass

    def SetBuildingConstructionOverride(self, constructionType, override):
        """
        SetBuildingConstructionOverride(self: MEPBuildingConstruction, constructionType: ConstructionType, override: bool)
            Sets the Building Construction override for a ConstructionType.
        
            constructionType: The ConstructionType to override.
            override: True to use analytical construction properties specified in Constructions.xml 
             in the given ConstructionType, false otherwise.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class MEPBuildingConstructionSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains MEPBuildingConstructions.
    
    MEPBuildingConstructionSet()
    """
    def Clear(self):
        """
        Clear(self: MEPBuildingConstructionSet)
            Removes every MEPBuildingConstruction from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: MEPBuildingConstructionSet, item: MEPBuildingConstruction) -> bool
        
            Tests for the existence of a MEPBuildingConstruction within the set.
        
            item: The MEPBuildingConstruction to be searched for.
            Returns: The Contains method returns True if the MEPBuildingConstruction is within the 
             set, otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: MEPBuildingConstructionSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: MEPBuildingConstructionSet, item: MEPBuildingConstruction) -> int
        
            Removes a specified MEPBuildingConstruction from the set.
        
            item: The MEPBuildingConstruction to be erased.
            Returns: The number of MEPBuildingConstructions that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: MEPBuildingConstructionSet) -> MEPBuildingConstructionSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MEPBuildingConstructionSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: MEPBuildingConstructionSet, item: MEPBuildingConstruction) -> bool
        
            Insert the specified MEPBuildingConstruction into the set.
        
            item: The MEPBuildingConstruction to be inserted into the set.
            Returns: Returns whether the MEPBuildingConstruction was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MEPBuildingConstructionSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: MEPBuildingConstructionSet) -> MEPBuildingConstructionSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: MEPBuildingConstructionSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of MEPBuildingConstructions that are in the set.

Get: Size(self: MEPBuildingConstructionSet) -> int

"""



class MEPBuildingConstructionSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a MEPBuildingConstruction set.
    
    MEPBuildingConstructionSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: MEPBuildingConstructionSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: MEPBuildingConstructionSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MEPBuildingConstructionSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: MEPBuildingConstructionSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: MEPBuildingConstructionSetIterator) -> object

"""



class MEPSection(object, IDisposable):
    """ A section in the Autodesk Revit MEP product. """
    def Dispose(self):
        """ Dispose(self: MEPSection) """
        pass

    def GetCoefficient(self, elemId):
        """
        GetCoefficient(self: MEPSection, elemId: ElementId) -> float
        
            Gets the loss coefficient for the specified element id in this section.
        
            elemId: The element id which can be duct segment, duct fitting , pipe segment and pipe 
             fitting.
        """
        pass

    def GetElementIds(self):
        """
        GetElementIds(self: MEPSection) -> IList[ElementId]
        
            Gets all element ids that are contained in the section.
        """
        pass

    def GetPressureDrop(self, elemId):
        """
        GetPressureDrop(self: MEPSection, elemId: ElementId) -> float
        
            Gets the pressure drop for the specified element id in this section.
        
            elemId: The element id which can be duct segment, duct fitting , pipe segment and pipe 
             fitting.
        """
        pass

    def GetSegmentLength(self, segmentId):
        """
        GetSegmentLength(self: MEPSection, segmentId: ElementId) -> float
        
            Get the length for the specified segment id in this section.
        
            segmentId: The element id which can be duct segment and pipe segment.
        """
        pass

    def IsMain(self, fittingId):
        """
        IsMain(self: MEPSection, fittingId: ElementId) -> bool
        
            Check whether the type of fitting in this section is main.
        
            fittingId: The element id which can be duct fitting and pipe fitting.
            Returns: True if the type of fitting in this section is main
           False if the type of 
             fitting in this section is branch
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: MEPSection, disposing: bool) """
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

    FixtureUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixture unit of the section.

Get: FixtureUnit(self: MEPSection) -> float

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow of the section.

Get: Flow(self: MEPSection) -> float

"""

    Friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The friction of the section.

Get: Friction(self: MEPSection) -> float

"""

    FrictionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The friction factor of the section.

Get: FrictionFactor(self: MEPSection) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: MEPSection) -> bool

"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Section number.

Get: Number(self: MEPSection) -> int

"""

    ReynoldsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Reynolds number of the section.

Get: ReynoldsNumber(self: MEPSection) -> float

"""

    Roughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The roughness of the section.

Get: Roughness(self: MEPSection) -> float

"""

    TotalCoefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The loss coefficient of the section.

Get: TotalCoefficient(self: MEPSection) -> float

"""

    TotalCurveLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total length of all segments in the section.

Get: TotalCurveLength(self: MEPSection) -> float

"""

    TotalPressureLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total pressure loss of the section.

Get: TotalPressureLoss(self: MEPSection) -> float

"""

    Velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity of the section.

Get: Velocity(self: MEPSection) -> float

"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity pressure of the section.

Get: VelocityPressure(self: MEPSection) -> float

"""



class MEPSpaceConstruction(object):
    """ Construction definition for Space. """
    def DeleteConstruction(self, pCurrentConstruction):
        """
        DeleteConstruction(self: MEPSpaceConstruction, pCurrentConstruction: MEPBuildingConstruction)
            Remove an existing construction from Space constructions.
        
            pCurrentConstruction: The Construction will be deleted.
        """
        pass

    def DuplicateConstruction(self, pCurrentConstruction, pName):
        """
        DuplicateConstruction(self: MEPSpaceConstruction, pCurrentConstruction: MEPBuildingConstruction, pName: str) -> MEPBuildingConstruction
        
            Create a new construction for Space constructions.
        
            pCurrentConstruction: The existing construction to be duplicated.
            pName: The name of the new construction.
        """
        pass

    def NewConstruction(self, pName):
        """
        NewConstruction(self: MEPSpaceConstruction, pName: str) -> MEPBuildingConstruction
        
            Create a new construction for Space constructions.
        
            pName: The name of the new Construction.
        """
        pass

    CurrentConstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get all the Building Constructions according to the specific Construction type.

Get: CurrentConstruction(self: MEPSpaceConstruction) -> MEPBuildingConstruction

Set: CurrentConstruction(self: MEPSpaceConstruction) = value
"""

    SpaceConstructions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return all the Space constructions of current space.

Get: SpaceConstructions(self: MEPSpaceConstruction) -> MEPBuildingConstructionSet

"""



class OccupancyUnit(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing the occupancy unit of measure for a space object.
    
    enum OccupancyUnit, values: AreaPerPerson (1), NumberOfPeople (0), UseDefaultValues (-1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AreaPerPerson = None
    NumberOfPeople = None
    UseDefaultValues = None
    value__ = None


class ReturnAirflowType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible return airflow types for a space object.
    
    enum ReturnAirflowType, values: ActualSupplyAirflow (3), CalculatedSupplyAirflow (2), Specified (0), SpecifiedSupplyAirflow (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActualSupplyAirflow = None
    CalculatedSupplyAirflow = None
    Specified = None
    SpecifiedSupplyAirflow = None
    value__ = None


class RiseDropSymbol(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumeration corresponds to the rise/drop symbol used
       in mechanical systems
    
    enum RiseDropSymbol, values: Backslash (6), BackslashFilled (7), BendFullCircle (14), BendThreeQuarterCircle (13), Cross (2), CrossFilled (3), CrossNoOutline (17), NoSymbol (0), Outline (1), OutlineFilled (10), ReverseWye (9), Slash (4), SlashFilled (5), TeeFullCircle (16), TeeHalfCircle (15), Wye (8), YinYang (11), YinYangFilled (12)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Backslash = None
    BackslashFilled = None
    BendFullCircle = None
    BendThreeQuarterCircle = None
    Cross = None
    CrossFilled = None
    CrossNoOutline = None
    NoSymbol = None
    Outline = None
    OutlineFilled = None
    ReverseWye = None
    Slash = None
    SlashFilled = None
    TeeFullCircle = None
    TeeHalfCircle = None
    value__ = None
    Wye = None
    YinYang = None
    YinYangFilled = None


class Space(SpatialElement, IDisposable):
    """ Provides access to the space topology in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsPointInSpace(self, point):
        """
        IsPointInSpace(self: Space, point: XYZ) -> bool
        
            Determines if a point lies within the volume of the Space.
        
            point: Point to be checked.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    ActualExhaustAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Actual Exhaust Airflow of the Space.

Get: ActualExhaustAirflow(self: Space) -> float

"""

    ActualHVACLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Actual HVAC Load of the Space.

Get: ActualHVACLoad(self: Space) -> float

"""

    ActualLightingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Actual Lighting Load of the Space.

Get: ActualLightingLoad(self: Space) -> float

"""

    ActualOtherLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Actual Other Load of the Space.

Get: ActualOtherLoad(self: Space) -> float

"""

    ActualPowerLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Actual Power Load of the Space.

Get: ActualPowerLoad(self: Space) -> float

"""

    ActualReturnAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Actual Return Airflow of the Space.

Get: ActualReturnAirflow(self: Space) -> float

"""

    ActualSupplyAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Actual Supply Airflow of the Space.

Get: ActualSupplyAirflow(self: Space) -> float

"""

    AreaperPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Area per Person of the Space.

Get: AreaperPerson(self: Space) -> float

Set: AreaperPerson(self: Space) = value
"""

    AverageEstimatedIllumination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Average Estimated Illumination of the Space.

Get: AverageEstimatedIllumination(self: Space) -> float

"""

    BaseHeatLoadOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The heat load-on.

Get: BaseHeatLoadOn(self: Space) -> BaseLoadOn

Set: BaseHeatLoadOn(self: Space) = value
"""

    BaseOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Base Offset of the Space.

Get: BaseOffset(self: Space) -> float

Set: BaseOffset(self: Space) = value
"""

    CalculatedCoolingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Calculated Cooling Load of the Space.

Get: CalculatedCoolingLoad(self: Space) -> float

"""

    CalculatedHeatingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Calculated Heating Load of the Space.

Get: CalculatedHeatingLoad(self: Space) -> float

"""

    CalculatedSupplyAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Calculated Supply Airflow of the Space.

Get: CalculatedSupplyAirflow(self: Space) -> float

"""

    CeilingReflectance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Ceiling Reflectance of the Space.

Get: CeilingReflectance(self: Space) -> float

Set: CeilingReflectance(self: Space) = value
"""

    ClosedShell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the closedShell of the space.

Get: ClosedShell(self: Space) -> GeometryElement

"""

    ConditionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Condition type of the Space.

Get: ConditionType(self: Space) -> ConditionType

Set: ConditionType(self: Space) = value
"""

    DesignCoolingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Design Cooling Load of the Space.

Get: DesignCoolingLoad(self: Space) -> float

Set: DesignCoolingLoad(self: Space) = value
"""

    DesignExhaustAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Specified Exhaust Airflow of the Space.

Get: DesignExhaustAirflow(self: Space) -> float

Set: DesignExhaustAirflow(self: Space) = value
"""

    DesignHeatingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Design Heating Load of the Space.

Get: DesignHeatingLoad(self: Space) -> float

Set: DesignHeatingLoad(self: Space) = value
"""

    DesignHVACLoadperArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Design HVAC Load per Area of the Space.

Get: DesignHVACLoadperArea(self: Space) -> float

Set: DesignHVACLoadperArea(self: Space) = value
"""

    DesignLightingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Design Lighting Load of the Space.

Get: DesignLightingLoad(self: Space) -> float

Set: DesignLightingLoad(self: Space) = value
"""

    DesignOtherLoadperArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Design Other Load per Area of the Space.

Get: DesignOtherLoadperArea(self: Space) -> float

Set: DesignOtherLoadperArea(self: Space) = value
"""

    DesignPowerLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Design Power Load of the Space.

Get: DesignPowerLoad(self: Space) -> float

Set: DesignPowerLoad(self: Space) = value
"""

    DesignReturnAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Specified Return Airflow of the Space.

Get: DesignReturnAirflow(self: Space) -> float

Set: DesignReturnAirflow(self: Space) = value
"""

    DesignSupplyAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Specified Supply Airflow of the Space.

Get: DesignSupplyAirflow(self: Space) -> float

Set: DesignSupplyAirflow(self: Space) = value
"""

    FloorReflectance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Floor Reflectance of the Space.

Get: FloorReflectance(self: Space) -> float

Set: FloorReflectance(self: Space) = value
"""

    LatentHeatGainperPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Latent Heat Gain per Person of the Space.

Get: LatentHeatGainperPerson(self: Space) -> float

Set: LatentHeatGainperPerson(self: Space) = value
"""

    LightingCalculationWorkplane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Lighting Calculation Workplane of the Space.

Get: LightingCalculationWorkplane(self: Space) -> float

Set: LightingCalculationWorkplane(self: Space) = value
"""

    LightingLoadUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Lighting Load Unit of the Space.

Get: LightingLoadUnit(self: Space) -> BaseLoadOn

Set: LightingLoadUnit(self: Space) = value
"""

    LimitOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Limit Offset of the Space.

Get: LimitOffset(self: Space) -> float

Set: LimitOffset(self: Space) = value
"""

    NumberofPeople = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Number of People of the Space.

Get: NumberofPeople(self: Space) -> float

Set: NumberofPeople(self: Space) = value
"""

    OccupancyUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Occupancy Unit of the Space.

Get: OccupancyUnit(self: Space) -> OccupancyUnit

Set: OccupancyUnit(self: Space) = value
"""

    Occupiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether this zone is Occupiable or not.

Get: Occupiable(self: Space) -> bool

"""

    Plenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether this zone is Plenum or not.

Get: Plenum(self: Space) -> bool

"""

    PowerLoadUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Power Load Unit of the Space.

Get: PowerLoadUnit(self: Space) -> BaseLoadOn

Set: PowerLoadUnit(self: Space) = value
"""

    ReturnAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Return type of Supply Airflow of the Space.

Get: ReturnAirflow(self: Space) -> ReturnAirflowType

Set: ReturnAirflow(self: Space) = value
"""

    Room = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the Room of the space.

Get: Room(self: Space) -> Room

"""

    SensibleHeatGainperPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Sensible Heat Gain per Person of the Space.

Get: SensibleHeatGainperPerson(self: Space) -> float

Set: SensibleHeatGainperPerson(self: Space) = value
"""

    SpaceCavityRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Space Cavity Ratio of the Space.

Get: SpaceCavityRatio(self: Space) -> float

"""

    SpaceConstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Space Construction of the Space.

Get: SpaceConstruction(self: Space) -> MEPSpaceConstruction

"""

    SpaceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Space type of the Space.

Get: SpaceType(self: Space) -> SpaceType

Set: SpaceType(self: Space) = value
"""

    UnboundedHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Unbounded Height of the Space.

Get: UnboundedHeight(self: Space) -> float

"""

    UpperLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Upper Limit of the Space.

Get: UpperLimit(self: Space) -> Level

Set: UpperLimit(self: Space) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Volume of the Space.

Get: Volume(self: Space) -> float

"""

    WallReflectance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Wall Reflectance of the Space.

Get: WallReflectance(self: Space) -> float

Set: WallReflectance(self: Space) = value
"""

    Zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports this space belong to which Zone.

Get: Zone(self: Space) -> Zone

"""



class SpaceFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match spaces.
    
    SpaceFilter()
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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


class SpaceSet(APIObject, IDisposable, IEnumerable):
    """
    A set that can contain any type of object.
    
    SpaceSet()
    """
    def Clear(self):
        """
        Clear(self: SpaceSet)
            Removes every item from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """ Contains(self: SpaceSet, item: Space) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: SpaceSet, A_0: bool) """
        pass

    def Erase(self, item):
        """ Erase(self: SpaceSet, item: Space) -> int """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: SpaceSet) -> SpaceSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SpaceSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """ Insert(self: SpaceSet, item: Space) -> bool """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SpaceSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: SpaceSet) -> SpaceSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: SpaceSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the set.

Get: Size(self: SpaceSet) -> int

"""



class SpaceSetIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a set.
    
    SpaceSetIterator()
    """
    def Dispose(self):
        """ Dispose(self: SpaceSetIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: SpaceSetIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the set.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SpaceSetIterator) """
        pass

    def Reset(self):
        """
        Reset(self: SpaceSetIterator)
            Bring the iterator back to the start of the set.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: SpaceSetIterator) -> object

"""



class SpaceTag(SpatialElementTag, IDisposable):
    """ Provides access to the space tag in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The space that the tag is associated with.

Get: Space(self: SpaceTag) -> Space

"""

    SpaceTagType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tag type.

Get: SpaceTagType(self: SpaceTag) -> SpaceTagType

Set: SpaceTagType(self: SpaceTag) = value
"""



class SpaceTagFilter(ElementSlowFilter, IDisposable):
    """
    A filter used to match space tags.
    
    SpaceTagFilter()
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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


class SpaceTagType(FamilySymbol, IDisposable):
    """ An object that represents a Space Tag style. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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


class SpaceType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible space types for a space object.
    
    enum SpaceType, values: kActiveStorage (0), kActiveStorageHospitalOrHealthcare (1), kAirOrTrainOrBusBaggageArea (2), kAirportConcourse (3), kAtriumEachAdditionalFloor (4), kAtriumFirstThreeFloors (5), kAudienceOrSeatingAreaAuditorium (16), kAudienceOrSeatingAreaConventionCenter (10), kAudienceOrSeatingAreaCourtHouse (15), kAudienceOrSeatingAreaExerciseCenter (7), kAudienceOrSeatingAreaGymnasium (8), kAudienceOrSeatingAreaMotionPictureTheatre (11), kAudienceOrSeatingAreaPenitentiary (6), kAudienceOrSeatingAreaPerformingArtsTheatre (12), kAudienceOrSeatingAreaPoliceOrFireStations (14), kAudienceOrSeatingAreaReligious (13), kAudienceOrSeatingAreaSportsArena (9), kBankCustomerArea (17), kBankingActivityAreaOffice (18), kBarberAndBeautyParlor (19), kCardFileAndCataloguingLibrary (20), kClassroomOrLectureOrTraining (22), kClassroomOrLectureOrTrainingPenitentiary (21), kComfinementCellsCourtHouse (24), kComfinementCellsPenitentiary (23), kConferenceMeetingOrMultipurpose (25), kCorridorOrTransition (26), kCorridorOrTransitionManufacturingFacility (27), kCorridorsWithPatientWaitingExamHospitalOrHealthcare (28), kCourtroomCourtHouse (30), kCourtSportsAreaSportsArena (29), kDepartmentStoreSalesAreaRetail (31), kDetailedManufacturingFacility (32), kDiningArea (33), kDiningAreaCivilServices (40), kDiningAreaFamilyDining (35), kDiningAreaHotel (34), kDiningAreaLoungeOrLeisureDining (36), kDiningAreaMotel (37), kDiningAreaPenitentiary (39), kDiningAreaTransportation (38), kDormitoryBedroom (41), kDormitoryStudyHall (42), kDressingOrLockerOrFittingRoomAuditorium (46), kDressingOrLockerOrFittingRoomCourtHouse (44), kDressingOrLockerOrFittingRoomExerciseCenter (47), kDressingOrLockerOrFittingRoomGymnasium (43), kDressingOrLockerOrFittingRoomPerformingArtsTheatre (45), kElectricalOrMechanical (48), kElevatorLobbies (49), kEmergencyHospitalOrHealthcare (50), kEquipmentRoomManufacturingFacility (51), kExamOrTreatmentHospitalOrHealthcare (52), kExerciseAreaExerciseCenter (53), kExerciseAreaGymnasium (54), kExhibitSpaceConventionCenter (55), kFellowshipHallReligiousBuildings (56), kFineMaterialWarehouse (57), kFineMerchandiseSalesAreaRetail (58), kFireStationEngineRoomPoliceOrFireStation (59), kFoodPreparation (60), kGarageServiceOrRepairAutomotiveFacility (61), kGeneralExhibitionMuseum (64), kGeneralHighBayManufacturingFacility (62), kGeneralLowBayManufacturingFacility (63), kHospitalNurseryHospitalOrHealthcare (65), kHospitalOrMedicalSuppliesHospitalOrHealthcare (66), kHospitalOrRadiologyHospitalOrHealthcare (67), kHotelOrConferenceCenterConferenceOrMeeting (68), kInactiveStorage (69), kJudgesChambersCourtHouse (70), kLaboratoryOffice (71), kLaundryIroningAndSorting (72), kLaundryWashingHospitalOrHealthcare (73), kLibraryAudioVisualLibraryAudioVisual (74), kLivingQuartersDormitory (75), kLivingQuartersHotel (77), kLivingQuartersMotel (76), kLobby (78), kLobbyAuditorium (81), kLobbyHotel (84), kLobbyMotionPictureTheatre (80), kLobbyPerformingArtsTheatre (82), kLobbyPostOffice (83), kLobbyReligiousBuildings (79), kLoungeOrRecreation (85), kMallConcourseSalesAreaRetail (86), kMassMerchandisingSalesAreaRetail (87), kMediumOrBulkyMaterialWarehouse (88), kMerchandisingSalesAreaRetail (89), kMuseumAndGalleryStorage (90), kNoOfSpaceTypes (125), kNurseStationHospitalOrHealthcare (91), kOfficeCommonActivityAreasInactiveStorage (94), kOfficeEnclosed (92), kOfficeOpenPlan (93), kOperatingRoomHospitalOrHealthcare (95), kOtherTelevisedPlayingAreaSportsArena (96), kParkingAreaAttendantOnlyParkingGarage (97), kParkingAreaPedestrianParkingGarage (98), kPatientRoomHospitalOrHealthcare (99), kPersonalServicesSalesAreaRetail (100), kPharmacyHospitalOrHealthcare (101), kPhysicalTherapyHospitalOrHealthcare (102), kPlayingAreaGymnasium (103), kPlenum (104), kPoliceStationLaboratoryPoliceOrFireStations (105), kPublicAndStaffLoungeHospitalOrHealthcare (106), kReadingAreaLibrary (107), kReceptionOrWaitingHotel (110), kReceptionOrWaitingMotel (109), kReceptionOrWaitingTransportation (108), kRecoveryHospitalOrHealthcare (111), kRestorationMuseum (112), kRestrooms (113), kRingSportsAreaSportsArena (114), kSleepingQuartersPoliceOrFireStation (115), kSortingAreaPostOffice (116), kSpecialtyStoreSalesAreaRetail (117), kStacksLibrary (118), kStairsInactive (119), kStairway (120), kSupermarketSalesAreaRetail (121), kTerminalTicketCounterTransportation (122), kWorkshopWorkshop (123), kWorshipPulpitChoirReligious (124), NoSpaceType (-1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    kActiveStorage = None
    kActiveStorageHospitalOrHealthcare = None
    kAirOrTrainOrBusBaggageArea = None
    kAirportConcourse = None
    kAtriumEachAdditionalFloor = None
    kAtriumFirstThreeFloors = None
    kAudienceOrSeatingAreaAuditorium = None
    kAudienceOrSeatingAreaConventionCenter = None
    kAudienceOrSeatingAreaCourtHouse = None
    kAudienceOrSeatingAreaExerciseCenter = None
    kAudienceOrSeatingAreaGymnasium = None
    kAudienceOrSeatingAreaMotionPictureTheatre = None
    kAudienceOrSeatingAreaPenitentiary = None
    kAudienceOrSeatingAreaPerformingArtsTheatre = None
    kAudienceOrSeatingAreaPoliceOrFireStations = None
    kAudienceOrSeatingAreaReligious = None
    kAudienceOrSeatingAreaSportsArena = None
    kBankCustomerArea = None
    kBankingActivityAreaOffice = None
    kBarberAndBeautyParlor = None
    kCardFileAndCataloguingLibrary = None
    kClassroomOrLectureOrTraining = None
    kClassroomOrLectureOrTrainingPenitentiary = None
    kComfinementCellsCourtHouse = None
    kComfinementCellsPenitentiary = None
    kConferenceMeetingOrMultipurpose = None
    kCorridorOrTransition = None
    kCorridorOrTransitionManufacturingFacility = None
    kCorridorsWithPatientWaitingExamHospitalOrHealthcare = None
    kCourtroomCourtHouse = None
    kCourtSportsAreaSportsArena = None
    kDepartmentStoreSalesAreaRetail = None
    kDetailedManufacturingFacility = None
    kDiningArea = None
    kDiningAreaCivilServices = None
    kDiningAreaFamilyDining = None
    kDiningAreaHotel = None
    kDiningAreaLoungeOrLeisureDining = None
    kDiningAreaMotel = None
    kDiningAreaPenitentiary = None
    kDiningAreaTransportation = None
    kDormitoryBedroom = None
    kDormitoryStudyHall = None
    kDressingOrLockerOrFittingRoomAuditorium = None
    kDressingOrLockerOrFittingRoomCourtHouse = None
    kDressingOrLockerOrFittingRoomExerciseCenter = None
    kDressingOrLockerOrFittingRoomGymnasium = None
    kDressingOrLockerOrFittingRoomPerformingArtsTheatre = None
    kElectricalOrMechanical = None
    kElevatorLobbies = None
    kEmergencyHospitalOrHealthcare = None
    kEquipmentRoomManufacturingFacility = None
    kExamOrTreatmentHospitalOrHealthcare = None
    kExerciseAreaExerciseCenter = None
    kExerciseAreaGymnasium = None
    kExhibitSpaceConventionCenter = None
    kFellowshipHallReligiousBuildings = None
    kFineMaterialWarehouse = None
    kFineMerchandiseSalesAreaRetail = None
    kFireStationEngineRoomPoliceOrFireStation = None
    kFoodPreparation = None
    kGarageServiceOrRepairAutomotiveFacility = None
    kGeneralExhibitionMuseum = None
    kGeneralHighBayManufacturingFacility = None
    kGeneralLowBayManufacturingFacility = None
    kHospitalNurseryHospitalOrHealthcare = None
    kHospitalOrMedicalSuppliesHospitalOrHealthcare = None
    kHospitalOrRadiologyHospitalOrHealthcare = None
    kHotelOrConferenceCenterConferenceOrMeeting = None
    kInactiveStorage = None
    kJudgesChambersCourtHouse = None
    kLaboratoryOffice = None
    kLaundryIroningAndSorting = None
    kLaundryWashingHospitalOrHealthcare = None
    kLibraryAudioVisualLibraryAudioVisual = None
    kLivingQuartersDormitory = None
    kLivingQuartersHotel = None
    kLivingQuartersMotel = None
    kLobby = None
    kLobbyAuditorium = None
    kLobbyHotel = None
    kLobbyMotionPictureTheatre = None
    kLobbyPerformingArtsTheatre = None
    kLobbyPostOffice = None
    kLobbyReligiousBuildings = None
    kLoungeOrRecreation = None
    kMallConcourseSalesAreaRetail = None
    kMassMerchandisingSalesAreaRetail = None
    kMediumOrBulkyMaterialWarehouse = None
    kMerchandisingSalesAreaRetail = None
    kMuseumAndGalleryStorage = None
    kNoOfSpaceTypes = None
    kNurseStationHospitalOrHealthcare = None
    kOfficeCommonActivityAreasInactiveStorage = None
    kOfficeEnclosed = None
    kOfficeOpenPlan = None
    kOperatingRoomHospitalOrHealthcare = None
    kOtherTelevisedPlayingAreaSportsArena = None
    kParkingAreaAttendantOnlyParkingGarage = None
    kParkingAreaPedestrianParkingGarage = None
    kPatientRoomHospitalOrHealthcare = None
    kPersonalServicesSalesAreaRetail = None
    kPharmacyHospitalOrHealthcare = None
    kPhysicalTherapyHospitalOrHealthcare = None
    kPlayingAreaGymnasium = None
    kPlenum = None
    kPoliceStationLaboratoryPoliceOrFireStations = None
    kPublicAndStaffLoungeHospitalOrHealthcare = None
    kReadingAreaLibrary = None
    kReceptionOrWaitingHotel = None
    kReceptionOrWaitingMotel = None
    kReceptionOrWaitingTransportation = None
    kRecoveryHospitalOrHealthcare = None
    kRestorationMuseum = None
    kRestrooms = None
    kRingSportsAreaSportsArena = None
    kSleepingQuartersPoliceOrFireStation = None
    kSortingAreaPostOffice = None
    kSpecialtyStoreSalesAreaRetail = None
    kStacksLibrary = None
    kStairsInactive = None
    kStairway = None
    kSupermarketSalesAreaRetail = None
    kTerminalTicketCounterTransportation = None
    kWorkshopWorkshop = None
    kWorshipPulpitChoirReligious = None
    NoSpaceType = None
    value__ = None


class SystemCalculationLevel(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerated type listing flags that can toggle on or off certain calculations related to MEP systems.
    
    enum SystemCalculationLevel, values: All (-1), Flow (1), None (0), Performance (4), Volume (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = None
    Flow = None
    None = None
    Performance = None
    value__ = None
    Volume = None


class Zone(Element, IDisposable):
    """ Provides access to the Zone Element in Autodesk Revit. """
    def AddSpaces(self, spaces):
        """
        AddSpaces(self: Zone, spaces: SpaceSet) -> bool
        
            Add a set of existing spaces to Zone element.
        
            spaces: The spaces which want to add to zone element.
            Returns: If successful the current zone element will add a set of input spaces, 
             otherwise ll.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveSpaces(self, spaces):
        """
        RemoveSpaces(self: Zone, spaces: SpaceSet) -> bool
        
            Remove a set of existing spaces to the current Zone element.
        
            spaces: The spaces which want to delete from the current zone element.
            Returns: If successful the current zone element will remove a set of input spaces, 
             otherwise ll.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Area of the Zone.

Get: Area(self: Zone) -> float

"""

    Boundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the boundary of the Zone.

Get: Boundary(self: Zone) -> CurveArray

"""

    CalculatedCoolingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Calculated Cooling Load of the Zone.

Get: CalculatedCoolingLoad(self: Zone) -> float

"""

    CalculatedHeatingLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Calculated Heating Load of the Zone.

Get: CalculatedHeatingLoad(self: Zone) -> float

"""

    CalculatedSupplyAirflow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Calculated Supply Airflow of the Zone.

Get: CalculatedSupplyAirflow(self: Zone) -> float

"""

    CoolingAirTemperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Cooling Air Temperature of the Zone.

Get: CoolingAirTemperature(self: Zone) -> float

Set: CoolingAirTemperature(self: Zone) = value
"""

    CoolingSetPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Cooling Set Point of the Zone.

Get: CoolingSetPoint(self: Zone) -> float

Set: CoolingSetPoint(self: Zone) = value
"""

    DehumidificationSetPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the DeHumidification Set Point of the Zone.

Get: DehumidificationSetPoint(self: Zone) -> float

Set: DehumidificationSetPoint(self: Zone) = value
"""

    GrossArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Gross Area of the Zone.

Get: GrossArea(self: Zone) -> float

"""

    GrossVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Gross Volume of the Zone.

Get: GrossVolume(self: Zone) -> float

"""

    HeatingAirTemperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Heating Air Temperature of the Zone.

Get: HeatingAirTemperature(self: Zone) -> float

Set: HeatingAirTemperature(self: Zone) = value
"""

    HeatingSetPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Heating Set Point of the Zone.

Get: HeatingSetPoint(self: Zone) -> float

Set: HeatingSetPoint(self: Zone) = value
"""

    HumidificationSetPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Humidification Set Point of the Zone.

Get: HumidificationSetPoint(self: Zone) -> float

Set: HumidificationSetPoint(self: Zone) = value
"""

    IsDefaultZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports whether this zone is default or not.

Get: IsDefaultZone(self: Zone) -> bool

Set: IsDefaultZone(self: Zone) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or Set the Name of the Zone.

Set: Name(self: Zone) = value
"""

    OutDoorAirPerArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the OutDoor Air Per Area of the Zone.

Get: OutDoorAirPerArea(self: Zone) -> float

Set: OutDoorAirPerArea(self: Zone) = value
"""

    OutDoorAirPerPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the OutDoor Air Per Person of the Zone.

Get: OutDoorAirPerPerson(self: Zone) -> float

Set: OutDoorAirPerPerson(self: Zone) = value
"""

    OutdoorAirRatePerAirChangesPerHour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Outdoor Air Rate Per Air Changes Per Hour of the Zone.

Get: OutdoorAirRatePerAirChangesPerHour(self: Zone) -> float

Set: OutdoorAirRatePerAirChangesPerHour(self: Zone) = value
"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Perimeter of the Zone.

Get: Perimeter(self: Zone) -> float

"""

    Phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Phase of the Zone.

Get: Phase(self: Zone) -> Phase

"""

    ServiceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set the Service Type of the Zone.

Get: ServiceType(self: Zone) -> ServiceType

Set: ServiceType(self: Zone) = value
"""

    Spaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Spaces of the Zone.

Get: Spaces(self: Zone) -> SpaceSet

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Volume of the Zone.

Get: Volume(self: Zone) -> float

"""



