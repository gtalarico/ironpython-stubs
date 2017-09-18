# encoding: utf-8
# module Rhino.Runtime calls itself Runtime
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AssemblyResolver(object):
    """ Assembly Resolver for the Rhino App Domain. """
    @staticmethod
    def AddSearchFile(file):
        """
        AddSearchFile(file: str)
            Register another file with the Assembly Resolver. File must be a .NET assembly, 
                    so 
             it should probably be a dll, rhp or exe.
        
        
            file: Path of file to include during Assembly Resolver events.
        """
        pass

    @staticmethod
    def AddSearchFolder(folder):
        """
        AddSearchFolder(folder: str)
            Register a custom folder with the Assembly Resolver. Folders will be 
                    searched 
             recursively, so this could potentially be a very expensive operation. 
                    If at all 
             possible, you should consider only registering individual files.
        
        
            folder: Path of folder to include during Assembly Resolver events.
        """
        pass

    __all__ = [
        'AddSearchFile',
        'AddSearchFolder',
    ]


class CommonObject(object, IDisposable, ISerializable):
    """ Base class for .NET classes that wrap C++ unmanaged Rhino classes. """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """
        ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int)
            Assigns a parent object and a subobject index to this.
        
            parentObject: The parent object.
            subobject_index: The subobject index.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CommonObject)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def EnsurePrivateCopy(self):
        """
        EnsurePrivateCopy(self: CommonObject)
            If you want to keep a copy of this class around by holding onto it in a variable after a command
             
                    completes, call EnsurePrivateCopy to make sure that this class is not tied to the 
             document. You can
                    call this function as many times as you want.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: CommonObject, info: SerializationInfo, context: StreamingContext)
            Populates a System.Runtime.Serialization.SerializationInfo with the data needed to serialize the 
             target object.
        
        
            info: The System.Runtime.Serialization.SerializationInfo to populate with data.
            context: The destination (see System.Runtime.Serialization.StreamingContext) for this serialization.
        """
        pass

    def IsValidWithLog(self, log):
        """
        IsValidWithLog(self: CommonObject) -> (bool, str)
        
            Determines if an object is valid. Also provides a report on errors if this
                    object 
             happens not to be valid.
        
            Returns: true if this object is valid; false otherwise.
        """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """
        NonConstOperation(self: CommonObject)
            For derived classes implementers.
                    Defines the necessary implementation to free the 
             instance from being const.
        """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """
        OnSwitchToNonConst(self: CommonObject)
            Is called when a non-const operation first occurs.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    HasUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if this class has any custom information attached to it through UserData.

Get: HasUserData(self: CommonObject) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true this object may not be modified. Any properties or functions that attempt
            to modify this object when it is set to "IsReadOnly" will throw a NotSupportedException.

Get: IsDocumentControlled(self: CommonObject) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests an object to see if it is valid.

Get: IsValid(self: CommonObject) -> bool

"""

    UserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of custom information that is attached to this class.

Get: UserData(self: CommonObject) -> UserDataList

"""

    UserDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary of custom information attached to this class. The dictionary is actually user
            data provided as an easy to use sharable set of information.

Get: UserDictionary(self: CommonObject) -> ArchivableDictionary

"""



class DocumentCollectedException(Exception, ISerializable, _Exception):
    """
    Represents the error that happen when a class user attempts to execute a modifying operation
                on an object that has been added to a document.
    
    DocumentCollectedException()
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class HostUtils(object):
    """ Contains static methods to deal with teh runtime environment. """
    @staticmethod
    def CheckForRdk(throwOnFalse, usePreviousResult):
        """
        CheckForRdk(throwOnFalse: bool, usePreviousResult: bool) -> bool
        
            Determines if the RDK is loaded.
        
            throwOnFalse: if the RDK is not loaded, then throws a
                    Rhino.Runtime.RdkNotLoadedException.
            usePreviousResult: if true, then the last result can be used instaed of
                    performing a full check.
            Returns: true if the RDK is loaded; false if the RDK is not loaded. Note that the
                    
             Rhino.Runtime.RdkNotLoadedException will hinder the retrieval of any return value.
        """
        pass

    @staticmethod
    def CreateCommands(*__args):
        """
        CreateCommands(pPlugIn: IntPtr, pluginAssembly: Assembly) -> int
        
            Parses a plugin and create all the commands defined therein.
        
            pPlugIn: Plugin to harvest for commands.
            pluginAssembly: Assembly associated with the plugin.
            Returns: The number of newly created commands.
        CreateCommands(plugin: PlugIn)
            Parses a plugin and create all the commands defined therein.
        
            plugin: Plugin to harvest for commands.
        """
        pass

    @staticmethod
    def CreatePlugIn(pluginType, printDebugMessages):
        """
        CreatePlugIn(pluginType: Type, printDebugMessages: bool) -> PlugIn
        
            Instantiates a plug-in type and registers the associated commands and classes.
        
            pluginType: A plug-in type. This type must derive from Rhino.PlugIns.PlugIn.
            printDebugMessages: true if debug messages should be printed.
            Returns: A new plug-in instance.
        """
        pass

    @staticmethod
    def DebugDumpToString(*__args):
        """
        DebugDumpToString(bezierCurve: BezierCurve) -> str
        
            Gets the debug dumps. This is a text description of the geometric contents.
                    
             DebugDump() is intended for debugging and is not suitable for creating high
                    quality 
             text descriptions of an object.
        
        
            bezierCurve: curve to evaluate
            Returns: A debug dump text.
        DebugDumpToString(geometry: GeometryBase) -> str
        
            Gets the debug dumps. This is a text description of the geometric contents.
                    
             DebugDump() is intended for debugging and is not suitable for creating high
                    quality 
             text descriptions of an object.
        
        
            geometry: Some geometry.
            Returns: A debug dump text.
        """
        pass

    @staticmethod
    def DebugString(*__args):
        """
        DebugString(format: str, *args: Array[object])
            Prints a debug message to the Rhino Command Line. 
                    The message will only appear if 
             the SendDebugToCommandLine property is set to true.
        
        
            format: Message to format and print.
            args: An Object array containing zero or more objects to format.
        DebugString(msg: str)
            Prints a debug message to the Rhino Command Line. 
                    The message will only appear if 
             the SendDebugToCommandLine property is set to true.
        
        
            msg: Message to print.
        """
        pass

    @staticmethod
    def DisplayOleAlerts(display):
        """
        DisplayOleAlerts(display: bool)
            Defines if Ole alerts ("Server busy") alerts should be visualized.
                    This function 
             makes no sense on Mono.
        
        
            display: Whether alerts should be visible.
        """
        pass

    @staticmethod
    def ExceptionReport(*__args):
        """
        ExceptionReport(source: str, ex: Exception)
            Informs RhinoCommon of an exception that has been handled but that the developer wants to screen.
        
            source: An exception source text.
            ex: An exception.
        ExceptionReport(ex: Exception)
            Informs RhinoCommon of an exception that has been handled but that the developer wants to screen.
        
            ex: An exception.
        """
        pass

    @staticmethod
    def GetAssemblySearchPaths():
        """
        GetAssemblySearchPaths() -> Array[str]
        
            Returns list of directory names where additional assemblies (plug-ins, DLLs, Grasshopper 
             components)
                    may be located
        """
        pass

    @staticmethod
    def GetRhinoDotNetAssembly():
        """
        GetRhinoDotNetAssembly() -> Assembly
        
            Only works on Windows. Returns null on Mac.
            Returns: An assembly.
        """
        pass

    @staticmethod
    def InitializeRhinoCommon():
        """
        InitializeRhinoCommon()
            Makes sure all static RhinoCommon components is set up correctly. 
                    This happens 
             automatically when a plug-in is loaded, so you probably won't 
                    have to call this 
             method.
        """
        pass

    @staticmethod
    def InitializeZooClient():
        """
        InitializeZooClient()
            Initializes the ZooClient and Rhino license manager, this should get
                    called 
             automatically when RhinoCommon is loaded so you probably won't
                    have to call this 
             method.
        """
        pass

    @staticmethod
    def InPlaceConstCast(geometry, makeNonConst):
        """
        InPlaceConstCast(geometry: GeometryBase, makeNonConst: bool)
            DO NOT USE UNLESS YOU ARE CERTAIN ABOUT THE IMPLICATIONS.
                    This is an expert user 
             function which should not be needed in most
                    cases. This function is similar to a 
             const_cast in C++ to allow an object
                    to be made temporarily modifiable without 
             causing RhinoCommon to convert
                    the class from const to non-const by creating a 
             duplicate.You must call this function with a true parameter, make your
                    
             modifications, and then restore the const flag by calling this function
                    again with 
             a false parameter. If you have any questions, please
                    contact McNeel developer 
             support before using!
        
        
            geometry: Some geometry.
            makeNonConst: A boolean value.
        """
        pass

    @staticmethod
    def InvokeOnMainUiThread(method, args=None):
        """
        InvokeOnMainUiThread(method: Delegate, *args: Array[object]) -> object
        
            Calls a method on the main Rhino UI thread if this is necessary.
        
            method: A method. This method is called with args arguments.
            args: The method arguments.
            Returns: A return object, or null.
        InvokeOnMainUiThread(method: Delegate) -> object
        
            Calls a method on the main Rhino UI thread if this is necessary.
        
            method: A method. This method is called with no arguments.
            Returns: A return object, or null.
        """
        pass

    @staticmethod
    def RegisterDynamicCommand(plugin, cmd):
        """
        RegisterDynamicCommand(plugin: PlugIn, cmd: Command) -> bool
        
            Adds a new dynamic command to Rhino.
        
            plugin: Plugin that owns the command.
            cmd: Command to add.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def SetInShutDown():
        """
        SetInShutDown()
            Informs the runtime that the application is shutting down.
        """
        pass

    ExceptionReportDelegate = None
    OnExceptionReport = None
    RunningInMono = False
    RunningInRhino = False
    RunningOnOSX = False
    RunningOnWindows = True
    SendDebugToCommandLine = False
    __all__ = [
        'CheckForRdk',
        'CreateCommands',
        'CreatePlugIn',
        'DebugDumpToString',
        'DebugString',
        'DisplayOleAlerts',
        'ExceptionReport',
        'ExceptionReportDelegate',
        'GetAssemblySearchPaths',
        'GetRhinoDotNetAssembly',
        'InitializeRhinoCommon',
        'InitializeZooClient',
        'InPlaceConstCast',
        'InvokeOnMainUiThread',
        'OnExceptionReport',
        'RegisterDynamicCommand',
        'SetInShutDown',
    ]


class Interop(object):
    """ Contains static methods to marshal objects between RhinoCommon and legacy Rhino_DotNet or C++. """
    @staticmethod
    def CreateFromNativePointer(pGeometry):
        """
        CreateFromNativePointer(pGeometry: IntPtr) -> GeometryBase
        
            Constructs a RhinoCommon Geometry class from a given ON_Geomety*. The ON_Geometry*
                    
             must be declared on the heap and its lifetime becomes controlled by RhinoCommon.
        
        
            pGeometry: ON_Geometry*
            Returns: The appropriate geometry class in RhinoCommon on success.
        """
        pass

    @staticmethod
    def FromOnBrep(source):
        """
        FromOnBrep(source: object) -> Brep
        
            Copies a Rhino_DotNet brep to a RhinoCommon brep class.
        
            source: RMA.OpenNURBS.IOnBrep or RMA.OpenNURBS.OnBrep.
            Returns: RhinoCommon object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def FromOnCurve(source):
        """
        FromOnCurve(source: object) -> Curve
        
            Copies a Rhino_DotNet curve to a RhinoCommon curve class.
        
            source: RMA.OpenNURBS.IOnCurve or RMA.OpenNURBS.OnCurve.
            Returns: RhinoCommon object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def FromOnMesh(source):
        """
        FromOnMesh(source: object) -> Mesh
        
            Copies a Rhino_DotNet mesh to a RhinoCommon mesh class.
        
            source: RMA.OpenNURBS.IOnMesh or RMA.OpenNURBS.OnMesh.
            Returns: RhinoCommon object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def FromOnSurface(source):
        """
        FromOnSurface(source: object) -> Surface
        
            Copies a Rhino_DotNet surface to a RhinoCommon Surface class.
        
            source: Any of the following in the RMA.OpenNURBS namespace are acceptable.
                    IOnSurface, 
             OnSurface, IOnPlaneSurface, OnPlaneSurface, IOnClippingPlaneSurface,
                    
             OnClippingPlaneSurface, IOnNurbsSurface, OnNurbsSurfac, IOnRevSurface, OnRevSurface,
                   
              IOnSumSurface, OnSumSurface.
        
            Returns: RhinoCommon object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def NativeGeometryConstPointer(geometry):
        """
        NativeGeometryConstPointer(geometry: GeometryBase) -> IntPtr
        
            Returns the underlying const ON_Geometry* for a RhinoCommon class. You should only
                    
             be interested in using this function if you are writing C++ code.
        
        
            geometry: A geometry object. This can be null and in such a case System.IntPtr.Zero is returned.
            Returns: A pointer to the const geometry.
        """
        pass

    @staticmethod
    def NativeGeometryNonConstPointer(geometry):
        """
        NativeGeometryNonConstPointer(geometry: GeometryBase) -> IntPtr
        
            Returns the underlying non-const ON_Geometry* for a RhinoCommon class. You should
                    
             only be interested in using this function if you are writing C++ code.
        
        
            geometry: A geometry object. This can be null and in such a case System.IntPtr.Zero is returned.
            Returns: A pointer to the non-const geometry.
        """
        pass

    @staticmethod
    def NativeNonConstPointer(viewport):
        """
        NativeNonConstPointer(viewport: ViewportInfo) -> IntPtr
        
            Get ON_Viewport* from a ViewportInfo instance
        """
        pass

    @staticmethod
    def NativeRhinoDocPointer(doc):
        """
        NativeRhinoDocPointer(doc: RhinoDoc) -> IntPtr
        
            Gets the C++ CRhinoDoc* for a given RhinoCommon RhinoDoc class.
        
            doc: A document.
            Returns: A pointer value.
        """
        pass

    @staticmethod
    def PlugInPointer(plugin):
        """
        PlugInPointer(plugin: PlugIn) -> IntPtr
        
            Gets a C++ plug-in pointer for a given RhinoCommon plug-in.
                    This is a Rhino SDK 
             function.
        
        
            plugin: A plug-in.
            Returns: A pointer.
        """
        pass

    @staticmethod
    def RhinoObjectConstPointer(rhinoObject):
        """
        RhinoObjectConstPointer(rhinoObject: RhinoObject) -> IntPtr
        
            Returns the underlying const CRhinoObject* for a RhinoCommon class. You should only
                    
             be interested in using this function if you are writing C++ code.
        
        
            rhinoObject: A Rhino object.
            Returns: A pointer to the Rhino const object.
        """
        pass

    @staticmethod
    def RhinoObjectFromPointer(pRhinoObject):
        """
        RhinoObjectFromPointer(pRhinoObject: IntPtr) -> RhinoObject
        
            Constructs a RhinoCommon Rhino object from an unmanaged C++ RhinoObject pointer.
        
            pRhinoObject: The original pointer.
            Returns: A new Rhino object, or null if the pointer was invalid or System.IntPtr.Zero.
        """
        pass

    @staticmethod
    def ToIRhinoViewport(source):
        """
        ToIRhinoViewport(source: RhinoViewport) -> object
        
            Convert a Rhino.Display.Viewport to an RMA.Rhino.IRhinoViewport.
        
            source: A RhinoCommon viewport.
            Returns: Rhino_DotNet IRhinoViewport object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def ToOnBrep(source):
        """
        ToOnBrep(source: Brep) -> object
        
            Constructs a Rhino_DotNet OnBrep that is a copy of a given brep.
        
            source: A source brep.
            Returns: Rhino_DotNet object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def ToOnCurve(source):
        """
        ToOnCurve(source: Curve) -> object
        
            Constructs a Rhino_DotNet OnCurve that is a copy of a given curve.
        
            source: A RhinoCommon source curve.
            Returns: Rhino_DotNet object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def ToOnMesh(source):
        """
        ToOnMesh(source: Mesh) -> object
        
            Constructs a Rhino_DotNet OnMesh that is a copy of a given mesh.
        
            source: A source brep.
            Returns: Rhino_DotNet object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def ToOnSurface(source):
        """
        ToOnSurface(source: Surface) -> object
        
            Constructs a Rhino_DotNet OnSurface that is a copy of a given curve.
        
            source: A source brep.
            Returns: Rhino_DotNet object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def ToOnXform(source):
        """
        ToOnXform(source: Transform) -> object
        
            Constructs a Rhino_DotNet OnXform from a given RhinoCommon Transform.
        
            source: A RhinoCommon source transform.
            Returns: Rhino_DotNet object on success. This will be an independent copy.
        """
        pass

    @staticmethod
    def TryCopyFromOnArc(source, destination):
        """
        TryCopyFromOnArc(source: object) -> (bool, Arc)
        
            Attempts to copy the contents of a RMA.OpenNURBS.OnArc to a Rhino.Geometry.Arc.
        
            source: A source OnArc.
            Returns: true if the operation succeeded; false otherwise.
        """
        pass

    @staticmethod
    def TryCopyToOnArc(source, destination):
        """
        TryCopyToOnArc(source: Arc, destination: object) -> bool
        
            Attempts to copy the contents of a Rhino.Geometry.Arc to a RMA.OpenNURBS.OnArc.
        
            source: A source arc.
            destination: A destination OnArc.
            Returns: true if the operation succeeded; false otherwise.
        """
        pass

    __all__ = [
        'CreateFromNativePointer',
        'FromOnBrep',
        'FromOnCurve',
        'FromOnMesh',
        'FromOnSurface',
        'NativeGeometryConstPointer',
        'NativeGeometryNonConstPointer',
        'NativeNonConstPointer',
        'NativeRhinoDocPointer',
        'PlugInPointer',
        'RhinoObjectConstPointer',
        'RhinoObjectFromPointer',
        'ToIRhinoViewport',
        'ToOnBrep',
        'ToOnCurve',
        'ToOnMesh',
        'ToOnSurface',
        'ToOnXform',
        'TryCopyFromOnArc',
        'TryCopyToOnArc',
    ]


class PythonCompiledCode(object):
    """ Represents scripting compiled code. """
    def Execute(self, scope):
        """
        Execute(self: PythonCompiledCode, scope: PythonScript)
            Executes the script in a specific scope.
        
            scope: The scope where the script should be executed.
        """
        pass


class PythonScript(object):
    """ Represents a Python script. """
    def Compile(self, script):
        """
        Compile(self: PythonScript, script: str) -> PythonCompiledCode
        
            Compiles a class in a quick-to-execute proxy.
        
            script: A string text.
            Returns: A Python compiled code instance.
        """
        pass

    def ContainsVariable(self, name):
        """
        ContainsVariable(self: PythonScript, name: str) -> bool
        
            Determines if the main scripting context has a variable with a name.
        
            name: The variable name.
            Returns: true if the variable is present.
        """
        pass

    @staticmethod
    def Create():
        """
        Create() -> PythonScript
        
            Constructs a new Python script context.
            Returns: A new Python script, or null if none could be created. Rhino 4 always returns null.
        """
        pass

    def CreateTextEditorControl(self, script, helpcallback):
        """ CreateTextEditorControl(self: PythonScript, script: str, helpcallback: Action[str]) -> Control """
        pass

    def EvaluateExpression(self, statements, expression):
        """
        EvaluateExpression(self: PythonScript, statements: str, expression: str) -> object
        
            Evaluates statements and an expression in the main scripting context.
        
            statements: One or several statements.
            expression: An expression.
            Returns: The expression result.
        """
        pass

    def ExecuteFile(self, path):
        """
        ExecuteFile(self: PythonScript, path: str) -> bool
        
            Executes a Python file.
        
            path: The path to the file.
            Returns: true if the file executed. This method can throw scripting-runtime based exceptions.
        """
        pass

    def ExecuteScript(self, script):
        """
        ExecuteScript(self: PythonScript, script: str) -> bool
        
            Executes a Python string.
        
            script: A Python text.
            Returns: true if the file executed. This method can throw scripting-runtime based exceptions.
        """
        pass

    def GetStackTraceFromException(self, ex):
        """
        GetStackTraceFromException(self: PythonScript, ex: Exception) -> str
        
            Retrieves a meaningful representation of the call stack.
        
            ex: An exception that was thrown by some of the methods in this class.
            Returns: A string that represents the Python exception.
        """
        pass

    def GetVariable(self, name):
        """
        GetVariable(self: PythonScript, name: str) -> object
        
            Gets the object associated with a variable name in the main scripting context.
        
            name: A variable name.
            Returns: The variable object.
        """
        pass

    def GetVariableNames(self):
        """
        GetVariableNames(self: PythonScript) -> IEnumerable[str]
        
            Retrieves all variable names in the script.
            Returns: An enumerable set with all names of the variables.
        """
        pass

    def RemoveVariable(self, name):
        """
        RemoveVariable(self: PythonScript, name: str)
            Removes a defined variable from the main scripting context.
        
            name: The variable name.
        """
        pass

    def SetIntellisenseVariable(self, name, value):
        """
        SetIntellisenseVariable(self: PythonScript, name: str, value: object)
            Sets a variable for runtime introspection.
        
            name: A variable name.
            value: A variable value.
        """
        pass

    def SetVariable(self, name, value):
        """
        SetVariable(self: PythonScript, name: str, value: object)
            Sets a variable with a name and an object. Object can be null (Nothing in Visual Basic).
        
            name: A valid variable name in Python.
            value: A valid value for that variable name.
        """
        pass

    ContextId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a context unique identified.

Get: ContextId(self: PythonScript) -> int

Set: ContextId(self: PythonScript) = value
"""

    Output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Python script "print()" target.
            By default string output goes to the Rhino.RhinoApp.Write function.
            Set Output if you want to redirect the output from python to a different function
            while this script executes.

Get: Output(self: PythonScript) -> Action[str]

Set: Output(self: PythonScript) = value
"""

    ScriptContextDoc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object set to variable held in scriptcontext.doc.

Get: ScriptContextDoc(self: PythonScript) -> object

Set: ScriptContextDoc(self: PythonScript) = value
"""



class RdkNotLoadedException(Exception, ISerializable, _Exception):
    """
    Is thrown when the RDK is not loaded.
    
    RdkNotLoadedException()
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Skin(object):
    """
    Represents a customized environment that changes the appearance of Rhino.
                Skin DLLs must contain a single class that derives from the Skin class.
    """
    def HideSplash(self, *args): #cannot find CLR method
        """
        HideSplash(self: Skin)
            Is called when the splash screen should be hidden.
        """
        pass

    def OnBeginLoadAtStartPlugIns(self, *args): #cannot find CLR method
        """
        OnBeginLoadAtStartPlugIns(self: Skin, expectedCount: int)
            Is called when the first plug-in that loads at start-up is going to be loaded.
        
            expectedCount: The complete amount of plug-ins.
        """
        pass

    def OnBeginLoadPlugIn(self, *args): #cannot find CLR method
        """
        OnBeginLoadPlugIn(self: Skin, description: str)
            Is called when a specific plug-in is going to be loaded.
        
            description: The plug-in description.
        """
        pass

    def OnBuiltInCommandsRegistered(self, *args): #cannot find CLR method
        """
        OnBuiltInCommandsRegistered(self: Skin)
            Is called when built-in commands are registered.
        """
        pass

    def OnEndLoadAtStartPlugIns(self, *args): #cannot find CLR method
        """
        OnEndLoadAtStartPlugIns(self: Skin)
            Is called after all of the load at start plug-ins have been loaded.
        """
        pass

    def OnEndLoadPlugIn(self, *args): #cannot find CLR method
        """
        OnEndLoadPlugIn(self: Skin)
            Is called after each plug-in has been loaded.
        """
        pass

    def OnLicenseCheckCompleted(self, *args): #cannot find CLR method
        """
        OnLicenseCheckCompleted(self: Skin)
            Is called when the license check is completed.
        """
        pass

    def OnMainFrameWindowCreated(self, *args): #cannot find CLR method
        """
        OnMainFrameWindowCreated(self: Skin)
            Is called when the main frame window is created.
        """
        pass

    def ShowHelp(self, *args): #cannot find CLR method
        """
        ShowHelp(self: Skin)
            Called when the "help" splash screen should be shown. Default
                    implementation just 
             calls ShowSplash()
        """
        pass

    def ShowSplash(self, *args): #cannot find CLR method
        """
        ShowSplash(self: Skin)
            Is called when the splash screen should be shown.
        """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If you want to provide a custom name for your skin.

"""

    MainRhinoIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If you want to provide a custom icon for your skin.

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets access to the skin persistent settings.

Get: Settings(self: Skin) -> PersistentSettings

"""


    ActiveSkin = None


# variables with complex values

