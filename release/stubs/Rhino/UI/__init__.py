# encoding: utf-8
# module Rhino.UI calls itself UI
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Dialogs(object):
    # no doc
    @staticmethod
    def KillSplash():
        """
        KillSplash()
            Destroy the splash screen if it is being displayed.
        """
        pass

    @staticmethod
    def PushPickButton(form, pickFunction):
        """ PushPickButton(form: Form, pickFunction: EventHandler[EventArgs]) """
        pass

    @staticmethod
    def SetCustomColorDialog(handler):
        """ SetCustomColorDialog(handler: EventHandler[GetColorEventArgs]) """
        pass

    @staticmethod
    def ShowCheckListBox(title, message, items, checkState):
        """ ShowCheckListBox(title: str, message: str, items: IList, checkState: IList[bool]) -> Array[bool] """
        pass

    @staticmethod
    def ShowColorDialog(*__args):
        """
        ShowColorDialog(parent: IWin32Window, color: Color4f, allowAlpha: bool) -> (bool, Color4f)
        
            Displays the standard modal color picker dialog for floating point colors.
        
            parent: Parent window for this dialog, should always pass this if calling from a form or user control.
            color: The initial color to set the picker to and also accepts the user's choice.
            allowAlpha: Specifies if the color picker should allow changes to the alpha channel or not.
            Returns: true if a color was picked, false if the user canceled the picker dialog.
        ShowColorDialog(color: Color4f, allowAlpha: bool) -> (bool, Color4f)
        
            Displays the standard modal color picker dialog for floating point colors.
        
            color: The initial color to set the picker to and also accepts the user's choice.
            allowAlpha: Specifies if the color picker should allow changes to the alpha channel or not.
            Returns: true if a color was picked, false if the user canceled the picker dialog.
        ShowColorDialog(color: Color) -> (bool, Color)
        
            Display Rhino's color selection dialog.
        
            color: [in/out] Default color for dialog, and will receive new color if function returns true.
            Returns: true if the color changed. false if the color has not changed or the user pressed cancel.
        ShowColorDialog(color: Color, includeButtonColors: bool, dialogTitle: str) -> (bool, Color)
        
            Display Rhino's color selection dialog.
        
            color: [in/out] Default color for dialog, and will receive new color if function returns true.
            includeButtonColors: Display button face and text options at top of named color list.
            dialogTitle: The title of the dialog.
            Returns: true if the color changed. false if the color has not changed or the user pressed cancel.
        """
        pass

    @staticmethod
    def ShowComboListBox(title, message, items):
        """
        ShowComboListBox(title: str, message: str, items: IList) -> object
        
            Displays Rhino's combo list box.
        
            title: The dialog title.
            message: The dialog message.
            items: A list of items to show.
            Returns: selected item.null if the user canceled.
        """
        pass

    @staticmethod
    def ShowContextMenu(items, screenPoint, modes):
        """ ShowContextMenu(items: IEnumerable[str], screenPoint: Point, modes: IEnumerable[int]) -> int """
        pass

    @staticmethod
    def ShowEditBox(title, message, defaultText, multiline, text):
        """ ShowEditBox(title: str, message: str, defaultText: str, multiline: bool) -> (DialogResult, str) """
        pass

    @staticmethod
    def ShowListBox(title, message, items, selectedItem=None):
        """
        ShowListBox(title: str, message: str, items: IList, selectedItem: object) -> object
        ShowListBox(title: str, message: str, items: IList) -> object
        """
        pass

    @staticmethod
    def ShowMessageBox(message, title, buttons=None, icon=None, defaultButton=None):
        """
        ShowMessageBox(message: str, title: str, buttons: MessageBoxButtons, icon: MessageBoxIcon, defaultButton: MessageBoxDefaultButton) -> DialogResult
        
            Same as System.Windows.Froms.MessageBox.Show but using a message box tailored to Rhino.
        
            message: Message box text content.
            title: Message box title text.
            buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 
             in the message box.
        
            icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 
             the message box.
        
            defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 
             for the message box.
        
            Returns: One of the System.Windows.Forms.DialogResult values.
        ShowMessageBox(message: str, title: str, buttons: MessageBoxButtons, icon: MessageBoxIcon) -> DialogResult
        
            Same as System.Windows.Froms.MessageBox.Show but using a message box tailored to Rhino.
        
            message: Message box text content.
            title: Message box title text.
            buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 
             in the message box.
        
            icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 
             the message box.
        
            Returns: One of the System.Windows.Forms.DialogResult values.
        ShowMessageBox(message: str, title: str) -> DialogResult
        
            Same as System.Windows.Froms.MessageBox.Show but using a message box tailored to Rhino.
        
            message: Message box text content.
            title: Message box title text.
            Returns: One of the System.Windows.Forms.DialogResult values.
        """
        pass

    @staticmethod
    def ShowMultiListBox(title, message, items, defaults):
        """ ShowMultiListBox(title: str, message: str, items: IList[str], defaults: IList[str]) -> Array[str] """
        pass

    @staticmethod
    def ShowNumberBox(title, message, number, minimum=None, maximum=None):
        """
        ShowNumberBox(title: str, message: str, number: float, minimum: float, maximum: float) -> (DialogResult, float)
        ShowNumberBox(title: str, message: str, number: float) -> (DialogResult, float)
        """
        pass

    @staticmethod
    def ShowPropertyListBox(title, message, items, values):
        """ ShowPropertyListBox(title: str, message: str, items: IList, values: IList[str]) -> Array[str] """
        pass

    @staticmethod
    def ShowSelectLayerDialog(layerIndex, dialogTitle, showNewLayerButton, showSetCurrentButton, initialSetCurrentState):
        """
        ShowSelectLayerDialog(layerIndex: int, dialogTitle: str, showNewLayerButton: bool, showSetCurrentButton: bool, initialSetCurrentState: bool) -> (DialogResult, int, bool)
        
            Displays Rhino's single layer selection dialog.
        
            layerIndex: Initial layer for the dialog, and will receive selected
                    layer if function returns 
             DialogResult.OK.
        
            dialogTitle: The dialog title.
            showNewLayerButton: true if the new layer button will be visible.
            showSetCurrentButton: true if the set current button will be visible.
            initialSetCurrentState: true if the current state will be initially set.
            Returns: A dialog result based on user choice.
        """
        pass

    @staticmethod
    def ShowSelectMultipleLayersDialog(defaultLayerIndices, dialogTitle, showNewLayerButton, layerIndices):
        """ ShowSelectMultipleLayersDialog(defaultLayerIndices: IEnumerable[int], dialogTitle: str, showNewLayerButton: bool) -> (DialogResult, Array[int]) """
        pass

    @staticmethod
    def ShowSemiModal(form):
        """
        ShowSemiModal(form: Form) -> DialogResult
        
            Show a windows form that is modal in the sense that this function does not return until
                
                 the form is closed, but also allows for interaction with other elements of the Rhino
               
                  user interface.
        
        
            form: The form must have buttons that are assigned to the "AcceptButton" and "CancelButton".
            Returns: One of the System.Windows.Forms.DialogResult values.
        """
        pass

    @staticmethod
    def ShowTextDialog(message, title):
        """
        ShowTextDialog(message: str, title: str) -> DialogResult
        
            Display a text dialog similar to the dialog used for the "What" command.
        
            message: Text to display as the message content.
            title: Test to display as the form title.
            Returns: One of the System.Windows.Forms.DialogResult values.
        """
        pass

    @staticmethod
    def StringBoxRects():
        """
        StringBoxRects() -> Array[Rectangle]
        
            FOR INTERNAL TESTING
                    Ignore - this is for internal testing and will be removed.
            Returns: On Windows (.NET)
                    {X=0,Y=0,Width=300,Height=126}
                      
             {X=0,Y=0,Width=284,Height=88}
                      {X=0,Y=0,Width=284,Height=88}
                    
             {X=10,Y=9,Width=49,Height=13}
                      {X=0,Y=0,Width=49,Height=13}
                      
             {X=0,Y=0,Width=49,Height=13}
                    {X=197,Y=55,Width=75,Height=23}
                      
             {X=0,Y=0,Width=75,Height=23}
                      {X=0,Y=0,Width=75,Height=23}
                    
             {X=116,Y=55,Width=75,Height=23}
                      {X=0,Y=0,Width=75,Height=23}
                      
             {X=0,Y=0,Width=75,Height=23}
                    {X=13,Y=29,Width=259,Height=20}
                      
             {X=0,Y=0,Width=255,Height=16}
                      {X=0,Y=0,Width=255,Height=16}
        """
        pass

    __all__ = [
        'KillSplash',
        'PushPickButton',
        'SetCustomColorDialog',
        'ShowCheckListBox',
        'ShowColorDialog',
        'ShowComboListBox',
        'ShowContextMenu',
        'ShowEditBox',
        'ShowListBox',
        'ShowMessageBox',
        'ShowMultiListBox',
        'ShowNumberBox',
        'ShowPropertyListBox',
        'ShowSelectLayerDialog',
        'ShowSelectMultipleLayersDialog',
        'ShowSemiModal',
        'ShowTextDialog',
        'StringBoxRects',
    ]


class DistanceDisplayMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum DistanceDisplayMode, values: Decimal (0), FeetInches (2), Fractional (1) """
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

    Decimal = None
    FeetInches = None
    Fractional = None
    value__ = None


class GetColorEventArgs(EventArgs):
    # no doc
    IncludeButtonColors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeButtonColors(self: GetColorEventArgs) -> bool

"""

    InputColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputColor(self: GetColorEventArgs) -> Color

"""

    SelectedColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedColor(self: GetColorEventArgs) -> Color

Set: SelectedColor(self: GetColorEventArgs) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: GetColorEventArgs) -> str

"""



class LOC(object):
    """
    Used a placeholded which is used by LocalizationProcessor application to create contextId
                mapped localized strings.
    """
    @staticmethod
    def COMMANDNAME(english):
        """
        COMMANDNAME(english: str) -> str
        
            Command names that need to be localized should call this function. The COMMANDNAME function 
             doesn't actually
                     do anything but return the original string. The 
             LocalizationProcessor application walks
                     through the source code of a project and 
             looks for LOC.COMMANDNAME and builds a record for each command
                     name for the 
             translators that can be used by developers in a commands overridden 
             Rhino.Commands.Command.LocalName
                     which should call 
             Rhino.UI.Localization.LocalizeCommandName(EnglishName)
        
        
            english: [in] The English string to localize.
        """
        pass

    @staticmethod
    def CON(english, assemblyFromObject=None):
        """
        CON(english: str, assemblyFromObject: object) -> LocalizeStringPair
        
            Command option name strings that need to be localized should call this function. The CON 
             function
                     doesn't actually do anything but return the original string. The 
             LocalizationProcessor application walks
                     through the source code of a project and 
             looks for LOC.CON. The function is then replaced with a
                     call to 
             Localization.LocalizeCommandOptionName using a unique context ID.
        
        
            english: [in] The English string to localize.
            assemblyFromObject: [in] The object that identifies the assembly that owns the command option name.
            Returns: Returns localized string pair with both the English and local names set to the English value.
        CON(english: str) -> LocalizeStringPair
        
            Command option name strings that need to be localized should call this function. The CON 
             function
                     doesn't actually do anything but return the original string. The 
             LocalizationProcessor application walks
                     through the source code of a project and 
             looks for LOC.CON. The function is then replaced with a
                     call to 
             Localization.LocalizeCommandOptionName using a unique context ID.
        
        
            english: [in] The English string to localize.
            Returns: Returns localized string pair with both the English and local names set to the English value.
        """
        pass

    @staticmethod
    def COV(engilsh, assemblyFromObject=None):
        """
        COV(engilsh: str, assemblyFromObject: object) -> LocalizeStringPair
        
            Command option name strings that need to be localized should call this function. The COV 
             function
                     doesn't actually do anything but return the original string. The 
             LocalizationProcessor application walks
                     through the source code of a project and 
             looks for LOC.COV. The function is then replaced with a
                     call to 
             Localization.LocalizeCommandOptionValue using a unique context ID.
        
        
            engilsh: [in] The English string to localize.
            assemblyFromObject: [in] The object that identifies the assembly that owns the command option value.
            Returns: Returns localized string pair with both the English and local names set to the English value.
        COV(engilsh: str) -> LocalizeStringPair
        
            Command option name strings that need to be localized should call this function. The COV 
             function
                     doesn't actually do anything but return the original string. The 
             LocalizationProcessor application walks
                     through the source code of a project and 
             looks for LOC.COV. The function is then replaced with a
                     call to 
             Localization.LocalizeCommandOptionValue using a unique context ID.
        
        
            engilsh: [in] The English string to localize.
            Returns: Returns localized string pair with both the English and local names set to the English value.
        """
        pass

    @staticmethod
    def STR(english, assemblyOrObject=None):
        """
        STR(english: str, assemblyOrObject: object) -> str
        
            Similar to System.String.Format(System.String,System.Object) function.
        
            english: The English name.
            assemblyOrObject: Unused.
            Returns: English name.
        STR(english: str) -> str
        
            Strings that need to be localized should call this function. The STR function doesn't actually
         
                         do anything but return the original string. The LocalizationProcessor application 
             walks
                     through the source code of a project and looks for LOC.STR. The function is 
             then replaced with a
                     call to Localization.LocalizeString using a unique context 
             ID.
        
        
            english: [in] The English string to localize.
        """
        pass

    __all__ = [
        'COMMANDNAME',
        'CON',
        'COV',
        'STR',
    ]


class Localization(object):
    # no doc
    @staticmethod
    def FormatNumber(x, units, mode, precision, appendUnitSystemName):
        """
        FormatNumber(x: float, units: UnitSystem, mode: DistanceDisplayMode, precision: int, appendUnitSystemName: bool) -> str
        
            Get a string version of a number in a given unit system / display mode.
        
            x: The number to format into a string.
            units: The unit system for the number.
            mode: How the number should be formatted.
            precision: The precision of the number.
            appendUnitSystemName: Adds unit system name to the end of the number.
            Returns: The formatted number.
        """
        pass

    @staticmethod
    def GetAssemblyFromObject(assemblyOrObject):
        """
        GetAssemblyFromObject(assemblyOrObject: object) -> Assembly
        
            Check to see if the passed object is an assembly, if not then get the assembly that owns the 
             object type.
        
        
            assemblyOrObject: An assembly or an object from an assembly.
            Returns: The localized string.
        """
        pass

    @staticmethod
    def LocalizeCommandName(english, assemblyOrObject=None):
        """
        LocalizeCommandName(english: str, assemblyOrObject: object) -> str
        LocalizeCommandName(english: str) -> str
        
            Commands that need to be localized should call this function.
        
            english: The localized command name.
        """
        pass

    @staticmethod
    def LocalizeCommandOptionName(english, *__args):
        """
        LocalizeCommandOptionName(english: str, assemblyOrObject: object, contextId: int) -> LocalizeStringPair
        LocalizeCommandOptionName(english: str, contextId: int) -> LocalizeStringPair
        """
        pass

    @staticmethod
    def LocalizeCommandOptionValue(english, *__args):
        """
        LocalizeCommandOptionValue(english: str, assemblyOrObject: object, contextId: int) -> LocalizeStringPair
        LocalizeCommandOptionValue(english: str, contextId: int) -> LocalizeStringPair
        """
        pass

    @staticmethod
    def LocalizeDialogItem(assemblyOrObject, key, english):
        """
        LocalizeDialogItem(assemblyOrObject: object, key: str, english: str) -> str
        
            Look in the dialog item list for the specified key and return the translated
                    
             localized string if the key is found otherwise return the English string.
        
        
            assemblyOrObject: An assembly or an object from an assembly.
            english: The text in English.
            Returns: Look in the dialog item list for the specified key and return the translated
                    
             localized string if the key is found otherwise return the English string.
        """
        pass

    @staticmethod
    def LocalizeForm(form):
        """
        LocalizeForm(form: Control)
            A form or user control should call this in its constructor if it wants to be localized
                 
                 the typical constructor for a localize form would look like:
                     MyForm::MyForm()
        
                          {
                       SuspendLayout();
                       InitializeComponent();
                 
                   Rhino.UI.Localize.LocalizeForm( this );
                       ResumeLayout(true);
                     
             }
        """
        pass

    @staticmethod
    def LocalizeString(english, *__args):
        """
        LocalizeString(english: str, assemblyOrObject: object, contextId: int) -> str
        
            Returns localized version of a given English string. This function should be autogenerated by 
             the
                    RmaLDotNetLocalizationProcessor application for every function that uses 
             RMASTR.
        
        
            english: The text in English.
            assemblyOrObject: An assembly or an object from an assembly.
            contextId: The context ID.
            Returns: The localized string.
        LocalizeString(english: str, contextId: int) -> str
        
            Returns localized version of a given English string. This function should be autogenerated by 
             the
                    RmaLDotNetLocalizationProcessor application for every function that uses 
             RMASTR.
        
        
            english: The text in English.
            contextId: The context ID.
            Returns: The localized string.
        """
        pass

    @staticmethod
    def LocalizeToolStripItemCollection(parent, collection):
        """
        LocalizeToolStripItemCollection(parent: Control, collection: ToolStripItemCollection)
            A form or user control should call this in its constructor if it wants to localize
                     
             context menus that are set on the fly and not assigned to a forms control in design
                    
              studio.
                     MyForm::MyForm()
                     {
                       SuspendLayout();
               
                     InitializeComponent();
                       
             Rhino.UI.Localize.LocalizeToolStripItemCollection( this, this.MyToolStrip.Items );
                     
             }
        """
        pass

    @staticmethod
    def SetLanguageId(id):
        """
        SetLanguageId(id: int) -> bool
        
            Sets the Id used for Localization in RhinoCommon.  Only useful for when
                    using 
             RhinoCommon outside of the Rhino process
        
            Returns: true if the language id could be set
        """
        pass

    @staticmethod
    def UnitSystemName(units, capitalize, singular, abbreviate):
        """
        UnitSystemName(units: UnitSystem, capitalize: bool, singular: bool, abbreviate: bool) -> str
        
            Gets localized unit system name.  Uses current application locale id.
        
            units: The unit system.
            capitalize: true if the name should be capitalized.
            singular: true if the name is expressed for a singular element.
            abbreviate: true if name should be the abbreviation.
            Returns: The unit system name.
        """
        pass

    __all__ = [
        'FormatNumber',
        'GetAssemblyFromObject',
        'LocalizeCommandName',
        'LocalizeCommandOptionName',
        'LocalizeCommandOptionValue',
        'LocalizeDialogItem',
        'LocalizeForm',
        'LocalizeString',
        'LocalizeToolStripItemCollection',
        'SetLanguageId',
        'UnitSystemName',
    ]


class LocalizeStringPair(object):
    """
    Pair of strings used for localization.
    
    LocalizeStringPair(english: str, local: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, english, local):
        """ __new__(cls: type, english: str, local: str) """
        pass

    English = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: English(self: LocalizeStringPair) -> str

"""

    Local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Local(self: LocalizeStringPair) -> str

"""



class MouseCallback(object):
    """ Used for intercepting mouse events in the Rhino viewports. """
    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """ OnMouseDoubleClick(self: MouseCallback, e: MouseCallbackEventArgs) """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """ OnMouseDown(self: MouseCallback, e: MouseCallbackEventArgs) """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """ OnMouseEnter(self: MouseCallback, view: RhinoView) """
        pass

    def OnMouseHover(self, *args): #cannot find CLR method
        """ OnMouseHover(self: MouseCallback, view: RhinoView) """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """ OnMouseLeave(self: MouseCallback, view: RhinoView) """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """ OnMouseMove(self: MouseCallback, e: MouseCallbackEventArgs) """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """ OnMouseUp(self: MouseCallback, e: MouseCallbackEventArgs) """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: MouseCallback) -> bool

Set: Enabled(self: MouseCallback) = value
"""


    MouseCallbackFromCPP = None


class MouseCallbackEventArgs(CancelEventArgs):
    # no doc
    Button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Button(self: MouseCallbackEventArgs) -> MouseButtons

"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: MouseCallbackEventArgs) -> RhinoView

"""

    ViewportPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportPoint(self: MouseCallbackEventArgs) -> Point

"""



class MouseCursor(object):
    """ Contains static methods to control the mouse icon. """
    @staticmethod
    def SetToolTip(tooltip):
        """
        SetToolTip(tooltip: str)
            Sets a cursor tooltip string shown next to the mouse cursor.
                    Overrides all cursor 
             tooltip panes.
        
        
            tooltip: The text to show.
        """
        pass

    Location = None
    __all__ = [
        'SetToolTip',
    ]


class ObjectPropertiesPage(object):
    # no doc
    def InitializeControls(self, rhObj):
        """ InitializeControls(self: ObjectPropertiesPage, rhObj: RhinoObject) """
        pass

    def OnActivate(self, active):
        """
        OnActivate(self: ObjectPropertiesPage, active: bool) -> bool
        
            Called when this page is activated/deactivated.
        
            active: If true then this page is on top otherwise it is about to be hidden.
            Returns: If true then the page is hidden and the requested page is not
                    activated otherwise 
             will not allow you to change the current page.
                    Default returns true
        """
        pass

    def OnCreateParent(self, hwndParent):
        """ OnCreateParent(self: ObjectPropertiesPage, hwndParent: IntPtr) """
        pass

    def OnHelp(self):
        """ OnHelp(self: ObjectPropertiesPage) """
        pass

    def OnSizeParent(self, width, height):
        """ OnSizeParent(self: ObjectPropertiesPage, width: int, height: int) """
        pass

    def ShouldDisplay(self, rhObj):
        """ ShouldDisplay(self: ObjectPropertiesPage, rhObj: RhinoObject) -> bool """
        pass

    EnglishPageTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnglishPageTitle(self: ObjectPropertiesPage) -> str

"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: ObjectPropertiesPage) -> Icon

"""

    LocalPageTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalPageTitle(self: ObjectPropertiesPage) -> str

"""

    PageControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the control that represents this page. This will typically be a custom user control.

Get: PageControl(self: ObjectPropertiesPage) -> Control

"""

    PageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageType(self: ObjectPropertiesPage) -> ProertyPageType

"""

    SelectedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return a list of Rhino objects to be processed by this object properties page

Get: SelectedObjects(self: ObjectPropertiesPage) -> Array[RhinoObject]

"""


    ProertyPageType = None


class OpenFileDialog(object):
    """
    Similar to the System.Windows.Forms.OpenFileDialog, but with customized
                Rhino user interface.
    
    OpenFileDialog()
    """
    def ShowDialog(self):
        """
        ShowDialog(self: OpenFileDialog) -> DialogResult
        
            Show the actual dialog to allow the user to select a file.
        """
        pass

    def ShowOpenDialog(self):
        """
        ShowOpenDialog(self: OpenFileDialog) -> bool
        
            Show the actual dialog to allow the user to select a file.
            Returns: Returns false if the dialog was canceled otherwise returns true
        """
        pass

    DefaultExt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default file name extension. The returned string does not include the period.

Get: DefaultExt(self: OpenFileDialog) -> str

Set: DefaultExt(self: OpenFileDialog) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string containing the file name selected in the file dialog box.

Get: FileName(self: OpenFileDialog) -> str

Set: FileName(self: OpenFileDialog) = value
"""

    FileNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the names of all of the selected files in the dialog box

Get: FileNames(self: OpenFileDialog) -> Array[str]

"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current file name filter string, which determines
            the choices that appear in the "Save as file type" or "Files of type"
            box in the dialog box. See System.Windows.Forms.FileDialog for details.

Get: Filter(self: OpenFileDialog) -> str

Set: Filter(self: OpenFileDialog) = value
"""

    InitialDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial directory displayed by the file dialog box.

Get: InitialDirectory(self: OpenFileDialog) -> str

Set: InitialDirectory(self: OpenFileDialog) = value
"""

    MultiSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the dialog box allows multiple files to be selected

Get: MultiSelect(self: OpenFileDialog) -> bool

Set: MultiSelect(self: OpenFileDialog) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file dialog box title.

Get: Title(self: OpenFileDialog) -> str

Set: Title(self: OpenFileDialog) = value
"""



class StackedDialogPage(object):
    """ Provides a base class to inherit from for the addition of stacked dialog pages. """
    def OnActivate(self, active):
        """
        OnActivate(self: StackedDialogPage, active: bool) -> bool
        
            Called when this page is activated/deactivated.
        
            active: If true then this page is on top otherwise it is about to be hidden.
            Returns: If true then the page is hidden and the requested page is not
                    activated otherwise 
             will not allow you to change the current page.
                    Default returns true
        """
        pass

    def OnApply(self):
        """
        OnApply(self: StackedDialogPage) -> bool
        
            Called when stacked dialog OK button is pressed.
            Returns: If return value is true then the dialog will be closed. A return of false means
                    
             there was an error and dialog remains open so page can be properly updated.
        """
        pass

    def OnCancel(self):
        """
        OnCancel(self: StackedDialogPage)
            Called when stacked dialog Cancel button is pressed.
        """
        pass

    def OnCreateParent(self, hwndParent):
        """ OnCreateParent(self: StackedDialogPage, hwndParent: IntPtr) """
        pass

    def OnDefaults(self):
        """
        OnDefaults(self: StackedDialogPage)
            Called when stacked dialog Defaults button is pressed (see ShowDefaultsButton).
        """
        pass

    def OnHelp(self):
        """ OnHelp(self: StackedDialogPage) """
        pass

    def OnSizeParent(self, width, height):
        """ OnSizeParent(self: StackedDialogPage, width: int, height: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, englishPageTitle: str) """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Children(self: StackedDialogPage) -> List[StackedDialogPage]

"""

    EnglishPageTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnglishPageTitle(self: StackedDialogPage) -> str

"""

    HasChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasChildren(self: StackedDialogPage) -> bool

"""

    LocalPageTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalPageTitle(self: StackedDialogPage) -> str

"""

    PageControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the control that represents this page. This will typically be a custom user control.

Get: PageControl(self: StackedDialogPage) -> Control

"""

    ShowDefaultsButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Called when this page is activated.

Get: ShowDefaultsButton(self: StackedDialogPage) -> bool

"""



class OptionsDialogPage(StackedDialogPage):
    # no doc
    def RunScript(self, doc, mode):
        """ RunScript(self: OptionsDialogPage, doc: RhinoDoc, mode: RunMode) -> Result """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, englishPageTitle: str) """
        pass


class PanelIds(object):
    # no doc
    ContextHelp = None
    Display = None
    Environment = None
    GroundPlane = None
    Layers = None
    Libraries = None
    LightManager = None
    Materials = None
    Notes = None
    ObjectProperties = None
    Sun = None
    Texture = None
    __all__ = []


class Panels(object):
    # no doc
    @staticmethod
    def ClosePanel(*__args):
        """ ClosePanel(panelType: Type)ClosePanel(panelId: Guid) """
        pass

    @staticmethod
    def GetOpenPanelIds():
        """ GetOpenPanelIds() -> Array[Guid] """
        pass

    @staticmethod
    def GetPanel(panelId):
        """ GetPanel(panelId: Guid) -> object """
        pass

    @staticmethod
    def IsPanelVisible(*__args):
        """
        IsPanelVisible(panelType: Type) -> bool
        IsPanelVisible(panelId: Guid) -> bool
        """
        pass

    @staticmethod
    def OpenPanel(*__args):
        """
        OpenPanel(dockBarId: Guid, panelId: Guid) -> Guid
        OpenPanel(dockBarId: Guid, panelType: Type) -> Guid
        OpenPanel(panelId: Guid)OpenPanel(panelType: Type)
        """
        pass

    @staticmethod
    def OpenPanelAsSibling(panelId, existingSiblingId):
        """ OpenPanelAsSibling(panelId: Guid, existingSiblingId: Guid) -> bool """
        pass

    @staticmethod
    def PanelDockBar(*__args):
        """
        PanelDockBar(panelType: Type) -> Guid
        PanelDockBar(panelId: Guid) -> Guid
        """
        pass

    @staticmethod
    def RegisterPanel(plugin, panelType, caption, icon):
        """
        RegisterPanel(plugin: PlugIn, panelType: Type, caption: str, icon: Icon)
            You typically register your panel class in your plug-in's OnLoad function.
                    This 
             informs Rhino of the existence of your panel class
        
        
            plugin: Plug-in this panel is associated with
            panelType: Class type to construct when a panel is shown.  Currently only types
                    that implement 
             the IWin32Window interface are supported. The requirements
                    for the class are that 
             it has a parameterless constructor and have a
                    GuidAttribute applied with a unique 
             Guid
        
            icon: Use a 32bit depth icon in order to get proper transparency
        """
        pass

    __all__ = [
        'ClosePanel',
        'GetOpenPanelIds',
        'GetPanel',
        'IsPanelVisible',
        'OpenPanel',
        'OpenPanelAsSibling',
        'PanelDockBar',
        'RegisterPanel',
    ]


class RuiUpdateUi(EventArgs):
    # no doc
    @staticmethod
    def RegisterMenuItem(*__args):
        """
        RegisterMenuItem(fileId: str, menuId: str, itemId: str, callBack: UpdateMenuItemEventHandler) -> bool
        RegisterMenuItem(file: Guid, menu: Guid, item: Guid, callBack: UpdateMenuItemEventHandler) -> bool
        """
        pass

    Checked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to true to enable menu item or false to check menu item

Get: Checked(self: RuiUpdateUi) -> bool

Set: Checked(self: RuiUpdateUi) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to true to enable menu item or false to disable menu item

Get: Enabled(self: RuiUpdateUi) -> bool

Set: Enabled(self: RuiUpdateUi) = value
"""

    FileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the RUI file that owns this menu item

Get: FileId(self: RuiUpdateUi) -> Guid

"""

    MenuHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Windows menu handle of menu that contains this item

Get: MenuHandle(self: RuiUpdateUi) -> IntPtr

"""

    MenuId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the menu that owns this menu item

Get: MenuId(self: RuiUpdateUi) -> Guid

"""

    MenuIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Zero based index of item in the Windows menu

Get: MenuIndex(self: RuiUpdateUi) -> int

"""

    MenuItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the menu item that owns this menu item

Get: MenuItemId(self: RuiUpdateUi) -> Guid

"""

    RadioChecked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set to true to enable menu item or false to check menu item

Get: RadioChecked(self: RuiUpdateUi) -> bool

Set: RadioChecked(self: RuiUpdateUi) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Menu item text

Get: Text(self: RuiUpdateUi) -> str

Set: Text(self: RuiUpdateUi) = value
"""

    WindowsMenuItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Windows menu item ID

Get: WindowsMenuItemId(self: RuiUpdateUi) -> UInt32

"""


    UpdateMenuItemEventHandler = None


class SaveFileDialog(object):
    """
    Similar to the System.Windows.Forms.SaveFileDialog, but with customized
                Rhino user interface.
    
    SaveFileDialog()
    """
    def ShowDialog(self):
        """ ShowDialog(self: SaveFileDialog) -> DialogResult """
        pass

    def ShowSaveDialog(self):
        """
        ShowSaveDialog(self: SaveFileDialog) -> bool
        
            Display the dialog box.
            Returns: Returns false if the dialog was canceled otherwise returns true
        """
        pass

    DefaultExt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default file name extension. The returned string does not include the period.

Get: DefaultExt(self: SaveFileDialog) -> str

Set: DefaultExt(self: SaveFileDialog) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string containing the file name selected in the file dialog box.

Get: FileName(self: SaveFileDialog) -> str

Set: FileName(self: SaveFileDialog) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current file name filter string, which determines
            the choices that appear in the "Save as file type" or "Files of type"
            box in the dialog box. See System.Windows.Forms.FileDialog for details.

Get: Filter(self: SaveFileDialog) -> str

Set: Filter(self: SaveFileDialog) = value
"""

    InitialDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial directory displayed by the file dialog box.

Get: InitialDirectory(self: SaveFileDialog) -> str

Set: InitialDirectory(self: SaveFileDialog) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file dialog box title.

Get: Title(self: SaveFileDialog) -> str

Set: Title(self: SaveFileDialog) = value
"""



class StatusBar(object):
    """ Contains static methods to control the application status bar. """
    @staticmethod
    def ClearMessagePane():
        """
        ClearMessagePane()
            Removes the message from the message pane.
        """
        pass

    @staticmethod
    def HideProgressMeter():
        """
        HideProgressMeter()
            Ends, or hides, Rhino's status bar progress meter.
        """
        pass

    @staticmethod
    def SetDistancePane(distance):
        """
        SetDistancePane(distance: float)
            Sets the distance pane to a distance value.
        
            distance: The distance value.
        """
        pass

    @staticmethod
    def SetMessagePane(message):
        """
        SetMessagePane(message: str)
            Sets the message pane to a message.
        
            message: The message value.
        """
        pass

    @staticmethod
    def SetPointPane(point):
        """
        SetPointPane(point: Point3d)
            Sets the point pane to a point value.
        
            point: The point value.
        """
        pass

    @staticmethod
    def ShowProgressMeter(lowerLimit, upperLimit, label, embedLabel, showPercentComplete):
        """
        ShowProgressMeter(lowerLimit: int, upperLimit: int, label: str, embedLabel: bool, showPercentComplete: bool) -> int
        
            Starts, or shows, Rhino's status bar progress meter.
        
            lowerLimit: The lower limit of the progress meter's range.
            upperLimit: The upper limit of the progress meter's range.
            label: The short description of the progress (e.g. "Calculating", "Meshing", etc)
            embedLabel: If true, then the label will be embeded in the progress meter.
                    If false, then the 
             label will appear to the left of the progress meter.
        
            showPercentComplete: If true, then the percent complete will appear in the progress meter.
            Returns: 1 - The progress meter was created successfully.
                    0 - The progress meter was not 
             created.
                    -1 - The progress meter was not created because some other process has 
             already created it.
        """
        pass

    @staticmethod
    def UpdateProgressMeter(position, absolute):
        """
        UpdateProgressMeter(position: int, absolute: bool) -> int
        
            Sets the current position of Rhino's status bar progress meter.
        
            position: The new value. This can be stated in absolute terms, or relative compared to the current 
             position.
                    The interval bounds are specified when you first show the bar using 
             Rhino.UI.StatusBar.ShowProgressMeter(System.Int32,System.Int32,System.String,System.Boolean,Syste
             m.Boolean).
        
            absolute: If true, then the progress meter is moved to position.
                    If false, then the progress 
             meter is moved position from the current position (relative).
        
            Returns: The previous position if successful.
        """
        pass

    __all__ = [
        'ClearMessagePane',
        'HideProgressMeter',
        'SetDistancePane',
        'SetMessagePane',
        'SetPointPane',
        'ShowProgressMeter',
        'UpdateProgressMeter',
    ]


class Toolbar(object):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Toolbar) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Toolbar) -> str

"""



class ToolbarFile(object):
    # no doc
    def Close(self, prompt):
        """ Close(self: ToolbarFile, prompt: bool) -> bool """
        pass

    def GetGroup(self, *__args):
        """
        GetGroup(self: ToolbarFile, name: str) -> ToolbarGroup
        GetGroup(self: ToolbarFile, index: int) -> ToolbarGroup
        """
        pass

    def GetToolbar(self, index):
        """ GetToolbar(self: ToolbarFile, index: int) -> Toolbar """
        pass

    def Save(self):
        """ Save(self: ToolbarFile) -> bool """
        pass

    def SaveAs(self, path):
        """ SaveAs(self: ToolbarFile, path: str) -> bool """
        pass

    GroupCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupCount(self: ToolbarFile) -> int

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ToolbarFile) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ToolbarFile) -> str

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full path to this file on disk

Get: Path(self: ToolbarFile) -> str

"""

    ToolbarCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolbarCount(self: ToolbarFile) -> int

"""



class ToolbarFileCollection(object, IEnumerable[ToolbarFile], IEnumerable):
    # no doc
    def FindByName(self, name, ignoreCase):
        """ FindByName(self: ToolbarFileCollection, name: str, ignoreCase: bool) -> ToolbarFile """
        pass

    def FindByPath(self, path):
        """ FindByPath(self: ToolbarFileCollection, path: str) -> ToolbarFile """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ToolbarFileCollection) -> IEnumerator[ToolbarFile] """
        pass

    def Open(self, path):
        """ Open(self: ToolbarFileCollection, path: str) -> ToolbarFile """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ToolbarFile](enumerable: IEnumerable[ToolbarFile], value: ToolbarFile) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of open toolbar files

Get: Count(self: ToolbarFileCollection) -> int

"""



class ToolbarGroup(object):
    # no doc
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ToolbarGroup) -> Guid

"""

    IsDocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDocked(self: ToolbarGroup) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ToolbarGroup) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: ToolbarGroup) -> bool

Set: Visible(self: ToolbarGroup) = value
"""



class WaitCursor(object, IDisposable):
    """ WaitCursor() """
    def Clear(self):
        """ Clear(self: WaitCursor) """
        pass

    def Dispose(self):
        """ Dispose(self: WaitCursor) """
        pass

    def Set(self):
        """ Set(self: WaitCursor) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


# variables with complex values

