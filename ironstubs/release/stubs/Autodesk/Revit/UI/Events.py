# encoding: utf-8
# module Autodesk.Revit.UI.Events calls itself Events
# from RevitAPIUI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationClosingEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The event arguments used by the ApplicationClosing event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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


class CommandEventArgs(RevitEventArgs):
    """ The base class of the command Executed and CanExecute event arguments. """
    ActiveDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The active document.

Get: ActiveDocument(self: CommandEventArgs) -> Document

"""

    CommandId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The command id.

Get: CommandId(self: CommandEventArgs) -> RevitCommandId

"""



class BeforeExecutedEventArgs(CommandEventArgs):
    """ The event arguments used by AddInCommandBinding's BeforeExecuted event. """
    UsingCommandData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether or not the Revit journal will include custom data populated by the application associated with this command.

Get: UsingCommandData(self: BeforeExecutedEventArgs) -> bool

Set: UsingCommandData(self: BeforeExecutedEventArgs) = value
"""



class CanExecuteEventArgs(CommandEventArgs):
    """ The event arguments used by AddInCommandBinding's CanExecute event. """
    def GetSelectedCategoryIds(self):
        """
        GetSelectedCategoryIds(self: CanExecuteEventArgs) -> ICollection[ElementId]
        
            Gets the category ids of selected elements.
        """
        pass

    CanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value that indicates whether the Command associated with this event can be executed.

Get: CanExecute(self: CanExecuteEventArgs) -> bool

Set: CanExecute(self: CanExecuteEventArgs) = value
"""



class RibbonItemEventArgs(EventArgs):
    """
    The base class of the RibbonItem event arguments which have UIApplication property.
    
    RibbonItemEventArgs()
    """
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current UIApplication.

Get: Application(self: RibbonItemEventArgs) -> UIApplication

"""



class ComboBoxCurrentChangedEventArgs(RibbonItemEventArgs):
    """ The event arguments used by ComboBox's CurrentChanged event. """
    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current item for the ComboBox after the change.

Get: NewValue(self: ComboBoxCurrentChangedEventArgs) -> ComboBoxMember

"""

    OldValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current item for the ComboBox before the change.

Get: OldValue(self: ComboBoxCurrentChangedEventArgs) -> ComboBoxMember

"""



class ComboBoxDropDownClosedEventArgs(RibbonItemEventArgs):
    """
    The event arguments used by ComboBox's DropDownClosed event.
    
    ComboBoxDropDownClosedEventArgs()
    """

class ComboBoxDropDownOpenedEventArgs(RibbonItemEventArgs):
    """
    The event arguments used by ComboBox's DropDownOpened event.
    
    ComboBoxDropDownOpenedEventArgs()
    """

class DialogBoxData(APIObject, IDisposable):
    """ An object that is passed to your application when a dialog is displayed in Revit. """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def OverrideResult(self, result):
        """
        OverrideResult(self: DialogBoxData, result: int) -> bool
        
            Call this method to cause the Autodesk Revit dialog to be dismissed with the 
             specified return value.
        
        
            result: The result code you wish the Revit dialog to return.
            Returns: Returns true if the result code was accepted.
        """
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

    HelpId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An ID that represents the dialog that has been displayed.

Get: HelpId(self: DialogBoxData) -> int

"""



class DialogBoxShowingEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The base class for the event arguments used by the DialogBoxShowing event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def OverrideResult(self, resultCode):
        """
        OverrideResult(self: DialogBoxShowingEventArgs, resultCode: int) -> bool
        
            Call this method to cause the Autodesk Revit dialog to be dismissed with the 
             specified return value.
        
        
            resultCode: The result code you wish the Revit dialog to return.
            Returns: True if the result code was accepted.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DialogId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unique string identifier for DialogBox and TaskDialog type dialogs in Revit.

Get: DialogId(self: DialogBoxShowingEventArgs) -> str

"""

    HelpId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An ID that represents the dialog that has been displayed.

Get: HelpId(self: DialogBoxShowingEventArgs) -> int

"""



class DisplayingOptionsDialogEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The event arguments used by DisplayingOptionDialog event. """
    def AddTab(self, newTabName, tabbedDialogExtension):
        """
        AddTab(self: DisplayingOptionsDialogEventArgs, newTabName: str, tabbedDialogExtension: TabbedDialogExtension)
            Add tab to option dialog with tab name and handler information.
        
            newTabName: The new tab page name.
            tabbedDialogExtension: The handlers information for the new tab page.
        """
        pass

    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    PagesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The count of pages in the options dialog (include the default pages added by Revit).

Get: PagesCount(self: DisplayingOptionsDialogEventArgs) -> int

"""



class DockableFrameFocusChangedEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the DockableFrameActivatedChanged event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    FocusGained = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the pane is being activated, false if it is being inactivated.

Get: FocusGained(self: DockableFrameFocusChangedEventArgs) -> bool

"""

    PaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier for dockable pane.

Get: PaneId(self: DockableFrameFocusChangedEventArgs) -> DockablePaneId

"""



class DockableFrameVisibilityChangedEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the DockableFrameVisibilityChanged event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DockableFrameShown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the pane is being shown, false if it is being hidden.

Get: DockableFrameShown(self: DockableFrameVisibilityChangedEventArgs) -> bool

"""

    PaneId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier for dockable pane.

Get: PaneId(self: DockableFrameVisibilityChangedEventArgs) -> DockablePaneId

"""



class ExecutedEventArgs(CommandEventArgs):
    """ The event arguments used by AddInCommandBinding's Executed event. """
    def GetJournalData(self):
        """
        GetJournalData(self: ExecutedEventArgs) -> IDictionary[str, str]
        
            Gets the journal data associated to this command (on journal playback).
        """
        pass

    def SetJournalData(self, data):
        """ SetJournalData(self: ExecutedEventArgs, data: IDictionary[str, str]) """
        pass


class FabricationPartBrowserChangedEventArgs(RevitAPISingleEventArgs, IDisposable):
    """ The event arguments used by the FabricationPartBrowserChangedEventArgs event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def GetAllSolutionsPartsTypeCounts(self):
        """
        GetAllSolutionsPartsTypeCounts(self: FabricationPartBrowserChangedEventArgs) -> IDictionary[ElementId, int]
        
            Returns the total fabrication part type usage count in all routing solutions.
        """
        pass

    def GetCurrentSolutionPartTypeIds(self):
        """
        GetCurrentSolutionPartTypeIds(self: FabricationPartBrowserChangedEventArgs) -> ISet[ElementId]
        
            Returns set of fabrication part types that are used in the currently selected 
             solution.
        
            Returns: The set of ElementIds.
        """
        pass

    def GetFabricationPartTypeIds(self):
        """
        GetFabricationPartTypeIds(self: FabricationPartBrowserChangedEventArgs) -> ISet[ElementId]
        
            Returns set of fabrication part types in use in the routing solution mode.
            Returns: The set of ElementIds for for fabrication part types that is in use in routing 
             solution mode.
        """
        pass

    def GetFilteredSolutionsPartsTypeCounts(self):
        """
        GetFilteredSolutionsPartsTypeCounts(self: FabricationPartBrowserChangedEventArgs) -> IDictionary[ElementId, int]
        
            Returns the active fabrication part type usage count in fitlered routing 
             solutions.
        """
        pass

    def GetRequiredFabricationPartTypeIds(self):
        """
        GetRequiredFabricationPartTypeIds(self: FabricationPartBrowserChangedEventArgs) -> ISet[ElementId]
        
            Returns set of required fabrication part types in use in routing solution mode.
            Returns: The set of ElementIds for for required fabrication part types that is in use in 
             routing solution mode.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    NumberOfSolutions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of active solutions in routing solution mode.

Get: NumberOfSolutions(self: FabricationPartBrowserChangedEventArgs) -> int

"""

    Operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The operation associated with this event

Get: Operation(self: FabricationPartBrowserChangedEventArgs) -> FabricationPartBrowserOperation

"""

    ServiceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The identifier for the fabrication service.

Get: ServiceId(self: FabricationPartBrowserChangedEventArgs) -> int

"""



class FabricationPartBrowserOperation(Enum, IComparable, IFormattable, IConvertible):
    """
    Operations for the FabricationPartBrowserChangedEventArgs Event
    
    enum FabricationPartBrowserOperation, values: CreatedRoutingSolutions (4), FinishRoutingSolutionMode (6), HideBrowser (1), RoutingSolutionChanged (5), ShowBrowser (0), ShowService (2), StartRoutingSolutionMode (3), UnknownOperation (-1)
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

    CreatedRoutingSolutions = None
    FinishRoutingSolutionMode = None
    HideBrowser = None
    RoutingSolutionChanged = None
    ShowBrowser = None
    ShowService = None
    StartRoutingSolutionMode = None
    UnknownOperation = None
    value__ = None


class IdlingEventArgs(RevitAPIPreEventArgs, IDisposable):
    """ The event arguments used by the Idling event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
        pass

    def SetRaiseWithoutDelay(self):
        """
        SetRaiseWithoutDelay(self: IdlingEventArgs)
            Sets the next invocation of the idling event to be called promptly,
           rather 
             than relying on the default recurrence of idling from the Revit application. 
             For more
           details see the remarks describing the Idling event.
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


class MessageBoxData(DialogBoxData, IDisposable):
    """
    An object that represents a simple message box that prompts the user
    for some action.
    """
    def Dispose(self):
        """ Dispose(self: MessageBoxData, A_0: bool) """
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

    DialogType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An integer that describes the standard windows type of the dialog box.

Get: DialogType(self: MessageBoxData) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message that has been displayed in the dialog box.

Get: Message(self: MessageBoxData) -> str

"""



class MessageBoxShowingEventArgs(DialogBoxShowingEventArgs, IDisposable):
    """ The event arguments used by the DialogBoxShowing event when a Windows message box is about to be displayed in Revit. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    DialogType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An integer that describes the standard Windows type of the dialog box.

Get: DialogType(self: MessageBoxShowingEventArgs) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message that has been displayed in the dialog box.

Get: Message(self: MessageBoxShowingEventArgs) -> str

"""



class TaskDialogShowingEventArgs(DialogBoxShowingEventArgs, IDisposable):
    """ The event arguments used by the DialogBoxShowing event when a Revit task dialog that prompts the user for some action is shown. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The message that has been displayed in the dialog box.

Get: Message(self: TaskDialogShowingEventArgs) -> str

"""



class TextBoxEnterPressedEventArgs(RibbonItemEventArgs):
    """
    The event arguments used by TextBox's EnterPressed event.
    
    TextBoxEnterPressedEventArgs()
    """

class ViewActivatedEventArgs(RevitAPIPostDocEventArgs, IDisposable):
    """ The event arguments used by the ViewActivated event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    CurrentActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view that has just become active.

Get: CurrentActiveView(self: ViewActivatedEventArgs) -> View

"""

    PreviousActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The previously active view.

Get: PreviousActiveView(self: ViewActivatedEventArgs) -> View

"""



class ViewActivatingEventArgs(RevitAPIPreDocEventArgs, IDisposable):
    """ The event arguments used by the ViewActivating event. """
    def Dispose(self):
        """ Dispose(self: RevitAPIEventArgs, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RevitAPIEventArgs, disposing: bool) """
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

    CurrentActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view that is currently active.

Get: CurrentActiveView(self: ViewActivatingEventArgs) -> View

"""

    NewActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view that is going to become active.

Get: NewActiveView(self: ViewActivatingEventArgs) -> View

"""



