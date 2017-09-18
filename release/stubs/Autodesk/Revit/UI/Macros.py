# encoding: utf-8
# module Autodesk.Revit.UI.Macros calls itself Macros
# from RevitAPIUI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationEntryPoint(UIApplication, IDisposable, IEntryPoint):
    """
    For Revit Macros use only.
    
    ApplicationEntryPoint()
    """
    def CreateRibbonPanel(self, *__args):
        """
        CreateRibbonPanel(self: ApplicationEntryPoint, tabName: str, panelName: str) -> RibbonPanel
        CreateRibbonPanel(self: ApplicationEntryPoint, panelName: str) -> RibbonPanel
        CreateRibbonPanel(self: ApplicationEntryPoint, tab: Tab, panelName: str) -> RibbonPanel
        """
        pass

    def CreateRibbonTab(self, tabName):
        """ CreateRibbonTab(self: ApplicationEntryPoint, tabName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: UIApplication, A_0: bool) """
        pass

    def FinishInitialization(self, *args): #cannot find CLR method
        """ FinishInitialization(self: ApplicationEntryPoint) """
        pass

    def FinishInitializationEO(self):
        """
        FinishInitializationEO(self: ApplicationEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def GetRibbonPanels(self, *__args):
        """
        GetRibbonPanels(self: ApplicationEntryPoint) -> List[RibbonPanel]
        GetRibbonPanels(self: ApplicationEntryPoint, tab: Tab) -> List[RibbonPanel]
        GetRibbonPanels(self: ApplicationEntryPoint, tabName: str) -> List[RibbonPanel]
        """
        pass

    def Initialize(self, obj, addinFolder):
        """
        Initialize(self: ApplicationEntryPoint, obj: object, addinFolder: str)
            For Revit Macros internal use only.
        """
        pass

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: ApplicationEntryPoint) """
        pass

    def OnShutdownEO(self):
        """
        OnShutdownEO(self: ApplicationEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UIApplication, disposing: bool) """
        pass

    def setNativeUIApplication(self, *args): #cannot find CLR method
        """ setNativeUIApplication(self: UIApplication, uiApp: UIApplication*) """
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

    AddinFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full path to the Revit Macros module.

Get: AddinFolder(self: ApplicationEntryPoint) -> str

"""

    PrimaryCookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DocumentEntryPoint(UIDocument, IDisposable, IEntryPoint):
    """
    For Revit Macros use only.
    
    DocumentEntryPoint()
    """
    def Dispose(self):
        """ Dispose(self: UIDocument, A_0: bool) """
        pass

    def FinishInitialization(self, *args): #cannot find CLR method
        """ FinishInitialization(self: DocumentEntryPoint) """
        pass

    def FinishInitializationEO(self):
        """
        FinishInitializationEO(self: DocumentEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def Initialize(self, obj, addinFolder):
        """
        Initialize(self: DocumentEntryPoint, obj: object, addinFolder: str)
            For Revit Macros internal use only.
        """
        pass

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: DocumentEntryPoint) """
        pass

    def OnShutdownEO(self):
        """
        OnShutdownEO(self: DocumentEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UIDocument, disposing: bool) """
        pass

    def setUIDocument(self, *args): #cannot find CLR method
        """ setUIDocument(self: UIDocument, pUIDocument: UIDocument*) """
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

    AddinFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full path to the Revit Macros module.

Get: AddinFolder(self: DocumentEntryPoint) -> str

"""

    PrimaryCookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



