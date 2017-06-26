class UIApplication(object, IDisposable):
    """
    Represents an active session of the Autodesk Revit user interface, providing access to
       UI customization methods, events, and the active document.
    
    UIApplication(revitApp: Application)
    """
    def CanPostCommand(self, commandId):
        """
        CanPostCommand(self: UIApplication, commandId: RevitCommandId) -> bool
        
            Identifies if the given command can be posted, using 
             Autodesk.Revit.UI.UIApplication.PostCommand(Autodesk.Revit.UI.RevitCommandId).
        
        
            commandId: The command Id.
        """
        pass

    def CreateAddInCommandBinding(self, revitCommandId):
        """
        CreateAddInCommandBinding(self: UIApplication, revitCommandId: RevitCommandId) -> AddInCommandBinding
        
            Creates a new AddInCommandBinding.
        
            revitCommandId: The Revit command id to identify the command handler you want to replace.
        """
        pass

    def CreateRibbonPanel(self, *__args):
        """
        CreateRibbonPanel(self: UIApplication, tabName: str, panelName: str) -> RibbonPanel
        
            Create a new RibbonPanel on the specified tab.
        
            tabName: The name of the tab, on which the new panel will be created.
            panelName: The name of the panel to be created.
        CreateRibbonPanel(self: UIApplication, panelName: str) -> RibbonPanel
        
            Create a new RibbonPanel on the Add-Ins tab.
        
            panelName: The name of the panel to be created.
        CreateRibbonPanel(self: UIApplication, tab: Tab, panelName: str) -> RibbonPanel
        
            Create a new RibbonPanel on the designated standard Revit tab.
        
            tab: The target tab, on which the new panel will be created.
            panelName: The name of the panel to be created.
        """
        pass

    def CreateRibbonTab(self, tabName):
        """
        CreateRibbonTab(self: UIApplication, tabName: str)
            Creates a new tab on the Revit user interface.
        
            tabName: The name of the tab to be created.
        """
        pass

    def Dispose(self):
        """ Dispose(self: UIApplication) """
        pass

    @staticmethod
    def DoDragDrop(dropData, handler=None):
        """
        DoDragDrop(dropData: ICollection[str])DoDragDrop(dropData: object, handler: IDropHandler)
            Initiates a drag and drop operation with a custom drop implementation.
        
            dropData: Any arbitrary data to be passed to the drop handler when the drop occurs.
            handler: The handler to be executed when the drop occurs.
        """
        pass

    def GetDockablePane(self, id):
        """
        GetDockablePane(self: UIApplication, id: DockablePaneId) -> DockablePane
        
            Gets a DockablePane object by its ID.
        
            id: Unique identifier for the new pane.
        """
        pass

    def GetRibbonPanels(self, *__args):
        """
        GetRibbonPanels(self: UIApplication) -> List[RibbonPanel]
        
            Get all the custom Panels on Add-Ins tab of Revit.
        GetRibbonPanels(self: UIApplication, tab: Tab) -> List[RibbonPanel]
        
            Get all the custom Panels on a designated standard Revit tab.
        
            tab: The tab on which the panels are located.
        GetRibbonPanels(self: UIApplication, tabName: str) -> List[RibbonPanel]
        
            Get all the custom Panels on a designated Revit tab.
        
            tabName: The name of the tab on which the panels are located.
        """
        pass

    def LoadAddIn(self, fileName):
        """
        LoadAddIn(self: UIApplication, fileName: str)
            Loads add-ins from the given manifest file.
        
            fileName: The name of the add-in manifest file including the extension is to identify the 
             
        manifest file which contains Revit add-ins.
        """
        pass

    def LoadPackageContents(self, packageContentsPath):
        """
        LoadPackageContents(self: UIApplication, packageContentsPath: str)
            Loads add-ins from the given packageContents.xml file.
        
            packageContentsPath: The name of package contents file
        """
        pass

    def OpenAndActivateDocument(self, *__args):
        """
        OpenAndActivateDocument(self: UIApplication, fileName: str) -> UIDocument
        
            Opens and activates a Revit document.
        
            fileName: A full path to a revit file to be opened.
           The file can be either a Revit 
             project, template, or family document.
        
        OpenAndActivateDocument(self: UIApplication, modelPath: ModelPath, openOptions: OpenOptions, bDetachAndPrompt: bool) -> UIDocument
        
            Opens and activates a Revit document.
        
            modelPath: A path to a revit file to be opened.
           The file can be either a Revit 
             project, template, or family document.
        
            openOptions: Options for opening the file.
            bDetachAndPrompt: True means if openOptions specifies DoNotDetach,
           then for workshared models 
             detach from central and query the user whether to preserve or discard worksets.
        """
        pass

    def PostCommand(self, commandId):
        """
        PostCommand(self: UIApplication, commandId: RevitCommandId)
            Posts the command to the Revit message queue to be invoked when control returns 
             from the current API context.
        
        
            commandId: The command Id.
        """
        pass

    def RegisterDockablePane(self, id, title, provider):
        """
        RegisterDockablePane(self: UIApplication, id: DockablePaneId, title: str, provider: IDockablePaneProvider)
            Adds a new dockable pane to the Revit user interface.
        
            id: Unique identifier for the new pane.
            title: String to use for the pane caption.
            provider: Your add-in's implementation of the IDockablePaneProvider interface.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UIApplication, disposing: bool) """
        pass

    def RemoveAddInCommandBinding(self, revitCommandId):
        """
        RemoveAddInCommandBinding(self: UIApplication, revitCommandId: RevitCommandId)
            Removes an AddInCommandBinding.
        
            revitCommandId: The Revit command id to identify the command handler you want to remove the 
             binding.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, revitApp):
        """
        __new__(cls: type)
        __new__(cls: type, revitApp: Application)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveAddInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get current active external application or external command id.

Get: ActiveAddInId(self: UIApplication) -> AddInId

"""

    ActiveUIDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides access to an object that represents the currently active project.

Get: ActiveUIDocument(self: UIApplication) -> UIDocument

"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the database level Application represented by this UI level Application.

Get: Application(self: UIApplication) -> Application

"""

    DrawingAreaExtents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the rectangle that represents the screen pixel coordinates of drawing area.

Get: DrawingAreaExtents(self: UIApplication) -> Rectangle

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: UIApplication) -> bool

"""

    LoadedApplications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns an array of successfully loaded external applications.

Get: LoadedApplications(self: UIApplication) -> ExternalApplicationArray

"""

    MainWindowExtents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the rectangle that represents the screen pixel coordinates of Revit main window.

Get: MainWindowExtents(self: UIApplication) -> Rectangle

"""


    ApplicationClosing = None
    DialogBoxShowing = None
    DisplayingOptionsDialog = None
    DockableFrameFocusChanged = None
    DockableFrameVisibilityChanged = None
    FabricationPartBrowserChanged = None
    Idling = None
    ViewActivated = None
    ViewActivating = None

