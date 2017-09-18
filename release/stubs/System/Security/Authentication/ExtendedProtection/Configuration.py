# encoding: utf-8
# module System.Security.Authentication.ExtendedProtection.Configuration calls itself Configuration
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ExtendedProtectionPolicyElement(ConfigurationElement):
    """
    The System.Security.Authentication.ExtendedProtection.Configuration.ExtendedProtectionPolicyElement class represents a configuration element for an System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy.
    
    ExtendedProtectionPolicyElement()
    """
    def BuildPolicy(self):
        """
        BuildPolicy(self: ExtendedProtectionPolicyElement) -> ExtendedProtectionPolicy
        
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ExtendedProtectionPolicyElement.B
             uildPolicy method builds a new 
             System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy instance based on the 
             properties set on the 
             System.Security.Authentication.ExtendedProtection.Configuration.ExtendedProtectionPolicyElement 
             class.
        
            Returns: A new System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy instance that 
             represents the extended protection policy created.
        """
        pass

    CustomServiceNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the custom Service Provider Name (SPN) list used to match against a client's SPN for this configuration policy element.

Get: CustomServiceNames(self: ExtendedProtectionPolicyElement) -> ServiceNameElementCollection

"""

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PolicyEnforcement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the policy enforcement value for this configuration policy element.

Get: PolicyEnforcement(self: ExtendedProtectionPolicyElement) -> PolicyEnforcement

Set: PolicyEnforcement(self: ExtendedProtectionPolicyElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProtectionScenario = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the kind of protection enforced by the extended protection policy for this configuration policy element.

Get: ProtectionScenario(self: ExtendedProtectionPolicyElement) -> ProtectionScenario

Set: ProtectionScenario(self: ExtendedProtectionPolicyElement) = value
"""



class ServiceNameElement(ConfigurationElement):
    """
    The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement class represents a configuration element for a service name used in a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
    
    ServiceNameElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Service Provider Name (SPN) for this System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance.

Get: Name(self: ServiceNameElement) -> str

Set: Name(self: ServiceNameElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ServiceNameElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    The System.Security.Authentication.ExtendedProtection.ServiceNameCollection class is a collection of service principal names that represent a configuration element for an System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy.
    
    ServiceNameElementCollection()
    """
    def Add(self, element):
        """
        Add(self: ServiceNameElementCollection, element: ServiceNameElement)
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Add(
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement) method adds 
             a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to 
             this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        
        
            element: The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance 
             to add to this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
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
        Clear(self: ServiceNameElementCollection)
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Clea
             r method removes all configuration element objects from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        """
        pass

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: ServiceNameElementCollection) -> ConfigurationElement
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
        """ GetElementKey(self: ServiceNameElementCollection, element: ConfigurationElement) -> object """
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
        IndexOf(self: ServiceNameElementCollection, element: ServiceNameElement) -> int
        
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Inde
             xOf(System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement) method 
             retrieves the index of the specified configuration element in this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        
        
            element: The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance 
             to retrieve the index of in this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        
            Returns: The index of the specified 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement in this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
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
        Remove(self: ServiceNameElementCollection, name: str)
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Remo
             ve(System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement) method 
             removes a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement 
             instance from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection 
             based on the System.String specified.
        
        
            name: A System.String that represents the 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to 
             remove from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection
        
        Remove(self: ServiceNameElementCollection, element: ServiceNameElement)
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Remo
             ve(System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement) method 
             removes a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement 
             instance from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        
        
            element: The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance 
             to remove from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ServiceNameElementCollection, index: int)
            The 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Remo
             ve(System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement) method 
             removes a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement 
             instance from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection 
             based on the index specified.
        
        
            index: The index of the 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to 
             remove from this 
             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
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



