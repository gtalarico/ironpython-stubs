# encoding: utf-8
# module Autodesk.Revit.DB.Fabrication calls itself Fabrication
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DesignToFabricationConverter(object, IDisposable):
    """
    This class represents the MEP design to fabrication part convert tool.
    
    DesignToFabricationConverter(document: Document)
    """
    def Convert(self, selection, serviceId):
        """ Convert(self: DesignToFabricationConverter, selection: ISet[ElementId], serviceId: int) -> DesignToFabricationConverterResult """
        pass

    def Dispose(self):
        """ Dispose(self: DesignToFabricationConverter) """
        pass

    def GetConvertedFabricationParts(self):
        """
        GetConvertedFabricationParts(self: DesignToFabricationConverter) -> ISet[ElementId]
        
            Gets the set of element identifiers for newly created fabrication parts.
        """
        pass

    def GetConvertedFabricationPartsWithInvalidConnections(self):
        """
        GetConvertedFabricationPartsWithInvalidConnections(self: DesignToFabricationConverter) -> IDictionary[ElementId, ElementId]
        
            Gets the collection of converted fabrication parts with invalid connections.
        """
        pass

    def GetDesignElementAndFabricationPartsWithDifferentOffsets(self):
        """
        GetDesignElementAndFabricationPartsWithDifferentOffsets(self: DesignToFabricationConverter) -> IDictionary[ElementId, ISet[ElementId]]
        
            Gets the collection of design elements that failed to convert and the 
             associated set of fabrication parts with different offsets.
        
            Returns: A map of design element identifiers that were not converted and the associated 
             set fabrication parts left with different offsets.
        """
        pass

    def GetDesignElementAndFabricationPartsWithOpenConnectors(self):
        """
        GetDesignElementAndFabricationPartsWithOpenConnectors(self: DesignToFabricationConverter) -> IDictionary[ElementId, ISet[ElementId]]
        
            Gets the collection of design elements that failed to convert and the 
             associated set of fabrication parts with open connectors.
        
            Returns: A map of design element identifiers that were not converted and the associated 
             set fabrication parts left with open connectors.
        """
        pass

    def GetElementsWithOpenConnector(self):
        """
        GetElementsWithOpenConnector(self: DesignToFabricationConverter) -> ISet[ElementId]
        
            Gets the set of fabrication part or MEP design element identifiers with open 
             connectors, caused by fittings failing to convert.
        """
        pass

    def GetPartialConvertFailureResults(self):
        """
        GetPartialConvertFailureResults(self: DesignToFabricationConverter) -> IList[PartialFailureResults]
        
            Gets the partial failure results.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DesignToFabricationConverter, disposing: bool) """
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
    def __new__(self, document):
        """ __new__(cls: type, document: Document) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DesignToFabricationConverter) -> bool

"""



class DesignToFabricationConverterResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results from invoking the DesignToFabricationConverter.
    
    enum DesignToFabricationConverterResult, values: PartialFailure (1), Success (0)
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

    PartialFailure = None
    Success = None
    value__ = None


class FabricationPartFitResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Fabrication part stretch/fill result.
    
    enum FabricationPartFitResult, values: BadDimensions (4), DimensionLocked (3), IncompatibleConnection (7), IncompatibleGeometry (1), MisalignedEnds (2), OffsetRequired (8), ShapeMismatch (5), SizeMismatch (6), Success (0), Unsupported (255)
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

    BadDimensions = None
    DimensionLocked = None
    IncompatibleConnection = None
    IncompatibleGeometry = None
    MisalignedEnds = None
    OffsetRequired = None
    ShapeMismatch = None
    SizeMismatch = None
    Success = None
    Unsupported = None
    value__ = None


class FabricationPartRouteEnd(object, IDisposable):
    """ Class to hold fabrication part routing start or end information. """
    @staticmethod
    def CreateFromCenterline(element, ptAt):
        """
        CreateFromCenterline(element: Element, ptAt: XYZ) -> FabricationPartRouteEnd
        
            Create fabrication routing end from centreline point on straight element.
        
            element: The straight element that the centerline is on.
            ptAt: A point along the straight element where the fitting to be cut in should be 
             positioned.
        """
        pass

    @staticmethod
    def CreateFromConnector(connnector):
        """
        CreateFromConnector(connnector: Connector) -> FabricationPartRouteEnd
        
            Create fabrication routing end from connector end point.
        
            connnector: The connector that the route will connect to. Must not already be connected.
        """
        pass

    def Dispose(self):
        """ Dispose(self: FabricationPartRouteEnd) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FabricationPartRouteEnd, disposing: bool) """
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

Get: IsValidObject(self: FabricationPartRouteEnd) -> bool

"""



class FabricationUtils(object):
    """ General utility methods in the Autodesk Revit MEP product for fabrication. """
    @staticmethod
    def ValidateConnectivity(pAdoc, pConn1, pConn2):
        """
        ValidateConnectivity(pAdoc: Document, pConn1: Connector, pConn2: Connector) -> bool
        
            Check if two connectors are valid to connect directly without couplings
        
            pAdoc: The document.
            pConn1: First connector to check.
            pConn2: Second connector to check against.
            Returns: True if connection is valid, false otherwise.
        """
        pass

    __all__ = [
        'ValidateConnectivity',
    ]


class PartialFailureResults(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible results of the partial failure from invoking the DesignToFabricationConverter.
    
    enum PartialFailureResults, values: HaveDifferentOffsets (3), HaveOpenConnectors (2), InvalidConnections (1), NoMatchingSize (4), NotAllPartsConverted (0)
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

    HaveDifferentOffsets = None
    HaveOpenConnectors = None
    InvalidConnections = None
    NoMatchingSize = None
    NotAllPartsConverted = None
    value__ = None


class ValidationStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Lists the validation type of the fabrication part.
    
    enum ValidationStatus, values: InvalidDimensions (1), NoMaterial (2), Valid (0)
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

    InvalidDimensions = None
    NoMaterial = None
    Valid = None
    value__ = None


