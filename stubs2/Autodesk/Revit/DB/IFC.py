# encoding: utf-8
# module Autodesk.Revit.DB.IFC calls itself IFC
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IFCImportAction(Enum, IComparable, IFormattable, IConvertible):
    """
    The action of the IFC import.
    
    enum IFCImportAction, values: Link (1), Open (0)
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

    Link = None
    Open = None
    value__ = None


class IFCImportIntent(Enum, IComparable, IFormattable, IConvertible):
    """
    The intent of the IFC import.
    
    enum IFCImportIntent, values: Parametric (0), Reference (1)
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

    Parametric = None
    Reference = None
    value__ = None


class IFCImportOptions(object, IDisposable):
    """
    IFC Import options.
    
    IFCImportOptions()
    """
    def Dispose(self):
        """ Dispose(self: IFCImportOptions) """
        pass

    def GetConversionData(self):
        """
        GetConversionData(self: IFCImportOptions) -> LinkConversionData
        
            Get the data used in the creation of the associated Revit file for an IFC link 
             operation, if it exists.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: IFCImportOptions, disposing: bool) """
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

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The action of the import.

Get: Action(self: IFCImportOptions) -> IFCImportAction

Set: Action(self: IFCImportOptions) = value
"""

    AutocorrectOffAxisLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable or disable correcting lines that are slight off-axis.

Get: AutocorrectOffAxisLines(self: IFCImportOptions) -> bool

Set: AutocorrectOffAxisLines(self: IFCImportOptions) = value
"""

    AutoJoin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enable or disable auto-join at the end of import.

Get: AutoJoin(self: IFCImportOptions) -> bool

Set: AutoJoin(self: IFCImportOptions) = value
"""

    CreateLinkInstanceOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether to create a linked symbol element or not.

Get: CreateLinkInstanceOnly(self: IFCImportOptions) -> bool

Set: CreateLinkInstanceOnly(self: IFCImportOptions) = value
"""

    ForceImport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Force the IFC file to be imported regardless of an existing corresponding Revit file.

Get: ForceImport(self: IFCImportOptions) -> bool

Set: ForceImport(self: IFCImportOptions) = value
"""

    Intent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The intent of the import.

Get: Intent(self: IFCImportOptions) -> IFCImportIntent

Set: Intent(self: IFCImportOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: IFCImportOptions) -> bool

"""

    RevitLinkFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full path of the intermediate Revit file created during a previous link action.
   This is used during "Reload From" to determine the path to the previous generated Revit file.

Get: RevitLinkFileName(self: IFCImportOptions) -> str

Set: RevitLinkFileName(self: IFCImportOptions) = value
"""



