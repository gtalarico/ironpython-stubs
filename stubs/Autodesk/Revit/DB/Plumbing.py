# encoding: utf-8
# module Autodesk.Revit.DB.Plumbing calls itself Plumbing
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FlexPipe(MEPCurve, IDisposable):
    """ A flex pipe in the Autodesk Revit MEP product. """
    @staticmethod
    def Create(document, systemTypeId, pipeTypeId, levelId, *__args):
        """
        Create(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, points: IList[XYZ]) -> FlexPipe
        Create(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, startTangent: XYZ, endTangent: XYZ, points: IList[XYZ]) -> FlexPipe
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsFlexPipeTypeId(document, pipeTypeId):
        """
        IsFlexPipeTypeId(document: Document, pipeTypeId: ElementId) -> bool
        
            Checks if given type is valid flexible pipe type.
        
            document: The document.
            pipeTypeId: ElementId of the flexible pipe type to check.
            Returns: True if flexible pipe type can used for this pipe, false otherwise.
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

    @staticmethod
    def IsPipingSystemTypeId(document, systemTypeId):
        """
        IsPipingSystemTypeId(document: Document, systemTypeId: ElementId) -> bool
        
            Checks if given type is valid piping system type.
        
            document: The document.
            systemTypeId: ElementId of the piping system type to check.
            Returns: True if the given systemTypeId is the piping system type, false otherwise.
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

Get: EndTangent(self: FlexPipe) -> XYZ

Set: EndTangent(self: FlexPipe) = value
"""

    FlexPipeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flex pipe type of this flex pipe.

Get: FlexPipeType(self: FlexPipe) -> FlexPipeType

Set: FlexPipeType(self: FlexPipe) = value
"""

    FlowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow state of the pipe.

Get: FlowState(self: FlexPipe) -> PipeFlowState

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The points of the flex pipe.

Get: Points(self: FlexPipe) -> IList[XYZ]

Set: Points(self: FlexPipe) = value
"""

    StartTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the tangent vector at the start of the curve. The invalid or zero vector is ignored when setting the tangent.

Get: StartTangent(self: FlexPipe) -> XYZ

Set: StartTangent(self: FlexPipe) = value
"""



class FlexPipeType(MEPCurveType, IDisposable):
    """ A flex pipe type in the Autodesk Revit MEP product. """
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


class FlowConversionMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerated type listing possible flow conversion modes for piping calculations.
    
    enum FlowConversionMode, values: Invalid (-1), Tanks (1), Valves (0)
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

    Invalid = None
    Tanks = None
    value__ = None
    Valves = None


class FluidTemperature(object, IDisposable):
    """
    Represents the dynamic viscosity and density properties as defined at a certain temperature.
    
    FluidTemperature(temperature: float, viscosity: float, density: float)
    """
    def Dispose(self):
        """ Dispose(self: FluidTemperature) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FluidTemperature, disposing: bool) """
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
    def __new__(self, temperature, viscosity, density):
        """ __new__(cls: type, temperature: float, viscosity: float, density: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Density = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The density value

Get: Density(self: FluidTemperature) -> float

Set: Density(self: FluidTemperature) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FluidTemperature) -> bool

"""

    Temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The temperature value

Get: Temperature(self: FluidTemperature) -> float

Set: Temperature(self: FluidTemperature) = value
"""

    Viscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The dynamic viscosity value

Get: Viscosity(self: FluidTemperature) -> float

Set: Viscosity(self: FluidTemperature) = value
"""



class FluidTemperatureSetIterator(object, IEnumerator[FluidTemperature], IDisposable, IEnumerator):
    """ An iterator to a set of FluidTemperature from FluidType. """
    def Dispose(self):
        """ Dispose(self: FluidTemperatureSetIterator) """
        pass

    def GetCurrent(self):
        """
        GetCurrent(self: FluidTemperatureSetIterator) -> FluidTemperature
        
            Returns the current FluidTemperature.
            Returns: The current FluidTemperature.
        """
        pass

    def IsDone(self):
        """
        IsDone(self: FluidTemperatureSetIterator) -> bool
        
            Identifies if the iteration has completed.
            Returns: True if the iteration has no more items.  False if there are more items to be 
             iterated.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: FluidTemperatureSetIterator) -> bool
        
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
        """ ReleaseUnmanagedResources(self: FluidTemperatureSetIterator, disposing: bool) """
        pass

    def Reset(self):
        """
        Reset(self: FluidTemperatureSetIterator)
            Resets the iterator to the initial state.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FluidTemperature](enumerator: IEnumerator[FluidTemperature], value: FluidTemperature) -> bool """
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

Get: Current(self: FluidTemperatureSetIterator) -> FluidTemperature

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FluidTemperatureSetIterator) -> bool

"""



class FluidType(ElementType, IDisposable, IEnumerable[FluidTemperature], IEnumerable):
    """ Has been extended to provide read and write access to a collection of FluidTemperature objects which represent the fluid's properties at various temperatures. """
    def AddTemperature(self, fluidTemperature):
        """
        AddTemperature(self: FluidType, fluidTemperature: FluidTemperature)
            Adds a fluid temperature to the set.
        
            fluidTemperature: The fluid temperature being inserted.
        """
        pass

    def ClearAllTemperatures(self):
        """
        ClearAllTemperatures(self: FluidType)
            Clears all fluid temperatures in the set.
        """
        pass

    @staticmethod
    def Create(document, fluidTypeName, basedOnFluidType=None):
        """
        Create(document: Document, fluidTypeName: str) -> FluidType
        
            Creates a new empty fluid type and adds it to the document.
        
            document: The document.
            fluidTypeName: The name of fluid type.
            Returns: The newly created fluid type.
        Create(document: Document, fluidTypeName: str, basedOnFluidType: FluidType) -> FluidType
        
            Creates a new fluid type and adds it to the document.
        
            document: The document.
            fluidTypeName: The name of new created fluid type.
            basedOnFluidType: The existing fluid type which is based on.
            Returns: The newly created fluid type.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FluidType) -> IEnumerator[FluidTemperature]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetFluidTemperatureSetIterator(self):
        """
        GetFluidTemperatureSetIterator(self: FluidType) -> FluidTemperatureSetIterator
        
            Returns a FluidTemperatureSetIterator that iterates through the collection.
            Returns: A FluidTemperatureSetIterator object that can be used to iterate through 
             key-value pairs in the collection.
        """
        pass

    @staticmethod
    def GetFluidType(document, fluidTypeName):
        """
        GetFluidType(document: Document, fluidTypeName: str) -> FluidType
        
            Gets a fluid type by name.
        
            document: The document.
            fluidTypeName: The name of fluid type.
            Returns: The fluid type. ll if the fluid type was not found.
        """
        pass

    def GetTemperature(self, temperature):
        """
        GetTemperature(self: FluidType, temperature: float) -> FluidTemperature
        
            Gets a copy of the FluidTemperature object matching a given temperature value.
        
            temperature: The temperature value.
            Returns: The fluid temperature. ll if not found.
        """
        pass

    @staticmethod
    def IsFluidInUse(document, fluidId):
        """
        IsFluidInUse(document: Document, fluidId: ElementId) -> bool
        
            Identifies if the fluid type is in use.
        
            document: The document.
            fluidId: The id of the fluid type.
            Returns: True if the fluid type is in use.
           False if the fluid type is not in use.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveTemperature(self, temperature):
        """
        RemoveTemperature(self: FluidType, temperature: float)
            Removes a fluid temperature via the temperature value from the set.
        
            temperature: The temperature value.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FluidTemperature](enumerable: IEnumerable[FluidTemperature], value: FluidTemperature) -> bool """
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


class IPipeFittingAndAccessoryPressureDropServer(IExternalServer):
    """ Interface class for external servers implementing pipe fitting and pipe accessory coefficient calculation. """
    def Calculate(self, data):
        """
        Calculate(self: IPipeFittingAndAccessoryPressureDropServer, data: PipeFittingAndAccessoryPressureDropData) -> bool
        
            Calculate the pipe fitting and pipe accessory coefficient.
        
            data: The input and output data of the calculation.
            Returns: True if calculation succeeds.
           False if calculation fails.
        """
        pass

    def GetDataSchema(self):
        """
        GetDataSchema(self: IPipeFittingAndAccessoryPressureDropServer) -> Schema
        
            Obtains the schema of the ESEntity.
            Returns: Null if the server has no data.
        """
        pass

    def IsApplicable(self, data):
        """
        IsApplicable(self: IPipeFittingAndAccessoryPressureDropServer, data: PipeFittingAndAccessoryPressureDropData) -> bool
        
            Check if the server is applicable for the pipe fitting or pipe accessory.
        
            data: The input data of the calculation.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPipePlumbingFixtureFlowServer(IExternalServer):
    """ Interface class for external servers implementing Pipe plumbing fixture flow calculation. """
    def Calculate(self, data):
        """
        Calculate(self: IPipePlumbingFixtureFlowServer, data: PipePlumbingFixtureFlowData)
            Calculate the pipe plumbing fixture flow.
        
            data: The input and output data of the calculation.
        """
        pass

    def GetHtmlDescription(self):
        """
        GetHtmlDescription(self: IPipePlumbingFixtureFlowServer) -> str
        
            The method that Revit will invoke to get an HTML formatted description of the 
             server.
        
            Returns: The HTML format description of the server.
        """
        pass

    def GetInformationLink(self):
        """
        GetInformationLink(self: IPipePlumbingFixtureFlowServer) -> str
        
            The method that Revit will invoke to obtain a URL address which provides more 
             information about the server.
        
            Returns: The URL providing server information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPipePressureDropServer(IExternalServer):
    """ Interface for external servers implementing pipe pressure drop calculation. """
    def Calculate(self, data):
        """
        Calculate(self: IPipePressureDropServer, data: PipePressureDropData)
            Calculate the pipe pressure drop.
        
            data: The input and output data of the calculation.
        """
        pass

    def GetHtmlDescription(self):
        """
        GetHtmlDescription(self: IPipePressureDropServer) -> str
        
            The method that Revit will invoke to get an HTML formatted description of the 
             server.
        
            Returns: The HTML format description of the server.
        """
        pass

    def GetInformationLink(self):
        """
        GetInformationLink(self: IPipePressureDropServer) -> str
        
            The method that Revit will invoke to obtain a URL address which provides more 
             information about the server.
        
            Returns: The URL providing server information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Pipe(MEPCurve, IDisposable):
    """ A pipe in the Autodesk Revit MEP product. """
    @staticmethod
    def Create(document, *__args):
        """
        Create(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Pipe
        
            Creates a new pipe from two points.
        
            document: The document.
            systemTypeId: The ElementId of the piping system type.
            pipeTypeId: The ElementId of the pipe type.
            levelId: The level ElementId for the pipe.
            startPoint: The start point of the pipe.
            endPoint: The end point of the pipe.
            Returns: The pipe.
        Create(document: Document, pipeTypeId: ElementId, levelId: ElementId, startConnector: Connector, endPoint: XYZ) -> Pipe
        
            Creates a new pipe that connects to the connector.
        
            document: The document.
            pipeTypeId: The ElementId of the new pipe type.
            levelId: The level id for the new pipe.
            startConnector: The first connector where the new pipe starts.
            endPoint: The second point of the new pipe.
            Returns: The pipe.
        Create(document: Document, pipeTypeId: ElementId, levelId: ElementId, startConnector: Connector, endConnector: Connector) -> Pipe
        
            Creates a new pipe that connects to two connectors.
        
            document: The document.
            pipeTypeId: The ElementId of the new pipe type.
            levelId: The level ElementId for the new pipe.
            startConnector: The first connector where the new pipe starts.
            endConnector: The second point of the new pipe.
            Returns: The pipe.
        """
        pass

    @staticmethod
    def CreatePlaceholder(document, systemTypeId, pipeTypeId, levelId, startPoint, endPoint):
        """
        CreatePlaceholder(document: Document, systemTypeId: ElementId, pipeTypeId: ElementId, levelId: ElementId, startPoint: XYZ, endPoint: XYZ) -> Pipe
        
            Creates a new placeholder pipe.
        
            document: The document.
            systemTypeId: The ElementId of the piping system type.
            pipeTypeId: The ElementId of the pipe type.
            levelId: The level id for the pipe.
            startPoint: The first point of the placeholder line.
            endPoint: The second point of the placeholder line.
            Returns: The placeholder pipe.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
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

    @staticmethod
    def IsPipeTypeId(document, pipeTypeId):
        """
        IsPipeTypeId(document: Document, pipeTypeId: ElementId) -> bool
        
            Checks if given type is valid pipe type.
        
            document: The document.
            pipeTypeId: ElementId of the pipe type to check.
            Returns: True if pipe type can used for this pipe, false otherwise.
        """
        pass

    @staticmethod
    def IsPipingConnector(connector):
        """
        IsPipingConnector(connector: Connector) -> bool
        
            Checks if the given connector is a valid piping connector.
        
            connector: Connector to check
            Returns: True if the connector has the Piping domain type.
        """
        pass

    @staticmethod
    def IsPipingSystemTypeId(document, systemTypeId):
        """
        IsPipingSystemTypeId(document: Document, systemTypeId: ElementId) -> bool
        
            Checks if given type is valid piping system type.
        
            document: The document.
            systemTypeId: ElementId of the piping system type to check.
            Returns: True if the given systemTypeId is the piping system type, false otherwise.
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
        SetSystemType(self: Pipe, systemTypeId: ElementId)
            Updates the associated system type for the pipe.
        
            systemTypeId: The ElementId of the piping system type.
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

    FlowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow state of the pipe.

Get: FlowState(self: Pipe) -> PipeFlowState

"""

    IsPlaceholder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the pipe is a placeholder or not.

Get: IsPlaceholder(self: Pipe) -> bool

"""

    PipeSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pipe segment that was assigned to this pipe according to the routing preference.

Get: PipeSegment(self: Pipe) -> PipeSegment

"""

    PipeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pipe type of this pipe.

Get: PipeType(self: Pipe) -> PipeType

Set: PipeType(self: Pipe) = value
"""



class PipeFittingAndAccessoryConnectorData(object, IDisposable):
    """ The input data used by external servers for calculation of the pipe fitting and pipe accessory coefficient. """
    def Dispose(self):
        """ Dispose(self: PipeFittingAndAccessoryConnectorData) """
        pass

    def GetCoordination(self):
        """
        GetCoordination(self: PipeFittingAndAccessoryConnectorData) -> Transform
        
            Gets the coordination of the connector
            Returns: The coordination of the connector
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipeFittingAndAccessoryConnectorData, disposing: bool) """
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
    """The angle of the fitting, Units:(rad).

Get: Angle(self: PipeFittingAndAccessoryConnectorData) -> float

"""

    Coordination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the coordination of the connector

Get: Coordination(self: PipeFittingAndAccessoryConnectorData) -> Transform

"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector diameter, Units:(ft).

Get: Diameter(self: PipeFittingAndAccessoryConnectorData) -> float

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector flow, Units:(ft³/s)

Get: Flow(self: PipeFittingAndAccessoryConnectorData) -> float

"""

    FlowDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow direction of this connector, In or Out.

Get: FlowDirection(self: PipeFittingAndAccessoryConnectorData) -> FlowDirectionType

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector height, Units:(ft).

Get: Height(self: PipeFittingAndAccessoryConnectorData) -> float

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the index of this connector

Get: Index(self: PipeFittingAndAccessoryConnectorData) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipeFittingAndAccessoryConnectorData) -> bool

"""

    LinkIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the connector which is linked with this connector

Get: LinkIndex(self: PipeFittingAndAccessoryConnectorData) -> int

"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector profile.

Get: Profile(self: PipeFittingAndAccessoryConnectorData) -> ConnectorProfileType

"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector velocity pressure. Units: (kg/(ft·s²)).

Get: VelocityPressure(self: PipeFittingAndAccessoryConnectorData) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector width, Units:(ft).

Get: Width(self: PipeFittingAndAccessoryConnectorData) -> float

"""



class PipeFittingAndAccessoryData(object, IDisposable):
    """ The input data used by external servers for calculation of the pipe fitting and pipe accessory coefficient. """
    def Dispose(self):
        """ Dispose(self: PipeFittingAndAccessoryData) """
        pass

    def GetAllConnectorData(self):
        """
        GetAllConnectorData(self: PipeFittingAndAccessoryData) -> IList[PipeFittingAndAccessoryConnectorData]
        
            Gets the connector data of the pipe fitting or pipe accessory.
            Returns: All connector data.
        """
        pass

    def GetEntity(self):
        """
        GetEntity(self: PipeFittingAndAccessoryData) -> Entity
        
            Returns an Entity of the Schema of the serverGUID.
            Returns: The Entity.
        """
        pass

    def GetFamilyInstanceId(self):
        """
        GetFamilyInstanceId(self: PipeFittingAndAccessoryData) -> ElementId
        
            Gets the Id of the fiting or accessory instance
            Returns: The element Id of the fiting or accessory instance.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipeFittingAndAccessoryData, disposing: bool) """
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

    BehaviorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The behavior type of the pipe fitting or pipe accessory.

Get: BehaviorType(self: PipeFittingAndAccessoryData) -> int

"""

    FluidDensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fluid density of the pipe fitting or pipe accessory, Units: (kg/ft³).

Get: FluidDensity(self: PipeFittingAndAccessoryData) -> float

"""

    FluidViscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fluid dynamic viscosity of the pipe fitting or pipe accessory, Units: (kg/(ft·s)).

Get: FluidViscosity(self: PipeFittingAndAccessoryData) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipeFittingAndAccessoryData) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The origin position of the pipe fitting or pipe accessory.

Get: Origin(self: PipeFittingAndAccessoryData) -> XYZ

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The part type of the pipe fitting or pipe accessory.

Get: PartType(self: PipeFittingAndAccessoryData) -> PartType

"""

    ServerGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The GUID of the pipe fitting or pipe accessory.

Get: ServerGUID(self: PipeFittingAndAccessoryData) -> Guid

"""

    SystemClassification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The system classification of the pipe fitting or pipe accessory.

Get: SystemClassification(self: PipeFittingAndAccessoryData) -> MEPSystemClassification

"""



class PipeFittingAndAccessoryPressureDropData(object, IDisposable):
    """ The input and output data used by external servers for calculation of the pipe fitting and pipe accessory pressure drop. """
    def Dispose(self):
        """ Dispose(self: PipeFittingAndAccessoryPressureDropData) """
        pass

    def GetPipeFittingAndAccessoryData(self):
        """
        GetPipeFittingAndAccessoryData(self: PipeFittingAndAccessoryPressureDropData) -> PipeFittingAndAccessoryData
        
            Returns the fitting and accessory information
        """
        pass

    def GetPresureDropItems(self):
        """
        GetPresureDropItems(self: PipeFittingAndAccessoryPressureDropData) -> IList[PipeFittingAndAccessoryPressureDropItem]
        
            Returns the pressure drop items
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipeFittingAndAccessoryPressureDropData, disposing: bool) """
        pass

    def SetDefaultEntity(self, defaultEntity):
        """
        SetDefaultEntity(self: PipeFittingAndAccessoryPressureDropData, defaultEntity: Entity)
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

Get: CalculationType(self: PipeFittingAndAccessoryPressureDropData) -> int

"""

    IsCurrentEntityValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the current settings stored in the entity is valid.

Get: IsCurrentEntityValid(self: PipeFittingAndAccessoryPressureDropData) -> bool

Set: IsCurrentEntityValid(self: PipeFittingAndAccessoryPressureDropData) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipeFittingAndAccessoryPressureDropData) -> bool

"""



class PipeFittingAndAccessoryPressureDropItem(object, IDisposable):
    """ A flow path of the pipe/pipe fitting and accessory. It is defined by the begin connector and end connector """
    def Dispose(self):
        """ Dispose(self: PipeFittingAndAccessoryPressureDropItem) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipeFittingAndAccessoryPressureDropItem, disposing: bool) """
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
    """The index of the begin connector of the flow path

Get: BeginConnectorIndex(self: PipeFittingAndAccessoryPressureDropItem) -> int

"""

    Coefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The coefficient between the begin connector and end connector, Units: (kg/(ft·s²)).

Get: Coefficient(self: PipeFittingAndAccessoryPressureDropItem) -> float

Set: Coefficient(self: PipeFittingAndAccessoryPressureDropItem) = value
"""

    EndConnectorIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the end conector of the flow path

Get: EndConnectorIndex(self: PipeFittingAndAccessoryPressureDropItem) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipeFittingAndAccessoryPressureDropItem) -> bool

"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity pressure, for converting between coefficient and pressure drop on this flow path. Units: (kg/(ft·s²)).

Get: VelocityPressure(self: PipeFittingAndAccessoryPressureDropItem) -> float

"""



class PipeFlowConfigurationType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all connector flow configuration
    
    enum PipeFlowConfigurationType, values: Calculated (0), Demand (3), Preset (1), System (2)
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
    Demand = None
    Preset = None
    System = None
    value__ = None


class PipeFlowState(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the pipe flow states for a pipe
    
    enum PipeFlowState, values: LaminarState (0), MultiValues (-1), TransitionState (1), TurbulentState (2)
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

    LaminarState = None
    MultiValues = None
    TransitionState = None
    TurbulentState = None
    value__ = None


class PipeInsulation(InsulationLiningBase, IDisposable):
    """ Represents insulation applied to the outside of a given pipe, fitting or content. """
    @staticmethod
    def Create(document, pipeOrContentElementId, pipeInsulationTypeId, Thickness):
        """
        Create(document: Document, pipeOrContentElementId: ElementId, pipeInsulationTypeId: ElementId, Thickness: float) -> PipeInsulation
        
            Creates a new instance of pipe insulation.
        
            document: The document.
            pipeOrContentElementId: The pipe, fitting, accessory ElementId to which insulation will be added.
            pipeInsulationTypeId: The pipe insulation type.
           If the input pipe insulation type is 
             InvalidElementId, the default insulation type from the document will be used.
        
            Thickness: The thickness of the insulation.
            Returns: The newly created pipe insulation.
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


class PipeInsulationType(ElementType, IDisposable):
    """ This class represents a pipe insulation type in Autodesk Revit. """
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


class PipeLossMethodType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all pipe loss method types for a connector
    
    enum PipeLossMethodType, values: Coefficient (6), NotDefined (0), SpecificLoss (4), Table (1)
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
    Table = None
    value__ = None


class PipePlumbingFixtureFlowData(object, IDisposable):
    """ The input and output data used by external servers for calculation of the pipe plumbing fixture flow. """
    def Dispose(self):
        """ Dispose(self: PipePlumbingFixtureFlowData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipePlumbingFixtureFlowData, disposing: bool) """
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

    DimensionFlow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The dimension flow which is used to calculate flow of the pipe. Units: (gal/min).

Get: DimensionFlow(self: PipePlumbingFixtureFlowData) -> float

"""

    FixtureUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixture units of the pipe.

Get: FixtureUnits(self: PipePlumbingFixtureFlowData) -> float

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual flow of the plumbing fixture converted from dimension flow or fixture unit. Units: (gal/min).

Get: Flow(self: PipePlumbingFixtureFlowData) -> float

Set: Flow(self: PipePlumbingFixtureFlowData) = value
"""

    FlowConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow configuration mode of the pipe.

Get: FlowConfiguration(self: PipePlumbingFixtureFlowData) -> PipeFlowConfigurationType

"""

    FlowConversionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow conversion mode of the pipe.

Get: FlowConversionMode(self: PipePlumbingFixtureFlowData) -> FlowConversionMode

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipePlumbingFixtureFlowData) -> bool

"""



class PipePressureDropData(object, IDisposable):
    """ The input and output data used by external servers for calculation of the pipe  pressure drop. """
    def Dispose(self):
        """ Dispose(self: PipePressureDropData) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipePressureDropData, disposing: bool) """
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
    """The category id of pipe curves. It will be OST_PipeCurves, OST_FlexPipeCurves, or OST_PlaceHolderPipes.

Get: CategoryId(self: PipePressureDropData) -> ElementId

"""

    Coefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The coefficient of the pipe.

Get: Coefficient(self: PipePressureDropData) -> float

Set: Coefficient(self: PipePressureDropData) = value
"""

    Density = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The density of the pipe. Units: (kg/ft³).

Get: Density(self: PipePressureDropData) -> float

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow of the pipe. Units: (ft³/s).

Get: Flow(self: PipePressureDropData) -> float

"""

    FlowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flowState of the pipe.

Get: FlowState(self: PipePressureDropData) -> PipeFlowState

Set: FlowState(self: PipePressureDropData) = value
"""

    Friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The friction of the pipe. Units: (kg/(ft²·s²)).

Get: Friction(self: PipePressureDropData) -> float

Set: Friction(self: PipePressureDropData) = value
"""

    FrictionFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The friction factor of the pipe.

Get: FrictionFactor(self: PipePressureDropData) -> float

Set: FrictionFactor(self: PipePressureDropData) = value
"""

    InsideDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The inside diameter of the pipe. Units: (ft).

Get: InsideDiameter(self: PipePressureDropData) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipePressureDropData) -> bool

"""

    KLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The system calculation level.

Get: KLevel(self: PipePressureDropData) -> SystemCalculationLevel

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the pipe. Units: (ft).

Get: Length(self: PipePressureDropData) -> float

"""

    NominalDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The nominal diameter of the pipe. Units: (ft).

Get: NominalDiameter(self: PipePressureDropData) -> float

"""

    OutsideDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The outside diameter of the pipe. Units: (ft).

Get: OutsideDiameter(self: PipePressureDropData) -> float

"""

    PressureDrop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pressure drop of the pipe. Units: (kg/(ft·s²)).

Get: PressureDrop(self: PipePressureDropData) -> float

Set: PressureDrop(self: PipePressureDropData) = value
"""

    RelativeRoughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The relative roughness of the pipe.

Get: RelativeRoughness(self: PipePressureDropData) -> float

Set: RelativeRoughness(self: PipePressureDropData) = value
"""

    ReynoldsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The reynolds number of the pipe.

Get: ReynoldsNumber(self: PipePressureDropData) -> float

Set: ReynoldsNumber(self: PipePressureDropData) = value
"""

    Roughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The roughness of the pipe. Units: (ft).

Get: Roughness(self: PipePressureDropData) -> float

"""

    Velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity of the pipe. Units: (ft/s) .

Get: Velocity(self: PipePressureDropData) -> float

Set: Velocity(self: PipePressureDropData) = value
"""

    VelocityPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The velocity pressure of the pipe. Units: (kg/(ft·s²))

Get: VelocityPressure(self: PipePressureDropData) -> float

Set: VelocityPressure(self: PipePressureDropData) = value
"""

    Viscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The viscosity of the pipe. Units: (kg/(ft·s)).

Get: Viscosity(self: PipePressureDropData) -> float

"""



class PipeScheduleType(ElementType, IDisposable):
    """ Represents a pipe schedule type in the Autodesk Revit MEP product. """
    @staticmethod
    def Create(doc, name):
        """
        Create(doc: Document, name: str) -> PipeScheduleType
        
            Creates a new pipe schedule type with the given name.
        
            doc: The document
            name: The name of requested schedule type.
            Returns: Returns the newly created schedule type.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetPipeScheduleId(doc, name):
        """
        GetPipeScheduleId(doc: Document, name: str) -> ElementId
        
            Returns an existing pipe schedule type with the same name.
        
            doc: The document
            name: The name of requested schedule type.
            Returns: Returns the element id of request schedule type, or invalidElementId if the 
             name is not found.
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


class PipeSegment(Segment, IDisposable):
    """
    The PipeSegment class represents an instance of pipe segment which has the design
       data for routing preference.
    """
    @staticmethod
    def Create(ADocument, MaterialId, ScheduleId, sizeSet):
        """ Create(ADocument: Document, MaterialId: ElementId, ScheduleId: ElementId, sizeSet: ICollection[MEPSize]) -> PipeSegment """
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

    ScheduleTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the PipeScheduleType.

Get: ScheduleTypeId(self: PipeSegment) -> ElementId

"""



class PipeSettings(Element, IDisposable):
    """ The pipe setting class. """
    def AddPipeSlope(self, slope):
        """
        AddPipeSlope(self: PipeSettings, slope: float)
            Add a pipe slope value.
        
            slope: The pipe slope value. Revit stores the slope value as a percentage (0-100).
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetFlowConvertionServerInfo(self):
        """
        GetFlowConvertionServerInfo(self: PipeSettings) -> MEPCalculationServerInfo
        
            Get the MEPServerInfo of the current plumbing flow convertion server.
            Returns: The MEPServerInfo of the current plumbing flow convertion server.
        """
        pass

    @staticmethod
    def GetPipeSettings(document):
        """
        GetPipeSettings(document: Document) -> PipeSettings
        
            Get the pipe settings of the project.
        
            document: The document.
            Returns: The pipe settings of the project.
        """
        pass

    def GetPipeSlopes(self):
        """
        GetPipeSlopes(self: PipeSettings) -> IList[float]
        
            Get pipe slopes.
            Returns: Pipe slope values. Revit stores the slope value as a percentage (0-100).
        """
        pass

    def GetPressLossCalculationServerInfo(self):
        """
        GetPressLossCalculationServerInfo(self: PipeSettings) -> MEPCalculationServerInfo
        
            Get the MEPServerInfo of the current pipe pressure loss calculation server.
            Returns: The MEPServerInfo of the current pipe pressure loss calculation server
        """
        pass

    def GetSpecificFittingAngles(self):
        """
        GetSpecificFittingAngles(self: PipeSettings) -> IList[float]
        
            Gets the list of specific fitting angles.
            Returns: Angles (in degrees).
        """
        pass

    def GetSpecificFittingAngleStatus(self, angle):
        """
        GetSpecificFittingAngleStatus(self: PipeSettings, angle: float) -> bool
        
            Gets the status of given specific angle.
        
            angle: The specific fitting angle (in degree) that must be one of 90, 60, 45, 30, 22.5 
             or 11.25 degrees.
        """
        pass

    def IsValidSpecificFittingAngle(self, angle):
        """
        IsValidSpecificFittingAngle(self: PipeSettings, angle: float) -> bool
        
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

    def SetFlowConvertionServerInfo(self, serverInfo):
        """
        SetFlowConvertionServerInfo(self: PipeSettings, serverInfo: MEPCalculationServerInfo)
            Set the MEPServerInfo of the current plumbing flow convertion server.
        """
        pass

    def SetPipeSlopes(self, slopes):
        """ SetPipeSlopes(self: PipeSettings, slopes: IList[float]) """
        pass

    def SetPressLossCalculationServerInfo(self, serverInfo):
        """
        SetPressLossCalculationServerInfo(self: PipeSettings, serverInfo: MEPCalculationServerInfo)
            Set the MEPServerInfo of the current pipe pressure loss calculation server.
        """
        pass

    def SetSpecificFittingAngleStatus(self, angle, bStatus):
        """
        SetSpecificFittingAngleStatus(self: PipeSettings, angle: float, bStatus: bool)
            Sets the status of given specific angle.
        
            angle: The specific angle (in degree) that must be one of 60, 45, 30, 22.5 or 11.25 
             degrees.
        
            bStatus: Status, true - using the given angle during the pipe layout.
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

    Centerline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Centerline (=) string.

Get: Centerline(self: PipeSettings) -> str

Set: Centerline(self: PipeSettings) = value
"""

    ConnectorSeparator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector separator string.

Get: ConnectorSeparator(self: PipeSettings) -> str

Set: ConnectorSeparator(self: PipeSettings) = value
"""

    ConnectorTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The connector tolerance value.

Get: ConnectorTolerance(self: PipeSettings) -> float

Set: ConnectorTolerance(self: PipeSettings) = value
"""

    FittingAngleUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine how to use fitting angle during pipe layout or modifying layout.

Get: FittingAngleUsage(self: PipeSettings) -> FittingAngleUsage

Set: FittingAngleUsage(self: PipeSettings) = value
"""

    FittingAnnotationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of fitting annotation size.

Get: FittingAnnotationSize(self: PipeSettings) -> float

Set: FittingAnnotationSize(self: PipeSettings) = value
"""

    FlatOnBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Flat On Bottom (FOB) string.

Get: FlatOnBottom(self: PipeSettings) -> str

Set: FlatOnBottom(self: PipeSettings) = value
"""

    FlatOnTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Flat On Top (FOT) string.

Get: FlatOnTop(self: PipeSettings) -> str

Set: FlatOnTop(self: PipeSettings) = value
"""

    SetDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Set Down (SD) string.

Get: SetDown(self: PipeSettings) -> str

Set: SetDown(self: PipeSettings) = value
"""

    SetUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The abbreviation of the Set Up (SU) string.

Get: SetUp(self: PipeSettings) -> str

Set: SetUp(self: PipeSettings) = value
"""

    SizePrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size prefix string.

Get: SizePrefix(self: PipeSettings) -> str

Set: SizePrefix(self: PipeSettings) = value
"""

    SizeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size suffix string.

Get: SizeSuffix(self: PipeSettings) -> str

Set: SizeSuffix(self: PipeSettings) = value
"""

    UseAnnotationScaleForSingleLineFittings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether use annotation scale for single line fittings or not.

Get: UseAnnotationScaleForSingleLineFittings(self: PipeSettings) -> bool

Set: UseAnnotationScaleForSingleLineFittings(self: PipeSettings) = value
"""



class PipeSystemType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the possible pipe system types for a connector object.
    
    enum PipeSystemType, values: DomesticColdWater (20), DomesticHotWater (19), FireProtectDry (24), FireProtectOther (26), FireProtectPreaction (25), FireProtectWet (23), Fitting (28), Global (29), OtherPipe (22), ReturnHydronic (8), Sanitary (16), SupplyHydronic (7), UndefinedSystemType (0), Vent (17)
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

    DomesticColdWater = None
    DomesticHotWater = None
    FireProtectDry = None
    FireProtectOther = None
    FireProtectPreaction = None
    FireProtectWet = None
    Fitting = None
    Global = None
    OtherPipe = None
    ReturnHydronic = None
    Sanitary = None
    SupplyHydronic = None
    UndefinedSystemType = None
    value__ = None
    Vent = None


class PipeType(MEPCurveType, IDisposable):
    """ A pipe type element. """
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

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The schedule type of the pipe type.

Get: Class(self: PipeType) -> PipeScheduleType

"""



class PipingSystem(MEPSystem, IDisposable):
    """ A piping system element. """
    @staticmethod
    def Create(ADocument, typeId, name=None):
        """
        Create(ADocument: Document, typeId: ElementId) -> PipingSystem
        
            Creates a new instance of a piping system and adds it to the document.
        
            ADocument: The document where the element will be created and added.
            typeId: The identifier of this piping system element's type.
            Returns: The newly created piping system element.
        Create(ADocument: Document, typeId: ElementId, name: str) -> PipingSystem
        
            Creates a new instance of a piping system and adds it to the document.
        
            ADocument: The document where the element will be created and added.
            typeId: The identifier of this piping system element's type.
            name: The name of the piping system to be created.
            Returns: The newly created piping system element.
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

    def GetFixtureUnits(self):
        """
        GetFixtureUnits(self: PipingSystem) -> float
        
            Gets the fixture units of this piping system.
        """
        pass

    def GetFlow(self):
        """
        GetFlow(self: PipingSystem) -> float
        
            Gets the flow of this piping system.
        """
        pass

    def getFlow(self, *args): #cannot find CLR method
        """ getFlow(self: MEPSystem, param: BuiltInParameter) -> float """
        pass

    def GetStaticPressure(self):
        """
        GetStaticPressure(self: PipingSystem) -> float
        
            Gets the static pressure of this piping system.
        """
        pass

    def getStaticPressure(self, *args): #cannot find CLR method
        """ getStaticPressure(self: MEPSystem, param: BuiltInParameter) -> float """
        pass

    def GetVolume(self):
        """
        GetVolume(self: PipingSystem) -> float
        
            Gets the volume of this piping system.
        """
        pass

    def IsFlowServerMissing(self):
        """
        IsFlowServerMissing(self: PipingSystem) -> bool
        
            Indicates if any flow server which was used in the piping system is not 
             available.
        
            Returns: True if there is any flow server not available, false otherwise.
        """
        pass

    def IsPressureDropServerMissing(self):
        """
        IsPressureDropServerMissing(self: PipingSystem) -> bool
        
            Indicates if any pressure drop server which was used in the piping system is 
             not available.
        
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
    """The connector within base equipment which is used to connect with system.

Get: BaseEquipmentConnector(self: PipingSystem) -> Connector

Set: BaseEquipmentConnector(self: PipingSystem) = value
"""

    FixtureUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixture units of this piping system

Get: FixtureUnits(self: PipingSystem) -> float

"""

    Flow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow of this piping system

Get: Flow(self: PipingSystem) -> float

"""

    IsWellConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the system is well connected or not.

Get: IsWellConnected(self: PipingSystem) -> bool

"""

    PipingNetwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pipes and fittings which are contained in this system.

Get: PipingNetwork(self: PipingSystem) -> ElementSet

"""

    StaticPressure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The static pressure of this piping system

Get: StaticPressure(self: PipingSystem) -> float

"""

    SystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of this piping system.

Get: SystemType(self: PipingSystem) -> PipeSystemType

"""



class PipingSystemType(MEPSystemType, IDisposable):
    """ Base class for piping system types """
    @staticmethod
    def Create(ADoc, systemClassification, name):
        """
        Create(ADoc: Document, systemClassification: MEPSystemClassification, name: str) -> PipingSystemType
        
            Creates a new instance of a piping system type and adds it to the document.
        
            ADoc: The document where the element will be created and added.
            systemClassification: The classification for the piping system type to be created
            name: The name of the piping system type to be created.
            Returns: The newly created piping system type element.
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
        ValidateRiseDropSymbolType(self: PipingSystemType, risedropType: RiseDropSymbol) -> bool
        
            Confirms if the parameter is a valid piping rise/drop symbol type.
        
            risedropType: The type.
            Returns: True if the input is a valid piping rise/drop symbol type, false otherwise.
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

    FlowConversionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flow conversion method for the piping system type.

Get: FlowConversionMethod(self: PipingSystemType) -> FlowConversionMode

Set: FlowConversionMethod(self: PipingSystemType) = value
"""

    FluidTemperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fluid Temperature

Get: FluidTemperature(self: PipingSystemType) -> float

Set: FluidTemperature(self: PipingSystemType) = value
"""

    FluidType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fluid Type

Get: FluidType(self: PipingSystemType) -> ElementId

Set: FluidType(self: PipingSystemType) = value
"""

    SingleLineBendDropType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol for a 1 line drop

Get: SingleLineBendDropType(self: PipingSystemType) -> RiseDropSymbol

Set: SingleLineBendDropType(self: PipingSystemType) = value
"""

    SingleLineBendRiseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol for a 1 line rise

Get: SingleLineBendRiseType(self: PipingSystemType) -> RiseDropSymbol

Set: SingleLineBendRiseType(self: PipingSystemType) = value
"""

    SingleLineJunctionDropType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol for a 1 line junction drop

Get: SingleLineJunctionDropType(self: PipingSystemType) -> RiseDropSymbol

Set: SingleLineJunctionDropType(self: PipingSystemType) = value
"""

    SingleLineJunctionRiseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol for a 1 line junction rise

Get: SingleLineJunctionRiseType(self: PipingSystemType) -> RiseDropSymbol

Set: SingleLineJunctionRiseType(self: PipingSystemType) = value
"""

    TwoLineDropType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol for a 2 line drop

Get: TwoLineDropType(self: PipingSystemType) -> RiseDropSymbol

Set: TwoLineDropType(self: PipingSystemType) = value
"""

    TwoLineRiseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol for a 2 line rise

Get: TwoLineRiseType(self: PipingSystemType) -> RiseDropSymbol

Set: TwoLineRiseType(self: PipingSystemType) = value
"""



class PlumbingUtils(object):
    """ General utility methods in the Autodesk Revit MEP product. """
    @staticmethod
    def BreakCurve(document, pipeId, ptBreak):
        """
        BreakCurve(document: Document, pipeId: ElementId, ptBreak: XYZ) -> ElementId
        
            Breaks the pipe curve into two parts at the given position.
        
            document: The document.
            pipeId: The element id of the pipe curve to break.
            ptBreak: The break point on the pipe curve.
            Returns: The new pipe curve element id if successful otherwise if a failure occurred an 
             invalidElementId is returned.
        """
        pass

    @staticmethod
    def ConnectPipePlaceholdersAtCross(document, *__args):
        """
        ConnectPipePlaceholdersAtCross(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool
        
            Connects placeholders that looks like Cross connection.
        
            document: The document.
            placeholder1Id: The first element Id of pipe placeholder.
            placeholder2Id: The second element Id of pipe placeholder.
            Returns: True if connection succeeds, false otherwise.
        ConnectPipePlaceholdersAtCross(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId, placeholder3Id: ElementId) -> bool
        
            Connects placeholders that looks like Cross connection.
        
            document: The document.
            placeholder1Id: The first element Id of pipe placeholder.
            placeholder2Id: The second element Id of pipe placeholder that intersects with first one.
            placeholder3Id: The third element Id of pipe placeholder that intersects with first one.
            Returns: True if connection succeeds, false otherwise.
        ConnectPipePlaceholdersAtCross(document: Document, connector1: Connector, connector2: Connector, connector3: Connector, connector4: Connector) -> bool
        
            Connects placeholders that looks like Cross connection.
        
            document: The document.
            connector1: The first end connector of placeholder to be connected to the second.
            connector2: The second end connector of placeholder to be connected to the first.
            connector3: The third end connector of placeholder to be connected to the forth.
            connector4: The fourth end connector of placeholder to be connected to the third.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConnectPipePlaceholdersAtElbow(document, *__args):
        """
        ConnectPipePlaceholdersAtElbow(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool
        
            Connects placeholders that looks like elbow connection.
        
            document: The document.
            placeholder1Id: The element Id of pipe placeholder.
            placeholder2Id: The element Id of pipe placeholder.
            Returns: True if connection succeeds, false otherwise.
        ConnectPipePlaceholdersAtElbow(document: Document, connector1: Connector, connector2: Connector) -> bool
        
            Connects placeholders that looks like elbow connection.
        
            document: The document.
            connector1: The first end connector of placeholder to be connected to.
            connector2: The second end connector of placeholder to be connected to.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConnectPipePlaceholdersAtTee(document, *__args):
        """
        ConnectPipePlaceholdersAtTee(document: Document, placeholder1Id: ElementId, placeholder2Id: ElementId) -> bool
        
            Connects two placeholders that looks like Tee connection.
        
            document: The document.
            placeholder1Id: The first element Id of pipe placeholder.
            placeholder2Id: The second element Id of pipe placeholder which connects to first.
            Returns: True if connection succeeds, false otherwise.
        ConnectPipePlaceholdersAtTee(document: Document, connector1: Connector, connector2: Connector, connector3: Connector) -> bool
        
            Connects three placeholders that looks like Tee connection.
        
            document: The document.
            connector1: The first end connector of placeholder to be connected to the second.
            connector2: The second end connector of placeholder to be connected to the first.
            connector3: The third end connector of placeholder to be connected to the first or second.
            Returns: True if connection succeeds, false otherwise.
        """
        pass

    @staticmethod
    def ConvertPipePlaceholders(document, placeholderIds):
        """ ConvertPipePlaceholders(document: Document, placeholderIds: ICollection[ElementId]) -> ICollection[ElementId] """
        pass

    @staticmethod
    def HasOpenConnector(document, elemId):
        """
        HasOpenConnector(document: Document, elemId: ElementId) -> bool
        
            Checks if there is open piping connector for the given element - object of pipe 
             curve, pipe fitting or pipe accessory.
        
        
            document: The document.
            elemId: Element id to check.
            Returns: True if given element has open piping connector, false otherwise.
        """
        pass

    @staticmethod
    def PlaceCapOnOpenEnds(document, elemId, typeId):
        """
        PlaceCapOnOpenEnds(document: Document, elemId: ElementId, typeId: ElementId)
            Places caps on the open connectors of the pipe curve, pipe fitting or pipe 
             accessory.
        
        
            document: The document.
            elemId: Element id of pipe curve, pipe fitting or pipe accessory.
            typeId: Pipe type element id.
           Default is invalidElementId.
        """
        pass

    __all__ = [
        'BreakCurve',
        'ConnectPipePlaceholdersAtCross',
        'ConnectPipePlaceholdersAtElbow',
        'ConnectPipePlaceholdersAtTee',
        'ConvertPipePlaceholders',
        'HasOpenConnector',
        'PlaceCapOnOpenEnds',
    ]


