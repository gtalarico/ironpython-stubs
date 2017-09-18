# encoding: utf-8
# module clr
# from (built-in)
# by generator 1.145
"""
Python module.  Stores classes, functions, and data.  Usually a module
            is created by importing a file or package from disk.  But a module can also
            be directly created by calling the module type and providing a name or
            optionally a documentation string.

module()
"""
# no imports

# Variables with simple values

IsNetStandard = False

# functions

def accepts(*types, p_object=None): # real signature unknown; restored from __doc__
    """
    accepts(*types: Array[object]) -> object
    
        accepts(*types) -> ArgChecker
                
                Decorator that returns a new callable 
         object which will validate the arguments are of the specified types.
    """
    return object()

def AddReference(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters can be an already loaded
    Assembly object, a full assembly name, or a partial assembly name. After the
    load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceByName(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are an assembly name. 
    After the load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceByPartialName(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are a partial assembly name. 
    After the load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceToFile(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided.  The assembly is searched for in the directories specified in 
    sys.path and dependencies will be loaded from sys.path as well.  The assembly 
    name should be the filename on disk without a directory specifier and 
    optionally including the .EXE or .DLL extension. After the load the assemblies 
    namespaces and top-level types will be available via import Namespace.
    """
    pass

def AddReferenceToFileAndPath(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  One or more assembly names can
    be provided which are fully qualified names to the file on disk.  The 
    directory is added to sys.path and AddReferenceToFile is then called. After the 
    load the assemblies namespaces and top-level types will be available via 
    import Namespace.
    """
    pass

def AddReferenceToTypeLibrary(rcw): # real signature unknown; restored from __doc__
    """
    AddReferenceToTypeLibrary(rcw: object)
        AddReferenceToTypeLibrary(rcw) -> None
                
                Makes the type lib desc 
         available for importing. See also LoadTypeLibrary.
    
    AddReferenceToTypeLibrary(typeLibGuid: Guid)
        AddReferenceToTypeLibrary(guid) -> None
                
                Makes the type lib desc 
         available for importing.  See also LoadTypeLibrary.
    """
    pass

def ClearProfilerData(): # real signature unknown; restored from __doc__
    """
    ClearProfilerData()
        Resets all profiler counters back to zero
    """
    pass

def CompileModules(assemblyName, **kwArgs, p_str=None, p_object=None, *args): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ CompileModules(assemblyName: str, **kwArgs: IDictionary[str, object], *filenames: Array[str]) """
    pass

def CompileSubclassTypes(assemblyName, *newTypes, p_object=None): # real signature unknown; restored from __doc__
    """
    CompileSubclassTypes(assemblyName: str, *newTypes: Array[object])
        clr.CompileSubclassTypes(assemblyName, *typeDescription)
                
                Provides a 
         helper for creating an assembly which contains pre-generated .NET 
                base types for 
         new-style types.
                
                This assembly can then be AddReferenced or put 
         sys.prefix\DLLs and the cached 
                types will be used instead of generating the types 
         at runtime.
                
                This function takes the name of the assembly to save to 
         and then an arbitrary 
                number of parameters describing the types to be created.  
         Each of those
                parameter can either be a plain type or a sequence of base types.
       
                  
                clr.CompileSubclassTypes(object) -> create a base type for object
           
              clr.CompileSubclassTypes(object, str, System.Collections.ArrayList) -> create 
                
             base  types for both object and ArrayList.
                    
                
         clr.CompileSubclassTypes(object, (object, IComparable)) -> create base types for 
                  
           object and an object which implements IComparable.
    """
    pass

def Convert(o, toType): # real signature unknown; restored from __doc__
    """
    Convert(o: object, toType: Type) -> object
    
        Attempts to convert the provided object to the specified type.  Conversions that 
                
         will be attempted include standard Python conversions as well as .NET implicit
                and 
         explicit conversions.
                
                If the conversion cannot be performed a 
         TypeError will be raised.
    """
    return object()

def Deserialize(serializationFormat, data): # real signature unknown; restored from __doc__
    """
    Deserialize(serializationFormat: str, data: str) -> object
    
        Deserializes the result of a Serialize call.  This can be used to perform serialization
            
             for .NET types which are serializable.  This method is the callable object provided
            
             from __reduce_ex__ for .serializable .NET types.
                
                The first 
         parameter indicates the serialization format and is the first tuple element
                
         returned from the Serialize call.  
                
                The second parameter is the 
         serialized data.
    """
    return object()

def Dir(o): # real signature unknown; restored from __doc__
    """
    Dir(o: object) -> list
    
        returns the result of dir(o) as-if "import clr" has not been performed.
    """
    return []

def DirClr(o): # real signature unknown; restored from __doc__
    """
    DirClr(o: object) -> list
    
        Returns the result of dir(o) as-if "import clr" has been performed.
    """
    return []

def EnableProfiler(enable): # real signature unknown; restored from __doc__
    """
    EnableProfiler(enable: bool)
        Enable or disable profiling for the current ScriptEngine.  This will only affect code
              
           that is compiled after the setting is changed; previously-compiled code will retain
              
           whatever setting was active when the code was originally compiled.
                
                
         The easiest way to recompile a module is to reload() it.
    """
    pass

def GetBytes(*args, **kwargs): # real signature unknown
    """ Converts a string to an array of bytesConverts maxCount of a string to an array of bytes """
    pass

def GetClrType(type): # real signature unknown; restored from __doc__
    """
    GetClrType(type: Type) -> Type
    
        Gets the CLR Type object from a given Python type object.
    """
    pass

def GetCurrentRuntime(): # real signature unknown; restored from __doc__
    """
    GetCurrentRuntime() -> ScriptDomainManager
    
        Gets the current ScriptDomainManager that IronPython is loaded into.  The
                
         ScriptDomainManager can then be used to work with the language portion of the
                DLR 
         hosting APIs.
    """
    pass

def GetDynamicType(t): # real signature unknown; restored from __doc__
    """
    GetDynamicType(t: Type) -> type
    
        OBSOLETE: Gets the Python type object from a given CLR Type object.
                
                
         Use clr.GetPythonType instead.
    """
    return type(*(), **{})

def GetProfilerData(includeUnused): # real signature unknown; restored from __doc__
    """
    GetProfilerData(includeUnused: bool) -> tuple
    
        Returns a list of profile data. The values are tuples of Profiler.Data objects
                
       
                  All times are expressed in the same unit of measure as DateTime.Ticks
    """
    return ()

def GetPythonType(t): # real signature unknown; restored from __doc__
    """
    GetPythonType(t: Type) -> type
    
        Gets the Python type object from a given CLR Type object.
    """
    return type(*(), **{})

def GetString(*args, **kwargs): # real signature unknown
    """ Converts an array of bytes to a string.Converts maxCount of an array of bytes to a string """
    pass

def GetSubclassedTypes(): # real signature unknown; restored from __doc__
    """
    GetSubclassedTypes() -> tuple
    
        clr.GetSubclassedTypes() -> tuple
                
                Returns a tuple of information 
         about the types which have been subclassed. 
                
                This tuple can be passed 
         to clr.CompileSubclassTypes to cache these
                types on disk such as:
                
       
                  clr.CompileSubclassTypes('assembly', *clr.GetSubclassedTypes())
    """
    return ()

def ImportExtensions(type): # real signature unknown; restored from __doc__
    """ ImportExtensions(type: type)ImportExtensions(namespace: namespace#) """
    pass

def LoadAssemblyByName(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified assembly name and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from 
    the assembly object.
    """
    pass

def LoadAssemblyByPartialName(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified partial assembly name and returns the 
    assembly object.  Namespaces or types in the assembly can be accessed directly 
    from the assembly object.
    """
    pass

def LoadAssemblyFromFile(*args, **kwargs): # real signature unknown
    """
    Loads an assembly from the specified filename and returns the assembly
    object.  Namespaces or types in the assembly can be accessed directly from 
    the assembly object.
    """
    pass

def LoadAssemblyFromFileWithPath(*args, **kwargs): # real signature unknown
    """
    Adds a reference to a .NET assembly.  Parameters are a full path to an. 
    assembly on disk. After the load the assemblies namespaces and top-level types 
    will be available via import Namespace.
    """
    pass

def LoadTypeLibrary(rcw): # real signature unknown; restored from __doc__
    """
    LoadTypeLibrary(rcw: object) -> ComTypeLibInfo
    
        LoadTypeLibrary(rcw) -> type lib desc
                
                Gets an ITypeLib object from 
         OLE Automation compatible RCW ,
                reads definitions of CoClass'es and Enum's from 
         this library
                and creates an object that allows to instantiate coclasses
               
          and get actual values for the enums.
    
    LoadTypeLibrary(typeLibGuid: Guid) -> ComTypeLibInfo
    
        LoadTypeLibrary(guid) -> type lib desc
                
                Reads the latest registered 
         type library for the corresponding GUID,
                reads definitions of CoClass'es and Enum's 
         from this library
                and creates a IDynamicMetaObjectProvider that allows to 
         instantiate coclasses
                and get actual values for the enums.
    """
    pass

def returns(type): # real signature unknown; restored from __doc__
    """
    returns(type: object) -> object
    
        returns(type) -> ReturnChecker
                
                Returns a new callable object which 
         will validate the return type is of the specified type.
    """
    return object()

def Self(): # real signature unknown; restored from __doc__
    """ Self() -> object """
    return object()

def Serialize(self): # real signature unknown; restored from __doc__
    """
    Serialize(self: object) -> tuple
    
        Serializes data using the .NET serialization formatter for complex
                types.  Returns 
         a tuple identifying the serialization format and the serialized 
                data which can be 
         fed back into clr.Deserialize.
                
                Current serialization formats include 
         custom formats for primitive .NET
                types which aren't already recognized as tuples.  
         None is used to indicate
                that the Binary .NET formatter is used.
    """
    return ()

def SetCommandDispatcher(dispatcher, Action=None): # real signature unknown; restored from __doc__
    """ SetCommandDispatcher(dispatcher: Action[Action]) -> Action[Action] """
    pass

def Use(name): # real signature unknown; restored from __doc__
    """
    Use(name: str) -> object
    
        Use(name) -> module
                
                Attempts to load the specified module searching 
         all languages in the loaded ScriptRuntime.
    
    Use(path: str, language: str) -> object
    
        Use(path, language) -> module
                
                Attempts to load the specified module 
         belonging to a specific language loaded into the
                current ScriptRuntime.
    """
    return object()

# classes

class ArgChecker(object):
    """ ArgChecker(prms: Array[object]) """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, prms):
        """ __new__(cls: type, prms: Array[object]) """
        pass


class StrongBox(object, IStrongBox):
    """
    StrongBox[T]()
    StrongBox[T](value: T)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: T)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Value = None


Reference = StrongBox


class ReferencesList(List[Assembly], IList[Assembly], ICollection[Assembly], IEnumerable[Assembly], IEnumerable, IList, ICollection, IReadOnlyList[Assembly], IReadOnlyCollection[Assembly], ICodeFormattable):
    """ ReferencesList() """
    def Add(self, *__args):
        """ Add(self: ReferencesList, other: Assembly) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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

    def __repr__(self, context):
        """ __repr__(self: ReferencesList) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class ReturnChecker(object):
    """ ReturnChecker(returnType: object) """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, returnType):
        """ __new__(cls: type, returnType: object) """
        pass

    retType = None


class RuntimeArgChecker(PythonTypeSlot):
    """
    RuntimeArgChecker(function: object, expectedArgs: Array[object])
    RuntimeArgChecker(instance: object, function: object, expectedArgs: Array[object])
    """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, function: object, expectedArgs: Array[object])
        __new__(cls: type, instance: object, function: object, expectedArgs: Array[object])
        """
        pass


class RuntimeReturnChecker(PythonTypeSlot):
    """
    RuntimeReturnChecker(function: object, expectedReturn: object)
    RuntimeReturnChecker(instance: object, function: object, expectedReturn: object)
    """
    def GetAttribute(self, instance, owner):
        """ GetAttribute(self: RuntimeReturnChecker, instance: object, owner: object) -> object """
        pass

    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, function: object, expectedReturn: object)
        __new__(cls: type, instance: object, function: object, expectedReturn: object)
        """
        pass


# variables with complex values

References = None

