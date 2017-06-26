class DockablePane(object, IDisposable):
    """
    A user interface pane that participates in Revit's docking window system.
    
    DockablePane(other: DockablePane)
    DockablePane(id: DockablePaneId)
    """
    def Dispose(self):
        """ Dispose(self: DockablePane) """
        pass

    def GetTitle(self):
        """
        GetTitle(self: DockablePane) -> str
        
            Returns the current title (a.k.a. window caption) of the dockable pane.
        """
        pass

    def Hide(self):
        """
        Hide(self: DockablePane)
            If the pane is on screen, hide it.  Has no effect on built-in Revit dockable 
             panes.
        """
        pass

    def IsShown(self):
        """
        IsShown(self: DockablePane) -> bool
        
            Identify the pane is currently visible or in a tab.
        """
        pass

    @staticmethod
    def PaneExists(id):
        """
        PaneExists(id: DockablePaneId) -> bool
        
            Returns true if %id% refers to a dockable pane window that currently exists in 
             the Revit user interface, whether it's hidden or shown.
        """
        pass

    @staticmethod
    def PaneIsBuiltIn(id):
        """
        PaneIsBuiltIn(id: DockablePaneId) -> bool
        
            Returns true if %id% refers to a built-in Revit dockable pane, rather than one 
             created by an add-in.
        """
        pass

    @staticmethod
    def PaneIsRegistered(id):
        """
        PaneIsRegistered(id: DockablePaneId) -> bool
        
            Returns true if %id% refers to a built-in Revit dockable pane, or an add-in 
             pane that has been properly registered with 
             %Autodesk.Revit.UI.UIApplication.RegisterDockablePane%.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DockablePane, disposing: bool) """
        pass

    def Show(self):
        """
        Show(self: DockablePane)
            If the pane is not currently visible or in a tab, display the pane in the Revit 
             user interface at its last docked location.
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
    def __new__(self, *__args):
        """
        __new__(cls: type, other: DockablePane)
        __new__(cls: type, id: DockablePaneId)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for this dockable pane.

Get: Id(self: DockablePane) -> DockablePaneId

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DockablePane) -> bool

"""


