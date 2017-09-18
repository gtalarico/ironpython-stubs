# encoding: utf-8
# module System.Net.Configuration calls itself Configuration
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AuthenticationModuleElement(ConfigurationElement):
    """
    Represents the type information for an authentication module. This class cannot be inherited.
    
    AuthenticationModuleElement()
    AuthenticationModuleElement(typeName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, typeName=None):
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        """
        pass

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type and assembly information for the current instance.

Get: Type(self: AuthenticationModuleElement) -> str

Set: Type(self: AuthenticationModuleElement) = value
"""



class AuthenticationModuleElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    Represents a container for authentication module configuration elements. This class cannot be inherited.
    
    AuthenticationModuleElementCollection()
    """
    def Add(self, element):
        """
        Add(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement)
            Adds an element to the collection.
        
            element: The System.Net.Configuration.AuthenticationModuleElement to add to the collection.
        """
        pass

    def BaseAdd(self, *args): #cannot find CLR method
        """
        BaseAdd(self: ConfigurationElementCollection, index: int, element: ConfigurationElement)
            Adds a configuration element to the configuration element collection.
        
            index: The index location at which to add the specified System.Configuration.ConfigurationElement.
            element: The System.Configuration.ConfigurationElement to add.
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement, throwIfExists: bool)
            Adds a configuration element to the configuration element collection.
        
            element: The System.Configuration.ConfigurationElement to add.
            throwIfExists: true to throw an exception if the System.Configuration.ConfigurationElement specified is already 
             contained in the System.Configuration.ConfigurationElementCollection; otherwise, false.
        
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement)
            Adds a configuration element to the System.Configuration.ConfigurationElementCollection.
        
            element: The System.Configuration.ConfigurationElement to add.
        """
        pass

    def BaseClear(self, *args): #cannot find CLR method
        """
        BaseClear(self: ConfigurationElementCollection)
            Removes all configuration element objects from the collection.
        """
        pass

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: ConfigurationElementCollection, index: int) -> ConfigurationElement
        
            Gets the configuration element at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to return.
            Returns: The System.Configuration.ConfigurationElement at the specified index.
        BaseGet(self: ConfigurationElementCollection, key: object) -> ConfigurationElement
        
            Returns the configuration element with the specified key.
        
            key: The key of the element to return.
            Returns: The System.Configuration.ConfigurationElement with the specified key; otherwise, null.
        """
        pass

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """
        BaseGetAllKeys(self: ConfigurationElementCollection) -> Array[object]
        
            Returns an array of the keys for all of the configuration elements contained in the 
             System.Configuration.ConfigurationElementCollection.
        
            Returns: An array that contains the keys for all of the System.Configuration.ConfigurationElement objects 
             contained in the System.Configuration.ConfigurationElementCollection.
        """
        pass

    def BaseGetKey(self, *args): #cannot find CLR method
        """
        BaseGetKey(self: ConfigurationElementCollection, index: int) -> object
        
            Gets the key for the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location for the System.Configuration.ConfigurationElement.
            Returns: The key for the specified System.Configuration.ConfigurationElement.
        """
        pass

    def BaseIndexOf(self, *args): #cannot find CLR method
        """
        BaseIndexOf(self: ConfigurationElementCollection, element: ConfigurationElement) -> int
        
            The index of the specified System.Configuration.ConfigurationElement.
        
            element: The System.Configuration.ConfigurationElement for the specified index location.
            Returns: The index of the specified System.Configuration.ConfigurationElement; otherwise, -1.
        """
        pass

    def BaseIsRemoved(self, *args): #cannot find CLR method
        """
        BaseIsRemoved(self: ConfigurationElementCollection, key: object) -> bool
        
            Gets a value indicating whether the System.Configuration.ConfigurationElement with the specified 
             key has been removed from the System.Configuration.ConfigurationElementCollection.
        
        
            key: The key of the element to check.
            Returns: true if the System.Configuration.ConfigurationElement with the specified key has been removed; 
             otherwise, false. The default is false.
        """
        pass

    def BaseRemove(self, *args): #cannot find CLR method
        """
        BaseRemove(self: ConfigurationElementCollection, key: object)
            Removes a System.Configuration.ConfigurationElement from the collection.
        
            key: The key of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """
        BaseRemoveAt(self: ConfigurationElementCollection, index: int)
            Removes the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def Clear(self):
        """
        Clear(self: AuthenticationModuleElementCollection)
            Removes all elements from the collection.
        """
        pass

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: AuthenticationModuleElementCollection) -> ConfigurationElement
        CreateNewElement(self: ConfigurationElementCollection, elementName: str) -> ConfigurationElement
        
            Creates a new System.Configuration.ConfigurationElement when overridden in a derived class.
        
            elementName: The name of the System.Configuration.ConfigurationElement to create.
            Returns: A new System.Configuration.ConfigurationElement.
        """
        pass

    def DeserializeElement(self, *args): #cannot find CLR method
        """
        DeserializeElement(self: ConfigurationElement, reader: XmlReader, serializeCollectionKey: bool)
            Reads XML from the configuration file.
        
            reader: The System.Xml.XmlReader that reads from the configuration file.
            serializeCollectionKey: true to serialize only the collection key properties; otherwise, false.
        """
        pass

    def GetElementKey(self, *args): #cannot find CLR method
        """ GetElementKey(self: AuthenticationModuleElementCollection, element: ConfigurationElement) -> object """
        pass

    def GetTransformedAssemblyString(self, *args): #cannot find CLR method
        """
        GetTransformedAssemblyString(self: ConfigurationElement, assemblyName: str) -> str
        
            Returns the transformed version of the specified assembly name.
        
            assemblyName: The name of the assembly.
            Returns: The transformed version of the assembly name. If no transformer is available, the assemblyName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def GetTransformedTypeString(self, *args): #cannot find CLR method
        """
        GetTransformedTypeString(self: ConfigurationElement, typeName: str) -> str
        
            Returns the transformed version of the specified type name.
        
            typeName: The name of the type.
            Returns: The transformed version of the specified type name. If no transformer is available, the typeName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def get_Item(self, *__args):
        """
        get_Item(self: ConfigurationElement, propertyName: str) -> object
        get_Item(self: ConfigurationElement, prop: ConfigurationProperty) -> object
        """
        pass

    def IndexOf(self, element):
        """
        IndexOf(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement) -> int
        
            Returns the index of the specified configuration element.
        
            element: A System.Net.Configuration.AuthenticationModuleElement.
            Returns: The zero-based index of element.
        """
        pass

    def Init(self, *args): #cannot find CLR method
        """
        Init(self: ConfigurationElement)
            Sets the System.Configuration.ConfigurationElement object to its initial state.
        """
        pass

    def InitializeDefault(self, *args): #cannot find CLR method
        """
        InitializeDefault(self: ConfigurationElement)
            Used to initialize a default set of values for the System.Configuration.ConfigurationElement 
             object.
        """
        pass

    def IsElementName(self, *args): #cannot find CLR method
        """
        IsElementName(self: ConfigurationElementCollection, elementName: str) -> bool
        
            Indicates whether the specified System.Configuration.ConfigurationElement exists in the 
             System.Configuration.ConfigurationElementCollection.
        
        
            elementName: The name of the element to verify.
            Returns: true if the element exists in the collection; otherwise, false. The default is false.
        """
        pass

    def IsElementRemovable(self, *args): #cannot find CLR method
        """
        IsElementRemovable(self: ConfigurationElementCollection, element: ConfigurationElement) -> bool
        
            Gets a value indicating whether the specified System.Configuration.ConfigurationElement can be 
             removed from the System.Configuration.ConfigurationElementCollection.
        
        
            element: The element to check.
            Returns: true if the specified System.Configuration.ConfigurationElement can be removed from this 
             System.Configuration.ConfigurationElementCollection; otherwise, false. The default is true.
        """
        pass

    def IsModified(self, *args): #cannot find CLR method
        """
        IsModified(self: ConfigurationElementCollection) -> bool
        
            Indicates whether this System.Configuration.ConfigurationElementCollection has been modified 
             since it was last saved or loaded when overridden in a derived class.
        
            Returns: true if any contained element has been modified; otherwise, false
        """
        pass

    def ListErrors(self, *args): #cannot find CLR method
        """
        ListErrors(self: ConfigurationElement, errorList: IList)
            Adds the invalid-property errors in this System.Configuration.ConfigurationElement object, and 
             in all subelements, to the passed list.
        
        
            errorList: An object that implements the System.Collections.IList interface.
        """
        pass

    def OnDeserializeUnrecognizedAttribute(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedAttribute(self: ConfigurationElement, name: str, value: str) -> bool
        
            Gets a value indicating whether an unknown attribute is encountered during deserialization.
        
            name: The name of the unrecognized attribute.
            value: The value of the unrecognized attribute.
            Returns: true when an unknown attribute is encountered while deserializing; otherwise, false.
        """
        pass

    def OnDeserializeUnrecognizedElement(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedElement(self: ConfigurationElementCollection, elementName: str, reader: XmlReader) -> bool
        
            Causes the configuration system to throw an exception.
        
            elementName: The name of the unrecognized element.
            reader: An input stream that reads XML from the configuration file.
            Returns: true if the unrecognized element was deserialized successfully; otherwise, false. The default is 
             false.
        """
        pass

    def OnRequiredPropertyNotFound(self, *args): #cannot find CLR method
        """
        OnRequiredPropertyNotFound(self: ConfigurationElement, name: str) -> object
        
            Throws an exception when a required property is not found.
        
            name: The name of the required attribute that was not found.
            Returns: None.
        """
        pass

    def PostDeserialize(self, *args): #cannot find CLR method
        """
        PostDeserialize(self: ConfigurationElement)
            Called after deserialization.
        """
        pass

    def PreSerialize(self, *args): #cannot find CLR method
        """
        PreSerialize(self: ConfigurationElement, writer: XmlWriter)
            Called before serialization.
        
            writer: The System.Xml.XmlWriter that will be used to serialize the 
             System.Configuration.ConfigurationElement.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: AuthenticationModuleElementCollection, name: str)
            Removes the element with the specified key.
        
            name: The key of the element to remove.
        Remove(self: AuthenticationModuleElementCollection, element: AuthenticationModuleElement)
            Removes the specified configuration element from the collection.
        
            element: The System.Net.Configuration.AuthenticationModuleElement to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: AuthenticationModuleElementCollection, index: int)
            Removes the element at the specified index.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def Reset(self, *args): #cannot find CLR method
        """
        Reset(self: ConfigurationElementCollection, parentElement: ConfigurationElement)
            Resets the System.Configuration.ConfigurationElementCollection to its unmodified state when 
             overridden in a derived class.
        
        
            parentElement: The System.Configuration.ConfigurationElement representing the collection parent element, if 
             any; otherwise, null.
        """
        pass

    def ResetModified(self, *args): #cannot find CLR method
        """
        ResetModified(self: ConfigurationElementCollection)
            Resets the value of the System.Configuration.ConfigurationElementCollection.IsModified property 
             to false when overridden in a derived class.
        """
        pass

    def SerializeElement(self, *args): #cannot find CLR method
        """
        SerializeElement(self: ConfigurationElementCollection, writer: XmlWriter, serializeCollectionKey: bool) -> bool
        
            Writes the configuration data to an XML element in the configuration file when overridden in a 
             derived class.
        
        
            writer: Output stream that writes XML to the configuration file.
            serializeCollectionKey: true to serialize the collection key; otherwise, false.
            Returns: true if the System.Configuration.ConfigurationElementCollection was written to the configuration 
             file successfully.
        """
        pass

    def SerializeToXmlElement(self, *args): #cannot find CLR method
        """
        SerializeToXmlElement(self: ConfigurationElement, writer: XmlWriter, elementName: str) -> bool
        
            Writes the outer tags of this configuration element to the configuration file when implemented 
             in a derived class.
        
        
            writer: The System.Xml.XmlWriter that writes to the configuration file.
            elementName: The name of the System.Configuration.ConfigurationElement to be written.
            Returns: true if writing was successful; otherwise, false.
        """
        pass

    def SetPropertyValue(self, *args): #cannot find CLR method
        """
        SetPropertyValue(self: ConfigurationElement, prop: ConfigurationProperty, value: object, ignoreLocks: bool)
            Sets a property to the specified value.
        
            prop: The element property to set.
            value: The value to assign to the property.
            ignoreLocks: true if the locks on the property should be ignored; otherwise, false.
        """
        pass

    def SetReadOnly(self, *args): #cannot find CLR method
        """
        SetReadOnly(self: ConfigurationElementCollection)
            Sets the System.Configuration.ConfigurationElementCollection.IsReadOnly property for the 
             System.Configuration.ConfigurationElementCollection object and for all sub-elements.
        """
        pass

    def set_Item(self, *__args):
        """ set_Item(self: ConfigurationElement, propertyName: str, value: object)set_Item(self: ConfigurationElement, prop: ConfigurationProperty, value: object) """
        pass

    def Unmerge(self, *args): #cannot find CLR method
        """
        Unmerge(self: ConfigurationElementCollection, sourceElement: ConfigurationElement, parentElement: ConfigurationElement, saveMode: ConfigurationSaveMode)
            Reverses the effect of merging configuration information from different levels of the 
             configuration hierarchy
        
        
            sourceElement: A System.Configuration.ConfigurationElement object at the current level containing a merged view 
             of the properties.
        
            parentElement: The parent System.Configuration.ConfigurationElement object of the current element, or null if 
             this is the top level.
        
            saveMode: A System.Configuration.ConfigurationSaveMode enumerated value that determines which property 
             values to include.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    AddElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ClearElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class.

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of properties.

"""

    RemoveElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ThrowOnDuplicate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown.

"""



class AuthenticationModulesSection(ConfigurationSection):
    """
    Represents the configuration section for authentication modules. This class cannot be inherited.
    
    AuthenticationModulesSection()
    """
    AuthenticationModules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of authentication modules in the section.

Get: AuthenticationModules(self: AuthenticationModulesSection) -> AuthenticationModuleElementCollection

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BypassElement(ConfigurationElement):
    """
    Represents the address information for resources that are not retrieved using a proxy server. This class cannot be inherited.
    
    BypassElement()
    BypassElement(address: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, address=None):
        """
        __new__(cls: type)
        __new__(cls: type, address: str)
        """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the addresses of resources that bypass the proxy server.

Get: Address(self: BypassElement) -> str

Set: Address(self: BypassElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BypassElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    Represents a container for the addresses of resources that bypass the proxy server. This class cannot be inherited.
    
    BypassElementCollection()
    """
    def Add(self, element):
        """
        Add(self: BypassElementCollection, element: BypassElement)
            Adds an element to the collection.
        
            element: The System.Net.Configuration.BypassElement to add to the collection.
        """
        pass

    def BaseAdd(self, *args): #cannot find CLR method
        """
        BaseAdd(self: ConfigurationElementCollection, index: int, element: ConfigurationElement)
            Adds a configuration element to the configuration element collection.
        
            index: The index location at which to add the specified System.Configuration.ConfigurationElement.
            element: The System.Configuration.ConfigurationElement to add.
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement, throwIfExists: bool)
            Adds a configuration element to the configuration element collection.
        
            element: The System.Configuration.ConfigurationElement to add.
            throwIfExists: true to throw an exception if the System.Configuration.ConfigurationElement specified is already 
             contained in the System.Configuration.ConfigurationElementCollection; otherwise, false.
        
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement)
            Adds a configuration element to the System.Configuration.ConfigurationElementCollection.
        
            element: The System.Configuration.ConfigurationElement to add.
        """
        pass

    def BaseClear(self, *args): #cannot find CLR method
        """
        BaseClear(self: ConfigurationElementCollection)
            Removes all configuration element objects from the collection.
        """
        pass

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: ConfigurationElementCollection, index: int) -> ConfigurationElement
        
            Gets the configuration element at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to return.
            Returns: The System.Configuration.ConfigurationElement at the specified index.
        BaseGet(self: ConfigurationElementCollection, key: object) -> ConfigurationElement
        
            Returns the configuration element with the specified key.
        
            key: The key of the element to return.
            Returns: The System.Configuration.ConfigurationElement with the specified key; otherwise, null.
        """
        pass

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """
        BaseGetAllKeys(self: ConfigurationElementCollection) -> Array[object]
        
            Returns an array of the keys for all of the configuration elements contained in the 
             System.Configuration.ConfigurationElementCollection.
        
            Returns: An array that contains the keys for all of the System.Configuration.ConfigurationElement objects 
             contained in the System.Configuration.ConfigurationElementCollection.
        """
        pass

    def BaseGetKey(self, *args): #cannot find CLR method
        """
        BaseGetKey(self: ConfigurationElementCollection, index: int) -> object
        
            Gets the key for the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location for the System.Configuration.ConfigurationElement.
            Returns: The key for the specified System.Configuration.ConfigurationElement.
        """
        pass

    def BaseIndexOf(self, *args): #cannot find CLR method
        """
        BaseIndexOf(self: ConfigurationElementCollection, element: ConfigurationElement) -> int
        
            The index of the specified System.Configuration.ConfigurationElement.
        
            element: The System.Configuration.ConfigurationElement for the specified index location.
            Returns: The index of the specified System.Configuration.ConfigurationElement; otherwise, -1.
        """
        pass

    def BaseIsRemoved(self, *args): #cannot find CLR method
        """
        BaseIsRemoved(self: ConfigurationElementCollection, key: object) -> bool
        
            Gets a value indicating whether the System.Configuration.ConfigurationElement with the specified 
             key has been removed from the System.Configuration.ConfigurationElementCollection.
        
        
            key: The key of the element to check.
            Returns: true if the System.Configuration.ConfigurationElement with the specified key has been removed; 
             otherwise, false. The default is false.
        """
        pass

    def BaseRemove(self, *args): #cannot find CLR method
        """
        BaseRemove(self: ConfigurationElementCollection, key: object)
            Removes a System.Configuration.ConfigurationElement from the collection.
        
            key: The key of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """
        BaseRemoveAt(self: ConfigurationElementCollection, index: int)
            Removes the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def Clear(self):
        """
        Clear(self: BypassElementCollection)
            Removes all elements from the collection.
        """
        pass

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: BypassElementCollection) -> ConfigurationElement
        CreateNewElement(self: ConfigurationElementCollection, elementName: str) -> ConfigurationElement
        
            Creates a new System.Configuration.ConfigurationElement when overridden in a derived class.
        
            elementName: The name of the System.Configuration.ConfigurationElement to create.
            Returns: A new System.Configuration.ConfigurationElement.
        """
        pass

    def DeserializeElement(self, *args): #cannot find CLR method
        """
        DeserializeElement(self: ConfigurationElement, reader: XmlReader, serializeCollectionKey: bool)
            Reads XML from the configuration file.
        
            reader: The System.Xml.XmlReader that reads from the configuration file.
            serializeCollectionKey: true to serialize only the collection key properties; otherwise, false.
        """
        pass

    def GetElementKey(self, *args): #cannot find CLR method
        """ GetElementKey(self: BypassElementCollection, element: ConfigurationElement) -> object """
        pass

    def GetTransformedAssemblyString(self, *args): #cannot find CLR method
        """
        GetTransformedAssemblyString(self: ConfigurationElement, assemblyName: str) -> str
        
            Returns the transformed version of the specified assembly name.
        
            assemblyName: The name of the assembly.
            Returns: The transformed version of the assembly name. If no transformer is available, the assemblyName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def GetTransformedTypeString(self, *args): #cannot find CLR method
        """
        GetTransformedTypeString(self: ConfigurationElement, typeName: str) -> str
        
            Returns the transformed version of the specified type name.
        
            typeName: The name of the type.
            Returns: The transformed version of the specified type name. If no transformer is available, the typeName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def get_Item(self, *__args):
        """
        get_Item(self: ConfigurationElement, propertyName: str) -> object
        get_Item(self: ConfigurationElement, prop: ConfigurationProperty) -> object
        """
        pass

    def IndexOf(self, element):
        """
        IndexOf(self: BypassElementCollection, element: BypassElement) -> int
        
            Returns the index of the specified configuration element.
        
            element: A System.Net.Configuration.BypassElement.
            Returns: The zero-based index of element.
        """
        pass

    def Init(self, *args): #cannot find CLR method
        """
        Init(self: ConfigurationElement)
            Sets the System.Configuration.ConfigurationElement object to its initial state.
        """
        pass

    def InitializeDefault(self, *args): #cannot find CLR method
        """
        InitializeDefault(self: ConfigurationElement)
            Used to initialize a default set of values for the System.Configuration.ConfigurationElement 
             object.
        """
        pass

    def IsElementName(self, *args): #cannot find CLR method
        """
        IsElementName(self: ConfigurationElementCollection, elementName: str) -> bool
        
            Indicates whether the specified System.Configuration.ConfigurationElement exists in the 
             System.Configuration.ConfigurationElementCollection.
        
        
            elementName: The name of the element to verify.
            Returns: true if the element exists in the collection; otherwise, false. The default is false.
        """
        pass

    def IsElementRemovable(self, *args): #cannot find CLR method
        """
        IsElementRemovable(self: ConfigurationElementCollection, element: ConfigurationElement) -> bool
        
            Gets a value indicating whether the specified System.Configuration.ConfigurationElement can be 
             removed from the System.Configuration.ConfigurationElementCollection.
        
        
            element: The element to check.
            Returns: true if the specified System.Configuration.ConfigurationElement can be removed from this 
             System.Configuration.ConfigurationElementCollection; otherwise, false. The default is true.
        """
        pass

    def IsModified(self, *args): #cannot find CLR method
        """
        IsModified(self: ConfigurationElementCollection) -> bool
        
            Indicates whether this System.Configuration.ConfigurationElementCollection has been modified 
             since it was last saved or loaded when overridden in a derived class.
        
            Returns: true if any contained element has been modified; otherwise, false
        """
        pass

    def ListErrors(self, *args): #cannot find CLR method
        """
        ListErrors(self: ConfigurationElement, errorList: IList)
            Adds the invalid-property errors in this System.Configuration.ConfigurationElement object, and 
             in all subelements, to the passed list.
        
        
            errorList: An object that implements the System.Collections.IList interface.
        """
        pass

    def OnDeserializeUnrecognizedAttribute(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedAttribute(self: ConfigurationElement, name: str, value: str) -> bool
        
            Gets a value indicating whether an unknown attribute is encountered during deserialization.
        
            name: The name of the unrecognized attribute.
            value: The value of the unrecognized attribute.
            Returns: true when an unknown attribute is encountered while deserializing; otherwise, false.
        """
        pass

    def OnDeserializeUnrecognizedElement(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedElement(self: ConfigurationElementCollection, elementName: str, reader: XmlReader) -> bool
        
            Causes the configuration system to throw an exception.
        
            elementName: The name of the unrecognized element.
            reader: An input stream that reads XML from the configuration file.
            Returns: true if the unrecognized element was deserialized successfully; otherwise, false. The default is 
             false.
        """
        pass

    def OnRequiredPropertyNotFound(self, *args): #cannot find CLR method
        """
        OnRequiredPropertyNotFound(self: ConfigurationElement, name: str) -> object
        
            Throws an exception when a required property is not found.
        
            name: The name of the required attribute that was not found.
            Returns: None.
        """
        pass

    def PostDeserialize(self, *args): #cannot find CLR method
        """
        PostDeserialize(self: ConfigurationElement)
            Called after deserialization.
        """
        pass

    def PreSerialize(self, *args): #cannot find CLR method
        """
        PreSerialize(self: ConfigurationElement, writer: XmlWriter)
            Called before serialization.
        
            writer: The System.Xml.XmlWriter that will be used to serialize the 
             System.Configuration.ConfigurationElement.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: BypassElementCollection, name: str)
            Removes the element with the specified key.
        
            name: The key of the element to remove.
        Remove(self: BypassElementCollection, element: BypassElement)
            Removes the specified configuration element from the collection.
        
            element: The System.Net.Configuration.BypassElement to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: BypassElementCollection, index: int)
            Removes the element at the specified index.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def Reset(self, *args): #cannot find CLR method
        """
        Reset(self: ConfigurationElementCollection, parentElement: ConfigurationElement)
            Resets the System.Configuration.ConfigurationElementCollection to its unmodified state when 
             overridden in a derived class.
        
        
            parentElement: The System.Configuration.ConfigurationElement representing the collection parent element, if 
             any; otherwise, null.
        """
        pass

    def ResetModified(self, *args): #cannot find CLR method
        """
        ResetModified(self: ConfigurationElementCollection)
            Resets the value of the System.Configuration.ConfigurationElementCollection.IsModified property 
             to false when overridden in a derived class.
        """
        pass

    def SerializeElement(self, *args): #cannot find CLR method
        """
        SerializeElement(self: ConfigurationElementCollection, writer: XmlWriter, serializeCollectionKey: bool) -> bool
        
            Writes the configuration data to an XML element in the configuration file when overridden in a 
             derived class.
        
        
            writer: Output stream that writes XML to the configuration file.
            serializeCollectionKey: true to serialize the collection key; otherwise, false.
            Returns: true if the System.Configuration.ConfigurationElementCollection was written to the configuration 
             file successfully.
        """
        pass

    def SerializeToXmlElement(self, *args): #cannot find CLR method
        """
        SerializeToXmlElement(self: ConfigurationElement, writer: XmlWriter, elementName: str) -> bool
        
            Writes the outer tags of this configuration element to the configuration file when implemented 
             in a derived class.
        
        
            writer: The System.Xml.XmlWriter that writes to the configuration file.
            elementName: The name of the System.Configuration.ConfigurationElement to be written.
            Returns: true if writing was successful; otherwise, false.
        """
        pass

    def SetPropertyValue(self, *args): #cannot find CLR method
        """
        SetPropertyValue(self: ConfigurationElement, prop: ConfigurationProperty, value: object, ignoreLocks: bool)
            Sets a property to the specified value.
        
            prop: The element property to set.
            value: The value to assign to the property.
            ignoreLocks: true if the locks on the property should be ignored; otherwise, false.
        """
        pass

    def SetReadOnly(self, *args): #cannot find CLR method
        """
        SetReadOnly(self: ConfigurationElementCollection)
            Sets the System.Configuration.ConfigurationElementCollection.IsReadOnly property for the 
             System.Configuration.ConfigurationElementCollection object and for all sub-elements.
        """
        pass

    def set_Item(self, *__args):
        """ set_Item(self: ConfigurationElement, propertyName: str, value: object)set_Item(self: ConfigurationElement, prop: ConfigurationProperty, value: object) """
        pass

    def Unmerge(self, *args): #cannot find CLR method
        """
        Unmerge(self: ConfigurationElementCollection, sourceElement: ConfigurationElement, parentElement: ConfigurationElement, saveMode: ConfigurationSaveMode)
            Reverses the effect of merging configuration information from different levels of the 
             configuration hierarchy
        
        
            sourceElement: A System.Configuration.ConfigurationElement object at the current level containing a merged view 
             of the properties.
        
            parentElement: The parent System.Configuration.ConfigurationElement object of the current element, or null if 
             this is the top level.
        
            saveMode: A System.Configuration.ConfigurationSaveMode enumerated value that determines which property 
             values to include.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    AddElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ClearElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class.

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of properties.

"""

    RemoveElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ThrowOnDuplicate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ConnectionManagementElement(ConfigurationElement):
    """
    Represents the maximum number of connections to a remote computer. This class cannot be inherited.
    
    ConnectionManagementElement()
    ConnectionManagementElement(address: str, maxConnection: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, address=None, maxConnection=None):
        """
        __new__(cls: type)
        __new__(cls: type, address: str, maxConnection: int)
        """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the address for remote computers.

Get: Address(self: ConnectionManagementElement) -> str

Set: Address(self: ConnectionManagementElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MaxConnection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of connections that can be made to a remote computer.

Get: MaxConnection(self: ConnectionManagementElement) -> int

Set: MaxConnection(self: ConnectionManagementElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ConnectionManagementElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    Represents a container for connection management configuration elements. This class cannot be inherited.
    
    ConnectionManagementElementCollection()
    """
    def Add(self, element):
        """
        Add(self: ConnectionManagementElementCollection, element: ConnectionManagementElement)
            Adds an element to the collection.
        
            element: The System.Net.Configuration.ConnectionManagementElement to add to the collection.
        """
        pass

    def BaseAdd(self, *args): #cannot find CLR method
        """
        BaseAdd(self: ConfigurationElementCollection, index: int, element: ConfigurationElement)
            Adds a configuration element to the configuration element collection.
        
            index: The index location at which to add the specified System.Configuration.ConfigurationElement.
            element: The System.Configuration.ConfigurationElement to add.
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement, throwIfExists: bool)
            Adds a configuration element to the configuration element collection.
        
            element: The System.Configuration.ConfigurationElement to add.
            throwIfExists: true to throw an exception if the System.Configuration.ConfigurationElement specified is already 
             contained in the System.Configuration.ConfigurationElementCollection; otherwise, false.
        
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement)
            Adds a configuration element to the System.Configuration.ConfigurationElementCollection.
        
            element: The System.Configuration.ConfigurationElement to add.
        """
        pass

    def BaseClear(self, *args): #cannot find CLR method
        """
        BaseClear(self: ConfigurationElementCollection)
            Removes all configuration element objects from the collection.
        """
        pass

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: ConfigurationElementCollection, index: int) -> ConfigurationElement
        
            Gets the configuration element at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to return.
            Returns: The System.Configuration.ConfigurationElement at the specified index.
        BaseGet(self: ConfigurationElementCollection, key: object) -> ConfigurationElement
        
            Returns the configuration element with the specified key.
        
            key: The key of the element to return.
            Returns: The System.Configuration.ConfigurationElement with the specified key; otherwise, null.
        """
        pass

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """
        BaseGetAllKeys(self: ConfigurationElementCollection) -> Array[object]
        
            Returns an array of the keys for all of the configuration elements contained in the 
             System.Configuration.ConfigurationElementCollection.
        
            Returns: An array that contains the keys for all of the System.Configuration.ConfigurationElement objects 
             contained in the System.Configuration.ConfigurationElementCollection.
        """
        pass

    def BaseGetKey(self, *args): #cannot find CLR method
        """
        BaseGetKey(self: ConfigurationElementCollection, index: int) -> object
        
            Gets the key for the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location for the System.Configuration.ConfigurationElement.
            Returns: The key for the specified System.Configuration.ConfigurationElement.
        """
        pass

    def BaseIndexOf(self, *args): #cannot find CLR method
        """
        BaseIndexOf(self: ConfigurationElementCollection, element: ConfigurationElement) -> int
        
            The index of the specified System.Configuration.ConfigurationElement.
        
            element: The System.Configuration.ConfigurationElement for the specified index location.
            Returns: The index of the specified System.Configuration.ConfigurationElement; otherwise, -1.
        """
        pass

    def BaseIsRemoved(self, *args): #cannot find CLR method
        """
        BaseIsRemoved(self: ConfigurationElementCollection, key: object) -> bool
        
            Gets a value indicating whether the System.Configuration.ConfigurationElement with the specified 
             key has been removed from the System.Configuration.ConfigurationElementCollection.
        
        
            key: The key of the element to check.
            Returns: true if the System.Configuration.ConfigurationElement with the specified key has been removed; 
             otherwise, false. The default is false.
        """
        pass

    def BaseRemove(self, *args): #cannot find CLR method
        """
        BaseRemove(self: ConfigurationElementCollection, key: object)
            Removes a System.Configuration.ConfigurationElement from the collection.
        
            key: The key of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """
        BaseRemoveAt(self: ConfigurationElementCollection, index: int)
            Removes the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def Clear(self):
        """
        Clear(self: ConnectionManagementElementCollection)
            Removes all elements from the collection.
        """
        pass

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: ConnectionManagementElementCollection) -> ConfigurationElement
        CreateNewElement(self: ConfigurationElementCollection, elementName: str) -> ConfigurationElement
        
            Creates a new System.Configuration.ConfigurationElement when overridden in a derived class.
        
            elementName: The name of the System.Configuration.ConfigurationElement to create.
            Returns: A new System.Configuration.ConfigurationElement.
        """
        pass

    def DeserializeElement(self, *args): #cannot find CLR method
        """
        DeserializeElement(self: ConfigurationElement, reader: XmlReader, serializeCollectionKey: bool)
            Reads XML from the configuration file.
        
            reader: The System.Xml.XmlReader that reads from the configuration file.
            serializeCollectionKey: true to serialize only the collection key properties; otherwise, false.
        """
        pass

    def GetElementKey(self, *args): #cannot find CLR method
        """ GetElementKey(self: ConnectionManagementElementCollection, element: ConfigurationElement) -> object """
        pass

    def GetTransformedAssemblyString(self, *args): #cannot find CLR method
        """
        GetTransformedAssemblyString(self: ConfigurationElement, assemblyName: str) -> str
        
            Returns the transformed version of the specified assembly name.
        
            assemblyName: The name of the assembly.
            Returns: The transformed version of the assembly name. If no transformer is available, the assemblyName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def GetTransformedTypeString(self, *args): #cannot find CLR method
        """
        GetTransformedTypeString(self: ConfigurationElement, typeName: str) -> str
        
            Returns the transformed version of the specified type name.
        
            typeName: The name of the type.
            Returns: The transformed version of the specified type name. If no transformer is available, the typeName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def get_Item(self, *__args):
        """
        get_Item(self: ConfigurationElement, propertyName: str) -> object
        get_Item(self: ConfigurationElement, prop: ConfigurationProperty) -> object
        """
        pass

    def IndexOf(self, element):
        """
        IndexOf(self: ConnectionManagementElementCollection, element: ConnectionManagementElement) -> int
        
            Returns the index of the specified configuration element.
        
            element: A System.Net.Configuration.ConnectionManagementElement.
            Returns: The zero-based index of element.
        """
        pass

    def Init(self, *args): #cannot find CLR method
        """
        Init(self: ConfigurationElement)
            Sets the System.Configuration.ConfigurationElement object to its initial state.
        """
        pass

    def InitializeDefault(self, *args): #cannot find CLR method
        """
        InitializeDefault(self: ConfigurationElement)
            Used to initialize a default set of values for the System.Configuration.ConfigurationElement 
             object.
        """
        pass

    def IsElementName(self, *args): #cannot find CLR method
        """
        IsElementName(self: ConfigurationElementCollection, elementName: str) -> bool
        
            Indicates whether the specified System.Configuration.ConfigurationElement exists in the 
             System.Configuration.ConfigurationElementCollection.
        
        
            elementName: The name of the element to verify.
            Returns: true if the element exists in the collection; otherwise, false. The default is false.
        """
        pass

    def IsElementRemovable(self, *args): #cannot find CLR method
        """
        IsElementRemovable(self: ConfigurationElementCollection, element: ConfigurationElement) -> bool
        
            Gets a value indicating whether the specified System.Configuration.ConfigurationElement can be 
             removed from the System.Configuration.ConfigurationElementCollection.
        
        
            element: The element to check.
            Returns: true if the specified System.Configuration.ConfigurationElement can be removed from this 
             System.Configuration.ConfigurationElementCollection; otherwise, false. The default is true.
        """
        pass

    def IsModified(self, *args): #cannot find CLR method
        """
        IsModified(self: ConfigurationElementCollection) -> bool
        
            Indicates whether this System.Configuration.ConfigurationElementCollection has been modified 
             since it was last saved or loaded when overridden in a derived class.
        
            Returns: true if any contained element has been modified; otherwise, false
        """
        pass

    def ListErrors(self, *args): #cannot find CLR method
        """
        ListErrors(self: ConfigurationElement, errorList: IList)
            Adds the invalid-property errors in this System.Configuration.ConfigurationElement object, and 
             in all subelements, to the passed list.
        
        
            errorList: An object that implements the System.Collections.IList interface.
        """
        pass

    def OnDeserializeUnrecognizedAttribute(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedAttribute(self: ConfigurationElement, name: str, value: str) -> bool
        
            Gets a value indicating whether an unknown attribute is encountered during deserialization.
        
            name: The name of the unrecognized attribute.
            value: The value of the unrecognized attribute.
            Returns: true when an unknown attribute is encountered while deserializing; otherwise, false.
        """
        pass

    def OnDeserializeUnrecognizedElement(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedElement(self: ConfigurationElementCollection, elementName: str, reader: XmlReader) -> bool
        
            Causes the configuration system to throw an exception.
        
            elementName: The name of the unrecognized element.
            reader: An input stream that reads XML from the configuration file.
            Returns: true if the unrecognized element was deserialized successfully; otherwise, false. The default is 
             false.
        """
        pass

    def OnRequiredPropertyNotFound(self, *args): #cannot find CLR method
        """
        OnRequiredPropertyNotFound(self: ConfigurationElement, name: str) -> object
        
            Throws an exception when a required property is not found.
        
            name: The name of the required attribute that was not found.
            Returns: None.
        """
        pass

    def PostDeserialize(self, *args): #cannot find CLR method
        """
        PostDeserialize(self: ConfigurationElement)
            Called after deserialization.
        """
        pass

    def PreSerialize(self, *args): #cannot find CLR method
        """
        PreSerialize(self: ConfigurationElement, writer: XmlWriter)
            Called before serialization.
        
            writer: The System.Xml.XmlWriter that will be used to serialize the 
             System.Configuration.ConfigurationElement.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: ConnectionManagementElementCollection, name: str)
            Removes the element with the specified key.
        
            name: The key of the element to remove.
        Remove(self: ConnectionManagementElementCollection, element: ConnectionManagementElement)
            Removes the specified configuration element from the collection.
        
            element: The System.Net.Configuration.ConnectionManagementElement to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ConnectionManagementElementCollection, index: int)
            Removes the element at the specified index.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def Reset(self, *args): #cannot find CLR method
        """
        Reset(self: ConfigurationElementCollection, parentElement: ConfigurationElement)
            Resets the System.Configuration.ConfigurationElementCollection to its unmodified state when 
             overridden in a derived class.
        
        
            parentElement: The System.Configuration.ConfigurationElement representing the collection parent element, if 
             any; otherwise, null.
        """
        pass

    def ResetModified(self, *args): #cannot find CLR method
        """
        ResetModified(self: ConfigurationElementCollection)
            Resets the value of the System.Configuration.ConfigurationElementCollection.IsModified property 
             to false when overridden in a derived class.
        """
        pass

    def SerializeElement(self, *args): #cannot find CLR method
        """
        SerializeElement(self: ConfigurationElementCollection, writer: XmlWriter, serializeCollectionKey: bool) -> bool
        
            Writes the configuration data to an XML element in the configuration file when overridden in a 
             derived class.
        
        
            writer: Output stream that writes XML to the configuration file.
            serializeCollectionKey: true to serialize the collection key; otherwise, false.
            Returns: true if the System.Configuration.ConfigurationElementCollection was written to the configuration 
             file successfully.
        """
        pass

    def SerializeToXmlElement(self, *args): #cannot find CLR method
        """
        SerializeToXmlElement(self: ConfigurationElement, writer: XmlWriter, elementName: str) -> bool
        
            Writes the outer tags of this configuration element to the configuration file when implemented 
             in a derived class.
        
        
            writer: The System.Xml.XmlWriter that writes to the configuration file.
            elementName: The name of the System.Configuration.ConfigurationElement to be written.
            Returns: true if writing was successful; otherwise, false.
        """
        pass

    def SetPropertyValue(self, *args): #cannot find CLR method
        """
        SetPropertyValue(self: ConfigurationElement, prop: ConfigurationProperty, value: object, ignoreLocks: bool)
            Sets a property to the specified value.
        
            prop: The element property to set.
            value: The value to assign to the property.
            ignoreLocks: true if the locks on the property should be ignored; otherwise, false.
        """
        pass

    def SetReadOnly(self, *args): #cannot find CLR method
        """
        SetReadOnly(self: ConfigurationElementCollection)
            Sets the System.Configuration.ConfigurationElementCollection.IsReadOnly property for the 
             System.Configuration.ConfigurationElementCollection object and for all sub-elements.
        """
        pass

    def set_Item(self, *__args):
        """ set_Item(self: ConfigurationElement, propertyName: str, value: object)set_Item(self: ConfigurationElement, prop: ConfigurationProperty, value: object) """
        pass

    def Unmerge(self, *args): #cannot find CLR method
        """
        Unmerge(self: ConfigurationElementCollection, sourceElement: ConfigurationElement, parentElement: ConfigurationElement, saveMode: ConfigurationSaveMode)
            Reverses the effect of merging configuration information from different levels of the 
             configuration hierarchy
        
        
            sourceElement: A System.Configuration.ConfigurationElement object at the current level containing a merged view 
             of the properties.
        
            parentElement: The parent System.Configuration.ConfigurationElement object of the current element, or null if 
             this is the top level.
        
            saveMode: A System.Configuration.ConfigurationSaveMode enumerated value that determines which property 
             values to include.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    AddElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ClearElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class.

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of properties.

"""

    RemoveElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ThrowOnDuplicate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown.

"""



class ConnectionManagementSection(ConfigurationSection):
    """
    Represents the configuration section for connection management. This class cannot be inherited.
    
    ConnectionManagementSection()
    """
    ConnectionManagement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of connection management objects in the section.

Get: ConnectionManagement(self: ConnectionManagementSection) -> ConnectionManagementElementCollection

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DefaultProxySection(ConfigurationSection):
    """
    Represents the configuration section for Web proxy server usage. This class cannot be inherited.
    
    DefaultProxySection()
    """
    BypassList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of resources that are not obtained using the Web proxy server.

Get: BypassList(self: DefaultProxySection) -> BypassElementCollection

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether a Web proxy is used.

Get: Enabled(self: DefaultProxySection) -> bool

Set: Enabled(self: DefaultProxySection) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type information for a custom Web proxy implementation.

Get: Module(self: DefaultProxySection) -> ModuleElement

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Proxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the URI that identifies the Web proxy server to use.

Get: Proxy(self: DefaultProxySection) -> ProxyElement

"""

    UseDefaultCredentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether default credentials are to be used to access a Web proxy server.

Get: UseDefaultCredentials(self: DefaultProxySection) -> bool

Set: UseDefaultCredentials(self: DefaultProxySection) = value
"""



class FtpCachePolicyElement(ConfigurationElement):
    """
    Represents the default FTP cache policy for network resources. This class cannot be inherited.
    
    FtpCachePolicyElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PolicyLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets FTP caching behavior for the local machine.

Get: PolicyLevel(self: FtpCachePolicyElement) -> RequestCacheLevel

Set: PolicyLevel(self: FtpCachePolicyElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HttpCachePolicyElement(ConfigurationElement):
    """
    Represents the default HTTP cache policy for network resources. This class cannot be inherited.
    
    HttpCachePolicyElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MaximumAge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum age permitted for a resource returned from the cache.

Get: MaximumAge(self: HttpCachePolicyElement) -> TimeSpan

Set: MaximumAge(self: HttpCachePolicyElement) = value
"""

    MaximumStale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum staleness value permitted for a resource returned from the cache.

Get: MaximumStale(self: HttpCachePolicyElement) -> TimeSpan

Set: MaximumStale(self: HttpCachePolicyElement) = value
"""

    MinimumFresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the minimum freshness permitted for a resource returned from the cache.

Get: MinimumFresh(self: HttpCachePolicyElement) -> TimeSpan

Set: MinimumFresh(self: HttpCachePolicyElement) = value
"""

    PolicyLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets HTTP caching behavior for the local machine.

Get: PolicyLevel(self: HttpCachePolicyElement) -> HttpRequestCacheLevel

Set: PolicyLevel(self: HttpCachePolicyElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HttpListenerElement(ConfigurationElement):
    """
    Represents the HttpListener element in the configuration file. This class cannot be inherited.
    
    HttpListenerElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Timeouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Timeouts(self: HttpListenerElement) -> HttpListenerTimeoutsElement

"""

    UnescapeRequestUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if System.Net.HttpListener uses the raw unescaped URI instead of the converted URI.

Get: UnescapeRequestUrl(self: HttpListenerElement) -> bool

"""



class HttpListenerTimeoutsElement(ConfigurationElement):
    """ HttpListenerTimeoutsElement() """
    DrainEntityBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrainEntityBody(self: HttpListenerTimeoutsElement) -> TimeSpan

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EntityBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityBody(self: HttpListenerTimeoutsElement) -> TimeSpan

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HeaderWait = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderWait(self: HttpListenerTimeoutsElement) -> TimeSpan

"""

    IdleConnection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdleConnection(self: HttpListenerTimeoutsElement) -> TimeSpan

"""

    MinSendBytesPerSecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinSendBytesPerSecond(self: HttpListenerTimeoutsElement) -> Int64

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RequestQueue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequestQueue(self: HttpListenerTimeoutsElement) -> TimeSpan

"""



class HttpWebRequestElement(ConfigurationElement):
    """
    Represents the maximum length for response headers. This class cannot be inherited.
    
    HttpWebRequestElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MaximumErrorResponseLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowed length of an error response.

Get: MaximumErrorResponseLength(self: HttpWebRequestElement) -> int

Set: MaximumErrorResponseLength(self: HttpWebRequestElement) = value
"""

    MaximumResponseHeadersLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum allowed length of the response headers.

Get: MaximumResponseHeadersLength(self: HttpWebRequestElement) -> int

Set: MaximumResponseHeadersLength(self: HttpWebRequestElement) = value
"""

    MaximumUnauthorizedUploadLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum length of an upload in response to an unauthorized error code.

Get: MaximumUnauthorizedUploadLength(self: HttpWebRequestElement) -> int

Set: MaximumUnauthorizedUploadLength(self: HttpWebRequestElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UseUnsafeHeaderParsing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Setting this property ignores validation errors that occur during HTTP parsing.

Get: UseUnsafeHeaderParsing(self: HttpWebRequestElement) -> bool

Set: UseUnsafeHeaderParsing(self: HttpWebRequestElement) = value
"""



class Ipv6Element(ConfigurationElement):
    """
    Determines whether Internet Protocol version 6 is enabled on the local computer. This class cannot be inherited.
    
    Ipv6Element()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that indicates whether Internet Protocol version 6 is enabled on the local computer.

Get: Enabled(self: Ipv6Element) -> bool

Set: Enabled(self: Ipv6Element) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MailSettingsSectionGroup(ConfigurationSectionGroup):
    """
    Initializes a new instance of the System.Net.Configuration.MailSettingsSectionGroup class.
    
    MailSettingsSectionGroup()
    """
    Smtp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the SMTP settings for the local computer.

Get: Smtp(self: MailSettingsSectionGroup) -> SmtpSection

"""



class ModuleElement(ConfigurationElement):
    """
    Represents the type information for a custom System.Net.IWebProxy module. This class cannot be inherited.
    
    ModuleElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type and assembly information for the current instance.

Get: Type(self: ModuleElement) -> str

Set: Type(self: ModuleElement) = value
"""



class NetSectionGroup(ConfigurationSectionGroup):
    """
    Gets the section group information for the networking namespaces. This class cannot be inherited.
    
    NetSectionGroup()
    """
    @staticmethod
    def GetSectionGroup(config):
        """
        GetSectionGroup(config: Configuration) -> NetSectionGroup
        
            Gets the System.Net configuration section group from the specified configuration file.
        
            config: A System.Configuration.Configuration that represents a configuration file.
            Returns: A System.Net.Configuration.NetSectionGroup that represents the System.Net settings in config.
        """
        pass

    AuthenticationModules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the authentication modules registered for the local computer.

Get: AuthenticationModules(self: NetSectionGroup) -> AuthenticationModulesSection

"""

    ConnectionManagement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the connection management settings for the local computer.

Get: ConnectionManagement(self: NetSectionGroup) -> ConnectionManagementSection

"""

    DefaultProxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the default Web proxy server settings for the local computer.

Get: DefaultProxy(self: NetSectionGroup) -> DefaultProxySection

"""

    MailSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the SMTP client e-mail settings for the local computer.

Get: MailSettings(self: NetSectionGroup) -> MailSettingsSectionGroup

"""

    RequestCaching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the cache configuration settings for the local computer.

Get: RequestCaching(self: NetSectionGroup) -> RequestCachingSection

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the network settings for the local computer.

Get: Settings(self: NetSectionGroup) -> SettingsSection

"""

    WebRequestModules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration section containing the modules registered for use with the System.Net.WebRequest class.

Get: WebRequestModules(self: NetSectionGroup) -> WebRequestModulesSection

"""



class PerformanceCountersElement(ConfigurationElement):
    """
    Represents the performance counter element in the System.Net configuration file that determines whether networking performance counters are enabled. This class cannot be inherited.
    
    PerformanceCountersElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether performance counters are enabled.

Get: Enabled(self: PerformanceCountersElement) -> bool

Set: Enabled(self: PerformanceCountersElement) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ProxyElement(ConfigurationElement):
    """
    Identifies the configuration settings for Web proxy server. This class cannot be inherited.
    
    ProxyElement()
    """
    AutoDetect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets an System.Net.Configuration.ProxyElement.AutoDetectValues value that controls whether the Web proxy is automatically detected.

Get: AutoDetect(self: ProxyElement) -> AutoDetectValues

Set: AutoDetect(self: ProxyElement) = value
"""

    BypassOnLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets a value that indicates whether local resources are retrieved by using a Web proxy server.

Get: BypassOnLocal(self: ProxyElement) -> BypassOnLocalValues

Set: BypassOnLocal(self: ProxyElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProxyAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets the URI that identifies the Web proxy server to use.

Get: ProxyAddress(self: ProxyElement) -> Uri

Set: ProxyAddress(self: ProxyElement) = value
"""

    ScriptLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets an System.Uri value that specifies the location of the automatic proxy detection script.

Get: ScriptLocation(self: ProxyElement) -> Uri

Set: ScriptLocation(self: ProxyElement) = value
"""

    UseSystemDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets and sets a System.Boolean value that controls whether the Internet Explorer Web proxy settings are used.

Get: UseSystemDefault(self: ProxyElement) -> UseSystemDefaultValues

Set: UseSystemDefault(self: ProxyElement) = value
"""


    AutoDetectValues = None
    BypassOnLocalValues = None
    UseSystemDefaultValues = None


class RequestCachingSection(ConfigurationSection):
    """
    Represents the configuration section for cache behavior. This class cannot be inherited.
    
    RequestCachingSection()
    """
    DefaultFtpCachePolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default FTP caching behavior for the local computer.

Get: DefaultFtpCachePolicy(self: RequestCachingSection) -> FtpCachePolicyElement

"""

    DefaultHttpCachePolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default caching behavior for the local computer.

Get: DefaultHttpCachePolicy(self: RequestCachingSection) -> HttpCachePolicyElement

"""

    DefaultPolicyLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cache policy level.

Get: DefaultPolicyLevel(self: RequestCachingSection) -> RequestCacheLevel

Set: DefaultPolicyLevel(self: RequestCachingSection) = value
"""

    DisableAllCaching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that enables caching on the local computer.

Get: DisableAllCaching(self: RequestCachingSection) -> bool

Set: DisableAllCaching(self: RequestCachingSection) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsPrivateCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that indicates whether the local computer cache is private.

Get: IsPrivateCache(self: RequestCachingSection) -> bool

Set: IsPrivateCache(self: RequestCachingSection) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UnspecifiedMaximumAge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value used as the maximum age for cached resources that do not have expiration information.

Get: UnspecifiedMaximumAge(self: RequestCachingSection) -> TimeSpan

Set: UnspecifiedMaximumAge(self: RequestCachingSection) = value
"""



class ServicePointManagerElement(ConfigurationElement):
    """
    Represents the default settings used to create connections to a remote computer. This class cannot be inherited.
    
    ServicePointManagerElement()
    """
    CheckCertificateName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that controls checking host name information in an X509 certificate.

Get: CheckCertificateName(self: ServicePointManagerElement) -> bool

Set: CheckCertificateName(self: ServicePointManagerElement) = value
"""

    CheckCertificateRevocationList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that indicates whether the certificate is checked against the certificate authority revocation list.

Get: CheckCertificateRevocationList(self: ServicePointManagerElement) -> bool

Set: CheckCertificateRevocationList(self: ServicePointManagerElement) = value
"""

    DnsRefreshTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of time after which address information is refreshed.

Get: DnsRefreshTimeout(self: ServicePointManagerElement) -> int

Set: DnsRefreshTimeout(self: ServicePointManagerElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EnableDnsRoundRobin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that controls using different IP addresses on connections to the same server.

Get: EnableDnsRoundRobin(self: ServicePointManagerElement) -> bool

Set: EnableDnsRoundRobin(self: ServicePointManagerElement) = value
"""

    EncryptionPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Net.Security.EncryptionPolicy to use.

Get: EncryptionPolicy(self: ServicePointManagerElement) -> EncryptionPolicy

Set: EncryptionPolicy(self: ServicePointManagerElement) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    Expect100Continue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that determines whether 100-Continue behavior is used.

Get: Expect100Continue(self: ServicePointManagerElement) -> bool

Set: Expect100Continue(self: ServicePointManagerElement) = value
"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UseNagleAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that determines whether the Nagle algorithm is used.

Get: UseNagleAlgorithm(self: ServicePointManagerElement) -> bool

Set: UseNagleAlgorithm(self: ServicePointManagerElement) = value
"""



class SettingsSection(ConfigurationSection):
    """
    Represents the configuration section for sockets, IPv6, response headers, and service points. This class cannot be inherited.
    
    SettingsSection()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HttpListener = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that controls the settings used by an System.Net.HttpListener object.

Get: HttpListener(self: SettingsSection) -> HttpListenerElement

"""

    HttpWebRequest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that controls the maximum response header length.

Get: HttpWebRequest(self: SettingsSection) -> HttpWebRequestElement

"""

    Ipv6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that enables Internet Protocol version 6 (IPv6).

Get: Ipv6(self: SettingsSection) -> Ipv6Element

"""

    PerformanceCounters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that controls whether performance counters are enabled.

Get: PerformanceCounters(self: SettingsSection) -> PerformanceCountersElement

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ServicePointManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that controls settings for connections to remote host computers.

Get: ServicePointManager(self: SettingsSection) -> ServicePointManagerElement

"""

    Socket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that controls settings for sockets.

Get: Socket(self: SettingsSection) -> SocketElement

"""

    WebProxyScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration element that controls the execution timeout and download timeout of Web proxy scripts.

Get: WebProxyScript(self: SettingsSection) -> WebProxyScriptElement

"""

    WebUtility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WebUtility(self: SettingsSection) -> WebUtilityElement

"""



class SmtpNetworkElement(ConfigurationElement):
    """
    Represents the network element in the SMTP configuration file. This class cannot be inherited.
    
    SmtpNetworkElement()
    """
    ClientDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the client domain name used in the initial SMTP protocol request to connect to an SMTP mail server.

Get: ClientDomain(self: SmtpNetworkElement) -> str

Set: ClientDomain(self: SmtpNetworkElement) = value
"""

    DefaultCredentials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether or not default user credentials are used to access an SMTP server. The default value is false.

Get: DefaultCredentials(self: SmtpNetworkElement) -> bool

Set: DefaultCredentials(self: SmtpNetworkElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EnableSsl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether SSL is used to access an SMTP mail server. The default value is false.

Get: EnableSsl(self: SmtpNetworkElement) -> bool

Set: EnableSsl(self: SmtpNetworkElement) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the SMTP server.

Get: Host(self: SmtpNetworkElement) -> str

Set: Host(self: SmtpNetworkElement) = value
"""

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the user password to use to connect to an SMTP mail server.

Get: Password(self: SmtpNetworkElement) -> str

Set: Password(self: SmtpNetworkElement) = value
"""

    Port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the port that SMTP clients use to connect to an SMTP mail server. The default value is 25.

Get: Port(self: SmtpNetworkElement) -> int

Set: Port(self: SmtpNetworkElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    TargetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Service Provider Name (SPN) to use for authentication when using extended protection to connect to an SMTP mail server.

Get: TargetName(self: SmtpNetworkElement) -> str

Set: TargetName(self: SmtpNetworkElement) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the user name to connect to an SMTP mail server.

Get: UserName(self: SmtpNetworkElement) -> str

Set: UserName(self: SmtpNetworkElement) = value
"""



class SmtpSection(ConfigurationSection):
    """
    Represents the SMTP section in the System.Net configuration file.
    
    SmtpSection()
    """
    DeliveryFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryFormat(self: SmtpSection) -> SmtpDeliveryFormat

Set: DeliveryFormat(self: SmtpSection) = value
"""

    DeliveryMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the SMTP delivery method. The default delivery method is System.Net.Mail.SmtpDeliveryMethod.Network.

Get: DeliveryMethod(self: SmtpSection) -> SmtpDeliveryMethod

Set: DeliveryMethod(self: SmtpSection) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default value that indicates who the email message is from.

Get: From(self: SmtpSection) -> str

Set: From(self: SmtpSection) = value
"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Network = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Net.Configuration.SmtpNetworkElement.

Get: Network(self: SmtpSection) -> SmtpNetworkElement

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpecifiedPickupDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the pickup directory that will be used by the SMPT client.

Get: SpecifiedPickupDirectory(self: SmtpSection) -> SmtpSpecifiedPickupDirectoryElement

"""



class SmtpSpecifiedPickupDirectoryElement(ConfigurationElement):
    """
    Represents an SMTP pickup directory configuration element.
    
    SmtpSpecifiedPickupDirectoryElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PickupDirectoryLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the folder where applications save mail messages to be processed by the SMTP server.

Get: PickupDirectoryLocation(self: SmtpSpecifiedPickupDirectoryElement) -> str

Set: PickupDirectoryLocation(self: SmtpSpecifiedPickupDirectoryElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SocketElement(ConfigurationElement):
    """
    Represents information used to configure System.Net.Sockets.Socket objects. This class cannot be inherited.
    
    SocketElement()
    """
    AlwaysUseCompletionPortsForAccept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether completion ports are used when accepting connections.

Get: AlwaysUseCompletionPortsForAccept(self: SocketElement) -> bool

Set: AlwaysUseCompletionPortsForAccept(self: SocketElement) = value
"""

    AlwaysUseCompletionPortsForConnect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a Boolean value that specifies whether completion ports are used when making connections.

Get: AlwaysUseCompletionPortsForConnect(self: SocketElement) -> bool

Set: AlwaysUseCompletionPortsForConnect(self: SocketElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IPProtectionLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies the default System.Net.Sockets.IPProtectionLevel to use for a socket.

Get: IPProtectionLevel(self: SocketElement) -> IPProtectionLevel

Set: IPProtectionLevel(self: SocketElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnicodeDecodingConformance(Enum, IComparable, IFormattable, IConvertible):
    """ enum UnicodeDecodingConformance, values: Auto (0), Compat (2), Loose (3), Strict (1) """
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

    Auto = None
    Compat = None
    Loose = None
    Strict = None
    value__ = None


class UnicodeEncodingConformance(Enum, IComparable, IFormattable, IConvertible):
    """ enum UnicodeEncodingConformance, values: Auto (0), Compat (2), Strict (1) """
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

    Auto = None
    Compat = None
    Strict = None
    value__ = None


class WebProxyScriptElement(ConfigurationElement):
    """
    Represents information used to configure Web proxy scripts. This class cannot be inherited.
    
    WebProxyScriptElement()
    """
    DownloadTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Web proxy script download timeout using the format hours:minutes:seconds.

Get: DownloadTimeout(self: WebProxyScriptElement) -> TimeSpan

Set: DownloadTimeout(self: WebProxyScriptElement) = value
"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class WebRequestModuleElement(ConfigurationElement):
    """
    Represents a URI prefix and the associated class that handles creating Web requests for the prefix. This class cannot be inherited.
    
    WebRequestModuleElement()
    WebRequestModuleElement(prefix: str, type: str)
    WebRequestModuleElement(prefix: str, type: Type)
    """
    @staticmethod # known case of __new__
    def __new__(self, prefix=None, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, prefix: str, type: str)
        __new__(cls: type, prefix: str, type: Type)
        """
        pass

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the URI prefix for the current Web request module.

Get: Prefix(self: WebRequestModuleElement) -> str

Set: Prefix(self: WebRequestModuleElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a class that creates Web requests.

Get: Type(self: WebRequestModuleElement) -> Type

Set: Type(self: WebRequestModuleElement) = value
"""



class WebRequestModuleElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    Represents a container for Web request module configuration elements. This class cannot be inherited.
    
    WebRequestModuleElementCollection()
    """
    def Add(self, element):
        """
        Add(self: WebRequestModuleElementCollection, element: WebRequestModuleElement)
            Adds an element to the collection.
        
            element: The System.Net.Configuration.WebRequestModuleElement to add to the collection.
        """
        pass

    def BaseAdd(self, *args): #cannot find CLR method
        """
        BaseAdd(self: ConfigurationElementCollection, index: int, element: ConfigurationElement)
            Adds a configuration element to the configuration element collection.
        
            index: The index location at which to add the specified System.Configuration.ConfigurationElement.
            element: The System.Configuration.ConfigurationElement to add.
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement, throwIfExists: bool)
            Adds a configuration element to the configuration element collection.
        
            element: The System.Configuration.ConfigurationElement to add.
            throwIfExists: true to throw an exception if the System.Configuration.ConfigurationElement specified is already 
             contained in the System.Configuration.ConfigurationElementCollection; otherwise, false.
        
        BaseAdd(self: ConfigurationElementCollection, element: ConfigurationElement)
            Adds a configuration element to the System.Configuration.ConfigurationElementCollection.
        
            element: The System.Configuration.ConfigurationElement to add.
        """
        pass

    def BaseClear(self, *args): #cannot find CLR method
        """
        BaseClear(self: ConfigurationElementCollection)
            Removes all configuration element objects from the collection.
        """
        pass

    def BaseGet(self, *args): #cannot find CLR method
        """
        BaseGet(self: ConfigurationElementCollection, index: int) -> ConfigurationElement
        
            Gets the configuration element at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to return.
            Returns: The System.Configuration.ConfigurationElement at the specified index.
        BaseGet(self: ConfigurationElementCollection, key: object) -> ConfigurationElement
        
            Returns the configuration element with the specified key.
        
            key: The key of the element to return.
            Returns: The System.Configuration.ConfigurationElement with the specified key; otherwise, null.
        """
        pass

    def BaseGetAllKeys(self, *args): #cannot find CLR method
        """
        BaseGetAllKeys(self: ConfigurationElementCollection) -> Array[object]
        
            Returns an array of the keys for all of the configuration elements contained in the 
             System.Configuration.ConfigurationElementCollection.
        
            Returns: An array that contains the keys for all of the System.Configuration.ConfigurationElement objects 
             contained in the System.Configuration.ConfigurationElementCollection.
        """
        pass

    def BaseGetKey(self, *args): #cannot find CLR method
        """
        BaseGetKey(self: ConfigurationElementCollection, index: int) -> object
        
            Gets the key for the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location for the System.Configuration.ConfigurationElement.
            Returns: The key for the specified System.Configuration.ConfigurationElement.
        """
        pass

    def BaseIndexOf(self, *args): #cannot find CLR method
        """
        BaseIndexOf(self: ConfigurationElementCollection, element: ConfigurationElement) -> int
        
            The index of the specified System.Configuration.ConfigurationElement.
        
            element: The System.Configuration.ConfigurationElement for the specified index location.
            Returns: The index of the specified System.Configuration.ConfigurationElement; otherwise, -1.
        """
        pass

    def BaseIsRemoved(self, *args): #cannot find CLR method
        """
        BaseIsRemoved(self: ConfigurationElementCollection, key: object) -> bool
        
            Gets a value indicating whether the System.Configuration.ConfigurationElement with the specified 
             key has been removed from the System.Configuration.ConfigurationElementCollection.
        
        
            key: The key of the element to check.
            Returns: true if the System.Configuration.ConfigurationElement with the specified key has been removed; 
             otherwise, false. The default is false.
        """
        pass

    def BaseRemove(self, *args): #cannot find CLR method
        """
        BaseRemove(self: ConfigurationElementCollection, key: object)
            Removes a System.Configuration.ConfigurationElement from the collection.
        
            key: The key of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def BaseRemoveAt(self, *args): #cannot find CLR method
        """
        BaseRemoveAt(self: ConfigurationElementCollection, index: int)
            Removes the System.Configuration.ConfigurationElement at the specified index location.
        
            index: The index location of the System.Configuration.ConfigurationElement to remove.
        """
        pass

    def Clear(self):
        """
        Clear(self: WebRequestModuleElementCollection)
            Removes all elements from the collection.
        """
        pass

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: WebRequestModuleElementCollection) -> ConfigurationElement
        CreateNewElement(self: ConfigurationElementCollection, elementName: str) -> ConfigurationElement
        
            Creates a new System.Configuration.ConfigurationElement when overridden in a derived class.
        
            elementName: The name of the System.Configuration.ConfigurationElement to create.
            Returns: A new System.Configuration.ConfigurationElement.
        """
        pass

    def DeserializeElement(self, *args): #cannot find CLR method
        """
        DeserializeElement(self: ConfigurationElement, reader: XmlReader, serializeCollectionKey: bool)
            Reads XML from the configuration file.
        
            reader: The System.Xml.XmlReader that reads from the configuration file.
            serializeCollectionKey: true to serialize only the collection key properties; otherwise, false.
        """
        pass

    def GetElementKey(self, *args): #cannot find CLR method
        """ GetElementKey(self: WebRequestModuleElementCollection, element: ConfigurationElement) -> object """
        pass

    def GetTransformedAssemblyString(self, *args): #cannot find CLR method
        """
        GetTransformedAssemblyString(self: ConfigurationElement, assemblyName: str) -> str
        
            Returns the transformed version of the specified assembly name.
        
            assemblyName: The name of the assembly.
            Returns: The transformed version of the assembly name. If no transformer is available, the assemblyName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def GetTransformedTypeString(self, *args): #cannot find CLR method
        """
        GetTransformedTypeString(self: ConfigurationElement, typeName: str) -> str
        
            Returns the transformed version of the specified type name.
        
            typeName: The name of the type.
            Returns: The transformed version of the specified type name. If no transformer is available, the typeName 
             parameter value is returned unchanged. The 
             System.Configuration.Configuration.TypeStringTransformer property is null if no transformer is 
             available.
        """
        pass

    def get_Item(self, *__args):
        """
        get_Item(self: ConfigurationElement, propertyName: str) -> object
        get_Item(self: ConfigurationElement, prop: ConfigurationProperty) -> object
        """
        pass

    def IndexOf(self, element):
        """
        IndexOf(self: WebRequestModuleElementCollection, element: WebRequestModuleElement) -> int
        
            Returns the index of the specified configuration element.
        
            element: A System.Net.Configuration.WebRequestModuleElement.
            Returns: The zero-based index of element.
        """
        pass

    def Init(self, *args): #cannot find CLR method
        """
        Init(self: ConfigurationElement)
            Sets the System.Configuration.ConfigurationElement object to its initial state.
        """
        pass

    def InitializeDefault(self, *args): #cannot find CLR method
        """
        InitializeDefault(self: ConfigurationElement)
            Used to initialize a default set of values for the System.Configuration.ConfigurationElement 
             object.
        """
        pass

    def IsElementName(self, *args): #cannot find CLR method
        """
        IsElementName(self: ConfigurationElementCollection, elementName: str) -> bool
        
            Indicates whether the specified System.Configuration.ConfigurationElement exists in the 
             System.Configuration.ConfigurationElementCollection.
        
        
            elementName: The name of the element to verify.
            Returns: true if the element exists in the collection; otherwise, false. The default is false.
        """
        pass

    def IsElementRemovable(self, *args): #cannot find CLR method
        """
        IsElementRemovable(self: ConfigurationElementCollection, element: ConfigurationElement) -> bool
        
            Gets a value indicating whether the specified System.Configuration.ConfigurationElement can be 
             removed from the System.Configuration.ConfigurationElementCollection.
        
        
            element: The element to check.
            Returns: true if the specified System.Configuration.ConfigurationElement can be removed from this 
             System.Configuration.ConfigurationElementCollection; otherwise, false. The default is true.
        """
        pass

    def IsModified(self, *args): #cannot find CLR method
        """
        IsModified(self: ConfigurationElementCollection) -> bool
        
            Indicates whether this System.Configuration.ConfigurationElementCollection has been modified 
             since it was last saved or loaded when overridden in a derived class.
        
            Returns: true if any contained element has been modified; otherwise, false
        """
        pass

    def ListErrors(self, *args): #cannot find CLR method
        """
        ListErrors(self: ConfigurationElement, errorList: IList)
            Adds the invalid-property errors in this System.Configuration.ConfigurationElement object, and 
             in all subelements, to the passed list.
        
        
            errorList: An object that implements the System.Collections.IList interface.
        """
        pass

    def OnDeserializeUnrecognizedAttribute(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedAttribute(self: ConfigurationElement, name: str, value: str) -> bool
        
            Gets a value indicating whether an unknown attribute is encountered during deserialization.
        
            name: The name of the unrecognized attribute.
            value: The value of the unrecognized attribute.
            Returns: true when an unknown attribute is encountered while deserializing; otherwise, false.
        """
        pass

    def OnDeserializeUnrecognizedElement(self, *args): #cannot find CLR method
        """
        OnDeserializeUnrecognizedElement(self: ConfigurationElementCollection, elementName: str, reader: XmlReader) -> bool
        
            Causes the configuration system to throw an exception.
        
            elementName: The name of the unrecognized element.
            reader: An input stream that reads XML from the configuration file.
            Returns: true if the unrecognized element was deserialized successfully; otherwise, false. The default is 
             false.
        """
        pass

    def OnRequiredPropertyNotFound(self, *args): #cannot find CLR method
        """
        OnRequiredPropertyNotFound(self: ConfigurationElement, name: str) -> object
        
            Throws an exception when a required property is not found.
        
            name: The name of the required attribute that was not found.
            Returns: None.
        """
        pass

    def PostDeserialize(self, *args): #cannot find CLR method
        """
        PostDeserialize(self: ConfigurationElement)
            Called after deserialization.
        """
        pass

    def PreSerialize(self, *args): #cannot find CLR method
        """
        PreSerialize(self: ConfigurationElement, writer: XmlWriter)
            Called before serialization.
        
            writer: The System.Xml.XmlWriter that will be used to serialize the 
             System.Configuration.ConfigurationElement.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: WebRequestModuleElementCollection, name: str)
            Removes the element with the specified key.
        
            name: The key of the element to remove.
        Remove(self: WebRequestModuleElementCollection, element: WebRequestModuleElement)
            Removes the specified configuration element from the collection.
        
            element: The System.Net.Configuration.WebRequestModuleElement to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: WebRequestModuleElementCollection, index: int)
            Removes the element at the specified index.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def Reset(self, *args): #cannot find CLR method
        """
        Reset(self: ConfigurationElementCollection, parentElement: ConfigurationElement)
            Resets the System.Configuration.ConfigurationElementCollection to its unmodified state when 
             overridden in a derived class.
        
        
            parentElement: The System.Configuration.ConfigurationElement representing the collection parent element, if 
             any; otherwise, null.
        """
        pass

    def ResetModified(self, *args): #cannot find CLR method
        """
        ResetModified(self: ConfigurationElementCollection)
            Resets the value of the System.Configuration.ConfigurationElementCollection.IsModified property 
             to false when overridden in a derived class.
        """
        pass

    def SerializeElement(self, *args): #cannot find CLR method
        """
        SerializeElement(self: ConfigurationElementCollection, writer: XmlWriter, serializeCollectionKey: bool) -> bool
        
            Writes the configuration data to an XML element in the configuration file when overridden in a 
             derived class.
        
        
            writer: Output stream that writes XML to the configuration file.
            serializeCollectionKey: true to serialize the collection key; otherwise, false.
            Returns: true if the System.Configuration.ConfigurationElementCollection was written to the configuration 
             file successfully.
        """
        pass

    def SerializeToXmlElement(self, *args): #cannot find CLR method
        """
        SerializeToXmlElement(self: ConfigurationElement, writer: XmlWriter, elementName: str) -> bool
        
            Writes the outer tags of this configuration element to the configuration file when implemented 
             in a derived class.
        
        
            writer: The System.Xml.XmlWriter that writes to the configuration file.
            elementName: The name of the System.Configuration.ConfigurationElement to be written.
            Returns: true if writing was successful; otherwise, false.
        """
        pass

    def SetPropertyValue(self, *args): #cannot find CLR method
        """
        SetPropertyValue(self: ConfigurationElement, prop: ConfigurationProperty, value: object, ignoreLocks: bool)
            Sets a property to the specified value.
        
            prop: The element property to set.
            value: The value to assign to the property.
            ignoreLocks: true if the locks on the property should be ignored; otherwise, false.
        """
        pass

    def SetReadOnly(self, *args): #cannot find CLR method
        """
        SetReadOnly(self: ConfigurationElementCollection)
            Sets the System.Configuration.ConfigurationElementCollection.IsReadOnly property for the 
             System.Configuration.ConfigurationElementCollection object and for all sub-elements.
        """
        pass

    def set_Item(self, *__args):
        """ set_Item(self: ConfigurationElement, propertyName: str, value: object)set_Item(self: ConfigurationElement, prop: ConfigurationProperty, value: object) """
        pass

    def Unmerge(self, *args): #cannot find CLR method
        """
        Unmerge(self: ConfigurationElementCollection, sourceElement: ConfigurationElement, parentElement: ConfigurationElement, saveMode: ConfigurationSaveMode)
            Reverses the effect of merging configuration information from different levels of the 
             configuration hierarchy
        
        
            sourceElement: A System.Configuration.ConfigurationElement object at the current level containing a merged view 
             of the properties.
        
            parentElement: The parent System.Configuration.ConfigurationElement object of the current element, or null if 
             this is the top level.
        
            saveMode: A System.Configuration.ConfigurationSaveMode enumerated value that determines which property 
             values to include.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    AddElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ClearElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class.

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of properties.

"""

    RemoveElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ThrowOnDuplicate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown.

"""



class WebRequestModulesSection(ConfigurationSection):
    """
    Represents the configuration section for Web request modules. This class cannot be inherited.
    
    WebRequestModulesSection()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    WebRequestModules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of Web request modules in the section.

Get: WebRequestModules(self: WebRequestModulesSection) -> WebRequestModuleElementCollection

"""



class WebUtilityElement(ConfigurationElement):
    """ WebUtilityElement() """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UnicodeDecodingConformance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnicodeDecodingConformance(self: WebUtilityElement) -> UnicodeDecodingConformance

Set: UnicodeDecodingConformance(self: WebUtilityElement) = value
"""

    UnicodeEncodingConformance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnicodeEncodingConformance(self: WebUtilityElement) -> UnicodeEncodingConformance

Set: UnicodeEncodingConformance(self: WebUtilityElement) = value
"""



