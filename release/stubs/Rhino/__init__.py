# encoding: utf-8
# module Rhino
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def PersistentSettingsEventArgs(*args, **kwargs): # real signature unknown
    """ Represents event data that is passed as state in persistent settings events. """
    pass

# classes

class DocumentEventArgs(EventArgs):
    """ Provides document information for RhinoDoc events. """
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document for this event. This field might be null.

Get: Document(self: DocumentEventArgs) -> RhinoDoc

"""

    DocumentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document Id of the document for this event.

Get: DocumentId(self: DocumentEventArgs) -> int

"""



class DocumentOpenEventArgs(DocumentEventArgs):
    """ Provides document information for RhinoDoc events. """
    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of file being opened.

Get: FileName(self: DocumentOpenEventArgs) -> str

"""

    Merge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if file is being merged into the current document. This
            occurs during the "Import" command.

Get: Merge(self: DocumentOpenEventArgs) -> bool

"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true is file is openend as a reference file.

Get: Reference(self: DocumentOpenEventArgs) -> bool

"""



class DocumentSaveEventArgs(DocumentEventArgs):
    """ Provides document information for RhinoDoc events. """
    ExportSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if only selected objects are being written to a file.

Get: ExportSelected(self: DocumentSaveEventArgs) -> bool

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of file being written.

Get: FileName(self: DocumentSaveEventArgs) -> str

"""



class IEpsilonComparable:
    # no doc
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: IEpsilonComparable[T], other: T, epsilon: float) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IEpsilonFComparable:
    # no doc
    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: IEpsilonFComparable[T], other: T, epsilon: Single) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IndexPair(object):
    """
    Represents two indices: I and J.
    
    IndexPair(i: int, j: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, i, j):
        """
        __new__[IndexPair]() -> IndexPair
        
        __new__(cls: type, i: int, j: int)
        """
        pass

    I = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the first, I index.

Get: I(self: IndexPair) -> int

Set: I(self: IndexPair) = value
"""

    J = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the second, J index.

Get: J(self: IndexPair) -> int

Set: J(self: IndexPair) = value
"""



class PersistentSettings(object, ISerializable):
    """
    A dictionary of SettingValue items.
    
    PersistentSettings(allUserSettings: PersistentSettings)
    """
    def ContainsModifiedValues(self, allUserSettings):
        """ ContainsModifiedValues(self: PersistentSettings, allUserSettings: PersistentSettings) -> bool """
        pass

    def DeleteItem(self, key):
        """ DeleteItem(self: PersistentSettings, key: str) """
        pass

    @staticmethod
    def FromPlugInId(pluginId):
        """ FromPlugInId(pluginId: Guid) -> PersistentSettings """
        pass

    def GetBool(self, key, defaultValue=None):
        """
        GetBool(self: PersistentSettings, key: str, defaultValue: bool) -> bool
        GetBool(self: PersistentSettings, key: str) -> bool
        """
        pass

    def GetByte(self, key, defaultValue=None):
        """
        GetByte(self: PersistentSettings, key: str, defaultValue: Byte) -> Byte
        GetByte(self: PersistentSettings, key: str) -> Byte
        """
        pass

    def GetChar(self, key, defaultValue=None):
        """
        GetChar(self: PersistentSettings, key: str, defaultValue: Char) -> Char
        GetChar(self: PersistentSettings, key: str) -> Char
        """
        pass

    def GetColor(self, key, defaultValue=None):
        """
        GetColor(self: PersistentSettings, key: str, defaultValue: Color) -> Color
        GetColor(self: PersistentSettings, key: str) -> Color
        """
        pass

    def GetDate(self, key, defaultValue=None):
        """
        GetDate(self: PersistentSettings, key: str, defaultValue: DateTime) -> DateTime
        GetDate(self: PersistentSettings, key: str) -> DateTime
        """
        pass

    def GetDouble(self, key, defaultValue=None):
        """
        GetDouble(self: PersistentSettings, key: str, defaultValue: float) -> float
        GetDouble(self: PersistentSettings, key: str) -> float
        """
        pass

    def GetEnumValue(self, *__args):
# Error generating skeleton for function GetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetInteger(self, key, defaultValue=None):
        """
        GetInteger(self: PersistentSettings, key: str, defaultValue: int) -> int
        GetInteger(self: PersistentSettings, key: str) -> int
        """
        pass

    def GetPoint(self, key, defaultValue=None):
        """
        GetPoint(self: PersistentSettings, key: str, defaultValue: Point) -> Point
        GetPoint(self: PersistentSettings, key: str) -> Point
        """
        pass

    def GetPoint3d(self, key, defaultValue=None):
        """
        GetPoint3d(self: PersistentSettings, key: str, defaultValue: Point3d) -> Point3d
        GetPoint3d(self: PersistentSettings, key: str) -> Point3d
        """
        pass

    def GetRectangle(self, key, defaultValue=None):
        """
        GetRectangle(self: PersistentSettings, key: str, defaultValue: Rectangle) -> Rectangle
        GetRectangle(self: PersistentSettings, key: str) -> Rectangle
        """
        pass

    def GetSize(self, key, defaultValue=None):
        """
        GetSize(self: PersistentSettings, key: str, defaultValue: Size) -> Size
        GetSize(self: PersistentSettings, key: str) -> Size
        """
        pass

    def GetString(self, key, defaultValue=None):
        """
        GetString(self: PersistentSettings, key: str, defaultValue: str) -> str
        GetString(self: PersistentSettings, key: str) -> str
        """
        pass

    def GetStringList(self, key, defaultValue=None):
        """
        GetStringList(self: PersistentSettings, key: str, defaultValue: Array[str]) -> Array[str]
        GetStringList(self: PersistentSettings, key: str) -> Array[str]
        """
        pass

    def GetUnsignedInteger(self, key, defaultValue=None):
        """
        GetUnsignedInteger(self: PersistentSettings, key: str, defaultValue: UInt32) -> UInt32
        GetUnsignedInteger(self: PersistentSettings, key: str) -> UInt32
        """
        pass

    def GetValidator(self, key):
        """ GetValidator(self: PersistentSettings, key: str) -> EventHandler[PersistentSettingsEventArgs] """
        pass

    def RegisterSettingsValidator(self, key, validator):
        """ RegisterSettingsValidator(self: PersistentSettings, key: str, validator: EventHandler[PersistentSettingsEventArgs]) """
        pass

    def SetBool(self, key, value):
        """ SetBool(self: PersistentSettings, key: str, value: bool) """
        pass

    def SetByte(self, key, value):
        """ SetByte(self: PersistentSettings, key: str, value: Byte) """
        pass

    def SetChar(self, key, value):
        """ SetChar(self: PersistentSettings, key: str, value: Char) """
        pass

    def SetColor(self, key, value):
        """ SetColor(self: PersistentSettings, key: str, value: Color) """
        pass

    def SetDate(self, key, value):
        """ SetDate(self: PersistentSettings, key: str, value: DateTime) """
        pass

    def SetDefault(self, key, value):
        """ SetDefault(self: PersistentSettings, key: str, value: Rectangle)SetDefault(self: PersistentSettings, key: str, value: Color)SetDefault(self: PersistentSettings, key: str, value: DateTime)SetDefault(self: PersistentSettings, key: str, value: Point3d)SetDefault(self: PersistentSettings, key: str, value: Point)SetDefault(self: PersistentSettings, key: str, value: Size)SetDefault(self: PersistentSettings, key: str, value: Array[str])SetDefault(self: PersistentSettings, key: str, value: int)SetDefault(self: PersistentSettings, key: str, value: Byte)SetDefault(self: PersistentSettings, key: str, value: bool)SetDefault(self: PersistentSettings, key: str, value: str)SetDefault(self: PersistentSettings, key: str, value: Char)SetDefault(self: PersistentSettings, key: str, value: float) """
        pass

    def SetDouble(self, key, value):
        """ SetDouble(self: PersistentSettings, key: str, value: float) """
        pass

    def SetEnumValue(self, *__args):
        """ SetEnumValue[T](self: PersistentSettings, key: str, enumValue: T)SetEnumValue[T](self: PersistentSettings, enumValue: T) """
        pass

    def SetInteger(self, key, value):
        """ SetInteger(self: PersistentSettings, key: str, value: int) """
        pass

    def SetPoint(self, key, value):
        """ SetPoint(self: PersistentSettings, key: str, value: Point) """
        pass

    def SetPoint3d(self, key, value):
        """ SetPoint3d(self: PersistentSettings, key: str, value: Point3d) """
        pass

    def SetRectangle(self, key, value):
        """ SetRectangle(self: PersistentSettings, key: str, value: Rectangle) """
        pass

    def SetSize(self, key, value):
        """ SetSize(self: PersistentSettings, key: str, value: Size) """
        pass

    def SetString(self, key, value):
        """ SetString(self: PersistentSettings, key: str, value: str) """
        pass

    def SetStringList(self, key, value):
        """
        SetStringList(self: PersistentSettings, key: str, value: Array[str])
            Including a item with the value of StringListRootKey will cause the ProgramData value to get 
             inserted at
                    that location in the list when calling GetStringList.
        
        
            key: The string key.
            value: An array of values to set.
        """
        pass

    def SetUnsignedInteger(self, key, value):
        """ SetUnsignedInteger(self: PersistentSettings, key: str, value: UInt32) """
        pass

    def TryGetBool(self, key, value):
        """ TryGetBool(self: PersistentSettings, key: str) -> (bool, bool) """
        pass

    def TryGetByte(self, key, value):
        """ TryGetByte(self: PersistentSettings, key: str) -> (bool, Byte) """
        pass

    def TryGetChar(self, key, value):
        """ TryGetChar(self: PersistentSettings, key: str) -> (bool, Char) """
        pass

    def TryGetColor(self, key, value):
        """ TryGetColor(self: PersistentSettings, key: str) -> (bool, Color) """
        pass

    def TryGetDate(self, key, value):
        """ TryGetDate(self: PersistentSettings, key: str) -> (bool, DateTime) """
        pass

    def TryGetDefault(self, key, value):
        """
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Color)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, DateTime)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Array[str])
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Rectangle)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Size)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Point3d)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, int)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Byte)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, bool)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, str)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, Char)
        TryGetDefault(self: PersistentSettings, key: str) -> (bool, float)
        """
        pass

    def TryGetDouble(self, key, value):
        """ TryGetDouble(self: PersistentSettings, key: str) -> (bool, float) """
        pass

    def TryGetEnumValue(self, *__args):
# Error generating skeleton for function TryGetEnumValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def TryGetInteger(self, key, value):
        """ TryGetInteger(self: PersistentSettings, key: str) -> (bool, int) """
        pass

    def TryGetPoint(self, key, value):
        """ TryGetPoint(self: PersistentSettings, key: str) -> (bool, Point) """
        pass

    def TryGetPoint3d(self, key, value):
        """ TryGetPoint3d(self: PersistentSettings, key: str) -> (bool, Point3d) """
        pass

    def TryGetRectangle(self, key, value):
        """ TryGetRectangle(self: PersistentSettings, key: str) -> (bool, Rectangle) """
        pass

    def TryGetSize(self, key, value):
        """ TryGetSize(self: PersistentSettings, key: str) -> (bool, Size) """
        pass

    def TryGetString(self, key, value):
        """ TryGetString(self: PersistentSettings, key: str) -> (bool, str) """
        pass

    def TryGetStringList(self, key, value):
        """ TryGetStringList(self: PersistentSettings, key: str) -> (bool, Array[str]) """
        pass

    def TryGetUnsignedInteger(self, key, value):
        """ TryGetUnsignedInteger(self: PersistentSettings, key: str) -> (bool, UInt32) """
        pass

    def __delitem__(self, *args): #cannot find CLR method
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allUserSettings):
        """
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, allUserSettings: PersistentSettings)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    StringListRootKey = '%root%'


class RhinoApp(object):
    """ .NET RhinoApp is parallel to C++ CRhinoApp. """
    @staticmethod
    def AskUserForRhinoLicense(standAlone, parent):
        """
        AskUserForRhinoLicense(standAlone: bool, parent: IWin32Window) -> bool
        
            Causes Rhino to display UI asking the user to enter a license for Rhino or use one from the Zoo.
        
            standAlone: True to ask for a stand-alone license, false to ask the user for a license from the Zoo
            parent: Parent window for the user interface dialog.
        """
        pass

    @staticmethod
    def ClearCommandHistoryWindow():
        """
        ClearCommandHistoryWindow()
            Clear the text in Rhino's command history window.
        """
        pass

    @staticmethod
    def Exit():
        """
        Exit()
            Exits, or closes, Rhino.
        """
        pass

    @staticmethod
    def GetPlugInObject(*__args):
        """
        GetPlugInObject(plugin: str) -> object
        
            Gets the object that is returned by PlugIn.GetPlugInObject for a given
                    plug-in. 
             This function attempts to find and load a plug-in with a given name.
                    When a plug-in 
             is found, it's GetPlugInObject function is called and the
                    result is returned here.
        
                         Note the plug-in must have already been installed in Rhino or the plug-in manager
          
                       will not know where to look for a plug-in with a matching name.
        
        
            plugin: Name of a plug-in.
            Returns: Result of PlugIn.GetPlugInObject for a given plug-in on success.
        GetPlugInObject(pluginId: Guid) -> object
        
            Gets the object that is returned by PlugIn.GetPlugInObject for a given
                    plug-in. 
             This function attempts to find and load a plug-in with a given Id.
                    When a plug-in 
             is found, it's GetPlugInObject function is called and the
                    result is returned here.
        
                         Note the plug-in must have already been installed in Rhino or the plug-in manager
          
                       will not know where to look for a plug-in with a matching id.
        
        
            pluginId: Guid for a given plug-in.
            Returns: Result of PlugIn.GetPlugInObject for a given plug-in on success.
        """
        pass

    @staticmethod
    def IsInstallationBeta(licenseType):
        """
        IsInstallationBeta(licenseType: Installation) -> bool
        
            If licenseType is a beta license, returns true. A beta license grants
                    full use of 
             the product during the pre-release development period.
        
            Returns: true if licenseType is a beta license. false otherwise
        """
        pass

    @staticmethod
    def IsInstallationCommercial(licenseType):
        """
        IsInstallationCommercial(licenseType: Installation) -> bool
        
            If licenseType is a commercial license, returns true. A commercial license grants
                    
             full use of the product.
        
            Returns: true if licenseType is a commercial license. false otherwise
        """
        pass

    @staticmethod
    def IsInstallationEvaluation(licenseType):
        """
        IsInstallationEvaluation(licenseType: Installation) -> bool
        
            If licenseType is an evaluation license, returns true. An evaluation license limits the ability 
             of
                    Rhino to save based on either the number of saves or a fixed period of time.
        
            Returns: true if licenseType is an evaluation license. false otherwise
        """
        pass

    @staticmethod
    def MainWindow():
        """
        MainWindow() -> IWin32Window
        
            Gets the Windows interface handle of the main window.
            Returns: A interface to the handle.
        """
        pass

    @staticmethod
    def MainWindowHandle():
        """
        MainWindowHandle() -> IntPtr
        
            Gets the WindowHandle of the Rhino main window.
        """
        pass

    @staticmethod
    def ReleaseMouseCapture():
        """
        ReleaseMouseCapture() -> bool
        
            Releases the mouse capture.
        """
        pass

    @staticmethod
    def RunScript(script, *__args):
        """
        RunScript(script: str, mruDisplayString: str, echo: bool) -> bool
        
            Runs a Rhino command script.
        
            script: [in] script to run.
            mruDisplayString: [in] String to display in the most recent command list.
            echo: Controls how the script is echoed in the command output window.
                     false = silent - 
             nothing is echoed.
                     true = verbatim - the script is echoed literally.
        
        RunScript(script: str, echo: bool) -> bool
        
            Runs a Rhino command script.
        
            script: [in] script to run.
            echo: Controls how the script is echoed in the command output window.
                     false = silent - 
             nothing is echoed.
                     true = verbatim - the script is echoed literally.
        """
        pass

    @staticmethod
    def SendKeystrokes(characters, appendReturn):
        """
        SendKeystrokes(characters: str, appendReturn: bool)
            Sends a string of printable characters, including spaces, to Rhino's command line.
        
            characters: [in] A string to characters to send to the command line. This can be null.
            appendReturn: [in] Append a return character to the end of the string.
        """
        pass

    @staticmethod
    def SetCommandPrompt(prompt, promptDefault=None):
        """
        SetCommandPrompt(prompt: str)
            Set Rhino command prompt.
        
            prompt: The new prompt text.
        SetCommandPrompt(prompt: str, promptDefault: str)
            Sets the command prompt in Rhino.
        
            prompt: The new prompt text.
            promptDefault: Text that appears in angle brackets and indicates what will happen if the user pressed ENTER.
        """
        pass

    @staticmethod
    def SetFocusToMainWindow():
        """
        SetFocusToMainWindow()
            Sets the focus to the main window.
        """
        pass

    @staticmethod
    def Wait():
        """
        Wait()
            Pauses to keep Windows message pump alive so views will update
                    and windows will 
             repaint.
        """
        pass

    @staticmethod
    def Write(*__args):
        """
        Write(format: str, arg0: object, arg1: object)
            Print formatted text in the command window.
        Write(format: str, arg0: object, arg1: object, arg2: object)
            Print formatted text in the command window.
        Write(message: str)
            Print formatted text in the command window.
        Write(format: str, arg0: object)
            Print formatted text in the command window.
        """
        pass

    @staticmethod
    def WriteLine(*__args):
        """
        WriteLine(format: str, arg0: object, arg1: object)
            Print formatted text with a newline in the command window.
        WriteLine(format: str, arg0: object, arg1: object, arg2: object)
            Print formatted text with a newline in the command window.
        WriteLine(format: str, arg0: object)
            Print formatted text with a newline in the command window.
        WriteLine()
            Print a newline in the command window.
        WriteLine(message: str)
            Print text in the command window.
        """
        pass

    AppSettingsChanged = None
    Closing = None
    EscapeKeyPressed = None
    Idle = None
    Initialized = None
    KeyboardEvent = None
    KeyboardHookEvent = None
    RdkCacheImageChanged = None
    RdkGlobalSettingsChanged = None
    RdkNewDocument = None
    RdkPlugInUnloading = None
    RdkUpdateAllPreviews = None
    RendererChanged = None
    ToolbarFiles = None
    Version = None
    __all__ = [
        'AppSettingsChanged',
        'AskUserForRhinoLicense',
        'ClearCommandHistoryWindow',
        'Closing',
        'EscapeKeyPressed',
        'Exit',
        'GetPlugInObject',
        'Idle',
        'Initialized',
        'IsInstallationBeta',
        'IsInstallationCommercial',
        'IsInstallationEvaluation',
        'KeyboardEvent',
        'KeyboardHookEvent',
        'MainWindow',
        'MainWindowHandle',
        'RdkCacheImageChanged',
        'RdkGlobalSettingsChanged',
        'RdkNewDocument',
        'RdkPlugInUnloading',
        'RdkUpdateAllPreviews',
        'ReleaseMouseCapture',
        'RendererChanged',
        'RunScript',
        'SendKeystrokes',
        'SetCommandPrompt',
        'SetFocusToMainWindow',
        'Wait',
        'Write',
        'WriteLine',
    ]


class RhinoDoc(object):
    """ Represents an active model. """
    def AddCustomUndoEvent(self, description, handler, tag=None):
        """
        AddCustomUndoEvent(self: RhinoDoc, description: str, handler: EventHandler[CustomUndoEventArgs], tag: object) -> bool
        AddCustomUndoEvent(self: RhinoDoc, description: str, handler: EventHandler[CustomUndoEventArgs]) -> bool
        """
        pass

    def AdjustModelUnitSystem(self, newUnitSystem, scale):
        """ AdjustModelUnitSystem(self: RhinoDoc, newUnitSystem: UnitSystem, scale: bool) """
        pass

    def AdjustPageUnitSystem(self, newUnitSystem, scale):
        """ AdjustPageUnitSystem(self: RhinoDoc, newUnitSystem: UnitSystem, scale: bool) """
        pass

    def BeginUndoRecord(self, description):
        """
        BeginUndoRecord(self: RhinoDoc, description: str) -> UInt32
        
            Instructs Rhino to begin recording undo information when the document
                    is changed 
             outside of a command. We use this, e.g., to save changes
                    caused by the modeless 
             layer or object properties dialogs
                    when commands are not running.
        
        
            description: A text describing the record.
            Returns: Serial number of record.  Returns 0 if record is not started
                    because undo 
             information is already being recorded or
                    undo is disabled.
        """
        pass

    def ClearRedoRecords(self):
        """ ClearRedoRecords(self: RhinoDoc) """
        pass

    def ClearUndoRecords(self, purgeDeletedObjects):
        """ ClearUndoRecords(self: RhinoDoc, purgeDeletedObjects: bool) """
        pass

    def CreateDefaultAttributes(self):
        """
        CreateDefaultAttributes(self: RhinoDoc) -> ObjectAttributes
        
            Gets the default object attributes for this document. 
                    The attributes will be 
             linked to the currently active layer 
                    and they will inherit the Document 
             WireDensity setting.
        """
        pass

    def EndUndoRecord(self, undoRecordSerialNumber):
        """ EndUndoRecord(self: RhinoDoc, undoRecordSerialNumber: UInt32) -> bool """
        pass

    @staticmethod
    def ExtractPreviewImage(path):
        """
        ExtractPreviewImage(path: str) -> Bitmap
        
            Extracts the bitmap preview image from the specified model (3DM).
        
            path: The model (3DM) from which to extract the preview image.
                    If null, the currently 
             loaded model is used.
        
            Returns: true on success.
        """
        pass

    def FindFile(self, filename):
        """
        FindFile(self: RhinoDoc, filename: str) -> str
        
            Search for a file using Rhino's search path.  Rhino will look in the
                    following 
             places:
                    1. Current model folder
                    2. Path specified in options 
             dialog/File tab
                    3. Rhino system folders
                    4. Rhino executable folder
        
            Returns: Path to existing file if found, an empty string if no file was found
        """
        pass

    @staticmethod
    def FromId(docId):
        """ FromId(docId: int) -> RhinoDoc """
        pass

    def GetMeshingParameters(self, style):
        """
        GetMeshingParameters(self: RhinoDoc, style: MeshingParameterStyle) -> MeshingParameters
        
            Get MeshingParameters currently used by the document
        """
        pass

    def GetRenderPrimitives(self, *__args):
        """
        GetRenderPrimitives(self: RhinoDoc, plugInId: Guid, viewport: ViewportInfo, forceTriangleMeshes: bool) -> IEnumerable[RenderPrimitive]
        GetRenderPrimitives(self: RhinoDoc, viewport: ViewportInfo, forceTriangleMeshes: bool) -> IEnumerable[RenderPrimitive]
        GetRenderPrimitives(self: RhinoDoc, forceTriangleMeshes: bool) -> IEnumerable[RenderPrimitive]
        """
        pass

    def GetUnitSystemName(self, modelUnits, capitalize, singular, abbreviate):
        """ GetUnitSystemName(self: RhinoDoc, modelUnits: bool, capitalize: bool, singular: bool, abbreviate: bool) -> str """
        pass

    @staticmethod
    def OpenFile(path):
        """ OpenFile(path: str) -> bool """
        pass

    @staticmethod
    def ReadFile(path, options):
        """ ReadFile(path: str, options: FileReadOptions) -> bool """
        pass

    def ReadFileVersion(self):
        """
        ReadFileVersion(self: RhinoDoc) -> int
        
            Returns the file version of the current document.  
                    Use this function to determine 
             which version of Rhino last saved the document.
        
            Returns: The file version (e.g. 1, 2, 3, 4, etc.) or -1 if the document has not been read from disk.
        """
        pass

    def SetCustomMeshingParameters(self, mp):
        """
        SetCustomMeshingParameters(self: RhinoDoc, mp: MeshingParameters)
            Set the custom meshing parameters that this document will use. You must also modify the
                
                 MeshingParameterStyle property on the document to Custom if you want these meshing
                 
                parameters to be used
        """
        pass

    def WriteFile(self, path, options):
        """ WriteFile(self: RhinoDoc, path: str, options: FileWriteOptions) -> bool """
        pass

    Bitmaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """bitmaps used in textures, backgrounds, wallpapers, ...

Get: Bitmaps(self: RhinoDoc) -> BitmapTable

"""

    DateCreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateCreated(self: RhinoDoc) -> DateTime

"""

    DateLastEdited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateLastEdited(self: RhinoDoc) -> DateTime

"""

    DimStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimStyles(self: RhinoDoc) -> DimStyleTable

"""

    DistanceDisplayPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceDisplayPrecision(self: RhinoDoc) -> int

"""

    DocumentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Document Id.

Get: DocumentId(self: RhinoDoc) -> int

"""

    EarthAnchorPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EarthAnchorPoint(self: RhinoDoc) -> EarthAnchorPoint

Set: EarthAnchorPoint(self: RhinoDoc) = value
"""

    Fonts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fonts(self: RhinoDoc) -> FontTable

"""

    GroundPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ground plane of this document.

Get: GroundPlane(self: RhinoDoc) -> GroundPlane

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Groups(self: RhinoDoc) -> GroupTable

"""

    HatchPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchPatterns(self: RhinoDoc) -> HatchPatternTable

"""

    InstanceDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstanceDefinitions(self: RhinoDoc) -> InstanceDefinitionTable

"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check to see if the file associated with this document is locked.  If it is
            locked then this is the only document that will be able to write the file.  Other
            instances of Rhino will fail to write this document.

Get: IsLocked(self: RhinoDoc) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current read-only mode for this document.
            true if the document is can be viewed but NOT saved.
            false if document can be viewed and saved.

Get: IsReadOnly(self: RhinoDoc) -> bool

"""

    IsSendingMail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if Rhino is in the process of sending this document as an email attachment.

Get: IsSendingMail(self: RhinoDoc) -> bool

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Layers in the document.

Get: Layers(self: RhinoDoc) -> LayerTable

"""

    Lights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lights(self: RhinoDoc) -> LightTable

"""

    Linetypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Linetypes in the document.

Get: Linetypes(self: RhinoDoc) -> LinetypeTable

"""

    Materials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Materials in the document.

Get: Materials(self: RhinoDoc) -> MaterialTable

"""

    MeshingParameterStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of MeshingParameters currently used by the document to mesh objects

Get: MeshingParameterStyle(self: RhinoDoc) -> MeshingParameterStyle

Set: MeshingParameterStyle(self: RhinoDoc) = value
"""

    ModelAbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Model space absolute tolerance.

Get: ModelAbsoluteTolerance(self: RhinoDoc) -> float

Set: ModelAbsoluteTolerance(self: RhinoDoc) = value
"""

    ModelAngleToleranceDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Model space angle tolerance.

Get: ModelAngleToleranceDegrees(self: RhinoDoc) -> float

Set: ModelAngleToleranceDegrees(self: RhinoDoc) = value
"""

    ModelAngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Model space angle tolerance.

Get: ModelAngleToleranceRadians(self: RhinoDoc) -> float

Set: ModelAngleToleranceRadians(self: RhinoDoc) = value
"""

    ModelDistanceDisplayPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelDistanceDisplayPrecision(self: RhinoDoc) -> int

Set: ModelDistanceDisplayPrecision(self: RhinoDoc) = value
"""

    ModelRelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Model space relative tolerance.

Get: ModelRelativeTolerance(self: RhinoDoc) -> float

Set: ModelRelativeTolerance(self: RhinoDoc) = value
"""

    ModelUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelUnitSystem(self: RhinoDoc) -> UnitSystem

Set: ModelUnitSystem(self: RhinoDoc) = value
"""

    Modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns or sets the document's modified flag.

Get: Modified(self: RhinoDoc) -> bool

Set: Modified(self: RhinoDoc) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the name of the currently loaded Rhino document (3DM file).

Get: Name(self: RhinoDoc) -> str

"""

    NamedConstructionPlanes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamedConstructionPlanes(self: RhinoDoc) -> NamedConstructionPlaneTable

"""

    NamedViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamedViews(self: RhinoDoc) -> NamedViewTable

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns or sets the document's notes.

Get: Notes(self: RhinoDoc) -> str

Set: Notes(self: RhinoDoc) = value
"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: RhinoDoc) -> ObjectTable

"""

    PageAbsoluteTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Page space absolute tolerance.

Get: PageAbsoluteTolerance(self: RhinoDoc) -> float

Set: PageAbsoluteTolerance(self: RhinoDoc) = value
"""

    PageAngleToleranceDegrees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Page space angle tolerance.

Get: PageAngleToleranceDegrees(self: RhinoDoc) -> float

Set: PageAngleToleranceDegrees(self: RhinoDoc) = value
"""

    PageAngleToleranceRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Page space angle tolerance.

Get: PageAngleToleranceRadians(self: RhinoDoc) -> float

Set: PageAngleToleranceRadians(self: RhinoDoc) = value
"""

    PageDistanceDisplayPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageDistanceDisplayPrecision(self: RhinoDoc) -> int

Set: PageDistanceDisplayPrecision(self: RhinoDoc) = value
"""

    PageRelativeTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Page space relative tolerance.

Get: PageRelativeTolerance(self: RhinoDoc) -> float

Set: PageRelativeTolerance(self: RhinoDoc) = value
"""

    PageUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageUnitSystem(self: RhinoDoc) -> UnitSystem

Set: PageUnitSystem(self: RhinoDoc) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the path of the currently loaded Rhino document (3DM file).

Get: Path(self: RhinoDoc) -> str

"""

    RenderEnvironments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderEnvironments(self: RhinoDoc) -> RenderEnvironmentTable

"""

    RenderMaterials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterials(self: RhinoDoc) -> RenderMaterialTable

"""

    RenderSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderSettings(self: RhinoDoc) -> RenderSettings

Set: RenderSettings(self: RhinoDoc) = value
"""

    RenderTextures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderTextures(self: RhinoDoc) -> RenderTextureTable

"""

    Strings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Strings(self: RhinoDoc) -> StringTable

"""

    TemplateFileUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of the template file used to create this document. This is a runtime value
            only present if the document was newly created.

Get: TemplateFileUsed(self: RhinoDoc) -> str

"""

    UndoRecordingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndoRecordingEnabled(self: RhinoDoc) -> bool

Set: UndoRecordingEnabled(self: RhinoDoc) = value
"""

    UndoRecordingIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if undo recording is actually happening now.

Get: UndoRecordingIsActive(self: RhinoDoc) -> bool

"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views(self: RhinoDoc) -> ViewTable

"""


    AddRhinoObject = None
    BeforeTransformObjects = None
    BeginOpenDocument = None
    BeginSaveDocument = None
    CloseDocument = None
    DeleteRhinoObject = None
    DeselectAllObjects = None
    DeselectObjects = None
    DocumentPropertiesChanged = None
    EndOpenDocument = None
    EndOpenDocumentInitialiViewUpdate = None
    EndSaveDocument = None
    GroupTableEvent = None
    InstanceDefinitionTableEvent = None
    LayerTableEvent = None
    LightTableEvent = None
    MaterialTableEvent = None
    ModifyObjectAttributes = None
    NewDocument = None
    PurgeRhinoObject = None
    RenderContentTableEventArgs = None
    RenderContentTableEventType = None
    RenderEnvironmentTableEvent = None
    RenderMaterialAssignmentChangedEventArgs = None
    RenderMaterialsTableEvent = None
    RenderTextureTableEvent = None
    ReplaceRhinoObject = None
    SelectObjects = None
    TextureMappingEvent = None
    TextureMappingEventArgs = None
    TextureMappingEventType = None
    UndeleteRhinoObject = None


class RhinoMath(object):
    """
    Provides constants and static methods that are additional to
                System.Math.
    """
    @staticmethod
    def Clamp(value, bound1, bound2):
        """
        Clamp(value: float, bound1: float, bound2: float) -> float
        
            Restricts a System.Double to be specified within an interval of two numbers.
        
            value: A number.
            bound1: A first bound.
            bound2: A second bound. This does not necessarily need to be larger or smaller than bound1.
            Returns: The clamped value.
        Clamp(value: int, bound1: int, bound2: int) -> int
        
            Restricts a System.Int32 to be specified within an interval of two integers.
        
            value: An integer.
            bound1: A first bound.
            bound2: A second bound. This does not necessarily need to be larger or smaller than bound1.
            Returns: The clamped value.
        """
        pass

    @staticmethod
    def CRC32(currentRemainder, *__args):
        """
        CRC32(currentRemainder: UInt32, value: int) -> UInt32
        
            Advances the cyclic redundancy check value remainder given a System.Int32.
                    
             http://en.wikipedia.org/wiki/Cyclic_redundancy_check.
        
        
            currentRemainder: The remainder from which to start.
            value: The value to add to the current remainder.
            Returns: The new current remainder.
        CRC32(currentRemainder: UInt32, value: float) -> UInt32
        
            Advances the cyclic redundancy check value remainder given a System.Double.
                    
             http://en.wikipedia.org/wiki/Cyclic_redundancy_check.
        
        
            currentRemainder: The remainder from which to start.
            value: The value to add to the current remainder.
            Returns: The new current remainder.
        CRC32(currentRemainder: UInt32, buffer: Array[Byte]) -> UInt32
        
            Advances the cyclic redundancy check value remainder given a byte array.
                    
             http://en.wikipedia.org/wiki/Cyclic_redundancy_check.
        
        
            currentRemainder: The remainder from which to start.
            buffer: The value to add to the current remainder.
            Returns: The new current remainder.
        """
        pass

    @staticmethod
    def EpsilonEquals(x, y, epsilon):
        """
        EpsilonEquals(x: Single, y: Single, epsilon: Single) -> bool
        
            Compare to floats for equality within some "epsilon" range
        EpsilonEquals(x: float, y: float, epsilon: float) -> bool
        
            Compare two doubles for equality within some "epsilon" range
        """
        pass

    @staticmethod
    def IsValidDouble(x):
        """
        IsValidDouble(x: float) -> bool
        
            Determines whether a System.Double value is valid within the RhinoCommon context.
                    
             Rhino does not use Double.NaN by convention, so this test evaluates to true if:x is not equal to 
             RhinoMath.UnsetValueSystem.Double.IsNaN(x) evaluates to falseSystem.Double.IsInfinity(x) 
             evaluates to false
        
        
            x: System.Double number to test for validity.
            Returns: true if the number if valid, false if the number is NaN, Infinity or Unset.
        """
        pass

    @staticmethod
    def IsValidSingle(x):
        """
        IsValidSingle(x: Single) -> bool
        
            Determines whether a System.Single value is valid within the RhinoCommon context.
                    
             Rhino does not use Single.NaN by convention, so this test evaluates to true if:x is not equal to 
             RhinoMath.UnsetValue,System.Single.IsNaN(x) evaluates to falseSystem.Single.IsInfinity(x) 
             evaluates to false
        
        
            x: System.Single number to test for validity.
            Returns: true if the number if valid, false if the number is NaN, Infinity or Unset.
        """
        pass

    @staticmethod
    def ToDegrees(radians):
        """
        ToDegrees(radians: float) -> float
        
            Convert an angle from radians to degrees.
        
            radians: Radians to convert (180 degrees equals pi radians).
        """
        pass

    @staticmethod
    def ToRadians(degrees):
        """
        ToRadians(degrees: float) -> float
        
            Convert an angle from degrees to radians.
        
            degrees: Degrees to convert (180 degrees equals pi radians).
        """
        pass

    @staticmethod
    def UnitScale(from, to):
        """
        UnitScale(from: UnitSystem, to: UnitSystem) -> float
        
            Computes the scale factor for changing the measurements unit systems.
        
            from: The system to convert from.
            to: The system to convert measurements into.
            Returns: A scale multiplier.
        """
        pass

    DefaultAngleTolerance = 0.017453292519943295
    SqrtEpsilon = 1.4901161193849999e-08
    UnsetSingle = None
    UnsetValue = -1.2343210123432101e+308
    ZeroTolerance = 9.9999999999999998e-13
    __all__ = [
        'Clamp',
        'CRC32',
        'DefaultAngleTolerance',
        'EpsilonEquals',
        'IsValidDouble',
        'IsValidSingle',
        'SqrtEpsilon',
        'ToDegrees',
        'ToRadians',
        'UnitScale',
        'UnsetSingle',
        'UnsetValue',
        'ZeroTolerance',
    ]


class RhinoWindow(object, IWin32Window):
    """ Represents the top level window in Rhino """
    def Invoke(self, method):
        """ Invoke(self: RhinoWindow, method: Delegate) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Handle(self: RhinoWindow) -> IntPtr

"""

    InvokeRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """See Control.InvokeRequired

Get: InvokeRequired(self: RhinoWindow) -> bool

"""



class UnitSystem(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides enumerated values for several unit systems.
    
    enum UnitSystem, values: Angstroms (12), Astronomical (23), Centimeters (3), CustomUnitSystem (11), Decimeters (14), Dekameters (15), Feet (9), Gigameters (18), Hectometers (16), Inches (8), Kilometers (5), Lightyears (24), Megameters (17), Meters (4), Microinches (6), Microns (1), Miles (10), Millimeters (2), Mils (7), Nanometers (13), NauticalMile (22), None (0), Parsecs (25), PrinterPica (21), PrinterPoint (20), Yards (19)
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

    Angstroms = None
    Astronomical = None
    Centimeters = None
    CustomUnitSystem = None
    Decimeters = None
    Dekameters = None
    Feet = None
    Gigameters = None
    Hectometers = None
    Inches = None
    Kilometers = None
    Lightyears = None
    Megameters = None
    Meters = None
    Microinches = None
    Microns = None
    Miles = None
    Millimeters = None
    Mils = None
    Nanometers = None
    NauticalMile = None
    None = None
    Parsecs = None
    PrinterPica = None
    PrinterPoint = None
    value__ = None
    Yards = None


# variables with complex values

