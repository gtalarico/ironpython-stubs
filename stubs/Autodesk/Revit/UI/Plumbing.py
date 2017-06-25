# encoding: utf-8
# module Autodesk.Revit.UI.Plumbing calls itself Plumbing
# from RevitAPIUI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IPipeFittingAndAccessoryPressureDropUIServer(IExternalServer):
    """ Interface for external servers providing optional UI for pipe fitting and pipe accessory coefficient calculation. """
    def GetDBServerId(self):
        """
        GetDBServerId(self: IPipeFittingAndAccessoryPressureDropUIServer) -> Guid
        
            Returns the Id of the corresponding DB server for which this server provides an 
             optional UI.
        
            Returns: The Id of the DB server.
        """
        pass

    def ShowSettings(self, data):
        """
        ShowSettings(self: IPipeFittingAndAccessoryPressureDropUIServer, data: PipeFittingAndAccessoryPressureDropUIData) -> bool
        
            Shows the settings UI.
        
            data: The input data of the calculation.
            Returns: True if the user makes any changes in the UI, false otherwise.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PipeFittingAndAccessoryPressureDropUIData(object, IDisposable):
    """ The input and output data used by external UI servers for storing UI settings. """
    def Dispose(self):
        """ Dispose(self: PipeFittingAndAccessoryPressureDropUIData) """
        pass

    def GetUIDataItems(self):
        """
        GetUIDataItems(self: PipeFittingAndAccessoryPressureDropUIData) -> IList[PipeFittingAndAccessoryPressureDropUIDataItem]
        
            Gets all UI data items stored in the UI data.
            Returns: An array of UI data items.
        """
        pass

    def GetUnits(self):
        """
        GetUnits(self: PipeFittingAndAccessoryPressureDropUIData) -> Units
        
            Gets units.
            Returns: The Units object.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipeFittingAndAccessoryPressureDropUIData, disposing: bool) """
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

Get: IsValidObject(self: PipeFittingAndAccessoryPressureDropUIData) -> bool

"""



class PipeFittingAndAccessoryPressureDropUIDataItem(object, IDisposable):
    """ The input and output data used by external UI servers for initializing and storing the UI settings. """
    def Dispose(self):
        """ Dispose(self: PipeFittingAndAccessoryPressureDropUIDataItem) """
        pass

    def GetEntity(self):
        """
        GetEntity(self: PipeFittingAndAccessoryPressureDropUIDataItem) -> Entity
        
            Returns the entity set by UI server.
           or an invalid entity otherwise.
            Returns: The returned Entity.
        """
        pass

    def GetPipeFittingAndAccessoryData(self):
        """
        GetPipeFittingAndAccessoryData(self: PipeFittingAndAccessoryPressureDropUIDataItem) -> PipeFittingAndAccessoryData
        
            Gets the fitting data stored in the UI data item.
            Returns: The fitting data stored in the UI data item.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PipeFittingAndAccessoryPressureDropUIDataItem, disposing: bool) """
        pass

    def SetEntity(self, entity):
        """
        SetEntity(self: PipeFittingAndAccessoryPressureDropUIDataItem, entity: Entity)
            Stores the entity in the UI data item.
        
            entity: The Entity to be stored.
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PipeFittingAndAccessoryPressureDropUIDataItem) -> bool

"""



