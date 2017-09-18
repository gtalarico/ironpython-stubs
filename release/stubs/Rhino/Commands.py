# encoding: utf-8
# module Rhino.Commands calls itself Commands
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Command(object):
    """ Defines a base class for all commands. This class is abstract. """
    @staticmethod
    def DisplayHelp(commandId):
        """
        DisplayHelp(commandId: Guid)
            Displays help for a command.
        
            commandId: A command ID.
        """
        pass

    @staticmethod
    def GetCommandNames(english, loaded):
        """
        GetCommandNames(english: bool, loaded: bool) -> Array[str]
        
            Gets list of command names in Rhino. This list does not include Test, Alpha, or System commands.
        
            english: if true, retrieve the english name for every command.
                     if false, retrieve the local 
             name for every command.
        
            loaded: if true, only get names of currently loaded commands.
                    if false, get names of all 
             registered (may not be currently loaded) commands.
        
            Returns: An array instance with command names. This array could be empty, but not null.
        """
        pass

    @staticmethod
    def GetCommandStack():
        """
        GetCommandStack() -> Array[Guid]
        
            Determines if Rhino is currently running a command. Because Rhino allow for transparent commands
             
                    (commands that can be run from inside of other commands), this method returns the 
             total ids of
                    active commands.
        
            Returns: Ids of running commands or null if no commands are currently running. 
                    The "active" 
             command is at the end of this list.
        """
        pass

    @staticmethod
    def GetMostRecentCommands():
        """
        GetMostRecentCommands() -> Array[MostRecentCommandDescription]
        
            Gets an array of most recent command descriptions.
            Returns: An array of command descriptions.
        """
        pass

    @staticmethod
    def InCommand():
        """
        InCommand() -> bool
        
            Determines if Rhino is currently running a command.
            Returns: true if a command is currently running, false if no commands are currently running.
        """
        pass

    @staticmethod
    def InScriptRunnerCommand():
        """
        InScriptRunnerCommand() -> bool
        
            This is a low level tool to determine if Rhino is currently running
                    a script 
             running command like "ReadCommandFile" or the RhinoScript
                    plug-in's "RunScript".
        
            Returns: true if a script running command is active.
        """
        pass

    @staticmethod
    def IsCommand(name):
        """
        IsCommand(name: str) -> bool
        
            Determines is a string is a command.
        
            name: A string.
            Returns: true if the string is a command.
        """
        pass

    @staticmethod
    def IsValidCommandName(name):
        """
        IsValidCommandName(name: str) -> bool
        
            Determines if a string is a valid command name.
        
            name: A string.
            Returns: true if the string is a valid command name.
        """
        pass

    @staticmethod
    def LookupCommandId(name, searchForEnglishName):
        """
        LookupCommandId(name: str, searchForEnglishName: bool) -> Guid
        
            Returns the ID of a command.
        
            name: The name of the command.
            searchForEnglishName: true if the name is to searched in English. This ensures that a '_' is prepended to the name.
            Returns: An of the command, or System.Guid.Empty on error.
        """
        pass

    @staticmethod
    def LookupCommandName(commandId, englishName):
        """
        LookupCommandName(commandId: Guid, englishName: bool) -> str
        
            Returns the command name given a command ID.
        
            commandId: A command ID.
            englishName: true if the requested command is in English.
            Returns: The command name, or null on error.
        """
        pass

    def OnHelp(self, *args): #cannot find CLR method
        """
        OnHelp(self: Command)
            Is called when the user needs assistance with this command.
        """
        pass

    def ReplayHistory(self, *args): #cannot find CLR method
        """
        ReplayHistory(self: Command, replayData: ReplayHistoryData) -> bool
        
            Repeats an operation of a command.
        
            replayData: The replay history information.
            Returns: true if the operation succeeded.
                    The default implementation always returns false.
        """
        pass

    def RunCommand(self, *args): #cannot find CLR method
        """
        RunCommand(self: Command, doc: RhinoDoc, mode: RunMode) -> Result
        
            Executes the command.
        
            doc: The current document.
            mode: The command running mode.
            Returns: The command result code.
        """
        pass

    CommandContextHelpUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the URL of the command contextual help. This is usually a location of a local CHM file.
            The default implementation return an empty string.

"""

    EnglishName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the command.
            This method is abstract.

Get: EnglishName(self: Command) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the  unique ID of this command. It is best to use a Guid
            attribute for each custom derived command class since this will
            keep the id consistent between sessions of Rhino
            System.Runtime.InteropServices.GuidAttributeGuidAttribute

Get: Id(self: Command) -> Guid

"""

    LocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the local name of the command.

Get: LocalName(self: Command) -> str

"""

    PlugIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the plug-in where this commands is placed.

Get: PlugIn(self: Command) -> PlugIn

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the settings of the command.

Get: Settings(self: Command) -> PersistentSettings

"""


    BeginCommand = None
    EndCommand = None
    UndoRedo = None


class CommandEventArgs(EventArgs):
    # no doc
    CommandEnglishName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the English name of the command that raised this event.

Get: CommandEnglishName(self: CommandEventArgs) -> str

"""

    CommandId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ID of the command that raised this event.

Get: CommandId(self: CommandEventArgs) -> Guid

"""

    CommandLocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the command that raised this event in the local language.

Get: CommandLocalName(self: CommandEventArgs) -> str

"""

    CommandPluginName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the plug-in that this command belongs to.  If the command is internal
            to Rhino, then this propert is an empty string.

Get: CommandPluginName(self: CommandEventArgs) -> str

"""

    CommandResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the result of the command that raised this event. 
            This value is only meaningful during EndCommand events.

Get: CommandResult(self: CommandEventArgs) -> Result

"""



class CommandStyleAttribute(Attribute, _Attribute):
    """
    Decorates Rhino.Commands.Commandcommands to provide styles.
    
    CommandStyleAttribute(styles: Style)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, styles):
        """ __new__(cls: type, styles: Style) """
        pass

    Styles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the associated style.

Get: Styles(self: CommandStyleAttribute) -> Style

"""



class CustomUndoEventArgs(EventArgs):
    """ Argument package that is passed to a custom undo delegate """
    ActionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActionDescription(self: CustomUndoEventArgs) -> str

"""

    CommandId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandId(self: CustomUndoEventArgs) -> Guid

"""

    CreatedByRedo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedByRedo(self: CustomUndoEventArgs) -> bool

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: CustomUndoEventArgs) -> RhinoDoc

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tag(self: CustomUndoEventArgs) -> object

"""

    UndoSerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndoSerialNumber(self: CustomUndoEventArgs) -> UInt32

"""



class MostRecentCommandDescription(object):
    """
    Stores the macro and display string of the most recent command.
    
    MostRecentCommandDescription()
    """
    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayString(self: MostRecentCommandDescription) -> str

Set: DisplayString(self: MostRecentCommandDescription) = value
"""

    Macro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Macro(self: MostRecentCommandDescription) -> str

Set: Macro(self: MostRecentCommandDescription) = value
"""



class Result(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines enumerated constant values for several command result types.
    
    enum Result, values: Cancel (1), CancelModelessDialog (5), ExitRhino (268435455), Failure (3), Nothing (2), Success (0), UnknownCommand (4)
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
    CancelModelessDialog = None
    ExitRhino = None
    Failure = None
    Nothing = None
    Success = None
    UnknownCommand = None
    value__ = None


class RunMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides enumerated constants for a command running mode. This is currently interactive or scripted.
    
    enum RunMode, values: Interactive (0), Scripted (1)
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

    Interactive = None
    Scripted = None
    value__ = None


class SelCommand(Command):
    """
    For adding nestable selection commands that work like the native Rhino
                SelCrv command, derive your command from SelCommand and override the
                virtual SelFilter function.
    """
    def SelFilter(self, *args): #cannot find CLR method
        """
        SelFilter(self: SelCommand, rhObj: RhinoObject) -> bool
        
            Override this virtual function and return true if object should be selected.
        
            rhObj: The object to check regarding selection status.
            Returns: true if the object should be selected; false otherwise.
        """
        pass

    BeQuiet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeQuiet(self: SelCommand) -> bool

Set: BeQuiet(self: SelCommand) = value
"""

    CommandContextHelpUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the URL of the command contextual help. This is usually a location of a local CHM file.
            The default implementation return an empty string.

"""

    TestGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TestGrips(self: SelCommand) -> bool

Set: TestGrips(self: SelCommand) = value
"""

    TestLights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TestLights(self: SelCommand) -> bool

Set: TestLights(self: SelCommand) = value
"""



class Style(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines bitwise mask flags for different styles of commands, such as
                Rhino.Commands.Style.HiddenHidden or Rhino.Commands.Style.DoNotRepeatDoNotRepeat.
    
    enum (flags) Style, values: DoNotRepeat (8), Hidden (1), None (0), NotUndoable (16), ScriptRunner (2), Transparent (4)
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

    DoNotRepeat = None
    Hidden = None
    None = None
    NotUndoable = None
    ScriptRunner = None
    Transparent = None
    value__ = None


class TransformCommand(Command):
    # no doc
    def DuplicateObjects(self, *args): #cannot find CLR method
        """ DuplicateObjects(self: TransformCommand, list: TransformObjectList) """
        pass

    def ResetGrips(self, *args): #cannot find CLR method
        """
        ResetGrips(self: TransformCommand, list: TransformObjectList)
            Sets dynamic grip locations back to starting grip locations. This makes things
                    like 
             the Copy command work when grips are "copied".
        
        
            list: A list of object to transform. This is a special list type.
        """
        pass

    def SelectObjects(self, *args): #cannot find CLR method
        """
        SelectObjects(self: TransformCommand, prompt: str, list: TransformObjectList) -> Result
        
            Selects objects within the command.
        
            prompt: The selection prompt.
            list: A list of objects to transform. This is a special list type.
            Returns: The operation result.
        """
        pass

    def TransformObjects(self, *args): #cannot find CLR method
        """ TransformObjects(self: TransformCommand, list: TransformObjectList, xform: Transform, copy: bool, autoHistory: bool) """
        pass

    CommandContextHelpUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the URL of the command contextual help. This is usually a location of a local CHM file.
            The default implementation return an empty string.

"""



class UndoRedoEventArgs(EventArgs):
    # no doc
    CommandId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandId(self: UndoRedoEventArgs) -> Guid

"""

    IsBeginRecording = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBeginRecording(self: UndoRedoEventArgs) -> bool

"""

    IsBeginRedo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBeginRedo(self: UndoRedoEventArgs) -> bool

"""

    IsBeginUndo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBeginUndo(self: UndoRedoEventArgs) -> bool

"""

    IsEndRecording = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEndRecording(self: UndoRedoEventArgs) -> bool

"""

    IsEndRedo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEndRedo(self: UndoRedoEventArgs) -> bool

"""

    IsEndUndo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEndUndo(self: UndoRedoEventArgs) -> bool

"""

    IsPurgeRecord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPurgeRecord(self: UndoRedoEventArgs) -> bool

"""

    UndoSerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndoSerialNumber(self: UndoRedoEventArgs) -> UInt32

"""



