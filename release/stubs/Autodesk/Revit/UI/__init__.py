# encoding: utf-8
# module Autodesk.Revit.UI calls itself UI
# from RevitAPIUI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddInCommandBinding(object):
    """
    This object represents a binding between a Revit command and one or more handlers which 
    override the behavior of the command in Revit.
    """
    RevitCommandId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Revit command Id.

Get: RevitCommandId(self: AddInCommandBinding) -> RevitCommandId

"""


    BeforeExecuted = None
    CanExecute = None
    Executed = None


class RibbonItemData(object):
    """ Base class used to contain information necessary to construct a RibbonItem in the Ribbon. """
    def GetContextualHelp(self):
        """
        GetContextualHelp(self: RibbonItemData) -> ContextualHelp
        
            Gets the contextual help bound with this control.
            Returns: The contextual help assigned to the item, or ll if there is no binding assigned.
        """
        pass

    def SetContextualHelp(self, contextualHelp):
        """
        SetContextualHelp(self: RibbonItemData, contextualHelp: ContextualHelp)
            Sets the contextual help bound with this button data.
        
            contextualHelp: The contextual help.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str) """
        pass

    LongDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Long description of the command tooltip

Get: LongDescription(self: RibbonItemData) -> str

Set: LongDescription(self: RibbonItemData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the item.

Get: Name(self: RibbonItemData) -> str

Set: Name(self: RibbonItemData) = value
"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description that appears as a ToolTip for the item.

Get: ToolTip(self: RibbonItemData) -> str

Set: ToolTip(self: RibbonItemData) = value
"""

    ToolTipImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image to show as a part of the button extended tooltip

Get: ToolTipImage(self: RibbonItemData) -> ImageSource

Set: ToolTipImage(self: RibbonItemData) = value
"""



class ButtonData(RibbonItemData):
    """ Base class used to contain information necessary to construct a button in the Ribbon. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, text: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image of the button.

Get: Image(self: ButtonData) -> ImageSource

Set: Image(self: ButtonData) = value
"""

    LargeImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The large image of the button.

Get: LargeImage(self: ButtonData) -> ImageSource

Set: LargeImage(self: ButtonData) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user-visible text of the button.

Get: Text(self: ButtonData) -> str

Set: Text(self: ButtonData) = value
"""



class ColorSelectionDialog(object, IDisposable):
    """
    Allows display of the Revit Color dialog.
    
    ColorSelectionDialog()
    """
    def Dispose(self):
        """ Dispose(self: ColorSelectionDialog) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ColorSelectionDialog, disposing: bool) """
        pass

    def Show(self):
        """
        Show(self: ColorSelectionDialog) -> ItemSelectionDialogResult
        
            Shows the Revit Color dialog as a modal dialog.
            Returns: A status indicating whether the user selected a color or cancelled the dialog 
             without making a selection.
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

Get: IsValidObject(self: ColorSelectionDialog) -> bool

"""

    OriginalColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The original color.

Get: OriginalColor(self: ColorSelectionDialog) -> Color

Set: OriginalColor(self: ColorSelectionDialog) = value
"""

    SelectedColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The new color selected by the user.

Get: SelectedColor(self: ColorSelectionDialog) -> Color

"""



class RibbonItem(object):
    """
    The RibbonItem object represents an item on RibbonPanel, can be a push-button or a pull-down 
    which should contain the information for creating one RibbonItem.
    """
    def Equals(self, obj):
        """
        Equals(self: RibbonItem, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Object.
        
        
            obj: Another panel object.
        """
        pass

    def GetContextualHelp(self):
        """
        GetContextualHelp(self: RibbonItem) -> ContextualHelp
        
            Gets the contextual help bound with this control.
            Returns: The contextual help assigned to the item, or ll if there is no binding assigned.
        """
        pass

    def SetContextualHelp(self, contextualHelp):
        """
        SetContextualHelp(self: RibbonItem, contextualHelp: ContextualHelp)
            Sets the contextual help bound with this button.
        
            contextualHelp: The contextual help.
        """
        pass

    def setItemText(self, *args): #cannot find CLR method
        """ setItemText(self: RibbonItem, text: str) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the item is enabled.

Get: Enabled(self: RibbonItem) -> bool

Set: Enabled(self: RibbonItem) = value
"""

    ItemText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text displayed on the item.

Get: ItemText(self: RibbonItem) -> str

Set: ItemText(self: RibbonItem) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the item type.

Get: ItemType(self: RibbonItem) -> RibbonItemType

"""

    LongDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Long description of the command tooltip

Get: LongDescription(self: RibbonItem) -> str

Set: LongDescription(self: RibbonItem) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the item.

Get: Name(self: RibbonItem) -> str

"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description that appears as a ToolTip for the item.

Get: ToolTip(self: RibbonItem) -> str

Set: ToolTip(self: RibbonItem) = value
"""

    ToolTipImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image to show as a part of the button extended tooltip

Get: ToolTipImage(self: RibbonItem) -> ImageSource

Set: ToolTipImage(self: RibbonItem) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the item is visible.

Get: Visible(self: RibbonItem) -> bool

Set: Visible(self: RibbonItem) = value
"""


    m_ItemType = None


class ComboBox(RibbonItem):
    """ This class represents a selection control with a drop-down list that can be shown or hidden by clicking the arrow. """
    def AddItem(self, memberData):
        """
        AddItem(self: ComboBox, memberData: ComboBoxMemberData) -> ComboBoxMember
        
            Adds a new item to the ComboBox.
        
            memberData: An object containing the data needed to construct the ComboBoxMember.
            Returns: The newly added ComboBoxMember.
        """
        pass

    def AddItems(self, memberData):
        """ AddItems(self: ComboBox, memberData: IList[ComboBoxMemberData]) -> IList[ComboBoxMember] """
        pass

    def AddSeparator(self):
        """
        AddSeparator(self: ComboBox)
            Adds a separator to the drop-down list.
        """
        pass

    def GetItems(self):
        """
        GetItems(self: ComboBox) -> IList[ComboBoxMember]
        
            Gets the copy of a collection of the ComboBoxMembers assigned to the ComboBox.
        """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current checked ComboBox member of the ComboBox.

Get: Current(self: ComboBox) -> ComboBoxMember

Set: Current(self: ComboBox) = value
"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image shown on the ComboBox.

Get: Image(self: ComboBox) -> ImageSource

Set: Image(self: ComboBox) = value
"""


    CurrentChanged = None
    DropDownClosed = None
    DropDownOpened = None
    m_ItemType = None


class ComboBoxData(RibbonItemData):
    """
    This class contains information necessary to construct a combo box in the Ribbon.
    
    ComboBoxData(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image shown on the ComboBox.

Get: Image(self: ComboBoxData) -> ImageSource

Set: Image(self: ComboBoxData) = value
"""



class ComboBoxMember(RibbonItem):
    """ This class represents an item in the drop-down list of a ComboBox. """
    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The group to which the ComboBoxMember is assigned.

Get: GroupName(self: ComboBoxMember) -> str

"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image shown on the ComboBoxMember.

Get: Image(self: ComboBoxMember) -> ImageSource

Set: Image(self: ComboBoxMember) = value
"""


    m_ItemType = None


class ComboBoxMemberData(RibbonItemData):
    """
    This class contains information necessary to construct a ComboBoxMember.
    
    ComboBoxMemberData(name: str, text: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, text):
        """ __new__(cls: type, name: str, text: str) """
        pass

    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a group name for the ComboBoxMember.

Get: GroupName(self: ComboBoxMemberData) -> str

Set: GroupName(self: ComboBoxMemberData) = value
"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image shown on the ComboBoxMember.

Get: Image(self: ComboBoxMemberData) -> ImageSource

Set: Image(self: ComboBoxMemberData) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user-visible text of the ComboBoxMember.

Get: Text(self: ComboBoxMemberData) -> str

Set: Text(self: ComboBoxMemberData) = value
"""



class ContextualHelp(object):
    """
    Contains the details for how Revit should allow invocation of contextual help for an item added by an application.
    
    ContextualHelp(helpType: ContextualHelpType, helpPath: str)
    """
    def Launch(self):
        """
        Launch(self: ContextualHelp)
            Launches and displays the help topic specified by the contents of this 
             ContextualHelp object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, helpType, helpPath):
        """ __new__(cls: type, helpType: ContextualHelpType, helpPath: str) """
        pass

    HelpPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The context id, help URL, or help file path.

Get: HelpPath(self: ContextualHelp) -> str

Set: HelpPath(self: ContextualHelp) = value
"""

    HelpTopicUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The help topic URL.

Get: HelpTopicUrl(self: ContextualHelp) -> str

Set: HelpTopicUrl(self: ContextualHelp) = value
"""

    HelpType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The contextual help type.

Get: HelpType(self: ContextualHelp) -> ContextualHelpType

Set: HelpType(self: ContextualHelp) = value
"""



class ContextualHelpType(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the contextual help type.
    
    enum ContextualHelpType, values: ChmFile (3), ContextId (1), None (0), Url (2)
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

    ChmFile = None
    ContextId = None
    None = None
    Url = None
    value__ = None


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



class DockablePaneId(GuidEnum):
    """
    Identifier for a pane that participates in the Revit docking window system.
    
    DockablePaneId(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass


class DockablePaneProviderData(object):
    """
    Information about a new dockable pane being added to the Revit user interface.
    
    DockablePaneProviderData()
    """
    ContextualHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The contextual help associated with the pane.

Get: ContextualHelp(self: DockablePaneProviderData) -> ContextualHelp

Set: ContextualHelp(self: DockablePaneProviderData) = value
"""

    EditorInteraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the interaction this pane has with the Active Editor when the pane becomes active.

Get: EditorInteraction(self: DockablePaneProviderData) -> EditorInteraction

Set: EditorInteraction(self: DockablePaneProviderData) = value
"""

    FrameworkElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Windows Presentation Framework object containing the pane's user interface.

Get: FrameworkElement(self: DockablePaneProviderData) -> FrameworkElement

Set: FrameworkElement(self: DockablePaneProviderData) = value
"""

    InitialState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The initial position of the docking pane.

Get: InitialState(self: DockablePaneProviderData) -> DockablePaneState

Set: InitialState(self: DockablePaneProviderData) = value
"""

    VisibleByDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls the default visibility of the pane upon the first time
   the pane/plugin is loaded into Revit.

Get: VisibleByDefault(self: DockablePaneProviderData) -> bool

Set: VisibleByDefault(self: DockablePaneProviderData) = value
"""



class DockablePanes(object):
    """ Provides a container of all Revit built-in DockablePaneId instances. """
    BuiltInDockablePanes = None
    __all__ = [
        'BuiltInDockablePanes',
    ]


class DockablePaneState(object, IDisposable):
    """
    Describes where a dockable pane window should appear in the Revit user interface.
    
    DockablePaneState(other: DockablePaneState)
    DockablePaneState()
    """
    def Dispose(self):
        """ Dispose(self: DockablePaneState) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DockablePaneState, disposing: bool) """
        pass

    def SetFloatingRectangle(self, rect):
        """
        SetFloatingRectangle(self: DockablePaneState, rect: Rectangle)
            When %dockPosition% is Floating, sets the rectangle used to determine the size 
             and position of the pane when %dockPosition% is Floating.  Coordinates are 
             relative to the upper-left-hand corner of the main Revit window.
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
    def __new__(self, other=None):
        """
        __new__(cls: type, other: DockablePaneState)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DockPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Which part of the Revit application frame the pane should dock to.

Get: DockPosition(self: DockablePaneState) -> DockPosition

Set: DockPosition(self: DockablePaneState) = value
"""

    FloatingRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When %dockPosition% is Floating, this rectangle determines the size and position of the pane.  Coordinates are relative to the upper-left-hand corner of the main Revit window.
   Note: the returned Rectangle is a copy. In order to change the pane state, you must call SetFloatingRectangle with a modified rectangle.

Get: FloatingRectangle(self: DockablePaneState) -> Rectangle

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: DockablePaneState) -> bool

"""

    TabBehind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ignored unless %dockPosition% is Tabbed.  The new pane will appear in a tab behind the specified existing pane ID.

Get: TabBehind(self: DockablePaneState) -> DockablePaneId

Set: TabBehind(self: DockablePaneState) = value
"""



class DockPosition(Enum, IComparable, IFormattable, IConvertible):
    """
    Which part of the Revit application frame the pane should dock to.
    
    enum DockPosition, values: Bottom (59422), Floating (59423), Left (59420), Right (59421), Tabbed (59424), Top (59419)
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
    Left = None
    Right = None
    Tabbed = None
    Top = None
    value__ = None


class DoubleClickAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Possible actions Revit can take in response to the user double-clicking on an element.
    
    enum DoubleClickAction, values: ActivateView (3), DeactivateView (5), EditFamily (1), EditType (2), EnterEditMode (4), NoAction (0)
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

    ActivateView = None
    DeactivateView = None
    EditFamily = None
    EditType = None
    EnterEditMode = None
    NoAction = None
    value__ = None


class DoubleClickOptions(object, IDisposable):
    """ Provides access to settings that control what happens when the current user double-clicks on an element. """
    def Dispose(self):
        """ Dispose(self: DoubleClickOptions) """
        pass

    def GetAction(self, target):
        """
        GetAction(self: DoubleClickOptions, target: DoubleClickTarget) -> DoubleClickAction
        
            Returns the active user's desired action for a particular double-click target.
        
            target: The target to check.
            Returns: The user's desired action for the specified target.
        """
        pass

    @staticmethod
    def GetDoubleClickOptions():
        """
        GetDoubleClickOptions() -> DoubleClickOptions
        
            Returns the current user's DoubleClickOptions.
            Returns: The DoubleClickOptions for the current user.
        """
        pass

    def IsSupportedAction(self, target, action):
        """
        IsSupportedAction(self: DoubleClickOptions, target: DoubleClickTarget, action: DoubleClickAction) -> bool
        
            Checks whether the specified double-click target supports the specified action.
        
            target: The double-click target to check.
            action: The desired double-click action.
            Returns: True if the target supports the specified action, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: DoubleClickOptions, disposing: bool) """
        pass

    def SetAction(self, target, action):
        """
        SetAction(self: DoubleClickOptions, target: DoubleClickTarget, action: DoubleClickAction)
            Changes the double-click action associated with a specified target.
        
            target: The double-click target whose action will be changed.
            action: The action to assign to the target.
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

Get: IsValidObject(self: DoubleClickOptions) -> bool

"""



class DoubleClickTarget(Enum, IComparable, IFormattable, IConvertible):
    """
    Elements that support double-click in Revit.  Note that this is meant to cover cases
       where the element itself is a double-click target.  Individual controls that are targets
       are handled separately.
    
    enum DoubleClickTarget, values: Assembly (3), ComponentStairs (5), Family (0), Group (4), OutsideViewOnSheet (6), SketchedElement (1), ViewOnSheet (2)
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

    Assembly = None
    ComponentStairs = None
    Family = None
    Group = None
    OutsideViewOnSheet = None
    SketchedElement = None
    value__ = None
    ViewOnSheet = None


class EditorInteraction(object):
    """
    Wraps the EditorInteractionType for the Pane to allow
       for clients to override their type dynamically if need
       be.
    
    EditorInteraction(interactionType: EditorInteractionType)
    EditorInteraction()
    """
    @staticmethod # known case of __new__
    def __new__(self, interactionType=None):
        """
        __new__(cls: type, interactionType: EditorInteractionType)
        __new__(cls: type)
        """
        pass

    InteractionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of interaction.

Get: InteractionType(self: EditorInteraction) -> EditorInteractionType

Set: InteractionType(self: EditorInteraction) = value
"""



class EditorInteractionType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the type of interactions a pane has with the active editor when it becomes active in the Revit UI.
    
    enum EditorInteractionType, values: Dismiss (0), KeepAlive (1)
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

    Dismiss = None
    KeepAlive = None
    value__ = None


class ExternalApplicationArray(APIObject, IDisposable, IEnumerable):
    """ ExternalApplicationArray() """
    def Append(self, item):
        """ Append(self: ExternalApplicationArray, item: IExternalApplication) """
        pass

    def Clear(self):
        """ Clear(self: ExternalApplicationArray) """
        pass

    def Dispose(self):
        """ Dispose(self: ExternalApplicationArray, A_0: bool) """
        pass

    def ForwardIterator(self):
        """ ForwardIterator(self: ExternalApplicationArray) -> ExternalApplicationArrayIterator """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ExternalApplicationArray) -> IEnumerator """
        pass

    def Insert(self, item, index):
        """ Insert(self: ExternalApplicationArray, item: IExternalApplication, index: int) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalApplicationArray) """
        pass

    def ReverseIterator(self):
        """ ReverseIterator(self: ExternalApplicationArray) -> ExternalApplicationArrayIterator """
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: ExternalApplicationArray) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: ExternalApplicationArray) -> int

"""



class ExternalApplicationArrayIterator(APIObject, IDisposable, IEnumerator):
    """ ExternalApplicationArrayIterator() """
    def Dispose(self):
        """ Dispose(self: ExternalApplicationArrayIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """ MoveNext(self: ExternalApplicationArrayIterator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalApplicationArrayIterator) """
        pass

    def Reset(self):
        """ Reset(self: ExternalApplicationArrayIterator) """
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
    """Get: Current(self: ExternalApplicationArrayIterator) -> object

"""



class ExternalCommandData(APIObject, IDisposable):
    """ A class contains reference to Application and View which are needed by external command. """
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

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that represents the current Application for 
external command.

Get: Application(self: ExternalCommandData) -> UIApplication

Set: Application(self: ExternalCommandData) = value
"""

    JournalData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A data map that can be used to read and write data to the Autodesk Revit journal file.

Get: JournalData(self: ExternalCommandData) -> IDictionary[str, str]

Set: JournalData(self: ExternalCommandData) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that represents the View external command work on.

Get: View(self: ExternalCommandData) -> View

Set: View(self: ExternalCommandData) = value
"""



class ExternalEvent(object, IDisposable):
    """ A class that represent an external event. """
    @staticmethod
    def Create(handler):
        """
        Create(handler: IExternalEventHandler) -> ExternalEvent
        
            Creates an instance of external event.
        
            handler: An instance of IExternalEventHandler which will execute the event.
            Returns: An instance of ExternalEvent class, which will be used to invoke the event
        """
        pass

    @staticmethod
    def CreateJournalable(handler):
        """
        CreateJournalable(handler: IExternalEventHandler) -> ExternalEvent
        
            Creates an instance of external event which will have the ability to record its 
             executions in the journal.
        
        
            handler: An instance of IExternalEventHandler which will execute the event.
            Returns: An instance of ExternalEvent class, which will be used to invoke the event
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExternalEvent) """
        pass

    def getNativeObject(self, *args): #cannot find CLR method
        """ getNativeObject(self: ExternalEvent) -> ExternalEvent* """
        pass

    def Raise(self):
        """
        Raise(self: ExternalEvent) -> ExternalEventRequest
        
            Instructing Revit to raise (signal) the external event.
            Returns: The result of event raising request. If the request is 'Accepted',
           the 
             event would be added to the event queue and its handler will
           be executed in 
             the next event-processing cycle.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalEvent, disposing: bool) """
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

    IsPending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checking whether an event has been raised but not yet executed.

Get: IsPending(self: ExternalEvent) -> bool

"""



class ExternalEventRequest(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the possible outcomes of a request for raising an external event.
    
    enum ExternalEventRequest, values: Accepted (0), Denied (2), Pending (1), TimedOut (3)
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

    Accepted = None
    Denied = None
    Pending = None
    TimedOut = None
    value__ = None


class FaceBasedPlacementType(Enum, IComparable, IFormattable, IConvertible):
    """
    This enumerated type specifies options available for placement of a face-based family instance.
    
    enum FaceBasedPlacementType, values: Default (0), PlaceOnFace (2), PlaceOnVerticalFace (1), PlaceOnWorkPlane (3)
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

    Default = None
    PlaceOnFace = None
    PlaceOnVerticalFace = None
    PlaceOnWorkPlane = None
    value__ = None


class FamilyInstancePlacingArgs(object, IDisposable):
    """ The class is used to access necessary data during the placement of a FamilyInstance. """
    def Dispose(self):
        """ Dispose(self: FamilyInstancePlacingArgs) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FamilyInstancePlacingArgs, disposing: bool) """
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

    ActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The active view

Get: ActiveView(self: FamilyInstancePlacingArgs) -> View

"""

    IsBanned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the cursor is banned or not.

Get: IsBanned(self: FamilyInstancePlacingArgs) -> bool

Set: IsBanned(self: FamilyInstancePlacingArgs) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FamilyInstancePlacingArgs) -> bool

"""

    StatusMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message to be shown on the status bar

Get: StatusMessage(self: FamilyInstancePlacingArgs) -> str

Set: StatusMessage(self: FamilyInstancePlacingArgs) = value
"""

    TooltipMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message to be shown via tooltip

Get: TooltipMessage(self: FamilyInstancePlacingArgs) -> str

Set: TooltipMessage(self: FamilyInstancePlacingArgs) = value
"""



class FileDialog(object, IDisposable):
    """ Base class supporting display of the dialog used to navigate to and select a file from Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: FileDialog) """
        pass

    def GetSelectedModelPath(self):
        """
        GetSelectedModelPath(self: FileDialog) -> ModelPath
        
            Returns the selected file path chosen by the user.
            Returns: The selected file path, or ll if the dialog has not been shown or selection was 
             cancelled.
        """
        pass

    @staticmethod
    def IsValidFilterString(filterString):
        """
        IsValidFilterString(filterString: str) -> bool
        
            Determines if the input string is acceptable as input for a FileDialog filter 
             string.
        
        
            filterString: The filter string.
            Returns: True of the filter string meets the minimal requirements to be a valid filter 
             string.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FileDialog, disposing: bool) """
        pass

    def Show(self):
        """
        Show(self: FileDialog) -> ItemSelectionDialogResult
        
            Shows the dialog using the stored settings.
            Returns: A status indicating whether the user selected a file name or cancelled the 
             dialog without making a selection.
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

    DefaultFilterEntry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default entry (from the filter) to be selected in the dialog.

Get: DefaultFilterEntry(self: FileDialog) -> str

Set: DefaultFilterEntry(self: FileDialog) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filter string representing a collection of extensions allowed by the dialog.

Get: Filter(self: FileDialog) -> str

Set: Filter(self: FileDialog) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FileDialog) -> bool

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The title to show on the dialog.

Get: Title(self: FileDialog) -> str

Set: Title(self: FileDialog) = value
"""



class FileOpenDialog(FileDialog, IDisposable):
    """
    This class allows an add-in to prompt the user with the Revit dialog used to navigate to and select an existing
       file path.  This dialog is typically used to select a file for opening or importing.
    
    FileOpenDialog(filter: str)
    """
    def Dispose(self):
        """ Dispose(self: FileDialog, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FileDialog, disposing: bool) """
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
    def __new__(self, filter):
        """ __new__(cls: type, filter: str) """
        pass

    ShowPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the dialog should include a region showing a preview of the selected file.

Get: ShowPreview(self: FileOpenDialog) -> bool

Set: ShowPreview(self: FileOpenDialog) = value
"""



class FileSaveDialog(FileDialog, IDisposable):
    """
    This class allows an add-in to prompt the user with the Revit dialog used to navigate to and select an existing
       or new file path.  This dialog is typically used to enter a file name for saving or exporting.
    
    FileSaveDialog(filter: str)
    """
    def Dispose(self):
        """ Dispose(self: FileDialog, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FileDialog, disposing: bool) """
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
    def __new__(self, filter):
        """ __new__(cls: type, filter: str) """
        pass

    InitialFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The initial file name to be shown for this save operation.

Get: InitialFileName(self: FileSaveDialog) -> str

Set: InitialFileName(self: FileSaveDialog) = value
"""



class FilterDialog(object, IDisposable):
    """
    Allows display of the dialog used to create and edit FilterElements in Autodesk Revit.
    
    FilterDialog(doc: Document, name: str)
    FilterDialog(doc: Document, filterToSelect: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: FilterDialog) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilterDialog, disposing: bool) """
        pass

    def Show(self):
        """
        Show(self: FilterDialog)
            Shows the FilterDialog editing dialog to the user.
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
    def __new__(self, doc, *__args):
        """
        __new__(cls: type, doc: Document, name: str)
        __new__(cls: type, doc: Document, filterToSelect: ElementId)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FilterToSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filter element to be selected once Show is invoked.

Get: FilterToSelect(self: FilterDialog) -> ElementId

Set: FilterToSelect(self: FilterDialog) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilterDialog) -> bool

"""

    NewFilterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the new filter created.
   The value is populated after Show method is executed.

Get: NewFilterId(self: FilterDialog) -> ElementId

"""

    NewFilterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the new ParameterFilterElement to be created and selected once Show is invoked.

Get: NewFilterName(self: FilterDialog) -> str

Set: NewFilterName(self: FilterDialog) = value
"""



class IDropHandler:
    """ An interface to be executed when custom data is dragged and dropped onto the Revit user interface. """
    def Execute(self, document, data):
        """
        Execute(self: IDropHandler, document: UIDocument, data: object)
            Implement this method to handle the drop event for your data.
        
            document: The document on which the data was dropped.
            data: The data.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IControllableDropHandler(IDropHandler):
    """
    An interface to be executed when custom data is dragged and dropped onto the Revit user interface.
       This interface is different from IDropHandler in that it allows the handler to verify whether the drop event can be executed on the given view.
    """
    def CanExecute(self, document, data, dropViewId):
        """
        CanExecute(self: IControllableDropHandler, document: UIDocument, data: object, dropViewId: ElementId) -> bool
        
            Implement this method to inform Revit whether the drop event can be executed 
             onto the given view.
        
        
            document: The document on which the data was dropped.
            data: The data.
            dropViewId: The view upon which the user will drop.
            Returns: Return true to activate the target view and execute the drop. 
        Return false to 
             cancel the activation and the drop execution.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDockablePaneProvider:
    """ Interface that the Revit UI will call during initialization of the user interface to gather information about add-in dockable pane windows. """
    def SetupDockablePane(self, data):
        """
        SetupDockablePane(self: IDockablePaneProvider, data: DockablePaneProviderData)
            Method called during initialization of the user interface to gather information 
             about a dockable pane window.
        
        
            data: Container for information about the new dockable pane.  Implementers should set 
             the 
           FrameworkElement and InitialState Properties. Optionally, providers 
             can set the 
           ContextualHelp property if they wish to provide or react to 
             help requests on the pane,
           or override the default EditorInteraction 
             property by setting it here.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalApplication:
    """ An interface that supports addition of external applications to Revit. """
    def OnShutdown(self, application):
        """
        OnShutdown(self: IExternalApplication, application: UIControlledApplication) -> Result
        
            Implement this method to execute some tasks when Autodesk Revit shuts down.
        
            application: A handle to the application being shut down.
            Returns: Indicates if the external application completes its work successfully.
        """
        pass

    def OnStartup(self, application):
        """
        OnStartup(self: IExternalApplication, application: UIControlledApplication) -> Result
        
            Implement this method to execute some tasks when Autodesk Revit starts.
        
            application: A handle to the application being started.
            Returns: Indicates if the external application completes its work successfully.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalCommand:
    """ An interface that should be implemented to provide the implementation for a Revit add-in External Command. """
    def Execute(self, commandData, message, elements):
        """
        Execute(self: IExternalCommand, commandData: ExternalCommandData) -> (Result, str, ElementSet)
        
            Overload this method to implement and external command within Revit.
        
            commandData: An ExternalCommandData object which contains reference to Application and View
        
             needed by external command.
        
            Returns: The result indicates if the execution fails, succeeds, or was canceled by user. 
             If it does not
        succeed, Revit will undo any changes made by the external 
             command.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalCommandAvailability:
    """ An interface that should be implemented to provide the implementation for a accessibility check for a Revit add-in External Command. """
    def IsCommandAvailable(self, applicationData, selectedCategories):
        """
        IsCommandAvailable(self: IExternalCommandAvailability, applicationData: UIApplication, selectedCategories: CategorySet) -> bool
        
            Implement this method to provide control over whether your external command is 
             enabled or disabled.
        
        
            applicationData: An ApplicationServices.Application object which contains reference to 
             Application
        needed by external command.
        
            selectedCategories: An list of categories of the elements which have been selected in Revit in the 
             active document, 
        or an empty set if no elements are selected or there is no 
             active document.
        
            Returns: Indicates whether Revit should enable or disable the corresponding external 
             command.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalEventHandler:
    """ An interface to be executed when an external event is raised. """
    def Execute(self, app):
        """
        Execute(self: IExternalEventHandler, app: UIApplication)
            This method is called to handle the external event.
        """
        pass

    def GetName(self):
        """
        GetName(self: IExternalEventHandler) -> str
        
            String identification of the event handler.
            Returns: The event's name
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExternalResourceUIServer(IExternalServer):
    """ The interface used to provide custom handling of UI operations related to external resources. """
    def GetDBServerId(self):
        """
        GetDBServerId(self: IExternalResourceUIServer) -> Guid
        
            Implement this method to return the id of the server which is associated with 
             this UI server.
        
            Returns: The id of the associated DB server.
        """
        pass

    def HandleBrowseResult(self, resultType, browsingItemPath):
        """
        HandleBrowseResult(self: IExternalResourceUIServer, resultType: ExternalResourceUIBrowseResultType, browsingItemPath: str)
            Implement this method to handle browsing external resources operation result.
        
            resultType: The result of browsing operation.
            browsingItemPath: The absolute path of item which is browsing.
        """
        pass

    def HandleLoadResourceResults(self, document, loadData):
        """ HandleLoadResourceResults(self: IExternalResourceUIServer, document: Document, loadData: IList[ExternalResourceLoadData]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ItemSelectionDialogResult(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing the possible responses from a prompted dialog where the
       user is asked to select one or more items.
    
    enum ItemSelectionDialogResult, values: Canceled (1), Confirmed (0)
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

    Canceled = None
    Confirmed = None
    value__ = None


class PostableCommand(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates all of the built-in commands which can be posted by an API application.
    
    enum PostableCommand, values: AcquireCoordinates (33863), ActivateView (33181), AddToSet (33908), AdjustAnalyticalModel (35739), AirTerminal (37005), Align (33218), AlignedDimension (48955), AlignedMultiRebarAnnotation (35831), AlignedToCurrentView (33320), AlignedToPickedLevel (33321), AlignedToSamePlace (33341), AlignedToSelectedLevels (33328), AlignedToSelectedViews (33332), AllowableBarTypes (35599), AnalysisDisplayStyles (32948), AnalyticalConsistencyChecks (3411), AngularDimension (48957), AngularDimensionTypes (1082), ApplyCoping (46450), ApplyTemplatePropertiesToCurrentView (33651), ArchitecturalColumn (32918), ArchitecturalFloor (32914), ArchitecturalWall (32771), ArcLengthDimension (48959), ArcWire (37106), Area (33720), AreaAndVolumeComputations (40382), AreaBoundary (33719), AreaPlan (33638), AreaReinforcementSymbol (46959), AreaTag (33718), Array (33121), Arrowheads (33349), AssemblyCode (54096), AutomaticBeamSystem (42398), AutomaticCeiling (33158), Beam (34972), BeamAnnotations (35585), BeamOrColumnJoins (49543), BeamSystemSymbol (46567), BottomChord (3621), BoundaryConditions (35223), Brace (34973), BrowserOrganization (33904), BuildingElevation (33255), BuildingOrSpaceTypeSettings (37259), BuildingPad (33481), CableTray (37297), CableTrayConnector (37291), CableTrayFitting (37295), Callout (33298), CalloutTags (3167), Camera (32956), CascadeWindows (57650), ChamferedWire (37260), CheckCircuits (37062), CheckDuctSystems (37167), CheckMemberSupports (3410), CheckPipeSystems (37155), CheckSpelling (40986), Close (57602), CloseHiddenWindows (33712), ColorFillLegend (33252), ColorSchemes (48739), Communication (37278), Conduit (37298), ConduitConnector (37292), ConduitFitting (37296), Control (33034), ConvertToFlexDuct (37014), CoordinationSettings (35149), Copy (33129), CopyToClipboard (57634), CreateAssembly (53677), CreateGroup (33305), CreateParts (35425), CreateSimilar (33441), CreateTemplateFromCurrentView (33684), CurtainGrid (33199), CurtainSystemByFace (35072), CurtainWallMullion (33200), CutGeometry (33407), CutProfile (33709), CutToClipboard (57635), Data (37279), DeactivateView (33185), DecalTypes (33188), Default3DView (33169), Delete (32778), DemandFactors (37068), Demolish (33534), DesignOptions (33907), DetailComponent (33424), DetailLevel (33384), DetailLine (33425), DiameterDimension (35778), DiameterDimensionTypes (35779), DisplaceElements (54029), Door (32772), DormerOpening (35255), DraftingView (33530), DrawOnFace (2706), DrawOnWorkPlane (2707), Duct (37006), DuctAccessory (37004), DuctConnector (37218), DuctFitting (37009), DuctLegend (37027), DuctPlaceholder (37427), DuctPressureLossReport (35811), DuplicateAsDependent (35280), DuplicateView (33245), DuplicateWithDetailing (33858), DWFMarkup (3401), EditATemplate (37315), EditingRequests (33911), EditRebarCover (48583), EditSelection (35183), ElectricalConnector (37217), ElectricalEquipment (37060), ElectricalFixture (37061), ElectricalSettings (37054), ElementKeynote (35158), ElevationTags (3168), EnergySettings (53612), ExitRevit (57665), ExportBuildingSite (35674), ExportCADFormatsACIS_SAT (3345), ExportCADFormatsDGN (3344), ExportCADFormatsDWG (3342), ExportCADFormatsDXF (3343), ExportDWFOrDWFx (3341), ExportExportTypes (3405), ExportFBX (35350), ExportGBXML (42672), ExportIFC (3278), ExportImagesandAnimationsImage (33838), ExportImagesandAnimationsSolarStudy (12075), ExportImagesandAnimationsWalkthrough (12059), ExportMassModelGBXML (53615), ExportODBCDatabase (33693), ExportOptionsExportSetupsDGN (33248), ExportOptionsExportSetupsDWGOrDXF (33251), ExportOptionsIFCOptions (3292), ExportReportsRoomOrAreaReport (3125), ExportReportsSchedule (33710), FabricationPart (54149), FabricationSettings (35839), FabricReinforcementSymbol (35793), FamilyCategoryAndParameters (10133), FamilyTypes (33203), Fascia (40601), FilledRegion (33204), FillPatterns (33163), Filters (33099), FindOrReplace (53591), FireAlarm (37280), FlexDuct (37010), FlexPipe (37102), FloorByFaceFloor (3234), FloorPlan (32953), FormWorkPlaneView (35703), FramingElevation (32814), GradedRegion (33640), GraphicalColumnSchedule (46139), GrayInactiveWorksets (2765), Grid (32770), GuideGrid (53675), Gutter (40602), HalftoneOrUnderlay (49786), HeatingAndCoolingLoads (37204), HideCategory (3240), HideElements (35261), IdsOfSelection (33866), ImportCAD (32959), ImportGBXML (3102), ImportTypes (3404), InPlaceMass (42645), Insert2DElementsFromFile (42310), InsertViewsFromFile (42309), Insulation (33432), Isolated (35114), JoinGeometry (33729), JoinOrUnjoinRoof (33277), KeyboardShortcuts (49211), KeynoteLegend (3449), KeynotingSettings (3450), Label (33174), LabelContours (33820), Legend (33531), LegendComponent (33751), Level (32794), Lighting (37281), LightingFixture (37059), LinearDimension (48956), LinearDimensionTypes (1081), LinearMultiRebarAnnotation (35832), LinePatterns (33120), LineStyles (33360), LineWeights (32946), Linework (33520), LinkCAD (32961), LinkIFC (35853), LinkRevit (33836), LoadAsGroup (33695), LoadCases (53531), LoadClassifications (37055), LoadCombinations (53532), LoadedTagsAndSymbols (33338), Loads (34987), LoadSelection (35180), LoadShapes (32984), Location (33862), MacroManager (35602), MacroSecurity (35603), MajorSegment (35293), ManageConnectionToARevitServerAccelerator (53949), ManageImages (33648), ManageLinks (33279), ManageTemplates (37314), ManageViewTemplates (33683), MaskingRegion (35287), Matchline (33905), MatchTypeProperties (33513), MaterialAssets (33186), MaterialKeynote (35159), Materials (33184), MaterialTag (35145), MaterialTakeoff (3388), MeasureAlongAnElement (48963), MeasureBetweenTwoReferences (48962), MechanicalEquipment (37008), MechanicalSettings (37168), MergeSurfaces (33742), MirrorDrawAxis (49000), MirrorPickAxis (32936), MirrorProject (32919), ModelInPlace (33544), ModelLine (33006), ModelText (33660), Move (33127), MultiCategoryTag (35203), NavigationBar (35631), NewAnnotationSymbol (33339), NewConceptualMass (32986), NewSheet (32958), NewTitleBlock (33140), NoteBlock (33659), NurseCall (37282), ObjectStyles (32947), Offset (33757), OpenBuildingComponent (3470), Opening (33177), OpeningByFace (35253), OpenRevitFile (57601), OpenSampleFiles (35815), Options (33195), OverrideByCategory (33422), OverrideByElement (35265), OverrideByFilter (35266), Paint (33656), PanelSchedules (37053), ParallelConduits (37361), ParallelPipes (37441), ParkingComponent (33698), PasteFromClipboard (57637), PathReinforcementSymbol (35228), Phases (33472), PickToEdit (33910), Pin (32997), Pipe (37100), PipeAccessory (37105), PipeConnector (37219), PipeFitting (37103), PipeLegend (37149), PipePlaceholder (37428), PipePressureLossReport (35812), PlaceAComponent (33003), PlaceDecal (33789), PlaceDetailGroup (33421), PlaceMass (42644), PlaceOnHost (35807), PlaceView (33132), PlanRegion (33900), PlumbingFixture (37203), PointCloud (32963), Print (57607), PrintPreview (57609), PrintSetup (57606), ProjectBrowser (32957), ProjectInformation (33543), ProjectParameters (33855), ProjectUnits (32950), PropertyLine (33480), PublishCoordinates (33869), PublishDGNToAutodeskBuzzsaw (3287), PublishDWFToAutodeskBuzzsaw (3284), PublishDWGToAutodeskBuzzsaw (3283), PublishDXFToAutodeskBuzzsaw (3285), PublishSATToAutodeskBuzzsaw (3289), PurgeUnused (33780), RadialDimension (48958), RadialDimensionTypes (1199), Railing (34969), Ramp (33316), RebarCoverSettings (35003), RebarLine (33810), RecentFiles (35364), ReconcileHosting (35708), ReferenceLine (34994), ReferencePlane (33026), ReflectedCeilingPlan (33380), ReinforcementNumbers (4700), ReinforcementSettings (35300), RelinquishAllMine (3363), ReloadLatest (1729), RelocateProject (33856), RemoveCoping (46451), RemoveHiddenLinesByElement (33673), RemovePaint (33657), Render (1782), RenderGallery (53962), RenderInCloud (53961), RepeatComponent (840), RepeatingDetailComponent (42058), ReplicateWindow (57648), ReportSharedCoordinates (33865), ResetAnalyticalModel (3288), RestoreBackup (33690), ResultsAndCompare (53614), RevealWall (33654), ReviewWarnings (33352), RevisionCloud (33540), RevisionSchedule (3154), RoofByExtrusion (1143), RoofByFace (20), RoofByFootprint (1142), Room (33198), RoomSeparator (33318), RoomTag (33208), Rotate (32934), RotateProjectNorth (32920), RotateTrueNorth (33857), RunEnergySimulation (53613), RunInterferenceCheck (3259), Save (57603), SaveAsLibraryFamily (33923), SaveAsLibraryGroup (33696), SaveAsLibraryView (42312), SaveAsProject (57604), SaveAsTemplate (49783), SaveSelection (35181), Scale (34986), ScheduleOrQuantities (33296), ScopeBox (33519), Section (32955), SectionTags (3169), Security (37283), SelectById (33867), SelectionBox (35857), SelectLink (35111), SetWorkPlane (33527), ShaftOpening (35257), SharedParameters (33748), SheetIssuesOrRevisions (3153), SheetList (33631), ShowDisconnects (37444), ShowEnergyModel (53964), ShowHiddenLinesByElement (33671), ShowHistory (1985), ShowLastReport (46061), ShowMassByViewSettings (35075), ShowMassFormAndFloors (35060), ShowMassSurfaceTypes (35078), ShowMassZonesAndShades (35079), ShowWorkPlane (40484), SingleFabricSheetPlacement (35823), SiteComponent (40239), Slab (35156), SlabEdgeFloor (40603), Snaps (32949), Soffit (493), SolidBlend (33278), SolidExtrusion (33002), SolidRevolve (33287), SolidSweep (33300), SolidSweptBlend (47163), Space (32784), SpaceSeparator (32786), SpaceTag (32785), SpanDirectionSymbol (34980), SpecifyCoordinatesAtPoint (3266), SplineWire (37261), SplitElement (1100), SplitFace (35732), SplitSurface (1992), SplitWithGap (33829), SpotCoordinate (1114), SpotCoordinateTypes (33351), SpotElevation (1109), SpotElevationTypes (33350), SpotSlope (35259), SpotSlopeTypes (33348), Sprinkler (37206), Stair (32916), StairBySketch (50126), StairPath (33010), StairTreadOrRiserNumber (53827), StartingView (33327), StatusBar (59393), StatusBarDesignOptions (4610), StatusBarWorksets (4609), StructuralAreaReinforcement (46932), StructuralColumn (34974), StructuralFabricArea (35781), StructuralFloor (34985), StructuralPathReinforcement (35225), StructuralPlan (32952), StructuralRebar (35098), StructuralSettings (34993), StructuralTrusses (43213), StructuralWall (34975), Subregion (34964), SunSettings (12299), SweepWall (33655), SwitchJoinOrder (33731), Symbol (33221), SymbolicLine (33700), SynchronizeAndModifySettings (33542), SynchronizeNow (42654), SystemBrowser (3280), TagAllNotTagged (33735), TagByCategory (33329), Telephone (37284), TemporaryDimensions (33100), Text (33134), ThinLines (33834), TileWindows (57652), TogglePropertiesPalette (4534), TopChord (3620), Toposurface (33641), TransferProjectStandards (33699), TrimOrExtendMultipleElements (48954), TrimOrExtendSingleElement (48953), TrimOrExtendToCorner (48952), TypeProperties (3302), UncutGeometry (33408), UnjoinGeometry (33730), Unpin (33001), UseCurrentProject (35110), UserKeynote (35160), VerticalOpening (35254), ViewCube (35458), ViewList (1075), ViewRange (33176), ViewReference (33906), VisibilityOrGraphics (33175), VoidBlend (33398), VoidExtrusion (33397), VoidRevolve (33399), VoidSweep (33400), VoidSweptBlend (47164), Wall (35113), WallByFaceWall (35074), WallJoins (33323), WallOpening (35256), Web (3619), Window (32773), Worksets (33460), Zone (37244)
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

    AcquireCoordinates = None
    ActivateView = None
    AddToSet = None
    AdjustAnalyticalModel = None
    AirTerminal = None
    Align = None
    AlignedDimension = None
    AlignedMultiRebarAnnotation = None
    AlignedToCurrentView = None
    AlignedToPickedLevel = None
    AlignedToSamePlace = None
    AlignedToSelectedLevels = None
    AlignedToSelectedViews = None
    AllowableBarTypes = None
    AnalysisDisplayStyles = None
    AnalyticalConsistencyChecks = None
    AngularDimension = None
    AngularDimensionTypes = None
    ApplyCoping = None
    ApplyTemplatePropertiesToCurrentView = None
    ArchitecturalColumn = None
    ArchitecturalFloor = None
    ArchitecturalWall = None
    ArcLengthDimension = None
    ArcWire = None
    Area = None
    AreaAndVolumeComputations = None
    AreaBoundary = None
    AreaPlan = None
    AreaReinforcementSymbol = None
    AreaTag = None
    Array = None
    Arrowheads = None
    AssemblyCode = None
    AutomaticBeamSystem = None
    AutomaticCeiling = None
    Beam = None
    BeamAnnotations = None
    BeamOrColumnJoins = None
    BeamSystemSymbol = None
    BottomChord = None
    BoundaryConditions = None
    Brace = None
    BrowserOrganization = None
    BuildingElevation = None
    BuildingOrSpaceTypeSettings = None
    BuildingPad = None
    CableTray = None
    CableTrayConnector = None
    CableTrayFitting = None
    Callout = None
    CalloutTags = None
    Camera = None
    CascadeWindows = None
    ChamferedWire = None
    CheckCircuits = None
    CheckDuctSystems = None
    CheckMemberSupports = None
    CheckPipeSystems = None
    CheckSpelling = None
    Close = None
    CloseHiddenWindows = None
    ColorFillLegend = None
    ColorSchemes = None
    Communication = None
    Conduit = None
    ConduitConnector = None
    ConduitFitting = None
    Control = None
    ConvertToFlexDuct = None
    CoordinationSettings = None
    Copy = None
    CopyToClipboard = None
    CreateAssembly = None
    CreateGroup = None
    CreateParts = None
    CreateSimilar = None
    CreateTemplateFromCurrentView = None
    CurtainGrid = None
    CurtainSystemByFace = None
    CurtainWallMullion = None
    CutGeometry = None
    CutProfile = None
    CutToClipboard = None
    Data = None
    DeactivateView = None
    DecalTypes = None
    Default3DView = None
    Delete = None
    DemandFactors = None
    Demolish = None
    DesignOptions = None
    DetailComponent = None
    DetailLevel = None
    DetailLine = None
    DiameterDimension = None
    DiameterDimensionTypes = None
    DisplaceElements = None
    Door = None
    DormerOpening = None
    DraftingView = None
    DrawOnFace = None
    DrawOnWorkPlane = None
    Duct = None
    DuctAccessory = None
    DuctConnector = None
    DuctFitting = None
    DuctLegend = None
    DuctPlaceholder = None
    DuctPressureLossReport = None
    DuplicateAsDependent = None
    DuplicateView = None
    DuplicateWithDetailing = None
    DWFMarkup = None
    EditATemplate = None
    EditingRequests = None
    EditRebarCover = None
    EditSelection = None
    ElectricalConnector = None
    ElectricalEquipment = None
    ElectricalFixture = None
    ElectricalSettings = None
    ElementKeynote = None
    ElevationTags = None
    EnergySettings = None
    ExitRevit = None
    ExportBuildingSite = None
    ExportCADFormatsACIS_SAT = None
    ExportCADFormatsDGN = None
    ExportCADFormatsDWG = None
    ExportCADFormatsDXF = None
    ExportDWFOrDWFx = None
    ExportExportTypes = None
    ExportFBX = None
    ExportGBXML = None
    ExportIFC = None
    ExportImagesandAnimationsImage = None
    ExportImagesandAnimationsSolarStudy = None
    ExportImagesandAnimationsWalkthrough = None
    ExportMassModelGBXML = None
    ExportODBCDatabase = None
    ExportOptionsExportSetupsDGN = None
    ExportOptionsExportSetupsDWGOrDXF = None
    ExportOptionsIFCOptions = None
    ExportReportsRoomOrAreaReport = None
    ExportReportsSchedule = None
    FabricationPart = None
    FabricationSettings = None
    FabricReinforcementSymbol = None
    FamilyCategoryAndParameters = None
    FamilyTypes = None
    Fascia = None
    FilledRegion = None
    FillPatterns = None
    Filters = None
    FindOrReplace = None
    FireAlarm = None
    FlexDuct = None
    FlexPipe = None
    FloorByFaceFloor = None
    FloorPlan = None
    FormWorkPlaneView = None
    FramingElevation = None
    GradedRegion = None
    GraphicalColumnSchedule = None
    GrayInactiveWorksets = None
    Grid = None
    GuideGrid = None
    Gutter = None
    HalftoneOrUnderlay = None
    HeatingAndCoolingLoads = None
    HideCategory = None
    HideElements = None
    IdsOfSelection = None
    ImportCAD = None
    ImportGBXML = None
    ImportTypes = None
    InPlaceMass = None
    Insert2DElementsFromFile = None
    InsertViewsFromFile = None
    Insulation = None
    Isolated = None
    JoinGeometry = None
    JoinOrUnjoinRoof = None
    KeyboardShortcuts = None
    KeynoteLegend = None
    KeynotingSettings = None
    Label = None
    LabelContours = None
    Legend = None
    LegendComponent = None
    Level = None
    Lighting = None
    LightingFixture = None
    LinearDimension = None
    LinearDimensionTypes = None
    LinearMultiRebarAnnotation = None
    LinePatterns = None
    LineStyles = None
    LineWeights = None
    Linework = None
    LinkCAD = None
    LinkIFC = None
    LinkRevit = None
    LoadAsGroup = None
    LoadCases = None
    LoadClassifications = None
    LoadCombinations = None
    LoadedTagsAndSymbols = None
    Loads = None
    LoadSelection = None
    LoadShapes = None
    Location = None
    MacroManager = None
    MacroSecurity = None
    MajorSegment = None
    ManageConnectionToARevitServerAccelerator = None
    ManageImages = None
    ManageLinks = None
    ManageTemplates = None
    ManageViewTemplates = None
    MaskingRegion = None
    Matchline = None
    MatchTypeProperties = None
    MaterialAssets = None
    MaterialKeynote = None
    Materials = None
    MaterialTag = None
    MaterialTakeoff = None
    MeasureAlongAnElement = None
    MeasureBetweenTwoReferences = None
    MechanicalEquipment = None
    MechanicalSettings = None
    MergeSurfaces = None
    MirrorDrawAxis = None
    MirrorPickAxis = None
    MirrorProject = None
    ModelInPlace = None
    ModelLine = None
    ModelText = None
    Move = None
    MultiCategoryTag = None
    NavigationBar = None
    NewAnnotationSymbol = None
    NewConceptualMass = None
    NewSheet = None
    NewTitleBlock = None
    NoteBlock = None
    NurseCall = None
    ObjectStyles = None
    Offset = None
    OpenBuildingComponent = None
    Opening = None
    OpeningByFace = None
    OpenRevitFile = None
    OpenSampleFiles = None
    Options = None
    OverrideByCategory = None
    OverrideByElement = None
    OverrideByFilter = None
    Paint = None
    PanelSchedules = None
    ParallelConduits = None
    ParallelPipes = None
    ParkingComponent = None
    PasteFromClipboard = None
    PathReinforcementSymbol = None
    Phases = None
    PickToEdit = None
    Pin = None
    Pipe = None
    PipeAccessory = None
    PipeConnector = None
    PipeFitting = None
    PipeLegend = None
    PipePlaceholder = None
    PipePressureLossReport = None
    PlaceAComponent = None
    PlaceDecal = None
    PlaceDetailGroup = None
    PlaceMass = None
    PlaceOnHost = None
    PlaceView = None
    PlanRegion = None
    PlumbingFixture = None
    PointCloud = None
    Print = None
    PrintPreview = None
    PrintSetup = None
    ProjectBrowser = None
    ProjectInformation = None
    ProjectParameters = None
    ProjectUnits = None
    PropertyLine = None
    PublishCoordinates = None
    PublishDGNToAutodeskBuzzsaw = None
    PublishDWFToAutodeskBuzzsaw = None
    PublishDWGToAutodeskBuzzsaw = None
    PublishDXFToAutodeskBuzzsaw = None
    PublishSATToAutodeskBuzzsaw = None
    PurgeUnused = None
    RadialDimension = None
    RadialDimensionTypes = None
    Railing = None
    Ramp = None
    RebarCoverSettings = None
    RebarLine = None
    RecentFiles = None
    ReconcileHosting = None
    ReferenceLine = None
    ReferencePlane = None
    ReflectedCeilingPlan = None
    ReinforcementNumbers = None
    ReinforcementSettings = None
    RelinquishAllMine = None
    ReloadLatest = None
    RelocateProject = None
    RemoveCoping = None
    RemoveHiddenLinesByElement = None
    RemovePaint = None
    Render = None
    RenderGallery = None
    RenderInCloud = None
    RepeatComponent = None
    RepeatingDetailComponent = None
    ReplicateWindow = None
    ReportSharedCoordinates = None
    ResetAnalyticalModel = None
    RestoreBackup = None
    ResultsAndCompare = None
    RevealWall = None
    ReviewWarnings = None
    RevisionCloud = None
    RevisionSchedule = None
    RoofByExtrusion = None
    RoofByFace = None
    RoofByFootprint = None
    Room = None
    RoomSeparator = None
    RoomTag = None
    Rotate = None
    RotateProjectNorth = None
    RotateTrueNorth = None
    RunEnergySimulation = None
    RunInterferenceCheck = None
    Save = None
    SaveAsLibraryFamily = None
    SaveAsLibraryGroup = None
    SaveAsLibraryView = None
    SaveAsProject = None
    SaveAsTemplate = None
    SaveSelection = None
    Scale = None
    ScheduleOrQuantities = None
    ScopeBox = None
    Section = None
    SectionTags = None
    Security = None
    SelectById = None
    SelectionBox = None
    SelectLink = None
    SetWorkPlane = None
    ShaftOpening = None
    SharedParameters = None
    SheetIssuesOrRevisions = None
    SheetList = None
    ShowDisconnects = None
    ShowEnergyModel = None
    ShowHiddenLinesByElement = None
    ShowHistory = None
    ShowLastReport = None
    ShowMassByViewSettings = None
    ShowMassFormAndFloors = None
    ShowMassSurfaceTypes = None
    ShowMassZonesAndShades = None
    ShowWorkPlane = None
    SingleFabricSheetPlacement = None
    SiteComponent = None
    Slab = None
    SlabEdgeFloor = None
    Snaps = None
    Soffit = None
    SolidBlend = None
    SolidExtrusion = None
    SolidRevolve = None
    SolidSweep = None
    SolidSweptBlend = None
    Space = None
    SpaceSeparator = None
    SpaceTag = None
    SpanDirectionSymbol = None
    SpecifyCoordinatesAtPoint = None
    SplineWire = None
    SplitElement = None
    SplitFace = None
    SplitSurface = None
    SplitWithGap = None
    SpotCoordinate = None
    SpotCoordinateTypes = None
    SpotElevation = None
    SpotElevationTypes = None
    SpotSlope = None
    SpotSlopeTypes = None
    Sprinkler = None
    Stair = None
    StairBySketch = None
    StairPath = None
    StairTreadOrRiserNumber = None
    StartingView = None
    StatusBar = None
    StatusBarDesignOptions = None
    StatusBarWorksets = None
    StructuralAreaReinforcement = None
    StructuralColumn = None
    StructuralFabricArea = None
    StructuralFloor = None
    StructuralPathReinforcement = None
    StructuralPlan = None
    StructuralRebar = None
    StructuralSettings = None
    StructuralTrusses = None
    StructuralWall = None
    Subregion = None
    SunSettings = None
    SweepWall = None
    SwitchJoinOrder = None
    Symbol = None
    SymbolicLine = None
    SynchronizeAndModifySettings = None
    SynchronizeNow = None
    SystemBrowser = None
    TagAllNotTagged = None
    TagByCategory = None
    Telephone = None
    TemporaryDimensions = None
    Text = None
    ThinLines = None
    TileWindows = None
    TogglePropertiesPalette = None
    TopChord = None
    Toposurface = None
    TransferProjectStandards = None
    TrimOrExtendMultipleElements = None
    TrimOrExtendSingleElement = None
    TrimOrExtendToCorner = None
    TypeProperties = None
    UncutGeometry = None
    UnjoinGeometry = None
    Unpin = None
    UseCurrentProject = None
    UserKeynote = None
    value__ = None
    VerticalOpening = None
    ViewCube = None
    ViewList = None
    ViewRange = None
    ViewReference = None
    VisibilityOrGraphics = None
    VoidBlend = None
    VoidExtrusion = None
    VoidRevolve = None
    VoidSweep = None
    VoidSweptBlend = None
    Wall = None
    WallByFaceWall = None
    WallJoins = None
    WallOpening = None
    Web = None
    Window = None
    Worksets = None
    Zone = None


class PreviewControl(UserControl, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient, IAddChild, IDisposable):
    """
    Presents a preview control to browse the Revit model.
    
    PreviewControl(document: Document, viewId: ElementId)
    """
    def AddChild(self, *args): #cannot find CLR method
        """
        AddChild(self: ContentControl, value: object)
            Adds a specified object as the child of a 
             System.Windows.Controls.ContentControl.
        
        
            value: The object to add.
        """
        pass

    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        """
        pass

    def AddText(self, *args): #cannot find CLR method
        """
        AddText(self: ContentControl, text: str)
            Adds a specified text string to a System.Windows.Controls.ContentControl.
        
            text: The string to add.
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Control, arrangeBounds: Size) -> Size
        
            Called to arrange and size the content of a System.Windows.Controls.Control 
             object.
        
        
            arrangeBounds: The computed size that is used to arrange the content.
            Returns: The size of the control.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: PreviewControl)
            This method is called if the user explicitly disposes of the
        object (by 
             calling the Dispose method in other managed languages, 
        or the destructor in 
             C++).
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Control, constraint: Size) -> Size
        
            Called to remeasure a control.
        
            constraint: The maximum size that the method can return.
            Returns: The size of the control, up to the maximum specified by constraint.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        """
        pass

    def OnContentChanged(self, *args): #cannot find CLR method
        """
        OnContentChanged(self: ContentControl, oldContent: object, newContent: object)
            Called when the System.Windows.Controls.ContentControl.Content property changes.
        
            oldContent: The old value of the System.Windows.Controls.ContentControl.Content property.
            newContent: The new value of the System.Windows.Controls.ContentControl.Content property.
        """
        pass

    def OnContentStringFormatChanged(self, *args): #cannot find CLR method
        """
        OnContentStringFormatChanged(self: ContentControl, oldContentStringFormat: str, newContentStringFormat: str)
            Occurs when the System.Windows.Controls.ContentControl.ContentStringFormat 
             property changes.
        
        
            oldContentStringFormat: The old value of System.Windows.Controls.ContentControl.ContentStringFormat.
            newContentStringFormat: The new value of System.Windows.Controls.ContentControl.ContentStringFormat.
        """
        pass

    def OnContentTemplateChanged(self, *args): #cannot find CLR method
        """
        OnContentTemplateChanged(self: ContentControl, oldContentTemplate: DataTemplate, newContentTemplate: DataTemplate)
            Called when the System.Windows.Controls.ContentControl.ContentTemplate property 
             changes.
        
        
            oldContentTemplate: The old value of the System.Windows.Controls.ContentControl.ContentTemplate 
             property.
        
            newContentTemplate: The new value of the System.Windows.Controls.ContentControl.ContentTemplate 
             property.
        """
        pass

    def OnContentTemplateSelectorChanged(self, *args): #cannot find CLR method
        """
        OnContentTemplateSelectorChanged(self: ContentControl, oldContentTemplateSelector: DataTemplateSelector, newContentTemplateSelector: DataTemplateSelector)
            Called when the System.Windows.Controls.ContentControl.ContentTemplateSelector 
             property changes.
        
        
            oldContentTemplateSelector: The old value of the 
             System.Windows.Controls.ContentControl.ContentTemplateSelector property.
        
            newContentTemplateSelector: The new value of the 
             System.Windows.Controls.ContentControl.ContentTemplateSelector property.
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UserControl) -> AutomationPeer
        
            Creates and returns an System.Windows.Automation.Peers.AutomationPeer for this 
             System.Windows.Controls.UserControl.
        
            Returns: A new System.Windows.Automation.Peers.UserControlAutomationPeer for this 
             System.Windows.Controls.UserControl.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        """
        pass

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnMouseDoubleClick(self: Control, e: MouseButtonEventArgs)
            Raises the System.Windows.Controls.Control.MouseDoubleClick routed event.
        
            e: The event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        """
        pass

    def OnPreviewMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDoubleClick(self: Control, e: MouseButtonEventArgs)
            Raises the System.Windows.Controls.Control.PreviewMouseDoubleClick routed event.
        
            e: The event data.
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: UIElement, drawingContext: DrawingContext)
            When overridden in a derived class, participates in rendering operations that 
             are directed by the layout system. The rendering instructions for this element 
             are not used directly when this method is invoked, and are instead preserved 
             for later asynchronous use by layout and drawing.
        
        
            drawingContext: The drawing instructions for a specific element. This context is provided to 
             the layout system.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnTemplateChanged(self, *args): #cannot find CLR method
        """
        OnTemplateChanged(self: Control, oldTemplate: ControlTemplate, newTemplate: ControlTemplate)
            Called whenever the control's template changes.
        
            oldTemplate: The old template.
            newTemplate: The new template.
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
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
    def __new__(self, document, viewId):
        """ __new__(cls: type, document: Document, viewId: ElementId) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    HandlesScrolling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a control supports scrolling.

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator to the content control's logical child elements.

"""

    ScrollbarVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The visibility of the preview view scrollbars.

Get: ScrollbarVisibility(self: PreviewControl) -> ScrollbarVisibility

Set: ScrollbarVisibility(self: PreviewControl) = value
"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    UIView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The UI view representing the preview view.

Get: UIView(self: PreviewControl) -> UIView

"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view Id.

Get: ViewId(self: PreviewControl) -> ElementId

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""



class PromptForFamilyInstancePlacementOptions(object, IDisposable):
    """
    This class contains options to control the behavior of interactive placement of family instances.
    
    PromptForFamilyInstancePlacementOptions(other: PromptForFamilyInstancePlacementOptions)
    PromptForFamilyInstancePlacementOptions()
    """
    def Dispose(self):
        """ Dispose(self: PromptForFamilyInstancePlacementOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PromptForFamilyInstancePlacementOptions, disposing: bool) """
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
    def __new__(self, other=None):
        """
        __new__(cls: type, other: PromptForFamilyInstancePlacementOptions)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FaceBasedPlacementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The placement type to be used if prompting to place an instance of a face-based family.
   This option is ignored if placing a non-face-based family. If placing a face-based family, Default is an acceptable value, but will correspond to the first available selection in the user interface.

Get: FaceBasedPlacementType(self: PromptForFamilyInstancePlacementOptions) -> FaceBasedPlacementType

Set: FaceBasedPlacementType(self: PromptForFamilyInstancePlacementOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: PromptForFamilyInstancePlacementOptions) -> bool

"""

    PlaceAirTerminalOnDuct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, when placing an air terminal, the terminal will be placed directly on the duct without fittings.
   If fase, the terminal will be placed with generated fittings.

Get: PlaceAirTerminalOnDuct(self: PromptForFamilyInstancePlacementOptions) -> bool

Set: PlaceAirTerminalOnDuct(self: PromptForFamilyInstancePlacementOptions) = value
"""

    SketchGalleryOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sketch option provided when promt to place a family instance.

Get: SketchGalleryOptions(self: PromptForFamilyInstancePlacementOptions) -> SketchGalleryOptions

Set: SketchGalleryOptions(self: PromptForFamilyInstancePlacementOptions) = value
"""



class RibbonButton(RibbonItem):
    """ This class is the base class of PushButton and PulldownButton. """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, item: RibbonButton, parentId: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image of the button.

Get: Image(self: RibbonButton) -> ImageSource

Set: Image(self: RibbonButton) = value
"""

    IsEnabledByContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this button can be executed. True if the pushbutton is permitted to be executed based on the 
current Revit context (active document, active view and active tool). False if the pushbutton is disabled because 
of the active context.

Get: IsEnabledByContext(self: RibbonButton) -> bool

"""

    LargeImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The large image shown on the button.

Get: LargeImage(self: RibbonButton) -> ImageSource

Set: LargeImage(self: RibbonButton) = value
"""


    m_ItemType = None


class PulldownButton(RibbonButton):
    """ The PulldownButton object represents a button with a drop-down list on RibbonPanel. """
    def AddPushButton(self, buttonData):
        """
        AddPushButton(self: PulldownButton, buttonData: PushButtonData) -> PushButton
        
            Adds a new pushbutton to the pulldown button and associates it with an 
             ExternalCommand.
        
        
            buttonData: An object containing the data needed to construct the pushbutton.
            Returns: The newly added pushbutton.
        """
        pass

    def AddSeparator(self):
        """
        AddSeparator(self: PulldownButton)
            Adds a separator to the drop-down list.
        """
        pass

    def GetItems(self):
        """
        GetItems(self: PulldownButton) -> IList[PushButton]
        
            Gets a copy of the collection of buttons assigned to the pulldown button.
        """
        pass

    m_ItemType = None


class PulldownButtonData(ButtonData):
    """
    This class contains information necessary to construct a pulldown button in the Ribbon.
    
    PulldownButtonData(name: str, text: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, text):
        """ __new__(cls: type, name: str, text: str) """
        pass


class PushButton(RibbonButton):
    """ The PushButton object represents an button on a RibbonPanel. """
    def setAssemblyName(self, *args): #cannot find CLR method
        """ setAssemblyName(self: PushButton, assemblyName: str) """
        pass

    def setAvailabilityClassName(self, *args): #cannot find CLR method
        """ setAvailabilityClassName(self: PushButton, availabilityClassName: str) """
        pass

    def setClassName(self, *args): #cannot find CLR method
        """ setClassName(self: PushButton, className: str) """
        pass

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The assembly path of the button.

Get: AssemblyName(self: PushButton) -> str

Set: AssemblyName(self: PushButton) = value
"""

    AvailabilityClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full class name for the class providing the entry point to decide availability of this push button.

Get: AvailabilityClassName(self: PushButton) -> str

Set: AvailabilityClassName(self: PushButton) = value
"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the class containing the implementation for the command.

Get: ClassName(self: PushButton) -> str

Set: ClassName(self: PushButton) = value
"""


    m_ItemType = None


class PushButtonData(ButtonData):
    """
    This class contains information necessary to construct a push button in the Ribbon.
    
    PushButtonData(name: str, text: str, assemblyName: str, className: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, text, assemblyName, className):
        """ __new__(cls: type, name: str, text: str, assemblyName: str, className: str) """
        pass

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The assembly path of the button.

Get: AssemblyName(self: PushButtonData) -> str

Set: AssemblyName(self: PushButtonData) = value
"""

    AvailabilityClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full class name for the class providing the entry point to decide availability of this push button.

Get: AvailabilityClassName(self: PushButtonData) -> str

Set: AvailabilityClassName(self: PushButtonData) = value
"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the class containing the implementation for the command.

Get: ClassName(self: PushButtonData) -> str

Set: ClassName(self: PushButtonData) = value
"""



class RadioButtonGroup(RibbonItem):
    """ Represents a group of related buttons in the Ribbon. """
    def AddItem(self, buttonData):
        """
        AddItem(self: RadioButtonGroup, buttonData: ToggleButtonData) -> ToggleButton
        
            Adds a new ToggleButton to the RadioButtonGroup.
        
            buttonData: An object containing the data needed to construct the ToggleButton.
            Returns: The newly added ToggleButton.
        """
        pass

    def AddItems(self, buttonData):
        """ AddItems(self: RadioButtonGroup, buttonData: IList[ToggleButtonData]) -> IList[ToggleButton] """
        pass

    def GetItems(self):
        """
        GetItems(self: RadioButtonGroup) -> IList[ToggleButton]
        
            Gets the collection of ToggleButtons assigned to the RadioButtonGroup.
        """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current checked ToggleButton of the RadioButtonGroup.

Get: Current(self: RadioButtonGroup) -> ToggleButton

Set: Current(self: RadioButtonGroup) = value
"""


    m_ItemType = None


class RadioButtonGroupData(RibbonItemData):
    """
    This class contains information necessary to construct a ribbon gallery in the Ribbon.
    
    RadioButtonGroupData(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass


class Result(Enum, IComparable, IFormattable, IConvertible):
    """
    Informs Autodesk Revit of the status of your application after execution.
    
    enum Result, values: Cancelled (1), Failed (-1), Succeeded (0)
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

    Cancelled = None
    Failed = None
    Succeeded = None
    value__ = None


class RevitCommandId(object, IDisposable):
    """ Represents a command id in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: RevitCommandId) """
        pass

    @staticmethod
    def LookupCommandId(name):
        """
        LookupCommandId(name: str) -> RevitCommandId
        
            Looks up and retrieves the Revit command id with the given id string.
        
            name: he Revit command name. Refer to the entries in the Revit journal to find the 
             string to use for a particular command.
        
            Returns: The Revit command id. Returning "null" if a command with the given name was not 
             found.
        """
        pass

    @staticmethod
    def LookupPostableCommandId(postableCommand):
        """
        LookupPostableCommandId(postableCommand: PostableCommand) -> RevitCommandId
        
            Looks up and retrieves the Revit command id with the given id string.
        
            postableCommand: The postable command.
            Returns: The Revit command id. Returning ll if a command with the given name was not 
             found.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitCommandId, disposing: bool) """
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

    CanHaveBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the command can be assigned a binding to an external add-in.

Get: CanHaveBinding(self: RevitCommandId) -> bool

"""

    HasBinding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether a replacement of either the Execute or CanExecute events (or both) have been applied to this command.

Get: HasBinding(self: RevitCommandId) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The command id.

Get: Id(self: RevitCommandId) -> UInt32

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RevitCommandId) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The command name.

Get: Name(self: RevitCommandId) -> str

"""



class RevitLinkUIUtils(object):
    """
    A class containing functions for displaying user interface related to
       Revit links.
    """
    @staticmethod
    def ReportLinkLoadResults(doc, loadResults):
        """ ReportLinkLoadResults(doc: Document, loadResults: IDictionary[str, RevitLinkLoadResult]) """
        pass

    __all__ = [
        'ReportLinkLoadResults',
    ]


class RibbonItemType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all the toolbar item styles.
    
    enum RibbonItemType, values: ComboBox (6), ComboBoxMember (5), PulldownButton (1), PushButton (0), RadioButtonGroup (4), SplitButton (2), TextBox (7), ToggleButton (3)
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

    ComboBox = None
    ComboBoxMember = None
    PulldownButton = None
    PushButton = None
    RadioButtonGroup = None
    SplitButton = None
    TextBox = None
    ToggleButton = None
    value__ = None


class RibbonPanel(object):
    """ Represents a panel added by an External Application or External Command into the Add-Ins tab. """
    def AddItem(self, itemData):
        """
        AddItem(self: RibbonPanel, itemData: RibbonItemData) -> RibbonItem
        
            Adds a Ribbon item to the panel.
        
            itemData: Data containing information about the new item.
            Returns: The added Ribbon item.
        """
        pass

    def AddSeparator(self):
        """
        AddSeparator(self: RibbonPanel)
            Adds a new Separator to the panel.
        """
        pass

    def AddSlideOut(self):
        """
        AddSlideOut(self: RibbonPanel)
            Adds a slideout to the current panel.
        """
        pass

    def AddStackedItems(self, item1, item2, item3=None):
        """
        AddStackedItems(self: RibbonPanel, item1: RibbonItemData, item2: RibbonItemData) -> IList[RibbonItem]
        
            Adds two stacked items to the panel.
        
            item1: Data containing information about the first item. This data must be of type 
             PushButtonData, PulldownButtonData, SplitButtonData, ComboBoxData, or 
             TextBoxData.
        
            item2: Data containing information about the second item. This data must be of type 
             PushButtonData, PulldownButtonData, SplitButtonData, ComboBoxData, or 
             TextBoxData.
        
            Returns: A collection containing the added items.
        AddStackedItems(self: RibbonPanel, item1: RibbonItemData, item2: RibbonItemData, item3: RibbonItemData) -> IList[RibbonItem]
        
            Adds three stacked items to the panel.
        
            item1: Data containing information about the first item. This data must be of type 
             PushButtonData, PulldownButtonData, SplitButtonData, ComboBoxData, or 
             TextBoxData.
        
            item2: Data containing information about the second item. This data must be of type 
             PushButtonData, PulldownButtonData, SplitButtonData, ComboBoxData, or 
             TextBoxData.
        
            item3: Data containing information about the third item. This data must be of type 
             PushButtonData, PulldownButtonData, SplitButtonData, ComboBoxData, or 
             TextBoxData.
        
            Returns: A collection containing the added items.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: RibbonPanel, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to the current 
             System.Object.
        
        
            obj: Another panel object.
        """
        pass

    def GetItems(self):
        """
        GetItems(self: RibbonPanel) -> IList[RibbonItem]
        
            Gets a copy of the collection of RibbonItems assigned to the RibbonPanel.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the RibbonPanel can respond to user interaction.

Get: Enabled(self: RibbonPanel) -> bool

Set: Enabled(self: RibbonPanel) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the RibbonPanel.

Get: Name(self: RibbonPanel) -> str

Set: Name(self: RibbonPanel) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text of the RibbonPanel.

Get: Title(self: RibbonPanel) -> str

Set: Title(self: RibbonPanel) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the RibbonPanel is displayed.

Get: Visible(self: RibbonPanel) -> bool

Set: Visible(self: RibbonPanel) = value
"""



class ScrollbarVisibility(Enum, IComparable, IFormattable, IConvertible):
    """
    Lists all the visibility types of the scrollbar in the preview view.
    
    enum ScrollbarVisibility, values: Both (3), Horizontal (1), None (0), Vertical (2)
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

    Both = None
    Horizontal = None
    None = None
    value__ = None
    Vertical = None


class SelectionUIOptions(object, IDisposable):
    """ Provides access to user settings related to how selection will behave in Revit's UI. """
    def Dispose(self):
        """ Dispose(self: SelectionUIOptions) """
        pass

    @staticmethod
    def ElementSelectsAsPinned(document, element):
        """
        ElementSelectsAsPinned(document: Document, element: Element) -> bool
        
            Checks whether the specified element will be treated as pinned for the purposes 
             of selection.
        
        
            document: The document containing the element.
            element: The element to check.
            Returns: True if the specified element should be treated as pinned for selection 
             purposes, false otherwise.
        """
        pass

    @staticmethod
    def GetSelectionUIOptions():
        """
        GetSelectionUIOptions() -> SelectionUIOptions
        
            Returns the current user's SelectionOptions.
            Returns: The SelectionOptions for the current user.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SelectionUIOptions, disposing: bool) """
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

    DragOnSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether elements can be dragged immediately when they are selected.

Get: DragOnSelection(self: SelectionUIOptions) -> bool

Set: DragOnSelection(self: SelectionUIOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SelectionUIOptions) -> bool

"""

    SelectFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether elements can be selected by clicking on the interior of a face.

Get: SelectFaces(self: SelectionUIOptions) -> bool

Set: SelectFaces(self: SelectionUIOptions) = value
"""

    SelectLinks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether Revit and CAD link instances can be selected.

Get: SelectLinks(self: SelectionUIOptions) -> bool

Set: SelectLinks(self: SelectionUIOptions) = value
"""

    SelectPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether pinned elements can be selected.

Get: SelectPinned(self: SelectionUIOptions) -> bool

Set: SelectPinned(self: SelectionUIOptions) = value
"""

    SelectUnderlay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether elements that are displayed as underlay can be selected.

Get: SelectUnderlay(self: SelectionUIOptions) -> bool

Set: SelectUnderlay(self: SelectionUIOptions) = value
"""



class SetupEnergySimulationDialog(object, IDisposable):
    """
    The Revit dialog which typically precedes invocation of an Energy Simulation run on the Green Building Studio server.
    
    SetupEnergySimulationDialog()
    """
    def Dispose(self):
        """ Dispose(self: SetupEnergySimulationDialog) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SetupEnergySimulationDialog, disposing: bool) """
        pass

    def Show(self):
        """
        Show(self: SetupEnergySimulationDialog) -> SetupEnergySimulationDialogResult
        
            Shows the SetupEnergySimulationDialog to the user as a modal dialog.
            Returns: One of the Autodesk.Revit.UI.SetupEnergySimulationDialogResult values.
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

Get: IsValidObject(self: SetupEnergySimulationDialog) -> bool

"""

    ProjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier of the project (on the Green Building Studio server) that was selected by the user.

Get: ProjectId(self: SetupEnergySimulationDialog) -> int

"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The project name (representing a project on the Green Building Studio server) selected or supplied by the user.

Get: ProjectName(self: SetupEnergySimulationDialog) -> str

"""

    RunName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the analysis run that was supplied by the user.

Get: RunName(self: SetupEnergySimulationDialog) -> str

"""



class SetupEnergySimulationDialogResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies identifiers to indicate the return value of the SetupEnergySimulationDialog
    
    enum SetupEnergySimulationDialogResult, values: Cancel (2), Continue (1)
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

    Cancel = None
    Continue = None
    value__ = None


class SketchGalleryOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Enumerates all the sketch options.
    
    enum SketchGalleryOptions, values: SGO_Arc3Point (6), SGO_ArcCenterEnds (7), SGO_ArcFillet (9), SGO_ArcTanEnd (8), SGO_Circle (5), SGO_CircumscribedPolygon (4), SGO_Default (0), SGO_FullEllipse (12), SGO_InscribedPolygon (3), SGO_LandingSquare (25), SGO_LandingWithTwoRuns (30), SGO_Line (1), SGO_PartialEllipse (13), SGO_PickFaces (15), SGO_PickLines (14), SGO_PickPoints (20), SGO_PickRoofs (18), SGO_PickSupports (17), SGO_PickWalls (16), SGO_Point (19), SGO_PointElement (21), SGO_Rect (2), SGO_RunArcCenterEnds (24), SGO_RunArcFullStep (23), SGO_RunLine (22), SGO_SketchLanding (32), SGO_SketchRun (31), SGO_Spline (10), SGO_SplineByPoints (11), SGO_SupportPickLine (28), SGO_WinderLShape (26), SGO_WinderPattern (27), SGO_WinderUShape (29)
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

    SGO_Arc3Point = None
    SGO_ArcCenterEnds = None
    SGO_ArcFillet = None
    SGO_ArcTanEnd = None
    SGO_Circle = None
    SGO_CircumscribedPolygon = None
    SGO_Default = None
    SGO_FullEllipse = None
    SGO_InscribedPolygon = None
    SGO_LandingSquare = None
    SGO_LandingWithTwoRuns = None
    SGO_Line = None
    SGO_PartialEllipse = None
    SGO_PickFaces = None
    SGO_PickLines = None
    SGO_PickPoints = None
    SGO_PickRoofs = None
    SGO_PickSupports = None
    SGO_PickWalls = None
    SGO_Point = None
    SGO_PointElement = None
    SGO_Rect = None
    SGO_RunArcCenterEnds = None
    SGO_RunArcFullStep = None
    SGO_RunLine = None
    SGO_SketchLanding = None
    SGO_SketchRun = None
    SGO_Spline = None
    SGO_SplineByPoints = None
    SGO_SupportPickLine = None
    SGO_WinderLShape = None
    SGO_WinderPattern = None
    SGO_WinderUShape = None
    value__ = None


class SplitButton(PulldownButton):
    """ The SplitButton object represents a button with a clickable button appearing above a pulldown. """
    CurrentButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current PushButton of the SplitButton.

Get: CurrentButton(self: SplitButton) -> PushButton

Set: CurrentButton(self: SplitButton) = value
"""

    IsSynchronizedWithCurrentItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the top PushButton on the SplitButton changes based on the CurrentButton property.

Get: IsSynchronizedWithCurrentItem(self: SplitButton) -> bool

Set: IsSynchronizedWithCurrentItem(self: SplitButton) = value
"""


    m_ItemType = None


class SplitButtonData(PulldownButtonData):
    """
    This class contains information necessary to construct a split button in the Ribbon.
    
    SplitButtonData(name: str, text: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, text):
        """ __new__(cls: type, name: str, text: str) """
        pass


class Tab(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing static tabs which support addition of panels via the API.
    
    enum Tab, values: AddIns (0), Analyze (1)
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

    AddIns = None
    Analyze = None
    value__ = None


class TabbedDialogAction(MulticastDelegate, ICloneable, ISerializable):
    """
    Delegate for tabbed dialog actions, such as OnOK, OnCancel and RestoreDefaults.
    
    TabbedDialogAction(A_0: object, A_1: IntPtr)
    """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: TabbedDialogAction, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new 
             delegate.
        
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by 
             the current delegate.-or- null, if the method represented by the current 
             delegate does not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TabbedDialogAction, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self):
        """ Invoke(self: TabbedDialogAction) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate 
             that is equal to the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new 
             System.Delegate without value in its invocation list; otherwise, this instance 
             with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class TabbedDialogExtension(object):
    """
    Contains the information required to create and implement the behavior for the new tab inside 
    the Revit options dialog.
    
    TabbedDialogExtension(userControl: UserControl, onOK: TabbedDialogAction)
    """
    def GetContextualHelp(self):
        """
        GetContextualHelp(self: TabbedDialogExtension) -> ContextualHelp
        
            Gets the contextual help.
            Returns: The contextual help assigned to the help button of the Revit options dialog, or 
             ll if there is no binding assigned.
        """
        pass

    def SetContextualHelp(self, contextualHelp):
        """
        SetContextualHelp(self: TabbedDialogExtension, contextualHelp: ContextualHelp)
            Sets the contextual help.
        
            contextualHelp: The contextual help.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, userControl, onOK):
        """ __new__(cls: type, userControl: UserControl, onOK: TabbedDialogAction) """
        pass

    Control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The control.

Get: Control(self: TabbedDialogExtension) -> UserControl

"""

    OnCancelAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The cancel handler.

Get: OnCancelAction(self: TabbedDialogExtension) -> TabbedDialogAction

Set: OnCancelAction(self: TabbedDialogExtension) = value
"""

    OnOKAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ok handler.

Get: OnOKAction(self: TabbedDialogExtension) -> TabbedDialogAction

"""

    OnRestoreDefaultsAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The restore defaults handler.

Get: OnRestoreDefaultsAction(self: TabbedDialogExtension) -> TabbedDialogAction

Set: OnRestoreDefaultsAction(self: TabbedDialogExtension) = value
"""



class TableViewUIUtils(object):
    """ This utility class contains members that involve the Revit UI and operate on schedule views or MEP electrical panel schedules. """
    @staticmethod
    def TestCellAndPromptToEditTypeParameter(tableView, sectionType, row, column):
        """
        TestCellAndPromptToEditTypeParameter(tableView: TableView, sectionType: SectionType, row: int, column: int) -> bool
        
            Prompts the end-user to control whether a type parameter contained in the 
             specified table cell should be allowed edited.
        
        
            tableView: The table view.
            sectionType: The section the row lies in.
            row: The row index in the section.
            column: The column index in the section.
            Returns: Returns true if editing the cell is allowed; otherwise false.
        """
        pass

    __all__ = [
        'TestCellAndPromptToEditTypeParameter',
    ]


class TaskDialog(APIObject, IDisposable):
    """
    A task dialog is a dialog box that can be used to display information and receive simple input from the user. It has a common set of controls  
    that are arranged in a standard order to assure consistent look and feel.
    
    TaskDialog(title: str)
    """
    def AddCommandLink(self, id, mainContent, supportingContent=None):
        """
        AddCommandLink(self: TaskDialog, id: TaskDialogCommandLinkId, mainContent: str, supportingContent: str)
            Adds a CommandLink associated to the given id, displaying the indicating main 
             and supporting content.
        
        
            id: The id of the CommandLink. This corresponds to the value returned by Show() 
             when the link is chosen by the user.
        
            mainContent: The main content of the CommandLink.
            supportingContent: The main content of the CommandLink.
        AddCommandLink(self: TaskDialog, id: TaskDialogCommandLinkId, mainContent: str)
            Adds a CommandLink associated to the given id, displaying the indicating main 
             content.
        
        
            id: The id of the CommandLink. This corresponds to the value returned by Show() 
             when the link is chosen by the user.
        
            mainContent: The main content of the CommandLink.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
        pass

    @staticmethod
    def Show(title=None, mainInstruction=None, buttons=None, defaultButton=None):
        """
        Show(title: str, mainInstruction: str) -> TaskDialogResult
        
            Shows a task dialog with title, main instruction and a Close button.
        
            title: The title of the task dialog.
            mainInstruction: The main instruction of the task dialog.
            Returns: The user's response to the task dialog.
        Show(self: TaskDialog) -> TaskDialogResult
        
            Shows the task dialog.
            Returns: The user's response to the task dialog.
        Show(title: str, mainInstruction: str, buttons: TaskDialogCommonButtons, defaultButton: TaskDialogResult) -> TaskDialogResult
        
            Shows a task dialog with title, main instruction, common buttons and default 
             buttons.
        
        
            title: The title of the task dialog.
            mainInstruction: The main instruction of the task dialog.
            buttons: The common buttons to be shown the task dialog.
            defaultButton: The default button of the task dialog.
            Returns: The user's response to the task dialog.
        Show(title: str, mainInstruction: str, buttons: TaskDialogCommonButtons) -> TaskDialogResult
        
            Shows a task dialog with title, main instruction and common buttons.
        
            title: The title of the task dialog.
            mainInstruction: The main instruction of the task dialog.
            buttons: The common buttons to be shown the task dialog.
            Returns: The user's response to the task dialog.
        """
        pass

    def WasExtraCheckBoxChecked(self):
        """
        WasExtraCheckBoxChecked(self: TaskDialog) -> bool
        
            Gets the status of the extra checkbox.
            Returns: Whether the extra checkbox is checked.
        """
        pass

    def WasVerificationChecked(self):
        """
        WasVerificationChecked(self: TaskDialog) -> bool
        
            Gets the status of the verification checkbox.
            Returns: Whether the verification checkbox is checked.
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
    def __new__(self, title):
        """ __new__(cls: type, title: str) """
        pass

    AllowCancellation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the task dialog can be cancelled if no cancel button is specified.

Get: AllowCancellation(self: TaskDialog) -> bool

Set: AllowCancellation(self: TaskDialog) = value
"""

    CommonButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The push buttons displayed in the task dialog.

Get: CommonButtons(self: TaskDialog) -> TaskDialogCommonButtons

Set: CommonButtons(self: TaskDialog) = value
"""

    DefaultButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default button for the dialog.

Get: DefaultButton(self: TaskDialog) -> TaskDialogResult

Set: DefaultButton(self: TaskDialog) = value
"""

    ExpandedContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ExpandedContent is hidden by default and will display at the bottom of the task dialog when the "Show details" button is pressed.

Get: ExpandedContent(self: TaskDialog) -> str

Set: ExpandedContent(self: TaskDialog) = value
"""

    ExtraCheckBoxText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ExtraCheckBoxText is used to label the extra checkbox.

Get: ExtraCheckBoxText(self: TaskDialog) -> str

Set: ExtraCheckBoxText(self: TaskDialog) = value
"""

    FooterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FooterText is used in the footer area of the task dialog.

Get: FooterText(self: TaskDialog) -> str

Set: FooterText(self: TaskDialog) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the task dialog.

Get: Id(self: TaskDialog) -> str

Set: Id(self: TaskDialog) = value
"""

    MainContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """MainContent is the smaller text that appears just below the main instructions.

Get: MainContent(self: TaskDialog) -> str

Set: MainContent(self: TaskDialog) = value
"""

    MainIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The icon shown in the task dialog.

Get: MainIcon(self: TaskDialog) -> TaskDialogIcon

Set: MainIcon(self: TaskDialog) = value
"""

    MainInstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The large primary text that appears at the top of a task dialog.

Get: MainInstruction(self: TaskDialog) -> str

Set: MainInstruction(self: TaskDialog) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Title of the task dialog.

Get: Title(self: TaskDialog) -> str

Set: Title(self: TaskDialog) = value
"""

    TitleAutoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TaskDialog's title will automatically have the add-in name added as a prefix.

Get: TitleAutoPrefix(self: TaskDialog) -> bool

Set: TitleAutoPrefix(self: TaskDialog) = value
"""

    VerificationText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """VerificationText is used to label the verification checkbox.

Get: VerificationText(self: TaskDialog) -> str

Set: VerificationText(self: TaskDialog) = value
"""



class TaskDialogCommandLinkId(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum to specify the Id of CommandLink.
    
    enum TaskDialogCommandLinkId, values: CommandLink1 (1001), CommandLink2 (1002), CommandLink3 (1003), CommandLink4 (1004)
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

    CommandLink1 = None
    CommandLink2 = None
    CommandLink3 = None
    CommandLink4 = None
    value__ = None


class TaskDialogCommonButtons(Enum, IComparable, IFormattable, IConvertible):
    """
    A enumerated type containing the standard buttons available for Task Dialogs.
    
    enum (flags) TaskDialogCommonButtons, values: Cancel (8), Close (32), No (4), None (0), Ok (1), Retry (16), Yes (2)
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

    Cancel = None
    Close = None
    No = None
    None = None
    Ok = None
    Retry = None
    value__ = None
    Yes = None


class TaskDialogIcon(Enum, IComparable, IFormattable, IConvertible):
    """
    Standard icons to be used in the task dialog.
    
    enum TaskDialogIcon, values: TaskDialogIconNone (0), TaskDialogIconWarning (65535)
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

    TaskDialogIconNone = None
    TaskDialogIconWarning = None
    value__ = None


class TaskDialogResult(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum to specify the task dialog result.
    
    enum TaskDialogResult, values: Cancel (2), Close (8), CommandLink1 (1001), CommandLink2 (1002), CommandLink3 (1003), CommandLink4 (1004), No (7), None (0), Ok (1), Retry (4), Yes (6)
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

    Cancel = None
    Close = None
    CommandLink1 = None
    CommandLink2 = None
    CommandLink3 = None
    CommandLink4 = None
    No = None
    None = None
    Ok = None
    Retry = None
    value__ = None
    Yes = None


class TextBox(RibbonItem):
    """ The TextBox object represents text-based control that allows the user to enter text. """
    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image of the TextBox.

Get: Image(self: TextBox) -> ImageSource

Set: Image(self: TextBox) = value
"""

    PromptText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The prompt text for the text box.

Get: PromptText(self: TextBox) -> str

Set: PromptText(self: TextBox) = value
"""

    SelectTextOnFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A value that indicates if the text is selected when the text box gains focus.

Get: SelectTextOnFocus(self: TextBox) -> bool

Set: SelectTextOnFocus(self: TextBox) = value
"""

    ShowImageAsButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates if the Image set 
in the text box should be displayed as a clickable button.

Get: ShowImageAsButton(self: TextBox) -> bool

Set: ShowImageAsButton(self: TextBox) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The object that supplies the text value.

Get: Value(self: TextBox) -> object

Set: Value(self: TextBox) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the TextBox.

Get: Width(self: TextBox) -> float

Set: Width(self: TextBox) = value
"""


    EnterPressed = None
    m_ItemType = None


class TextBoxData(RibbonItemData):
    """
    This class contains information necessary to construct a text box in the Ribbon.
    
    TextBoxData(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image of the TextBox.

Get: Image(self: TextBoxData) -> ImageSource

Set: Image(self: TextBoxData) = value
"""



class TextEditorOptions(object, IDisposable):
    """ Provides access to settings that control Revit's Text Editor appearance and functionality. """
    def Dispose(self):
        """ Dispose(self: TextEditorOptions) """
        pass

    @staticmethod
    def GetTextEditorOptions():
        """
        GetTextEditorOptions() -> TextEditorOptions
        
            Returns the current Revit instance's TextEditorOptions.
            Returns: The TextEditorOptions for the current Revit instance.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TextEditorOptions, disposing: bool) """
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

Get: IsValidObject(self: TextEditorOptions) -> bool

"""

    ShowBorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Show the border box around the text during editing.

Get: ShowBorder(self: TextEditorOptions) -> bool

Set: ShowBorder(self: TextEditorOptions) = value
"""

    ShowOpaqueBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Show opaque background behind the text during editing.

Get: ShowOpaqueBackground(self: TextEditorOptions) -> bool

Set: ShowOpaqueBackground(self: TextEditorOptions) = value
"""



class ThinLinesOptions(object, IDisposable):
    """ A utility class containing setting related to the Thin Lines option which affects the display in the UI. """
    def Dispose(self):
        """ Dispose(self: ThinLinesOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ThinLinesOptions, disposing: bool) """
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

Get: IsValidObject(self: ThinLinesOptions) -> bool

"""


    AreThinLinesEnabled = False


class ToggleButton(PushButton):
    """ The ToggleButton object represents a button that has been added to a RadioButtonGroup. """
    m_ItemType = None


class ToggleButtonData(PushButtonData):
    """
    This class contains information necessary to construct a toggle button in a RadioButtonGroup.
    
    ToggleButtonData(name: str, text: str)
    ToggleButtonData(name: str, text: str, assemblyName: str, className: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, text, assemblyName=None, className=None):
        """
        __new__(cls: type, name: str, text: str)
        __new__(cls: type, name: str, text: str, assemblyName: str, className: str)
        """
        pass


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


class UIControlledApplication(object):
    """
    Represents the Autodesk Revit user interface, providing access to
    UI customization methods and events.
    """
    def CreateAddInCommandBinding(self, revitCommandId):
        """
        CreateAddInCommandBinding(self: UIControlledApplication, revitCommandId: RevitCommandId) -> AddInCommandBinding
        
            Creates a new AddInCommandBinding.
        
            revitCommandId: The Revit command id to identify the command handler you want to replace.
        """
        pass

    def CreateRibbonPanel(self, *__args):
        """
        CreateRibbonPanel(self: UIControlledApplication, tabName: str, panelName: str) -> RibbonPanel
        
            Create a new RibbonPanel on the specified tab.
        
            tabName: The name of the tab, on which the new panel will be created.
            panelName: The name of the panel to be created.
        CreateRibbonPanel(self: UIControlledApplication, panelName: str) -> RibbonPanel
        
            Create a new RibbonPanel on the Add-Ins tab.
        
            panelName: The name of the panel to be created.
        CreateRibbonPanel(self: UIControlledApplication, tab: Tab, panelName: str) -> RibbonPanel
        
            Create a new RibbonPanel on the designated standard Revit tab.
        
            tab: The target tab, on which the new panel will be created.
            panelName: The name of the panel to be created.
        """
        pass

    def CreateRibbonTab(self, tabName):
        """
        CreateRibbonTab(self: UIControlledApplication, tabName: str)
            Creates a new tab on the Revit user interface.
        
            tabName: The name of the tab to be created.
        """
        pass

    def GetDockablePane(self, id):
        """
        GetDockablePane(self: UIControlledApplication, id: DockablePaneId) -> DockablePane
        
            Gets a DockablePane object by its ID.
        
            id: Unique identifier for the new pane.
        """
        pass

    def GetRibbonPanels(self, *__args):
        """
        GetRibbonPanels(self: UIControlledApplication) -> List[RibbonPanel]
        
            Get all the custom Panels on Add-Ins tab of Revit.
        GetRibbonPanels(self: UIControlledApplication, tab: Tab) -> List[RibbonPanel]
        
            Get all the custom Panels on a designated standard Revit tab.
        
            tab: The tab on which the panels are located.
        GetRibbonPanels(self: UIControlledApplication, tabName: str) -> List[RibbonPanel]
        
            Get all the custom Panels on a designated Revit tab.
        
            tabName: The name of the tab on which the panels are located.
        """
        pass

    def LoadAddIn(self, fileName):
        """
        LoadAddIn(self: UIControlledApplication, fileName: str)
            Loads add-ins from the given manifest file.
        
            fileName: The name of the add-in manifest file including the extension is to identify the 
             
        manifest file which contains Revit add-ins.
        """
        pass

    def LoadPackageContents(self, packageContentsPath):
        """
        LoadPackageContents(self: UIControlledApplication, packageContentsPath: str)
            Loads add-ins from the given packageContents.xml file.
        
            packageContentsPath: The name of package contents file
        """
        pass

    def RegisterDockablePane(self, id, title, provider):
        """
        RegisterDockablePane(self: UIControlledApplication, id: DockablePaneId, title: str, provider: IDockablePaneProvider)
            Adds a new dockable pane to the Revit user interface.
        
            id: Unique identifier for the new pane.
            title: String to use for the pane caption.
            provider: Your add-in's implementation of the IDockablePaneProvider interface.
        """
        pass

    def RemoveAddInCommandBinding(self, revitCommandId):
        """
        RemoveAddInCommandBinding(self: UIControlledApplication, revitCommandId: RevitCommandId)
            Removes an AddInCommandBinding.
        
            revitCommandId: The Revit command id to identify the command handler you want to remove the 
             binding.
        """
        pass

    ActiveAddInId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get current active external application or external command id.

Get: ActiveAddInId(self: UIControlledApplication) -> AddInId

"""

    ControlledApplication = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the database level ControlledApplication represented by this UI-level ControlledApplication.

Get: ControlledApplication(self: UIControlledApplication) -> ControlledApplication

"""

    IsLateAddinLoading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this add-in is loaded on the fly or not. If it is loaded when Revit is starting up, it
is false, otherwise it should be true.

Get: IsLateAddinLoading(self: UIControlledApplication) -> bool

"""

    LoadedApplications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns an array of successfully loaded external applications.

Get: LoadedApplications(self: UIControlledApplication) -> ExternalApplicationArray

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


class UIDocument(object, IDisposable):
    """
    An object that represents an Autodesk Revit project opened in the Revit user interface.
    
    UIDocument(document: Document)
    """
    def CanPlaceElementType(self, elementType):
        """
        CanPlaceElementType(self: UIDocument, elementType: ElementType) -> bool
        
            Verifies that the user can be prompted to place the input element type on the 
             current active view.
        
        
            elementType: The ElementType.
            Returns: True if the user can be prompted to place the input element type on the active 
             view, false otherwise.
        """
        pass

    def Dispose(self):
        """ Dispose(self: UIDocument) """
        pass

    def GetOpenUIViews(self):
        """
        GetOpenUIViews(self: UIDocument) -> IList[UIView]
        
            Get a list of all open view windows in the Revit user interface.
        """
        pass

    def GetPlacementTypes(self, familySymbol, pDBView):
        """
        GetPlacementTypes(self: UIDocument, familySymbol: FamilySymbol, pDBView: View) -> IList[FaceBasedPlacementType]
        
            Get a collection of valid placement types for input family symbol.
        
            familySymbol: The family symbol.
            pDBView: The view in which the family instance will be placed in.
        """
        pass

    @staticmethod
    def GetRevitUIFamilyLoadOptions():
        """
        GetRevitUIFamilyLoadOptions() -> IFamilyLoadOptions
        
            Return the option object that allows you to use Revit's dialog boxes to let the 
             user respond to questions that arise during loading of families.
        """
        pass

    def GetSketchGalleryOptions(self, familySymbol):
        """
        GetSketchGalleryOptions(self: UIDocument, familySymbol: FamilySymbol) -> IList[SketchGalleryOptions]
        
            Gets the valid sketch gallery options of a family symbol.
        
            familySymbol: The family symbol.
            Returns: The valid list of SketchGalleryOptions.
        """
        pass

    def PostRequestForElementTypePlacement(self, elementType):
        """
        PostRequestForElementTypePlacement(self: UIDocument, elementType: ElementType)
            Places a request on Revit's command queue for the user to place instances of 
             the specified ElementType.  This does not execute immediately,
           but instead 
             when control returns to Revit from the current API context.
        
        
            elementType: The ElementType of which instances are to be placed.
        """
        pass

    def PromptForFamilyInstancePlacement(self, familySymbol, options=None):
        """
        PromptForFamilyInstancePlacement(self: UIDocument, familySymbol: FamilySymbol)
            Prompts the user to place instances of the specified FamilySymbol.
        
            familySymbol: The FamilySymbol.
        PromptForFamilyInstancePlacement(self: UIDocument, familySymbol: FamilySymbol, options: PromptForFamilyInstancePlacementOptions)
            Prompts the user to place instances of the specified FamilySymbol.
        
            familySymbol: The FamilySymbol.
            options: The PromptForFamilyInstancePlacementOptions, to place the family instance 
             according to the options.
        """
        pass

    def PromptToMatchElementType(self, elementType):
        """
        PromptToMatchElementType(self: UIDocument, elementType: ElementType)
            Prompts the user to select elements to change them to the input type.
        
            elementType: The ElementType applied to selected instances.
        """
        pass

    def PromptToPlaceElementTypeOnLegendView(self, elementType):
        """
        PromptToPlaceElementTypeOnLegendView(self: UIDocument, elementType: ElementType)
            Prompts the user to place an element type onto a legend view.
        
            elementType: The ElementType of which instances are to be placed.
        """
        pass

    def PromptToPlaceViewOnSheet(self, view, allowReplaceExistingSheetViewport):
        """
        PromptToPlaceViewOnSheet(self: UIDocument, view: View, allowReplaceExistingSheetViewport: bool)
            Prompts the user to place a specified view onto a sheet.
        
            view: The view to insert onto a sheet.
            allowReplaceExistingSheetViewport: A indicator which allows the user to replace the existing viewport.
           If 
             true, the viewport representing this view will be replaced by the new viewport 
             created during placement.
           If the view is allowed only to be on one sheet, 
             this will remove the viewport from the old sheet.
           If the view is allowed to 
             be on multiple sheets, and the view is currently placed on the active sheet,
          
              the old viewport on this sheet will be replaced. 
           If false, if the view is 
             only allowed to be on one sheet,
           or if the view is allowed to be on 
             multiple sheets but is already on the active sheet, an exception will be 
             thrown.
        """
        pass

    def RefreshActiveView(self):
        """
        RefreshActiveView(self: UIDocument)
            Refresh the display of the active view in the active document.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UIDocument, disposing: bool) """
        pass

    def RequestViewChange(self, view):
        """
        RequestViewChange(self: UIDocument, view: View)
            Requests an asynchronous change of the active view in the currently active 
             document.
        
        
            view: The View.
        """
        pass

    def SaveAndClose(self):
        """
        SaveAndClose(self: UIDocument) -> bool
        
            Close the document, prompting the user for saving it when necessary.
            Returns: False if closing procedure fails or if saving of a modified document was 
             requested but failed. 
        Also returns False if closing is cancelled by an 
             external application during 'DocumentClosing' event. 
        When function succeeds, 
             True is returned.
        """
        pass

    def SaveAs(self, options=None):
        """
        SaveAs(self: UIDocument)
            Saves the document to a file name obtained from the Revit user without 
             prompting the user to overwrite file if it exists.
        
        SaveAs(self: UIDocument, options: UISaveAsOptions)
            Saves the document to a file name obtained from the Revit user optionally 
             prompting the user to overwrite file if it exists.
        
        
            options: UI options for the SaveAs operation.
        """
        pass

    def setUIDocument(self, *args): #cannot find CLR method
        """ setUIDocument(self: UIDocument, pUIDocument: UIDocument*) """
        pass

    def ShowElements(self, *__args):
        """
        ShowElements(self: UIDocument, element: Element)
            Shows the element by zoom to fit.
        
            element: Element that will be shown.
        ShowElements(self: UIDocument, elementId: ElementId)
            Shows the element by zoom to fit.
        
            elementId: Element id that will be shown.
        ShowElements(self: UIDocument, elementIds: ICollection[ElementId])ShowElements(self: UIDocument, elements: ElementSet)
            Shows the elements by zoom to fit.
        
            elements: The set of elements that will be shown.
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
    def __new__(self, document):
        """ __new__(cls: type, document: Document) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveGraphicalView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The currently active graphical view of the currently active document.

Get: ActiveGraphicalView(self: UIDocument) -> View

"""

    ActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The currently active view of the currently active document.

Get: ActiveView(self: UIDocument) -> View

Set: ActiveView(self: UIDocument) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that represents the current Application.

Get: Application(self: UIDocument) -> UIApplication

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the database level document represented by this UI-level document.

Get: Document(self: UIDocument) -> Document

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: UIDocument) -> bool

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the currently selected Elements in Autodesk Revit.

Get: Selection(self: UIDocument) -> Selection

"""



class UIFabricationUtils(object):
    """ General Fabrication UI utility methods in Revit UI. """
    @staticmethod
    def GetOpenConnectorIndicatorAwayColor():
        """
        GetOpenConnectorIndicatorAwayColor() -> Color
        
            Gets the color of the open connector indicator in away direction.
        """
        pass

    @staticmethod
    def GetOpenConnectorIndicatorPlanColor():
        """
        GetOpenConnectorIndicatorPlanColor() -> Color
        
            Gets the color of the open connector indicator in plan view.
        """
        pass

    @staticmethod
    def GetOpenConnectorIndicatorTowardsColor():
        """
        GetOpenConnectorIndicatorTowardsColor() -> Color
        
            Gets the color of the open connector indicator in towards direction.
        """
        pass

    @staticmethod
    def SetOpenConnectorIndicatorAwayColor(color):
        """
        SetOpenConnectorIndicatorAwayColor(color: Color)
            Sets the color of the open connector indicator in away direction
        """
        pass

    @staticmethod
    def SetOpenConnectorIndicatorPlanColor(color):
        """
        SetOpenConnectorIndicatorPlanColor(color: Color)
            Sets the color of the open connector indicator in plan view.
        """
        pass

    @staticmethod
    def SetOpenConnectorIndicatorTowardsColor(color):
        """
        SetOpenConnectorIndicatorTowardsColor(color: Color)
            Sets the color of the open connector indicator in towards direction
        """
        pass

    __all__ = [
        'GetOpenConnectorIndicatorAwayColor',
        'GetOpenConnectorIndicatorPlanColor',
        'GetOpenConnectorIndicatorTowardsColor',
        'SetOpenConnectorIndicatorAwayColor',
        'SetOpenConnectorIndicatorPlanColor',
        'SetOpenConnectorIndicatorTowardsColor',
    ]


class UISaveAsOptions(object, IDisposable):
    """
    This class contains UI options available for saving a document to disk with a new filename.
    
    UISaveAsOptions()
    """
    def Dispose(self):
        """ Dispose(self: UISaveAsOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UISaveAsOptions, disposing: bool) """
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

Get: IsValidObject(self: UISaveAsOptions) -> bool

"""

    ShowOverwriteWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if UI should show an overwrite warning dialog.

Get: ShowOverwriteWarning(self: UISaveAsOptions) -> bool

Set: ShowOverwriteWarning(self: UISaveAsOptions) = value
"""



class UITheme(Enum, IComparable, IFormattable, IConvertible):
    """
    The application frame theme.
    
    enum UITheme, values: Dark (0), Light (1)
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

    Dark = None
    Light = None
    value__ = None


class UIThemeManager(object):
    """ Manager object for the UITheme class. """
    @staticmethod
    def GetThemeName(frameTheme):
        """
        GetThemeName(frameTheme: UITheme) -> str
        
            Gets the theme name for the given theme type.
        
            frameTheme: The theme.
            Returns: The name of the theme.
        """
        pass

    CurrentTheme = None
    DefaultTheme = None
    __all__ = [
        'GetThemeName',
    ]


class UIView(object, IDisposable):
    """ A class containing data about view windows in the Revit user interface. """
    def Close(self):
        """
        Close(self: UIView)
            Closes the view.
        """
        pass

    def Dispose(self):
        """ Dispose(self: UIView) """
        pass

    def GetWindowRectangle(self):
        """
        GetWindowRectangle(self: UIView) -> Rectangle
        
            Gets the rectangle containing the coordinates of the view's drawing area.
            Returns: The rectangle of the view window.
        """
        pass

    def GetZoomCorners(self):
        """
        GetZoomCorners(self: UIView) -> IList[XYZ]
        
            Gets the corners of the view's rectangle.
           The two points that define the 
             corners of the view's rectangle in model coordinates.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: UIView, disposing: bool) """
        pass

    def Zoom(self, zoomFactor):
        """
        Zoom(self: UIView, zoomFactor: float)
            Zoom the view.
        
            zoomFactor: Factor by which to zoom in or out. Values greater than 1 zooms in, less than 1 
             zooms out.
        """
        pass

    def ZoomAndCenterRectangle(self, viewCorner1, viewCorner2):
        """
        ZoomAndCenterRectangle(self: UIView, viewCorner1: XYZ, viewCorner2: XYZ)
            Zoom and center the view to a specified rectangle.
        
            viewCorner1: A corner of the desired view rectangle in model coordinates.
            viewCorner2: The opposite corner of the desired view rectangle in model coordinates.
        """
        pass

    def ZoomSheetSize(self):
        """
        ZoomSheetSize(self: UIView)
            Zoom to the sheet size.
        """
        pass

    def ZoomToFit(self):
        """
        ZoomToFit(self: UIView)
            Zoom the view to fit its contents.
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

Get: IsValidObject(self: UIView) -> bool

"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The id of the View associated with a UIView.

Get: ViewId(self: UIView) -> ElementId

"""



# variables with complex values

