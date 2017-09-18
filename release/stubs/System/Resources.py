# encoding: utf-8
# module System.Resources calls itself Resources
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class IResourceReader(IEnumerable, IDisposable):
    """ Provides the base functionality to read data from resource files. """
    def Close(self):
        """
        Close(self: IResourceReader)
            Closes the resource reader after releasing any resources associated with it.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: IResourceReader) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator of the resources for this reader.
            Returns: A dictionary enumerator for the resources for this reader.
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
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class IResourceWriter(IDisposable):
    """ Provides functionality to write resources to an output file or stream. """
    def AddResource(self, name, value):
        """
        AddResource(self: IResourceWriter, name: str, value: Array[Byte])
            Adds an 8-bit unsigned integer array as a named resource to the list of resources to be written.
        
            name: Name of a resource.
            value: Value of a resource as an 8-bit unsigned integer array.
        AddResource(self: IResourceWriter, name: str, value: object)
            Adds a named resource of type System.Object to the list of resources to be written.
        
            name: The name of the resource.
            value: The value of the resource.
        AddResource(self: IResourceWriter, name: str, value: str)
            Adds a named resource of type System.String to the list of resources to be written.
        
            name: The name of the resource.
            value: The value of the resource.
        """
        pass

    def Close(self):
        """
        Close(self: IResourceWriter)
            Closes the underlying resource file or stream, ensuring all the data has been written to the 
             file.
        """
        pass

    def Generate(self):
        """
        Generate(self: IResourceWriter)
            Writes all the resources added by the 
             System.Resources.IResourceWriter.AddResource(System.String,System.String) method to the output 
             file or stream.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class MissingManifestResourceException(SystemException, ISerializable, _Exception):
    """
    The exception thrown if the main assembly does not contain the resources for the neutral culture, and they are required because of a missing appropriate satellite assembly.
    
    MissingManifestResourceException()
    MissingManifestResourceException(message: str)
    MissingManifestResourceException(message: str, inner: Exception)
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

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class MissingSatelliteAssemblyException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown when the satellite assembly for the resources of the neutral culture is missing.
    
    MissingSatelliteAssemblyException()
    MissingSatelliteAssemblyException(message: str)
    MissingSatelliteAssemblyException(message: str, cultureName: str)
    MissingSatelliteAssemblyException(message: str, inner: Exception)
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

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, cultureName: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CultureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of a neutral culture.

Get: CultureName(self: MissingSatelliteAssemblyException) -> str

"""



class NeutralResourcesLanguageAttribute(Attribute, _Attribute):
    """
    Informs the System.Resources.ResourceManager of the default culture of an application. This class cannot be inherited.
    
    NeutralResourcesLanguageAttribute(cultureName: str)
    NeutralResourcesLanguageAttribute(cultureName: str, location: UltimateResourceFallbackLocation)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cultureName, location=None):
        """
        __new__(cls: type, cultureName: str)
        __new__(cls: type, cultureName: str, location: UltimateResourceFallbackLocation)
        """
        pass

    CultureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the culture name.

Get: CultureName(self: NeutralResourcesLanguageAttribute) -> str

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the location for the System.Resources.ResourceManager class to use to retrieve neutral resources by using the resource fallback process.

Get: Location(self: NeutralResourcesLanguageAttribute) -> UltimateResourceFallbackLocation

"""



class ResourceManager(object):
    """
    Represents a resource manager that provides convenient access to culture-specific resources at run time.
    
    ResourceManager(baseName: str, assembly: Assembly)
    ResourceManager(baseName: str, assembly: Assembly, usingResourceSet: Type)
    ResourceManager(resourceSource: Type)
    """
    @staticmethod
    def CreateFileBasedResourceManager(baseName, resourceDir, usingResourceSet):
        """
        CreateFileBasedResourceManager(baseName: str, resourceDir: str, usingResourceSet: Type) -> ResourceManager
        
            Returns a System.Resources.ResourceManager that searches a specific directory for resources 
             instead of in the assembly manifest.
        
        
            baseName: The root name of the resources. For example, the root name for the resource file named 
             "MyResource.en-US.resources" is "MyResource".
        
            resourceDir: The name of the directory to search for the resources.
            usingResourceSet: The System.Type of the custom System.Resources.ResourceSet to use. If null, the default runtime 
             System.Resources.ResourceSet is used.
        
            Returns: The newly created System.Resources.ResourceManager that searches a specific directory for 
             resources instead of in the assembly manifest.
        """
        pass

    def GetNeutralResourcesLanguage(self, *args): #cannot find CLR method
        """
        GetNeutralResourcesLanguage(a: Assembly) -> CultureInfo
        
            Returns the System.Globalization.CultureInfo for the main assembly's neutral resources by 
             reading the value of the System.Resources.NeutralResourcesLanguageAttribute on a specified 
             System.Reflection.Assembly.
        
        
            a: The assembly for which to return a System.Globalization.CultureInfo.
            Returns: The culture from the System.Resources.NeutralResourcesLanguageAttribute, if found; otherwise, 
             System.Globalization.CultureInfo.InvariantCulture.
        """
        pass

    def GetObject(self, name, culture=None):
        """
        GetObject(self: ResourceManager, name: str, culture: CultureInfo) -> object
        
            Gets the value of the specified non-string  resource localized for the specified culture.
        
            name: The name of the resource to get.
            culture: The culture for which the resource is localized. If the resource is not localized for this 
             culture, the resource manager uses fallback rules to locate an appropriate resource.If this 
             value is null, the System.Globalization.CultureInfo object is obtained using the culture's 
             System.Globalization.CultureInfo.CurrentUICulture property.
        
            Returns: The value of the resource, localized for the specified culture. If an appropriate resource set 
             exists but name cannot be found, the method returns null.
        
        GetObject(self: ResourceManager, name: str) -> object
        
            Returns the value of the specified non-string resource.
        
            name: The name of the resource to get.
            Returns: The value of the resource localized for the caller's current culture settings. If an appropriate 
             resource set exists but name cannot be found, the method returns null.
        """
        pass

    def GetResourceFileName(self, *args): #cannot find CLR method
        """
        GetResourceFileName(self: ResourceManager, culture: CultureInfo) -> str
        
            Generates the name for the resource file for the given System.Globalization.CultureInfo.
        
            culture: The System.Globalization.CultureInfo for which a resource file name is constructed.
            Returns: The name that can be used for a resource file for the given System.Globalization.CultureInfo.
        """
        pass

    def GetResourceSet(self, culture, createIfNotExists, tryParents):
        """
        GetResourceSet(self: ResourceManager, culture: CultureInfo, createIfNotExists: bool, tryParents: bool) -> ResourceSet
        
            Gets the System.Resources.ResourceSet for a particular culture.
        
            culture: The System.Globalization.CultureInfo to look for.
            createIfNotExists: If true and if the System.Resources.ResourceSet has not been loaded yet, load it.
            tryParents: If the System.Resources.ResourceSet cannot be loaded, try parent 
             System.Globalization.CultureInfo objects to see if they exist.
        
            Returns: The specified System.Resources.ResourceSet.
        """
        pass

    def GetSatelliteContractVersion(self, *args): #cannot find CLR method
        """
        GetSatelliteContractVersion(a: Assembly) -> Version
        
            Returns the System.Version specified by the System.Resources.SatelliteContractVersionAttribute 
             in the given assembly.
        
        
            a: The System.Reflection.Assembly for which to look up the 
             System.Resources.SatelliteContractVersionAttribute.
        
            Returns: The satellite contract System.Version of the given assembly, or null if no version was found.
        """
        pass

    def GetStream(self, name, culture=None):
        """
        GetStream(self: ResourceManager, name: str, culture: CultureInfo) -> UnmanagedMemoryStream
        
            Returns an unmanaged memory stream  object from the specified resource, using the specified 
             culture.
        
        
            name: The name of a resource.
            culture: An object that specifies the culture to use for the resource lookup. If culture is null, the 
             culture for the current thread is used.
        
            Returns: An System.IO.UnmanagedMemoryStream object.
        GetStream(self: ResourceManager, name: str) -> UnmanagedMemoryStream
        
            Returns an unmanaged memory stream object from the specified resource.
        
            name: The name of a resource.
            Returns: An unmanaged memory stream object object that represents a resource.
        """
        pass

    def GetString(self, name, culture=None):
        """
        GetString(self: ResourceManager, name: str, culture: CultureInfo) -> str
        
            Returns the value of the string resource localized for the specified culture.
        
            name: The name of the resource to get.
            culture: An object that represents the culture for which the resource is localized.
            Returns: The value of the resource localized for the specified culture, or null if name cannot be found 
             in a resource set.
        
        GetString(self: ResourceManager, name: str) -> str
        
            Returns the value of the specified string resource.
        
            name: The name of the resource to retrieve.
            Returns: The value of the resource localized for the caller's current UI culture, or null if name cannot 
             be found in a resource set.
        """
        pass

    def InternalGetResourceSet(self, *args): #cannot find CLR method
        """
        InternalGetResourceSet(self: ResourceManager, culture: CultureInfo, createIfNotExists: bool, tryParents: bool) -> ResourceSet
        
            Provides the implementation for finding a System.Resources.ResourceSet.
        
            culture: The System.Globalization.CultureInfo to look for.
            createIfNotExists: If true and if the System.Resources.ResourceSet has not been loaded yet, load it.
            tryParents: If the System.Resources.ResourceSet cannot be loaded, try parent 
             System.Globalization.CultureInfo objects to see if they exist.
        
            Returns: The specified System.Resources.ResourceSet.
        """
        pass

    def ReleaseAllResources(self):
        """
        ReleaseAllResources(self: ResourceManager)
            Tells the System.Resources.ResourceManager to call System.Resources.ResourceSet.Close on all 
             System.Resources.ResourceSet objects and release all resources.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, baseName: str, assembly: Assembly)
        __new__(cls: type, baseName: str, assembly: Assembly, usingResourceSet: Type)
        __new__(cls: type, resourceSource: Type)
        """
        pass

    BaseName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root name of the resource files that the System.Resources.ResourceManager searches for resources.

Get: BaseName(self: ResourceManager) -> str

"""

    FallbackLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the location from which to retrieve neutral fallback resources.

"""

    IgnoreCase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value indicating whether the current instance of ResourceManager allows case-insensitive resource lookups in the System.Resources.ResourceManager.GetString(System.String) and System.Resources.ResourceManager.GetObject(System.String) methods.

Get: IgnoreCase(self: ResourceManager) -> bool

Set: IgnoreCase(self: ResourceManager) = value
"""

    ResourceSetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Type of the System.Resources.ResourceSet the System.Resources.ResourceManager uses to construct a System.Resources.ResourceSet object.

Get: ResourceSetType(self: ResourceManager) -> Type

"""


    BaseNameField = None
    HeaderVersionNumber = 1
    MagicNumber = -1091581234
    MainAssembly = None
    ResourceSets = None


class ResourceReader(object, IResourceReader, IEnumerable, IDisposable):
    """
    Enumerates the resources in a binary resources (.resources) file by reading sequential resource name/value pairs.
    
    ResourceReader(fileName: str)
    ResourceReader(stream: Stream)
    """
    def Close(self):
        """
        Close(self: ResourceReader)
            Releases all operating system resources associated with this System.Resources.ResourceReader 
             object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ResourceReader)
            Releases all resources used by the current instance of the System.Resources.ResourceReader class.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ResourceReader) -> IDictionaryEnumerator
        
            Returns an enumerator for this System.Resources.ResourceReader object.
            Returns: An enumerator for this System.Resources.ResourceReader object.
        """
        pass

    def GetResourceData(self, resourceName, resourceType, resourceData):
        """
        GetResourceData(self: ResourceReader, resourceName: str) -> (str, Array[Byte])
        
            Retrieves the type name and data of a named resource from an open resource file or stream.
        
            resourceName: The name of a resource.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, stream: Stream)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ResourceSet(object, IDisposable, IEnumerable):
    """
    Stores all the resources localized for one particular culture, ignoring all other cultures, including any fallback rules.
    
    ResourceSet(fileName: str)
    ResourceSet(stream: Stream)
    ResourceSet(reader: IResourceReader)
    """
    def Close(self):
        """
        Close(self: ResourceSet)
            Closes and releases any resources used by this System.Resources.ResourceSet.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ResourceSet)
            Disposes of the resources (other than memory) used by the current instance of 
             System.Resources.ResourceSet.
        """
        pass

    def GetDefaultReader(self):
        """
        GetDefaultReader(self: ResourceSet) -> Type
        
            Returns the preferred resource reader class for this kind of System.Resources.ResourceSet.
            Returns: Returns the System.Type for the preferred resource reader for this kind of 
             System.Resources.ResourceSet.
        """
        pass

    def GetDefaultWriter(self):
        """
        GetDefaultWriter(self: ResourceSet) -> Type
        
            Returns the preferred resource writer class for this kind of System.Resources.ResourceSet.
            Returns: Returns the System.Type for the preferred resource writer for this kind of 
             System.Resources.ResourceSet.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ResourceSet) -> IDictionaryEnumerator
        
            Returns an System.Collections.IDictionaryEnumerator that can iterate through the 
             System.Resources.ResourceSet.
        
            Returns: An System.Collections.IDictionaryEnumerator for this System.Resources.ResourceSet.
        """
        pass

    def GetObject(self, name, ignoreCase=None):
        """
        GetObject(self: ResourceSet, name: str, ignoreCase: bool) -> object
        
            Searches for a resource object with the specified name in a case-insensitive manner, if 
             requested.
        
        
            name: Name of the resource to search for.
            ignoreCase: Indicates whether the case of the specified name should be ignored.
            Returns: The requested resource.
        GetObject(self: ResourceSet, name: str) -> object
        
            Searches for a resource object with the specified name.
        
            name: Case-sensitive name of the resource to search for.
            Returns: The requested resource.
        """
        pass

    def GetString(self, name, ignoreCase=None):
        """
        GetString(self: ResourceSet, name: str, ignoreCase: bool) -> str
        
            Searches for a System.String resource with the specified name in a case-insensitive manner, if 
             requested.
        
        
            name: Name of the resource to search for.
            ignoreCase: Indicates whether the case of the case of the specified name should be ignored.
            Returns: The value of a resource, if the value is a System.String.
        GetString(self: ResourceSet, name: str) -> str
        
            Searches for a System.String resource with the specified name.
        
            name: Name of the resource to search for.
            Returns: The value of a resource, if the value is a System.String.
        """
        pass

    def ReadResources(self, *args): #cannot find CLR method
        """
        ReadResources(self: ResourceSet)
            Reads all the resources and stores them in a System.Collections.Hashtable indicated in the 
             System.Resources.ResourceSet.Table property.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, reader: IResourceReader)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Reader = None
    Table = None


class ResourceWriter(object, IResourceWriter, IDisposable):
    """
    Writes resources in the system-default format to an output file or an output stream. This class cannot be inherited.
    
    ResourceWriter(fileName: str)
    ResourceWriter(stream: Stream)
    """
    def AddResource(self, name, value, closeAfterWrite=None):
        """
        AddResource(self: ResourceWriter, name: str, value: Stream, closeAfterWrite: bool)
            Adds a named resource specified as a stream to the list of resources to be written, and 
             specifies whether the stream should be closed after the System.Resources.ResourceWriter.Generate 
             method is called.
        
        
            name: The name of the resource to add.
            value: The value of the resource to add that supports the System.IO.Stream.Length property.
            closeAfterWrite: true to close the stream after the System.Resources.ResourceWriter.Generate method is called; 
             otherwise, false.
        
        AddResource(self: ResourceWriter, name: str, value: Array[Byte])
            Adds a named resource specified as a byte array to the list of resources to be written.
        
            name: The name of the resource.
            value: Value of the resource as an 8-bit unsigned integer array.
        AddResource(self: ResourceWriter, name: str, value: Stream)
            Adds a named resource specified as a stream to the list of resources to be written.
        
            name: The name of the resource to add.
            value: The value of the resource to add. The resource must support the System.IO.Stream.Length property.
        AddResource(self: ResourceWriter, name: str, value: str)
            Adds a string resource to the list of resources to be written.
        
            name: The name of the resource.
            value: The value of the resource.
        AddResource(self: ResourceWriter, name: str, value: object)
            Adds a named resource specified as an object to the list of resources to be written.
        
            name: The name of the resource.
            value: The value of the resource.
        """
        pass

    def AddResourceData(self, name, typeName, serializedData):
        """
        AddResourceData(self: ResourceWriter, name: str, typeName: str, serializedData: Array[Byte])
            Adds a unit of data as a resource to the list of resources to be written.
        
            name: A name that identifies the resource that contains the added data.
            typeName: The type name of the added data. For more information, see the Remarks section.
            serializedData: A byte array that contains the binary representation of the added data.
        """
        pass

    def Close(self):
        """
        Close(self: ResourceWriter)
            Saves the resources to the output stream and then closes it.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ResourceWriter)
            Allows users to close the resource file or stream, explicitly releasing resources.
        """
        pass

    def Generate(self):
        """
        Generate(self: ResourceWriter)
            Saves all resources to the output stream in the system default format.
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
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, stream: Stream)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    TypeNameConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a delegate that enables resource assemblies to be written that target versions of the .NET Framework prior to the .NET Framework version�4�by using qualified assembly names.

Get: TypeNameConverter(self: ResourceWriter) -> Func[Type, str]

Set: TypeNameConverter(self: ResourceWriter) = value
"""



class ResXDataNode(object, ISerializable):
    """
    Represents an element in a resource file.
    
    ResXDataNode(name: str, value: object)
    ResXDataNode(name: str, value: object, typeNameConverter: Func[Type, str])
    ResXDataNode(name: str, fileRef: ResXFileRef)
    ResXDataNode(name: str, fileRef: ResXFileRef, typeNameConverter: Func[Type, str])
    """
    def GetNodePosition(self):
        """
        GetNodePosition(self: ResXDataNode) -> Point
        
            Gets the position of the resource in the resource file.
            Returns: A System.Drawing.Point structure specifying the location of this resource in the resource file 
             as a line position (System.Drawing.Point.X) and a column position (System.Drawing.Point.Y). If 
             this resource is not part of a resource file, returns a System.Drawing.Point structure with an 
             System.Drawing.Point.X of 0 and a System.Drawing.Point.Y of 0.
        """
        pass

    def GetValue(self, *__args):
        """
        GetValue(self: ResXDataNode, names: Array[AssemblyName]) -> object
        
            Gets the object stored by this node.
        
            names: The list of assemblies in which to look for the type of the object.
            Returns: The System.Object corresponding to the stored value.
        GetValue(self: ResXDataNode, typeResolver: ITypeResolutionService) -> object
        
            Gets the object stored by this node.
        
            typeResolver: The type resolution service to use when looking for a type converter.
            Returns: The System.Object corresponding to the stored value.
        """
        pass

    def GetValueTypeName(self, *__args):
        """
        GetValueTypeName(self: ResXDataNode, names: Array[AssemblyName]) -> str
        
            Gets the name of the type of the value.
        
            names: The assemblies to examine for the type.
            Returns: A System.String representing the fully qualified name of the type.
        GetValueTypeName(self: ResXDataNode, typeResolver: ITypeResolutionService) -> str
        
            A System.String representing the fully qualified name of the type.
        
            typeResolver: The type resolution service to use to locate a converter for this type.
            Returns: A System.String representing the fully qualified name of the type.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, *__args):
        """
        __new__(cls: type, name: str, value: object)
        __new__(cls: type, name: str, value: object, typeNameConverter: Func[Type, str])
        __new__(cls: type, name: str, fileRef: ResXFileRef)
        __new__(cls: type, name: str, fileRef: ResXFileRef, typeNameConverter: Func[Type, str])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an arbitrary comment regarding this resource.

Get: Comment(self: ResXDataNode) -> str

Set: Comment(self: ResXDataNode) = value
"""

    FileRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file reference for this resource.

Get: FileRef(self: ResXDataNode) -> ResXFileRef

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of this resource.

Get: Name(self: ResXDataNode) -> str

Set: Name(self: ResXDataNode) = value
"""



class ResXFileRef(object):
    """
    Represents a link to an external resource.
    
    ResXFileRef(fileName: str, typeName: str)
    ResXFileRef(fileName: str, typeName: str, textFileEncoding: Encoding)
    """
    def ToString(self):
        """
        ToString(self: ResXFileRef) -> str
        
            Gets the text representation of the current System.Resources.ResXFileRef object.
            Returns: A string that consists of the concatenated text representations of the parameters specified in 
             the current erload:System.Resources.ResXFileRef.#ctor constructor.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fileName, typeName, textFileEncoding=None):
        """
        __new__(cls: type, fileName: str, typeName: str)
        __new__(cls: type, fileName: str, typeName: str, textFileEncoding: Encoding)
        """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file name specified in the current erload:System.Resources.ResXFileRef.#ctor constructor.

Get: FileName(self: ResXFileRef) -> str

"""

    TextFileEncoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the encoding specified in the current erload:System.Resources.ResXFileRef.#ctor constructor.

Get: TextFileEncoding(self: ResXFileRef) -> Encoding

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type name specified in the current erload:System.Resources.ResXFileRef.#ctor constructor.

Get: TypeName(self: ResXFileRef) -> str

"""


    Converter = None


class ResXResourceReader(object, IResourceReader, IEnumerable, IDisposable):
    """
    Enumerates XML resource (.resx) files and streams, and reads the sequential resource name and value pairs.
    
    ResXResourceReader(fileName: str)
    ResXResourceReader(fileName: str, typeResolver: ITypeResolutionService)
    ResXResourceReader(reader: TextReader)
    ResXResourceReader(reader: TextReader, typeResolver: ITypeResolutionService)
    ResXResourceReader(stream: Stream)
    ResXResourceReader(stream: Stream, typeResolver: ITypeResolutionService)
    ResXResourceReader(stream: Stream, assemblyNames: Array[AssemblyName])
    ResXResourceReader(reader: TextReader, assemblyNames: Array[AssemblyName])
    ResXResourceReader(fileName: str, assemblyNames: Array[AssemblyName])
    """
    def Close(self):
        """
        Close(self: ResXResourceReader)
            Releases all resources used by the System.Resources.ResXResourceReader.
        """
        pass

    def Dispose(self, *args): #cannot find CLR method
        """
        Dispose(self: ResXResourceReader, disposing: bool)
            Releases the unmanaged resources used by the System.Resources.ResXResourceReader and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    @staticmethod
    def FromFileContents(fileContents, *__args):
        """
        FromFileContents(fileContents: str, assemblyNames: Array[AssemblyName]) -> ResXResourceReader
        
            Creates a new System.Resources.ResXResourceReader object and initializes it to read a string 
             whose contents are in the form of an XML resource file, and to use an array of 
             System.Reflection.AssemblyName objects to resolve type names specified in a resource.
        
        
            fileContents: A string whose contents are in the form of an XML resource file.
            assemblyNames: An array of System.Reflection.AssemblyName objects that specifies one or more assemblies. The 
             assemblies are used to resolve a type name in the resource to an actual type.
        
            Returns: An object that reads resources from the fileContents string.
        FromFileContents(fileContents: str, typeResolver: ITypeResolutionService) -> ResXResourceReader
        
            Creates a new System.Resources.ResXResourceReader object and initializes it to read a string 
             whose contents are in the form of an XML resource file, and to use an 
             System.ComponentModel.Design.ITypeResolutionService object to resolve type names specified in a 
             resource.
        
        
            fileContents: A string containing XML resource-formatted information.
            typeResolver: An object that resolves type names specified in a resource.
            Returns: An object that reads resources from the fileContents string.
        FromFileContents(fileContents: str) -> ResXResourceReader
        
            Creates a new System.Resources.ResXResourceReader object and initializes it to read a string 
             whose contents are in the form of an XML resource file.
        
        
            fileContents: A string containing XML resource-formatted information.
            Returns: An object that reads resources from the fileContents string.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ResXResourceReader) -> IDictionaryEnumerator
        
            Returns an enumerator for the current System.Resources.ResXResourceReader object.
            Returns: An enumerator for the current System.Resources.ResourceReader object.
        """
        pass

    def GetMetadataEnumerator(self):
        """
        GetMetadataEnumerator(self: ResXResourceReader) -> IDictionaryEnumerator
        
            Provides a dictionary enumerator that can retrieve the design-time properties from the current 
             XML resource file or stream.
        
            Returns: An enumerator for the metadata in a resource.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, typeResolver: ITypeResolutionService)
        __new__(cls: type, reader: TextReader)
        __new__(cls: type, reader: TextReader, typeResolver: ITypeResolutionService)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, typeResolver: ITypeResolutionService)
        __new__(cls: type, stream: Stream, assemblyNames: Array[AssemblyName])
        __new__(cls: type, reader: TextReader, assemblyNames: Array[AssemblyName])
        __new__(cls: type, fileName: str, assemblyNames: Array[AssemblyName])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BasePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base path for the relative file path specified in a System.Resources.ResXFileRef object.

Get: BasePath(self: ResXResourceReader) -> str

Set: BasePath(self: ResXResourceReader) = value
"""

    UseResXDataNodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether System.Resources.ResXDataNode objects are returned when reading the current XML resource file or stream.

Get: UseResXDataNodes(self: ResXResourceReader) -> bool

Set: UseResXDataNodes(self: ResXResourceReader) = value
"""



class ResXResourceSet(ResourceSet, IDisposable, IEnumerable):
    """
    Gathers all items that represent an XML resource (.resx) file into a single object.
    
    ResXResourceSet(fileName: str)
    ResXResourceSet(stream: Stream)
    """
    def Dispose(self):
        """
        Dispose(self: ResourceSet, disposing: bool)
            Releases resources (other than memory) associated with the current instance, closing internal 
             managed objects if requested.
        
        
            disposing: Indicates whether the objects contained in the current instance should be explicitly closed.
        """
        pass

    def GetDefaultReader(self):
        """
        GetDefaultReader(self: ResXResourceSet) -> Type
        
            Returns the preferred resource reader class for this kind of System.Resources.ResXResourceSet.
            Returns: The System.Type of the preferred resource reader for this kind of 
             System.Resources.ResXResourceSet.
        """
        pass

    def GetDefaultWriter(self):
        """
        GetDefaultWriter(self: ResXResourceSet) -> Type
        
            Returns the preferred resource writer class for this kind of System.Resources.ResXResourceSet.
            Returns: The System.Type of the preferred resource writer for this kind of 
             System.Resources.ResXResourceSet.
        """
        pass

    def ReadResources(self, *args): #cannot find CLR method
        """
        ReadResources(self: ResourceSet)
            Reads all the resources and stores them in a System.Collections.Hashtable indicated in the 
             System.Resources.ResourceSet.Table property.
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, stream: Stream)
        """
        pass

    Reader = None
    Table = None


class ResXResourceWriter(object, IResourceWriter, IDisposable):
    """
    Writes resources in an XML resource (.resx) file or an output stream.
    
    ResXResourceWriter(fileName: str)
    ResXResourceWriter(fileName: str, typeNameConverter: Func[Type, str])
    ResXResourceWriter(stream: Stream)
    ResXResourceWriter(stream: Stream, typeNameConverter: Func[Type, str])
    ResXResourceWriter(textWriter: TextWriter)
    ResXResourceWriter(textWriter: TextWriter, typeNameConverter: Func[Type, str])
    """
    def AddAlias(self, aliasName, assemblyName):
        """
        AddAlias(self: ResXResourceWriter, aliasName: str, assemblyName: AssemblyName)
            Adds the specified alias to a list of aliases.
        
            aliasName: The name of the alias.
            assemblyName: The name of the assembly represented by aliasName.
        """
        pass

    def AddMetadata(self, name, value):
        """
        AddMetadata(self: ResXResourceWriter, name: str, value: object)
            Adds a design-time property whose value is specified as an object to the list of resources to 
             write.
        
        
            name: The name of a property.
            value: An object that is the value of the property to add.
        AddMetadata(self: ResXResourceWriter, name: str, value: str)
            Adds a design-time property whose value is specified as a string to the list of resources to 
             write.
        
        
            name: The name of a property.
            value: A string that is the value of the property to add.
        AddMetadata(self: ResXResourceWriter, name: str, value: Array[Byte])
            Adds a design-time property whose value is specifed as a byte array to the list of resources to 
             write.
        
        
            name: The name of a property.
            value: A byte array containing the value of the property to add.
        """
        pass

    def AddResource(self, *__args):
        """
        AddResource(self: ResXResourceWriter, name: str, value: str)
            Adds a string resource to the resources.
        
            name: The name of the resource.
            value: The value of the resource.
        AddResource(self: ResXResourceWriter, node: ResXDataNode)
            Adds a named resource specified in a System.Resources.ResXDataNode object to the list of 
             resources to write.
        
        
            node: A System.Resources.ResXDataNode object that contains a resource name/value pair.
        AddResource(self: ResXResourceWriter, name: str, value: Array[Byte])
            Adds a named resource specified as a byte array to the list of resources to write.
        
            name: The name of the resource.
            value: The value of the resource to add as an 8-bit unsigned integer array.
        AddResource(self: ResXResourceWriter, name: str, value: object)
            Adds a named resource specified as an object to the list of resources to write.
        
            name: The name of the resource.
            value: The value of the resource.
        """
        pass

    def Close(self):
        """
        Close(self: ResXResourceWriter)
            Releases all resources used by the System.Resources.ResXResourceWriter.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ResXResourceWriter)
            Releases all resources used by the System.Resources.ResXResourceWriter.
        """
        pass

    def Generate(self):
        """
        Generate(self: ResXResourceWriter)
            Writes all resources added by the 
             System.Resources.ResXResourceWriter.AddResource(System.String,System.Byte[]) method to the 
             output file or stream.
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
    def __new__(self, *__args):
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, typeNameConverter: Func[Type, str])
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, typeNameConverter: Func[Type, str])
        __new__(cls: type, textWriter: TextWriter)
        __new__(cls: type, textWriter: TextWriter, typeNameConverter: Func[Type, str])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BasePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base path for the relative file path specified in a System.Resources.ResXFileRef object.

Get: BasePath(self: ResXResourceWriter) -> str

Set: BasePath(self: ResXResourceWriter) = value
"""


    BinSerializedObjectMimeType = 'application/x-microsoft.net.object.binary.base64'
    ByteArraySerializedObjectMimeType = 'application/x-microsoft.net.object.bytearray.base64'
    DefaultSerializedObjectMimeType = 'application/x-microsoft.net.object.binary.base64'
    ResMimeType = 'text/microsoft-resx'
    ResourceSchema = '\r\n    <!-- \r\n    Microsoft ResX Schema \r\n    \r\n    Version 2.0\r\n    \r\n    The primary goals of this format is to allow a simple XML format \r\n    that is mostly human readable. The generation and parsing of the \r\n    various data types are done through the TypeConverter classes \r\n    associated with the data types.\r\n    \r\n    Example:\r\n    \r\n    ... ado.net/XML headers & schema ...\r\n    <resheader name="resmimetype">text/microsoft-resx</resheader>\r\n    <resheader name="version">2.0</resheader>\r\n    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>\r\n    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>\r\n    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>\r\n    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>\r\n    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">\r\n        <value>[base64 mime encoded serialized .NET Framework object]</value>\r\n    </data>\r\n    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">\r\n        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>\r\n        <comment>This is a comment</comment>\r\n    </data>\r\n                \r\n    There are any number of "resheader" rows that contain simple \r\n    name/value pairs.\r\n    \r\n    Each data row contains a name, and value. The row also contains a \r\n    type or mimetype. Type corresponds to a .NET class that support \r\n    text/value conversion through the TypeConverter architecture. \r\n    Classes that don\'t support this are serialized and stored with the \r\n    mimetype set.\r\n    \r\n    The mimetype is used for serialized objects, and tells the \r\n    ResXResourceReader how to depersist the object. This is currently not \r\n    extensible. For a given mimetype the value must be set accordingly:\r\n    \r\n    Note - application/x-microsoft.net.object.binary.base64 is the format \r\n    that the ResXResourceWriter will generate, however the reader can \r\n    read any of the formats listed below.\r\n    \r\n    mimetype: application/x-microsoft.net.object.binary.base64\r\n    value   : The object must be serialized with \r\n            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter\r\n            : and then encoded with base64 encoding.\r\n    \r\n    mimetype: application/x-microsoft.net.object.soap.base64\r\n    value   : The object must be serialized with \r\n            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter\r\n            : and then encoded with base64 encoding.\r\n\r\n    mimetype: application/x-microsoft.net.object.bytearray.base64\r\n    value   : The object must be serialized into a byte array \r\n            : using a System.ComponentModel.TypeConverter\r\n            : and then encoded with base64 encoding.\r\n    -->\r\n    <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">\r\n        <xsd:import namespace="http://www.w3.org/XML/1998/namespace"/>\r\n        <xsd:element name="root" msdata:IsDataSet="true">\r\n            <xsd:complexType>\r\n                <xsd:choice maxOccurs="unbounded">\r\n                    <xsd:element name="metadata">\r\n                        <xsd:complexType>\r\n                            <xsd:sequence>\r\n                            <xsd:element name="value" type="xsd:string" minOccurs="0"/>\r\n                            </xsd:sequence>\r\n                            <xsd:attribute name="name" use="required" type="xsd:string"/>\r\n                            <xsd:attribute name="type" type="xsd:string"/>\r\n                            <xsd:attribute name="mimetype" type="xsd:string"/>\r\n                            <xsd:attribute ref="xml:space"/>                            \r\n                        </xsd:complexType>\r\n                    </xsd:element>\r\n                    <xsd:element name="assembly">\r\n                      <xsd:complexType>\r\n                        <xsd:attribute name="alias" type="xsd:string"/>\r\n                        <xsd:attribute name="name" type="xsd:string"/>\r\n                      </xsd:complexType>\r\n                    </xsd:element>\r\n                    <xsd:element name="data">\r\n                        <xsd:complexType>\r\n                            <xsd:sequence>\r\n                                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />\r\n                                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />\r\n                            </xsd:sequence>\r\n                            <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />\r\n                            <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />\r\n                            <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />\r\n                            <xsd:attribute ref="xml:space"/>\r\n                        </xsd:complexType>\r\n                    </xsd:element>\r\n                    <xsd:element name="resheader">\r\n                        <xsd:complexType>\r\n                            <xsd:sequence>\r\n                                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />\r\n                            </xsd:sequence>\r\n                            <xsd:attribute name="name" type="xsd:string" use="required" />\r\n                        </xsd:complexType>\r\n                    </xsd:element>\r\n                </xsd:choice>\r\n            </xsd:complexType>\r\n        </xsd:element>\r\n        </xsd:schema>\r\n        '
    SoapSerializedObjectMimeType = 'application/x-microsoft.net.object.soap.base64'
    Version = '2.0'


class SatelliteContractVersionAttribute(Attribute, _Attribute):
    """
    Instructs the System.Resources.ResourceManager to ask for a particular version of a satellite assembly to simplify updates of the main assembly of an application.
    
    SatelliteContractVersionAttribute(version: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, version):
        """ __new__(cls: type, version: str) """
        pass

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of the satellite assemblies with the required resources.

Get: Version(self: SatelliteContractVersionAttribute) -> str

"""



class UltimateResourceFallbackLocation(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the assembly for the System.Resources.ResourceManager class to use to retrieve neutral resources by using the Packaging and Deploying Resources.
    
    enum UltimateResourceFallbackLocation, values: MainAssembly (0), Satellite (1)
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

    MainAssembly = None
    Satellite = None
    value__ = None


