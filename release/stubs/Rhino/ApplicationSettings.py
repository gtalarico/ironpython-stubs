# encoding: utf-8
# module Rhino.ApplicationSettings calls itself ApplicationSettings
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AppearanceSettings(object):
    """ Provides static methods and properties to deal with the appearance of the application. """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> AppearanceSettingsState
        
            Gets the current settings of the application.
            Returns: An instance of a class that represents all the settings as they appear in the Rhino _Options 
             dialog,
                    joined in a single class.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> AppearanceSettingsState
        
            Gets the factory settings of the application.
            Returns: An instance of a class that represents all the default settings joined together.
        """
        pass

    @staticmethod
    def GetPaintColor(whichColor):
        """
        GetPaintColor(whichColor: PaintColor) -> Color
        
            Gets the .Net library color that is currently associated with a paint color.
        
            whichColor: A color association.
            Returns: A .Net library color.
        """
        pass

    @staticmethod
    def InitialMainWindowState(bounds, state):
        """
        InitialMainWindowState() -> (bool, Rectangle, FormWindowState)
        
            Location where the Main Rhino window attempts to show when the application is first
                    
             started.
        
            Returns: false if the information could not be retrieved.
        """
        pass

    @staticmethod
    def RestoreDefaults():
        """
        RestoreDefaults()
            Commits the default settings as the current settings.
        """
        pass

    @staticmethod
    def SetPaintColor(whichColor, c, forceUiUpdate=None):
        """
        SetPaintColor(whichColor: PaintColor, c: Color, forceUiUpdate: bool)
            Sets the logical paint color association to a spacific .Net library color.
        
            whichColor: A logical color association.
            c: A .Net library color.
            forceUiUpdate: true if the UI should be forced to update.
        SetPaintColor(whichColor: PaintColor, c: Color)
            Sets the logical paint color association to a spacific .Net library color, without forced UI 
             update.
        
        
            whichColor: A logical color association.
            c: A .Net library color.
        """
        pass

    @staticmethod
    def UpdateFromState(state):
        """
        UpdateFromState(state: AppearanceSettingsState)
            Sets all settings to a particular defined joined state.
        
            state: A joined settings object.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
        'GetPaintColor',
        'InitialMainWindowState',
        'RestoreDefaults',
        'SetPaintColor',
        'UpdateFromState',
    ]


class AppearanceSettingsState(object):
    """ Represents a snapshot of the values in Rhino.ApplicationSettings.AppearanceSettings. """
    CommandPromptBackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the comand prompt background color.

Get: CommandPromptBackgroundColor(self: AppearanceSettingsState) -> Color

Set: CommandPromptBackgroundColor(self: AppearanceSettingsState) = value
"""

    CommandPromptHypertextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the comand prompt hypertext color.

Get: CommandPromptHypertextColor(self: AppearanceSettingsState) -> Color

Set: CommandPromptHypertextColor(self: AppearanceSettingsState) = value
"""

    CommandPromptTextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the command prompt text color.

Get: CommandPromptTextColor(self: AppearanceSettingsState) -> Color

Set: CommandPromptTextColor(self: AppearanceSettingsState) = value
"""

    CrosshairColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the crosshair color.

Get: CrosshairColor(self: AppearanceSettingsState) -> Color

Set: CrosshairColor(self: AppearanceSettingsState) = value
"""

    CurrentLayerBackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color used by the layer manager dialog as the background color for the current layer.

Get: CurrentLayerBackgroundColor(self: AppearanceSettingsState) -> Color

Set: CurrentLayerBackgroundColor(self: AppearanceSettingsState) = value
"""

    DefaultFontFaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the default font face.

Get: DefaultFontFaceName(self: AppearanceSettingsState) -> str

Set: DefaultFontFaceName(self: AppearanceSettingsState) = value
"""

    DefaultLayerColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default layer color.

Get: DefaultLayerColor(self: AppearanceSettingsState) -> Color

Set: DefaultLayerColor(self: AppearanceSettingsState) = value
"""

    DefaultObjectColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default object color.

Get: DefaultObjectColor(self: AppearanceSettingsState) -> Color

Set: DefaultObjectColor(self: AppearanceSettingsState) = value
"""

    EchoCommandsToHistoryWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines if command names are written to the history window.

Get: EchoCommandsToHistoryWindow(self: AppearanceSettingsState) -> bool

Set: EchoCommandsToHistoryWindow(self: AppearanceSettingsState) = value
"""

    EchoPromptsToHistoryWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines if prompt messages are written to the history window.

Get: EchoPromptsToHistoryWindow(self: AppearanceSettingsState) -> bool

Set: EchoPromptsToHistoryWindow(self: AppearanceSettingsState) = value
"""

    FeedbackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the feedback color.

Get: FeedbackColor(self: AppearanceSettingsState) -> Color

Set: FeedbackColor(self: AppearanceSettingsState) = value
"""

    FrameBackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the frame background color.

Get: FrameBackgroundColor(self: AppearanceSettingsState) -> Color

Set: FrameBackgroundColor(self: AppearanceSettingsState) = value
"""

    GridThickLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the thick line in the grid.

Get: GridThickLineColor(self: AppearanceSettingsState) -> Color

Set: GridThickLineColor(self: AppearanceSettingsState) = value
"""

    GridThinLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the thin line in the grid.

Get: GridThinLineColor(self: AppearanceSettingsState) -> Color

Set: GridThinLineColor(self: AppearanceSettingsState) = value
"""

    GridXAxisLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of X axis line in the grid.

Get: GridXAxisLineColor(self: AppearanceSettingsState) -> Color

Set: GridXAxisLineColor(self: AppearanceSettingsState) = value
"""

    GridYAxisLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of Y axis line in the grid.

Get: GridYAxisLineColor(self: AppearanceSettingsState) -> Color

Set: GridYAxisLineColor(self: AppearanceSettingsState) = value
"""

    GridZAxisLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of Z axis line in the grid.

Get: GridZAxisLineColor(self: AppearanceSettingsState) -> Color

Set: GridZAxisLineColor(self: AppearanceSettingsState) = value
"""

    LockedObjectColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color used to draw locked objects.

Get: LockedObjectColor(self: AppearanceSettingsState) -> Color

Set: LockedObjectColor(self: AppearanceSettingsState) = value
"""

    PageviewPaperColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CRhinoPageView paper background. A rectangle is drawn into the background
            of page views to represent the printed area. The alpha portion of the color
            is used to draw the paper blended into the background

Get: PageviewPaperColor(self: AppearanceSettingsState) -> Color

Set: PageviewPaperColor(self: AppearanceSettingsState) = value
"""

    SelectedObjectColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color used to draw selected objects.
            The default is yellow, but this can be customized by the user.

Get: SelectedObjectColor(self: AppearanceSettingsState) -> Color

Set: SelectedObjectColor(self: AppearanceSettingsState) = value
"""

    ShowCrosshairs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines if cross hairs are visible.

Get: ShowCrosshairs(self: AppearanceSettingsState) -> bool

Set: ShowCrosshairs(self: AppearanceSettingsState) = value
"""

    ShowFullPathInTitleBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines if the full path of the document is shown in the Rhino title bar.

Get: ShowFullPathInTitleBar(self: AppearanceSettingsState) -> bool

Set: ShowFullPathInTitleBar(self: AppearanceSettingsState) = value
"""

    TrackingColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the tracking color.

Get: TrackingColor(self: AppearanceSettingsState) -> Color

Set: TrackingColor(self: AppearanceSettingsState) = value
"""

    ViewportBackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the viewport background color.

Get: ViewportBackgroundColor(self: AppearanceSettingsState) -> Color

Set: ViewportBackgroundColor(self: AppearanceSettingsState) = value
"""

    WorldCoordIconXAxisColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the world X axis of the world coordinates icon,
            appearing usually bottom left in viewports.

Get: WorldCoordIconXAxisColor(self: AppearanceSettingsState) -> Color

Set: WorldCoordIconXAxisColor(self: AppearanceSettingsState) = value
"""

    WorldCoordIconYAxisColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the world Y axis of the world coordinate icon,
            appearing usually bottom left in viewports.

Get: WorldCoordIconYAxisColor(self: AppearanceSettingsState) -> Color

Set: WorldCoordIconYAxisColor(self: AppearanceSettingsState) = value
"""

    WorldCoordIconZAxisColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the color of the world Z axis of the world coordinate icon,
            appearing usually bottom left in viewports.

Get: WorldCoordIconZAxisColor(self: AppearanceSettingsState) -> Color

Set: WorldCoordIconZAxisColor(self: AppearanceSettingsState) = value
"""



class ClipboardState(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values for diferent behaviour that is related to clipboard data.
    
    enum ClipboardState, values: DeleteData (1), KeepData (0), PromptWhenBig (2)
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

    DeleteData = None
    KeepData = None
    PromptWhenBig = None
    value__ = None


class CommandAliasList(object):
    """ Contains static methods and properties to access command aliases. """
    @staticmethod
    def Add(alias, macro):
        """
        Add(alias: str, macro: str) -> bool
        
            Adds a new command alias to Rhino.
        
            alias: [in] The name of the command alias.
            macro: [in] The command macro to run when the alias is executed.
            Returns: true if successful.
        """
        pass

    @staticmethod
    def Clear():
        """
        Clear()
            Removes all aliases from the list.
        """
        pass

    @staticmethod
    def Delete(alias):
        """
        Delete(alias: str) -> bool
        
            Deletes an existing command alias from Rhino.
        
            alias: [in] The name of the command alias.
            Returns: true if successful.
        """
        pass

    @staticmethod
    def GetDefaults():
        """
        GetDefaults() -> Dictionary[str, str]
        
            Constructs a dictionary containing as keys the default names and as value the default macro.
           
                      The returned dicionary contains a copy of the settings.
        
            Returns: A new dictionary with the default name/macro combinantions.
        """
        pass

    @staticmethod
    def GetMacro(alias):
        """
        GetMacro(alias: str) -> str
        
            Returns the macro of a command alias.
        
            alias: [in] The name of the command alias.
        """
        pass

    @staticmethod
    def GetNames():
        """
        GetNames() -> Array[str]
        
            Returns a list of command alias names.
            Returns: An array of strings. This can be empty.
        """
        pass

    @staticmethod
    def IsAlias(alias):
        """
        IsAlias(alias: str) -> bool
        
            Verifies that a command alias exists in Rhino.
        
            alias: [in] The name of the command alias.
            Returns: true if the alias exists.
        """
        pass

    @staticmethod
    def IsDefault():
        """
        IsDefault() -> bool
        
            Computes a value indicating if the current alias list is the same as the default alias list.
            Returns: true if the current alias list is exactly equal to the default alias list; false otherwise.
        """
        pass

    @staticmethod
    def SetMacro(alias, macro):
        """
        SetMacro(alias: str, macro: str) -> bool
        
            Modifies the macro of a command alias.
        
            alias: [in] The name of the command alias.
            macro: [in] The new command macro to run when the alias is executed.
            Returns: true if successful.
        """
        pass

    @staticmethod
    def ToDictionary():
        """
        ToDictionary() -> Dictionary[str, str]
        
            Constructs a new dictionary that contains: as keys all names and as values all macros.
                 
                Modifications to this dictionary do not affect any Rhino command alias.
        
            Returns: The new dictionary.
        """
        pass

    __all__ = [
        'Add',
        'Clear',
        'Delete',
        'GetDefaults',
        'GetMacro',
        'GetNames',
        'IsAlias',
        'IsDefault',
        'SetMacro',
        'ToDictionary',
    ]


class CommandPromptPosition(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values for default positions of the command prompt inside the frame of the full editor window.
    
    enum CommandPromptPosition, values: Bottom (1), Floating (2), Hidden (3), Top (0)
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

    Bottom = None
    Floating = None
    Hidden = None
    Top = None
    value__ = None


class CursorMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values for particular OSnap cursor colors.
    
    enum CursorMode, values: BlackOnWhite (1), None (0), WhiteOnBlack (2)
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

    BlackOnWhite = None
    None = None
    value__ = None
    WhiteOnBlack = None


class CursorTooltipSettings(object):
    """
    Cursor tooltips place information at the cursor location.
                Note: Turning on cursor tooltips turns off object snap cursors.
    """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> CursorTooltipSettingsState
        
            Gets the current settings.
            Returns: A new cursor tooltip state with current settings.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> CursorTooltipSettingsState
        
            Gets the cursor tooltip factory settings.
            Returns: A new cursor tooltip state with factory settings.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
    ]


class CursorTooltipSettingsState(object):
    """
    Represents a snapshot of Rhino.ApplicationSettings.CursorTooltipSettings.
    
    CursorTooltipSettingsState()
    """
    AutoSuppress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Attempts to display only the most useful tooltip.

Get: AutoSuppress(self: CursorTooltipSettingsState) -> bool

Set: AutoSuppress(self: CursorTooltipSettingsState) = value
"""

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tooltip background color.

Get: BackgroundColor(self: CursorTooltipSettingsState) -> Color

Set: BackgroundColor(self: CursorTooltipSettingsState) = value
"""

    CommandPromptPane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Displays the current command prompt.

Get: CommandPromptPane(self: CursorTooltipSettingsState) -> bool

Set: CommandPromptPane(self: CursorTooltipSettingsState) = value
"""

    DistancePane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Displays the distance from the last picked point.

Get: DistancePane(self: CursorTooltipSettingsState) -> bool

Set: DistancePane(self: CursorTooltipSettingsState) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The x and y distances in pixels from the cursor location to the tooltip.

Get: Offset(self: CursorTooltipSettingsState) -> Point

Set: Offset(self: CursorTooltipSettingsState) = value
"""

    OsnapPane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Displays the current object snap selection.

Get: OsnapPane(self: CursorTooltipSettingsState) -> bool

Set: OsnapPane(self: CursorTooltipSettingsState) = value
"""

    PointPane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Displays the current construction plane coordinates.

Get: PointPane(self: CursorTooltipSettingsState) -> bool

Set: PointPane(self: CursorTooltipSettingsState) = value
"""

    RelativePointPane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Displays the relative construction plane coordinates and angle from the last picked point.

Get: RelativePointPane(self: CursorTooltipSettingsState) -> bool

Set: RelativePointPane(self: CursorTooltipSettingsState) = value
"""

    TextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tooltip text color.

Get: TextColor(self: CursorTooltipSettingsState) -> Color

Set: TextColor(self: CursorTooltipSettingsState) = value
"""

    TooltipsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Turns on/off cursor tooltips.

Get: TooltipsEnabled(self: CursorTooltipSettingsState) -> bool

Set: TooltipsEnabled(self: CursorTooltipSettingsState) = value
"""



class EdgeAnalysisSettings(object):
    """ Contains static methods and properties to modify the visitbility of edges in edge-related commands. """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> EdgeAnalysisSettingsState
        
            Gets the current settings of the application.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> EdgeAnalysisSettingsState
        
            Gets the factory settings of the application.
        """
        pass

    @staticmethod
    def RestoreDefaults():
        """
        RestoreDefaults()
            Commits the default settings as the current settings.
        """
        pass

    @staticmethod
    def UpdateFromState(state):
        """
        UpdateFromState(state: EdgeAnalysisSettingsState)
            Sets all settings to a particular defined joined state.
        
            state: The particular state.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
        'RestoreDefaults',
        'UpdateFromState',
    ]


class EdgeAnalysisSettingsState(object):
    """ Represents a snapshot of Rhino.ApplicationSettings.EdgeAnalysisSettings. """
    ShowEdgeColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a color used to enhance display edges in commands like _ShowEdges and _ShowNakedEdges.

Get: ShowEdgeColor(self: EdgeAnalysisSettingsState) -> Color

Set: ShowEdgeColor(self: EdgeAnalysisSettingsState) = value
"""

    ShowEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value referring to the group of edges that are targeted.
            0 = all.1 = naked.2 = non-manifold.

Get: ShowEdges(self: EdgeAnalysisSettingsState) -> int

Set: ShowEdges(self: EdgeAnalysisSettingsState) = value
"""



class FileSettings(object):
    """ Contains static methods and properties relating Rhino files. """
    @staticmethod
    def AddSearchPath(folder, index):
        """
        AddSearchPath(folder: str, index: int) -> int
        
            Adds a new imagePath to Rhino's search imagePath list.
                     See "Options Files 
             settings" in the Rhino help file for more details.
        
        
            folder: [in] The valid folder, or imagePath, to add.
            index: [in] A zero-based position index in the search imagePath list to insert the string.
                    
              If -1, the imagePath will be appended to the end of the list.
        
            Returns: The index where the item was inserted if success.
                     -1 on failure.
        """
        pass

    @staticmethod
    def AutoSaveBeforeCommands():
        """
        AutoSaveBeforeCommands() -> Array[str]
        
            Input list of commands that force AutoSave prior to running.
        """
        pass

    @staticmethod
    def DeleteSearchPath(folder):
        """
        DeleteSearchPath(folder: str) -> bool
        
            Removes an existing imagePath from Rhino's search imagePath list.
                    See "Options 
             Files settings" in the Rhino help file for more details.
        
        
            folder: [in] The valid folder, or imagePath, to remove.
            Returns: true or false indicating success or failure.
        """
        pass

    @staticmethod
    def FindFile(fileName):
        """
        FindFile(fileName: str) -> str
        
            Searches for a file using Rhino's search imagePath. Rhino will look for a file in the following 
             locations:
                    1. The current document's folder.
                    2. Folder's specified in 
             Options dialog, File tab.
                    3. Rhino's System folders.
        
        
            fileName: short file name to search for.
            Returns: full imagePath on success; null on error.
        """
        pass

    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> FileSettingsState
        
            Returns the current state.
            Returns: A new instance containing the current state.
        """
        pass

    @staticmethod
    def GetDataFolder(currentUser):
        """
        GetDataFolder(currentUser: bool) -> str
        
            Gets the data folder for machine or current user.
        
            currentUser: true if the query relates to the current user.
            Returns: A directory to user or machine data.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> FileSettingsState
        
            Returns the default state.
            Returns: A new instance containing the default state.
        """
        pass

    @staticmethod
    def GetSearchPaths():
        """
        GetSearchPaths() -> Array[str]
        
            Returns all of the imagePath items in Rhino's search imagePath list. See "Options Files 
             settings" in the Rhino help file for more details.
        """
        pass

    @staticmethod
    def RecentlyOpenedFiles():
        """
        RecentlyOpenedFiles() -> Array[str]
        
            Returns a list of recently opened files. Note that this function does not
                    check to 
             make sure that these files still exist.
        
            Returns: An array of strings with the paths to the recently opened files.
        """
        pass

    @staticmethod
    def SetAutoSaveBeforeCommands(commands):
        """
        SetAutoSaveBeforeCommands(commands: Array[str])
            Set list of commands that force AutoSave prior to running.
        """
        pass

    __all__ = [
        'AddSearchPath',
        'AutoSaveBeforeCommands',
        'DeleteSearchPath',
        'FindFile',
        'GetCurrentState',
        'GetDataFolder',
        'GetDefaultState',
        'GetSearchPaths',
        'RecentlyOpenedFiles',
        'SetAutoSaveBeforeCommands',
    ]


class FileSettingsState(object):
    """ Represents a snapshot of Rhino.ApplicationSettings.FileSettings. """
    AutoSaveEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enables or disables Rhino's automatic file saving mechanism.

Get: AutoSaveEnabled(self: FileSettingsState) -> bool

Set: AutoSaveEnabled(self: FileSettingsState) = value
"""

    AutoSaveInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How often the document will be saved when Rhino's automatic file saving mechanism is enabled.

Get: AutoSaveInterval(self: FileSettingsState) -> TimeSpan

Set: AutoSaveInterval(self: FileSettingsState) = value
"""

    AutoSaveMeshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Saves render and display meshes in autosave file.

Get: AutoSaveMeshes(self: FileSettingsState) -> bool

Set: AutoSaveMeshes(self: FileSettingsState) = value
"""

    ClipboardCopyToPreviousRhinoVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that decides if copies to the clipboard are performed in both the current
            and previous Rhino clipboard formats.  This means you will double the size of what is saved in
            the clipboard but will be able to copy from the current to the previous version using the
            clipboard.

Get: ClipboardCopyToPreviousRhinoVersion(self: FileSettingsState) -> bool

Set: ClipboardCopyToPreviousRhinoVersion(self: FileSettingsState) = value
"""

    ClipboardOnExit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines what to do with clipboad data on exit.

Get: ClipboardOnExit(self: FileSettingsState) -> ClipboardState

Set: ClipboardOnExit(self: FileSettingsState) = value
"""

    CreateBackupFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to create backup files.

Get: CreateBackupFiles(self: FileSettingsState) -> bool

Set: CreateBackupFiles(self: FileSettingsState) = value
"""

    FileLockingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ensures that only one person at a time can have a file open for saving.

Get: FileLockingEnabled(self: FileSettingsState) -> bool

Set: FileLockingEnabled(self: FileSettingsState) = value
"""

    FileLockingOpenWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Displays an information dialog which identifies computer file is open on.

Get: FileLockingOpenWarning(self: FileSettingsState) -> bool

Set: FileLockingOpenWarning(self: FileSettingsState) = value
"""

    SaveViewChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true for users who consider view changes a document change.

Get: SaveViewChanges(self: FileSettingsState) -> bool

Set: SaveViewChanges(self: FileSettingsState) = value
"""



class GeneralSettings(object):
    """ Contains static methods and properties to give access to Rhinoceros settings. """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> GeneralSettingsState
        
            Gets the current settings.
            Returns: A new general state with current settings.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> GeneralSettingsState
        
            Gets the factory settings.
            Returns: A new general state with factory settings.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
    ]


class GeneralSettingsState(object):
    """ Represents a snapshot of Rhino.ApplicationSettings.GeneralSettings. """
    AutoUpdateCommandHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the command help dialog auto-update feature.

Get: AutoUpdateCommandHelp(self: GeneralSettingsState) -> bool

Set: AutoUpdateCommandHelp(self: GeneralSettingsState) = value
"""

    ContextMenuDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the time to wait before permitting context menu display.

Get: ContextMenuDelay(self: GeneralSettingsState) -> TimeSpan

Set: ContextMenuDelay(self: GeneralSettingsState) = value
"""

    EnableContextMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if right mouse down + delay will pop up context menu on a mouse up if no move happens.

Get: EnableContextMenu(self: GeneralSettingsState) -> bool

Set: EnableContextMenu(self: GeneralSettingsState) = value
"""

    MaximumPopupMenuLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of popup menu lines.

Get: MaximumPopupMenuLines(self: GeneralSettingsState) -> int

Set: MaximumPopupMenuLines(self: GeneralSettingsState) = value
"""

    MaximumUndoMemoryMb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum undo memory Mb.
            Undo records will be purged if there are more than MinimumUndoSteps and
            they use more than MaximumUndoMemoryMb.

Get: MaximumUndoMemoryMb(self: GeneralSettingsState) -> int

Set: MaximumUndoMemoryMb(self: GeneralSettingsState) = value
"""

    MiddleMouseMacro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the toolbar to popup when the middle mouse is clicked on
            a view, this value is only used when MiddleMouseMode is set to
            PopupToolbar.

Get: MiddleMouseMacro(self: GeneralSettingsState) -> str

Set: MiddleMouseMacro(self: GeneralSettingsState) = value
"""

    MiddleMouseMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets what happens when the user clicks the middle mouse.

Get: MiddleMouseMode(self: GeneralSettingsState) -> MiddleMouseMode

Set: MiddleMouseMode(self: GeneralSettingsState) = value
"""

    MiddleMousePopupToolbar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the toolbar to popup when the middle mouse is clicked on
            a view, this value is only used when MiddleMouseMode is set to
            PopupToolbar.

Get: MiddleMousePopupToolbar(self: GeneralSettingsState) -> str

Set: MiddleMousePopupToolbar(self: GeneralSettingsState) = value
"""

    MinimumUndoSteps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum undo steps.
            Undo records will be purged if there are more than MinimumUndoSteps and
            they use more than MaximumUndoMemoryMb.

Get: MinimumUndoSteps(self: GeneralSettingsState) -> int

Set: MinimumUndoSteps(self: GeneralSettingsState) = value
"""

    MouseSelectMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current selection mode.

Get: MouseSelectMode(self: GeneralSettingsState) -> MouseSelectMode

Set: MouseSelectMode(self: GeneralSettingsState) = value
"""

    NewObjectIsoparmCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of isoparm curves to show on new objects.

Get: NewObjectIsoparmCount(self: GeneralSettingsState) -> int

Set: NewObjectIsoparmCount(self: GeneralSettingsState) = value
"""



class HistorySettings(object):
    """ Provides static (Shared in Vb.Net) properties to modify Rhino History settings. """
    __all__ = []


class Installation(Enum, IComparable, IFormattable, IConvertible):
    """
    The type of Rhino executable that is executing
    
    enum Installation, values: Beta (6), BetaLab (7), Commercial (1), Corporate (9), Educational (2), EducationalLab (3), Evaluation (8), EvaluationTimed (10), NotForResale (4), NotForResaleLab (5), Undefined (0)
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

    Beta = None
    BetaLab = None
    Commercial = None
    Corporate = None
    Educational = None
    EducationalLab = None
    Evaluation = None
    EvaluationTimed = None
    NotForResale = None
    NotForResaleLab = None
    Undefined = None
    value__ = None


class LicenseNode(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides enumerated constant values for license node types.
    
    enum LicenseNode, values: Network (1), NetworkCheckedOut (2), Standalone (0)
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

    Network = None
    NetworkCheckedOut = None
    Standalone = None
    value__ = None


class MiddleMouseMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values to define what happens when
                either the middle mouse button on a three-button mouse is clicked or after pressing the wheel on a wheeled mouse.
    
    enum MiddleMouseMode, values: PopupMenu (0), PopupToolbar (1), RunMacro (2)
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

    PopupMenu = None
    PopupToolbar = None
    RunMacro = None
    value__ = None


class ModelAidSettings(object):
    """ Contains static methods and properties to modify model aid settings. """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> ModelAidSettingsState
        
            Gets the current settings.
            Returns: A new model aid state with current settings.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> ModelAidSettingsState
        
            Gets the factory settings.
            Returns: A new model aid state with factory settings.
        """
        pass

    @staticmethod
    def UpdateFromState(state):
        """
        UpdateFromState(state: ModelAidSettingsState)
            Updates from a particular setting state.
        
            state: The new states that will be set.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
        'UpdateFromState',
    ]


class ModelAidSettingsState(object):
    """ Represents a snapshot of Rhino.ApplicationSettings.ModelAidSettings. """
    AltPlusArrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true mean Alt+arrow is used for nudging.

Get: AltPlusArrow(self: ModelAidSettingsState) -> bool

Set: AltPlusArrow(self: ModelAidSettingsState) = value
"""

    ControlPolygonDisplayDensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the control polygon display density.

Get: ControlPolygonDisplayDensity(self: ModelAidSettingsState) -> int

Set: ControlPolygonDisplayDensity(self: ModelAidSettingsState) = value
"""

    CtrlNudgeKeyStep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Ctrl-key based nudge step amount.

Get: CtrlNudgeKeyStep(self: ModelAidSettingsState) -> float

Set: CtrlNudgeKeyStep(self: ModelAidSettingsState) = value
"""

    DisplayControlPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's display control polygon.

Get: DisplayControlPolygon(self: ModelAidSettingsState) -> bool

Set: DisplayControlPolygon(self: ModelAidSettingsState) = value
"""

    ExtendToApparentIntersection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's extend to apparent intersections.

Get: ExtendToApparentIntersection(self: ModelAidSettingsState) -> bool

Set: ExtendToApparentIntersection(self: ModelAidSettingsState) = value
"""

    ExtendTrimLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's extend trim lines.

Get: ExtendTrimLines(self: ModelAidSettingsState) -> bool

Set: ExtendTrimLines(self: ModelAidSettingsState) = value
"""

    GridSnap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's grid snap modeling aid.

Get: GridSnap(self: ModelAidSettingsState) -> bool

Set: GridSnap(self: ModelAidSettingsState) = value
"""

    HighlightControlPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's highlight dialog modeling aid.

Get: HighlightControlPolygon(self: ModelAidSettingsState) -> bool

Set: HighlightControlPolygon(self: ModelAidSettingsState) = value
"""

    MousePickboxRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the radius of the mouse pick box in pixels.

Get: MousePickboxRadius(self: ModelAidSettingsState) -> int

Set: MousePickboxRadius(self: ModelAidSettingsState) = value
"""

    NudgeKeyStep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the nudge step amount.

Get: NudgeKeyStep(self: ModelAidSettingsState) -> float

Set: NudgeKeyStep(self: ModelAidSettingsState) = value
"""

    NudgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """0 = world, 1 = cplane, 2 = view, 3 = uvn, -1 = not set.

Get: NudgeMode(self: ModelAidSettingsState) -> int

Set: NudgeMode(self: ModelAidSettingsState) = value
"""

    Ortho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's ortho modeling aid.

Get: Ortho(self: ModelAidSettingsState) -> bool

Set: Ortho(self: ModelAidSettingsState) = value
"""

    OrthoAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base orthogonal angle.

Get: OrthoAngle(self: ModelAidSettingsState) -> float

Set: OrthoAngle(self: ModelAidSettingsState) = value
"""

    Osnap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's object snap modeling aid.

Get: Osnap(self: ModelAidSettingsState) -> bool

Set: Osnap(self: ModelAidSettingsState) = value
"""

    OsnapCursorMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the OSnap cursor mode.

Get: OsnapCursorMode(self: ModelAidSettingsState) -> CursorMode

Set: OsnapCursorMode(self: ModelAidSettingsState) = value
"""

    OsnapModes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns or sets Rhino's current object snap mode.
            The mode is a bitwise value based on the OsnapModes enumeration.

Get: OsnapModes(self: ModelAidSettingsState) -> OsnapModes

Set: OsnapModes(self: ModelAidSettingsState) = value
"""

    OsnapPickboxRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enables or disables Rhino's planar modeling aid.

Get: OsnapPickboxRadius(self: ModelAidSettingsState) -> int

Set: OsnapPickboxRadius(self: ModelAidSettingsState) = value
"""

    Planar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's Planar modeling aid.

Get: Planar(self: ModelAidSettingsState) -> bool

Set: Planar(self: ModelAidSettingsState) = value
"""

    PointDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point display mode.

Get: PointDisplay(self: ModelAidSettingsState) -> PointDisplayMode

Set: PointDisplay(self: ModelAidSettingsState) = value
"""

    ProjectSnapToCPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's Project modeling aid.

Get: ProjectSnapToCPlane(self: ModelAidSettingsState) -> bool

Set: ProjectSnapToCPlane(self: ModelAidSettingsState) = value
"""

    ShiftNudgeKeyStep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Shift-key based nudge step amount.

Get: ShiftNudgeKeyStep(self: ModelAidSettingsState) -> float

Set: ShiftNudgeKeyStep(self: ModelAidSettingsState) = value
"""

    SnapToLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the locked state of the snap modeling aid.

Get: SnapToLocked(self: ModelAidSettingsState) -> bool

Set: SnapToLocked(self: ModelAidSettingsState) = value
"""

    UniversalConstructionPlaneMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the locked state of the snap modeling aid.

Get: UniversalConstructionPlaneMode(self: ModelAidSettingsState) -> bool

Set: UniversalConstructionPlaneMode(self: ModelAidSettingsState) = value
"""

    UseHorizontalDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the enabled state of Rhino's use horizontal dialog modeling aid.

Get: UseHorizontalDialog(self: ModelAidSettingsState) -> bool

Set: UseHorizontalDialog(self: ModelAidSettingsState) = value
"""



class MouseSelectMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values to indicate a particular window selection mode.
    
    enum MouseSelectMode, values: Combo (2), Crossing (0), Window (1)
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

    Combo = None
    Crossing = None
    value__ = None
    Window = None


class NeverRepeatList(object):
    """ Contains static methods and properties relating to the list of commands that are never repeated. """
    @staticmethod
    def CommandNames():
        """
        CommandNames() -> Array[str]
        
            The list of commands to not repeat.
        """
        pass

    @staticmethod
    def SetList(commandNames):
        """
        SetList(commandNames: Array[str]) -> int
        
            Puts the command name tokens in m_dont_repeat_list.
            Returns: Number of items added to m_dont_repeat_list.
        """
        pass

    __all__ = [
        'CommandNames',
        'SetList',
    ]


class OsnapModes(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines several bit masks for each of the OSnap that are defined.
                Refer to the Rhino Help file for further information.
    
    enum (flags) OsnapModes, values: Center (32), End (131072), Focus (8), Intersection (8192), Knot (128), Midpoint (2048), Near (2), None (0), Perpendicular (524288), Point (134217728), Quadrant (512), Tangent (2097152), Vertex (64)
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

    Center = None
    End = None
    Focus = None
    Intersection = None
    Knot = None
    Midpoint = None
    Near = None
    None = None
    Perpendicular = None
    Point = None
    Quadrant = None
    Tangent = None
    value__ = None
    Vertex = None


class PaintColor(Enum, IComparable, IFormattable, IConvertible):
    """
    Contains enumerated constant values to represent logical colors associated with elements of the user interface.
    
    enum PaintColor, values: HotBorder (5), HotEnd (4), HotStart (3), MouseOverControlBorder (13), MouseOverControlEnd (12), MouseOverControlStart (11), NormalBorder (2), NormalEnd (1), NormalStart (0), PressedBorder (8), PressedEnd (7), PressedStart (6), TextDisabled (10), TextEnabled (9)
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

    HotBorder = None
    HotEnd = None
    HotStart = None
    MouseOverControlBorder = None
    MouseOverControlEnd = None
    MouseOverControlStart = None
    NormalBorder = None
    NormalEnd = None
    NormalStart = None
    PressedBorder = None
    PressedEnd = None
    PressedStart = None
    TextDisabled = None
    TextEnabled = None
    value__ = None


class PointDisplayMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values for world coordinates and CPlane point display modes.
    
    enum PointDisplayMode, values: CplanePoint (1), WorldPoint (0)
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

    CplanePoint = None
    value__ = None
    WorldPoint = None


class ShortcutKey(Enum, IComparable, IFormattable, IConvertible):
    """
    Shortcut key combinations
    
    enum ShortcutKey, values: AltCtrl0 (146), AltCtrl1 (147), AltCtrl2 (148), AltCtrl3 (149), AltCtrl4 (150), AltCtrl5 (151), AltCtrl6 (152), AltCtrl7 (153), AltCtrl8 (154), AltCtrl9 (155), AltCtrlA (100), AltCtrlB (101), AltCtrlC (102), AltCtrlD (103), AltCtrlE (104), AltCtrlEnd (165), AltCtrlF (105), AltCtrlF1 (36), AltCtrlF10 (45), AltCtrlF11 (46), AltCtrlF12 (47), AltCtrlF2 (37), AltCtrlF3 (38), AltCtrlF4 (39), AltCtrlF5 (40), AltCtrlF6 (41), AltCtrlF7 (42), AltCtrlF8 (43), AltCtrlF9 (44), AltCtrlG (106), AltCtrlH (107), AltCtrlHome (164), AltCtrlI (108), AltCtrlJ (109), AltCtrlK (110), AltCtrlL (111), AltCtrlM (112), AltCtrlN (113), AltCtrlO (114), AltCtrlP (115), AltCtrlPageDown (175), AltCtrlPageUp (174), AltCtrlQ (116), AltCtrlR (117), AltCtrlS (118), AltCtrlT (119), AltCtrlU (120), AltCtrlV (121), AltCtrlW (122), AltCtrlX (123), AltCtrlY (124), AltCtrlZ (125), Ctrl0 (126), Ctrl1 (127), Ctrl2 (128), Ctrl3 (129), Ctrl4 (130), Ctrl5 (131), Ctrl6 (132), Ctrl7 (133), Ctrl8 (134), Ctrl9 (135), CtrlA (48), CtrlB (49), CtrlC (50), CtrlD (51), CtrlE (52), CtrlEnd (159), CtrlF (53), CtrlF1 (12), CtrlF10 (21), CtrlF11 (22), CtrlF12 (23), CtrlF2 (13), CtrlF3 (14), CtrlF4 (15), CtrlF5 (16), CtrlF6 (17), CtrlF7 (18), CtrlF8 (19), CtrlF9 (20), CtrlG (54), CtrlH (55), CtrlHome (158), CtrlI (56), CtrlJ (57), CtrlK (58), CtrlL (59), CtrlM (60), CtrlN (61), CtrlO (62), CtrlP (63), CtrlPageDown (171), CtrlPageUp (170), CtrlQ (64), CtrlR (65), CtrlS (66), CtrlT (67), CtrlU (68), CtrlV (69), CtrlW (70), CtrlX (71), CtrlY (72), CtrlZ (73), End (157), F1 (0), F10 (9), F11 (10), F12 (11), F2 (1), F3 (2), F4 (3), F5 (4), F6 (5), F7 (6), F8 (7), F9 (8), Home (156), PageDown (167), PageUp (166), ShiftCtrl0 (136), ShiftCtrl1 (137), ShiftCtrl2 (138), ShiftCtrl3 (139), ShiftCtrl4 (140), ShiftCtrl5 (141), ShiftCtrl6 (142), ShiftCtrl7 (143), ShiftCtrl8 (144), ShiftCtrl9 (145), ShiftCtrlA (74), ShiftCtrlB (75), ShiftCtrlC (76), ShiftCtrlD (77), ShiftCtrlE (78), ShiftCtrlEnd (163), ShiftCtrlF (79), ShiftCtrlF1 (24), ShiftCtrlF10 (33), ShiftCtrlF11 (34), ShiftCtrlF12 (35), ShiftCtrlF2 (25), ShiftCtrlF3 (26), ShiftCtrlF4 (27), ShiftCtrlF5 (28), ShiftCtrlF6 (29), ShiftCtrlF7 (30), ShiftCtrlF8 (31), ShiftCtrlF9 (32), ShiftCtrlG (80), ShiftCtrlH (81), ShiftCtrlHome (162), ShiftCtrlI (82), ShiftCtrlJ (83), ShiftCtrlK (84), ShiftCtrlL (85), ShiftCtrlM (86), ShiftCtrlN (87), ShiftCtrlO (88), ShiftCtrlP (89), ShiftCtrlPageDown (173), ShiftCtrlPageUp (172), ShiftCtrlQ (90), ShiftCtrlR (91), ShiftCtrlS (92), ShiftCtrlT (93), ShiftCtrlU (94), ShiftCtrlV (95), ShiftCtrlW (96), ShiftCtrlX (97), ShiftCtrlY (98), ShiftCtrlZ (99), ShiftEnd (161), ShiftHome (160), ShiftPageDown (169), ShiftPageUp (168)
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

    AltCtrl0 = None
    AltCtrl1 = None
    AltCtrl2 = None
    AltCtrl3 = None
    AltCtrl4 = None
    AltCtrl5 = None
    AltCtrl6 = None
    AltCtrl7 = None
    AltCtrl8 = None
    AltCtrl9 = None
    AltCtrlA = None
    AltCtrlB = None
    AltCtrlC = None
    AltCtrlD = None
    AltCtrlE = None
    AltCtrlEnd = None
    AltCtrlF = None
    AltCtrlF1 = None
    AltCtrlF10 = None
    AltCtrlF11 = None
    AltCtrlF12 = None
    AltCtrlF2 = None
    AltCtrlF3 = None
    AltCtrlF4 = None
    AltCtrlF5 = None
    AltCtrlF6 = None
    AltCtrlF7 = None
    AltCtrlF8 = None
    AltCtrlF9 = None
    AltCtrlG = None
    AltCtrlH = None
    AltCtrlHome = None
    AltCtrlI = None
    AltCtrlJ = None
    AltCtrlK = None
    AltCtrlL = None
    AltCtrlM = None
    AltCtrlN = None
    AltCtrlO = None
    AltCtrlP = None
    AltCtrlPageDown = None
    AltCtrlPageUp = None
    AltCtrlQ = None
    AltCtrlR = None
    AltCtrlS = None
    AltCtrlT = None
    AltCtrlU = None
    AltCtrlV = None
    AltCtrlW = None
    AltCtrlX = None
    AltCtrlY = None
    AltCtrlZ = None
    Ctrl0 = None
    Ctrl1 = None
    Ctrl2 = None
    Ctrl3 = None
    Ctrl4 = None
    Ctrl5 = None
    Ctrl6 = None
    Ctrl7 = None
    Ctrl8 = None
    Ctrl9 = None
    CtrlA = None
    CtrlB = None
    CtrlC = None
    CtrlD = None
    CtrlE = None
    CtrlEnd = None
    CtrlF = None
    CtrlF1 = None
    CtrlF10 = None
    CtrlF11 = None
    CtrlF12 = None
    CtrlF2 = None
    CtrlF3 = None
    CtrlF4 = None
    CtrlF5 = None
    CtrlF6 = None
    CtrlF7 = None
    CtrlF8 = None
    CtrlF9 = None
    CtrlG = None
    CtrlH = None
    CtrlHome = None
    CtrlI = None
    CtrlJ = None
    CtrlK = None
    CtrlL = None
    CtrlM = None
    CtrlN = None
    CtrlO = None
    CtrlP = None
    CtrlPageDown = None
    CtrlPageUp = None
    CtrlQ = None
    CtrlR = None
    CtrlS = None
    CtrlT = None
    CtrlU = None
    CtrlV = None
    CtrlW = None
    CtrlX = None
    CtrlY = None
    CtrlZ = None
    End = None
    F1 = None
    F10 = None
    F11 = None
    F12 = None
    F2 = None
    F3 = None
    F4 = None
    F5 = None
    F6 = None
    F7 = None
    F8 = None
    F9 = None
    Home = None
    PageDown = None
    PageUp = None
    ShiftCtrl0 = None
    ShiftCtrl1 = None
    ShiftCtrl2 = None
    ShiftCtrl3 = None
    ShiftCtrl4 = None
    ShiftCtrl5 = None
    ShiftCtrl6 = None
    ShiftCtrl7 = None
    ShiftCtrl8 = None
    ShiftCtrl9 = None
    ShiftCtrlA = None
    ShiftCtrlB = None
    ShiftCtrlC = None
    ShiftCtrlD = None
    ShiftCtrlE = None
    ShiftCtrlEnd = None
    ShiftCtrlF = None
    ShiftCtrlF1 = None
    ShiftCtrlF10 = None
    ShiftCtrlF11 = None
    ShiftCtrlF12 = None
    ShiftCtrlF2 = None
    ShiftCtrlF3 = None
    ShiftCtrlF4 = None
    ShiftCtrlF5 = None
    ShiftCtrlF6 = None
    ShiftCtrlF7 = None
    ShiftCtrlF8 = None
    ShiftCtrlF9 = None
    ShiftCtrlG = None
    ShiftCtrlH = None
    ShiftCtrlHome = None
    ShiftCtrlI = None
    ShiftCtrlJ = None
    ShiftCtrlK = None
    ShiftCtrlL = None
    ShiftCtrlM = None
    ShiftCtrlN = None
    ShiftCtrlO = None
    ShiftCtrlP = None
    ShiftCtrlPageDown = None
    ShiftCtrlPageUp = None
    ShiftCtrlQ = None
    ShiftCtrlR = None
    ShiftCtrlS = None
    ShiftCtrlT = None
    ShiftCtrlU = None
    ShiftCtrlV = None
    ShiftCtrlW = None
    ShiftCtrlX = None
    ShiftCtrlY = None
    ShiftCtrlZ = None
    ShiftEnd = None
    ShiftHome = None
    ShiftPageDown = None
    ShiftPageUp = None
    value__ = None


class ShortcutKeySettings(object):
    """ Contains static methods and properties to control keyboard shortcut keys """
    @staticmethod
    def GetMacro(key):
        """
        GetMacro(key: ShortcutKey) -> str
        
            Get macro associated with a given keyboard shortcut
        """
        pass

    @staticmethod
    def SetMacro(key, macro):
        """
        SetMacro(key: ShortcutKey, macro: str)
            Set macro associated with a keyboard shortcut
        """
        pass

    __all__ = [
        'GetMacro',
        'SetMacro',
    ]


class SmartTrackSettings(object):
    """ Contains static methods and properties that target the Smart Track feature behavior. """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> SmartTrackSettingsState
        
            Gets the current settings.
            Returns: A new Smart Track state with current settings.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> SmartTrackSettingsState
        
            Gets the Smart Track factory settings.
            Returns: A new Smart Track state with factory settings.
        """
        pass

    @staticmethod
    def UpdateFromState(state):
        """
        UpdateFromState(state: SmartTrackSettingsState)
            Updates from a particular setting state.
        
            state: The new state that will be set.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
        'UpdateFromState',
    ]


class SmartTrackSettingsState(object):
    """ Represents a snapshot of Rhino.ApplicationSettings.SmartTrackSettings. """
    ActivationDelayMilliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the activation delay in milliseconds.

Get: ActivationDelayMilliseconds(self: SmartTrackSettingsState) -> int

Set: ActivationDelayMilliseconds(self: SmartTrackSettingsState) = value
"""

    ActivePointColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the active point color.

Get: ActivePointColor(self: SmartTrackSettingsState) -> Color

Set: ActivePointColor(self: SmartTrackSettingsState) = value
"""

    LineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the smart track line color.

Get: LineColor(self: SmartTrackSettingsState) -> Color

Set: LineColor(self: SmartTrackSettingsState) = value
"""

    PointColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the point color.

Get: PointColor(self: SmartTrackSettingsState) -> Color

Set: PointColor(self: SmartTrackSettingsState) = value
"""

    SmartOrtho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating if the 'Smart Ortho' feature is active.

Get: SmartOrtho(self: SmartTrackSettingsState) -> bool

Set: SmartOrtho(self: SmartTrackSettingsState) = value
"""

    SmartTangents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating if the 'Smart Tangents' feature is active.

Get: SmartTangents(self: SmartTrackSettingsState) -> bool

Set: SmartTangents(self: SmartTrackSettingsState) = value
"""

    TanPerpLineColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the tangent and perpendicular line color.

Get: TanPerpLineColor(self: SmartTrackSettingsState) -> Color

Set: TanPerpLineColor(self: SmartTrackSettingsState) = value
"""

    UseDottedLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating if lines are drawn dotted.

Get: UseDottedLines(self: SmartTrackSettingsState) -> bool

Set: UseDottedLines(self: SmartTrackSettingsState) = value
"""

    UseSmartTrack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if the 'smart track' feature is active.

Get: UseSmartTrack(self: SmartTrackSettingsState) -> bool

Set: UseSmartTrack(self: SmartTrackSettingsState) = value
"""


    MaxSmartPoints = 0


class ViewSettings(object):
    """ Contains static methods and properties to control view settings. """
    @staticmethod
    def GetCurrentState():
        """
        GetCurrentState() -> ViewSettingsState
        
            Gets the current settings.
            Returns: A new view state with current settings.
        """
        pass

    @staticmethod
    def GetDefaultState():
        """
        GetDefaultState() -> ViewSettingsState
        
            Gets the view factory settings.
            Returns: A new view state with factory settings.
        """
        pass

    @staticmethod
    def RestoreDefaults():
        """
        RestoreDefaults()
            Updates from the default setting state.
        """
        pass

    @staticmethod
    def UpdateFromState(state):
        """
        UpdateFromState(state: ViewSettingsState)
            Updates from a particular setting state.
        
            state: The new state that will be set.
        """
        pass

    __all__ = [
        'GetCurrentState',
        'GetDefaultState',
        'RestoreDefaults',
        'UpdateFromState',
    ]


class ViewSettingsState(object):
    """ Represents a snapshot of Rhino.ApplicationSettings.ViewSettings. """
    AlwaysPanParallelViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 'always pan parallel views' value.
            If the view is not looking straight at the construction plane, then
            sets parallel viewports so they will not rotate.

Get: AlwaysPanParallelViews(self: ViewSettingsState) -> bool

Set: AlwaysPanParallelViews(self: ViewSettingsState) = value
"""

    DefinedViewSetCPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 'named views set CPlane' value.
            When true, restoring a named view causes the construction plane saved with that view to also restore.

Get: DefinedViewSetCPlane(self: ViewSettingsState) -> bool

Set: DefinedViewSetCPlane(self: ViewSettingsState) = value
"""

    DefinedViewSetProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 'named views set projection' value.
            When true, restoring a named view causes the viewport projection saved with the view to also restore.

Get: DefinedViewSetProjection(self: ViewSettingsState) -> bool

Set: DefinedViewSetProjection(self: ViewSettingsState) = value
"""

    LinkedViewports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 'linked views' activated setting.
            true enables real-time view synchronization.
            When a standard view is manipulated, the camera lens length of all parallel projection
            viewports are set to match the current viewport.

Get: LinkedViewports(self: ViewSettingsState) -> bool

Set: LinkedViewports(self: ViewSettingsState) = value
"""

    PanReverseKeyboardAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if panning with the keyboard is reversed.
            false, then Rhino pans the camera in the direction of the arrow key you press.
            true, then Rhino pans the scene instead.

Get: PanReverseKeyboardAction(self: ViewSettingsState) -> bool

Set: PanReverseKeyboardAction(self: ViewSettingsState) = value
"""

    PanScreenFraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the faction used as multiplier to pan the screen.

Get: PanScreenFraction(self: ViewSettingsState) -> float

Set: PanScreenFraction(self: ViewSettingsState) = value
"""

    RotateCircleIncrement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation increment.
            When the user rotates a view with the keyboard, Rhino rotates the view in steps.
            The usual step is 1/60th of a circle, which equals six degrees.

Get: RotateCircleIncrement(self: ViewSettingsState) -> int

Set: RotateCircleIncrement(self: ViewSettingsState) = value
"""

    RotateReverseKeyboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation direction.
            If true, then Rhino rotates the camera around the scene, otherwise, rotates the scene itself.

Get: RotateReverseKeyboard(self: ViewSettingsState) -> bool

Set: RotateReverseKeyboard(self: ViewSettingsState) = value
"""

    RotateToView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation reference.
            If true, then the views rotates relative to the view axes; false, than relative to the world x, y, and z axes.

Get: RotateToView(self: ViewSettingsState) -> bool

Set: RotateToView(self: ViewSettingsState) = value
"""

    SingleClickMaximize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the 'single-click maximize' value.
            When true, maximizing a viewport needs a single click on the viewport title rather than a double-click.

Get: SingleClickMaximize(self: ViewSettingsState) -> bool

Set: SingleClickMaximize(self: ViewSettingsState) = value
"""

    ZoomScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the step size for zooming with a wheeled mouse or the Page Up and Page Down keys.

Get: ZoomScale(self: ViewSettingsState) -> float

Set: ZoomScale(self: ViewSettingsState) = value
"""



