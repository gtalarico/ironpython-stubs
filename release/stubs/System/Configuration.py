# encoding: utf-8
# module System.Configuration calls itself Configuration
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class SettingAttribute(Attribute, _Attribute):
    """
    Represents a custom settings attribute used to associate settings information with a settings property.
    
    SettingAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ApplicationScopedSettingAttribute(SettingAttribute, _Attribute):
    """
    Specifies that an application settings property has a common value for all users of an application. This class cannot be inherited.
    
    ApplicationScopedSettingAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SettingsBase(object):
    """ Provides the base class used to support user property settings. """
    def Initialize(self, context, properties, providers):
        """
        Initialize(self: SettingsBase, context: SettingsContext, properties: SettingsPropertyCollection, providers: SettingsProviderCollection)
            Initializes internal properties used by System.Configuration.SettingsBase object.
        
            context: The settings context related to the settings properties.
            properties: The settings properties that will be accessible from the System.Configuration.SettingsBase 
             instance.
        
            providers: The initialized providers that should be used when loading and saving property values.
        """
        pass

    def Save(self):
        """
        Save(self: SettingsBase)
            Stores the current values of the settings properties.
        """
        pass

    @staticmethod
    def Synchronized(settingsBase):
        """
        Synchronized(settingsBase: SettingsBase) -> SettingsBase
        
            Provides a System.Configuration.SettingsBase class that is synchronized (thread safe).
        
            settingsBase: The class used to support user property settings.
            Returns: A System.Configuration.SettingsBase class that is synchronized.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the associated settings context.

Get: Context(self: SettingsBase) -> SettingsContext

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to the object is synchronized (thread safe).

Get: IsSynchronized(self: SettingsBase) -> bool

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of settings properties.

Get: Properties(self: SettingsBase) -> SettingsPropertyCollection

"""

    PropertyValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of settings property values.

Get: PropertyValues(self: SettingsBase) -> SettingsPropertyValueCollection

"""

    Providers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of settings providers.

Get: Providers(self: SettingsBase) -> SettingsProviderCollection

"""



class ApplicationSettingsBase(SettingsBase, INotifyPropertyChanged):
    """ Acts as a base class for deriving concrete wrapper classes to implement the application settings feature in Window Forms applications. """
    def GetPreviousVersion(self, propertyName):
        """
        GetPreviousVersion(self: ApplicationSettingsBase, propertyName: str) -> object
        
            Returns the value of the named settings property for the previous version of the same 
             application.
        
        
            propertyName: A System.String containing the name of the settings property whose value is to be returned.
            Returns: An System.Object containing the value of the specified System.Configuration.SettingsProperty if 
             found; otherwise, null.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: ApplicationSettingsBase, sender: object, e: PropertyChangedEventArgs)
            Raises the System.Configuration.ApplicationSettingsBase.PropertyChanged event.
        
            sender: The source of the event.
            e: A System.ComponentModel.PropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnSettingChanging(self, *args): #cannot find CLR method
        """
        OnSettingChanging(self: ApplicationSettingsBase, sender: object, e: SettingChangingEventArgs)
            Raises the System.Configuration.ApplicationSettingsBase.SettingChanging event.
        
            sender: The source of the event.
            e: A System.Configuration.SettingChangingEventArgs that contains the event data.
        """
        pass

    def OnSettingsLoaded(self, *args): #cannot find CLR method
        """
        OnSettingsLoaded(self: ApplicationSettingsBase, sender: object, e: SettingsLoadedEventArgs)
            Raises the System.Configuration.ApplicationSettingsBase.SettingsLoaded event.
        
            sender: The source of the event.
            e: A System.Configuration.SettingsLoadedEventArgs that contains the event data.
        """
        pass

    def OnSettingsSaving(self, *args): #cannot find CLR method
        """
        OnSettingsSaving(self: ApplicationSettingsBase, sender: object, e: CancelEventArgs)
            Raises the System.Configuration.ApplicationSettingsBase.SettingsSaving event.
        
            sender: The source of the event.
            e: A System.ComponentModel.CancelEventArgs that contains the event data.
        """
        pass

    def Reload(self):
        """
        Reload(self: ApplicationSettingsBase)
            Refreshes the application settings property values from persistent storage.
        """
        pass

    def Reset(self):
        """
        Reset(self: ApplicationSettingsBase)
            Restores the persisted application settings values to their corresponding default properties.
        """
        pass

    def Save(self):
        """
        Save(self: ApplicationSettingsBase)
            Stores the current values of the application settings properties.
        """
        pass

    def Upgrade(self):
        """
        Upgrade(self: ApplicationSettingsBase)
            Updates application settings to reflect a more recent installation of the application.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, owner: IComponent)
        __new__(cls: type, settingsKey: str)
        __new__(cls: type, owner: IComponent, settingsKey: str)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the application settings context associated with the settings group.

Get: Context(self: ApplicationSettingsBase) -> SettingsContext

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of settings properties in the wrapper.

Get: Properties(self: ApplicationSettingsBase) -> SettingsPropertyCollection

"""

    PropertyValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of property values.

Get: PropertyValues(self: ApplicationSettingsBase) -> SettingsPropertyValueCollection

"""

    Providers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of application settings providers used by the wrapper.

Get: Providers(self: ApplicationSettingsBase) -> SettingsProviderCollection

"""

    SettingsKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the settings key for the application settings group.

Get: SettingsKey(self: ApplicationSettingsBase) -> str

Set: SettingsKey(self: ApplicationSettingsBase) = value
"""


    PropertyChanged = None
    SettingChanging = None
    SettingsLoaded = None
    SettingsSaving = None


class ApplicationSettingsGroup(ConfigurationSectionGroup):
    """
    Represents a grouping of related application settings sections within a configuration file. This class cannot be inherited.
    
    ApplicationSettingsGroup()
    """

class AppSettingsReader(object):
    """
    Provides a method for reading values of a particular type from the configuration.
    
    AppSettingsReader()
    """
    def GetValue(self, key, type):
        """
        GetValue(self: AppSettingsReader, key: str, type: Type) -> object
        
            Gets the value for a specified key from the 
             System.Configuration.ConfigurationSettings.AppSettings property and returns an object of the 
             specified type containing the value from the configuration.
        
        
            key: The key for which to get the value.
            type: The type of the object to return.
            Returns: The value of the specified key.
        """
        pass


class ClientSettingsSection(ConfigurationSection):
    """
    Represents a group of user-scoped application settings in a configuration file.
    
    ClientSettingsSection()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of client settings for the section.

Get: Settings(self: ClientSettingsSection) -> SettingElementCollection

"""



class ConfigurationException(SystemException, ISerializable, _Exception):
    """
    The exception that is thrown when a configuration system error has occurred.
    
    ConfigurationException()
    ConfigurationException(message: str)
    ConfigurationException(message: str, inner: Exception)
    ConfigurationException(message: str, node: XmlNode)
    ConfigurationException(message: str, inner: Exception, node: XmlNode)
    ConfigurationException(message: str, filename: str, line: int)
    ConfigurationException(message: str, inner: Exception, filename: str, line: int)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: ConfigurationException, info: SerializationInfo, context: StreamingContext)
            Sets the System.Runtime.Serialization.SerializationInfo object with the file name and line 
             number at which this configuration exception occurred.
        
        
            info: The object that holds the information to be serialized.
            context: The contextual information about the source or destination.
        """
        pass

    @staticmethod
    def GetXmlNodeFilename(node):
        """
        GetXmlNodeFilename(node: XmlNode) -> str
        
            Gets the path to the configuration file from which the internal System.Xml.XmlNode object was 
             loaded when this configuration exception was thrown.
        
        
            node: The System.Xml.XmlNode that caused this System.Configuration.ConfigurationException exception to 
             be thrown.
        
            Returns: A string representing the node file name.
        """
        pass

    @staticmethod
    def GetXmlNodeLineNumber(node):
        """
        GetXmlNodeLineNumber(node: XmlNode) -> int
        
            Gets the line number within the configuration file that the internal System.Xml.XmlNode object 
             represented when this configuration exception was thrown.
        
        
            node: The System.Xml.XmlNode that caused this System.Configuration.ConfigurationException exception to 
             be thrown.
        
            Returns: An int representing the node line number.
        """
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
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, node: XmlNode)
        __new__(cls: type, message: str, inner: Exception, node: XmlNode)
        __new__(cls: type, message: str, filename: str, line: int)
        __new__(cls: type, message: str, inner: Exception, filename: str, line: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BareMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a description of why this configuration exception was thrown.

Get: BareMessage(self: ConfigurationException) -> str

"""

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the path to the configuration file that caused this configuration exception to be thrown.

Get: Filename(self: ConfigurationException) -> str

"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line number within the configuration file at which this configuration exception was thrown.

Get: Line(self: ConfigurationException) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an extended description of why this configuration exception was thrown.

Get: Message(self: ConfigurationException) -> str

"""



class ConfigurationSettings(object):
    """ Provides runtime versions 1.0 and 1.1 support for reading configuration sections and common configuration settings. """
    @staticmethod
    def GetConfig(sectionName):
        """
        GetConfig(sectionName: str) -> object
        
            Returns the System.Configuration.ConfigurationSection object for the passed configuration 
             section name and path.
        
        
            sectionName: A configuration name and path, such as "system.net/settings".
            Returns: The System.Configuration.ConfigurationSection object for the passed configuration section name 
             and path.NoteThe System.Configuration.ConfigurationSettings class provides backward 
             compatibility only. You should use the System.Configuration.ConfigurationManager class or 
             System.Web.Configuration.WebConfigurationManager class instead.
        """
        pass

    AppSettings = None


class ConfigXmlDocument(XmlDocument, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    """
    Wraps the corresponding System.Xml.XmlDocument type and also carries the necessary information for reporting file-name and line numbers.
    
    ConfigXmlDocument()
    """
    def CreateAttribute(self, *__args):
        """
        CreateAttribute(self: ConfigXmlDocument, prefix: str, localName: str, namespaceUri: str) -> XmlAttribute
        
            Creates a configuration element attribute.
        
            prefix: The prefix definition.
            localName: The name that is used locally.
            namespaceUri: The URL that is assigned to the namespace.
            Returns: The System.Xml.Serialization.XmlAttributes.XmlAttribute attribute.
        """
        pass

    def CreateCDataSection(self, data):
        """
        CreateCDataSection(self: ConfigXmlDocument, data: str) -> XmlCDataSection
        
            Creates an XML CData section.
        
            data: The data to use.
            Returns: The System.Xml.XmlCDataSection value.
        """
        pass

    def CreateComment(self, data):
        """
        CreateComment(self: ConfigXmlDocument, data: str) -> XmlComment
        
            Create an XML comment.
        
            data: The comment data.
            Returns: The System.Xml.XmlComment value.
        """
        pass

    def CreateDefaultAttribute(self, *args): #cannot find CLR method
        """
        CreateDefaultAttribute(self: XmlDocument, prefix: str, localName: str, namespaceURI: str) -> XmlAttribute
        
            Creates a default attribute with the specified prefix, local name and namespace URI.
        
            prefix: The prefix of the attribute (if any).
            localName: The local name of the attribute.
            namespaceURI: The namespace URI of the attribute (if any).
            Returns: The new System.Xml.XmlAttribute.
        """
        pass

    def CreateElement(self, *__args):
        """
        CreateElement(self: ConfigXmlDocument, prefix: str, localName: str, namespaceUri: str) -> XmlElement
        
            Creates a configuration element.
        
            prefix: The prefix definition.
            localName: The name used locally.
            namespaceUri: The namespace for the URL.
            Returns: The System.Xml.XmlElement value.
        """
        pass

    def CreateNavigator(self):
        """
        CreateNavigator(self: XmlDocument, node: XmlNode) -> XPathNavigator
        
            Creates an System.Xml.XPath.XPathNavigator object for navigating this document positioned on the 
             System.Xml.XmlNode specified.
        
        
            node: The System.Xml.XmlNode you want the navigator initially positioned on.
            Returns: An System.Xml.XPath.XPathNavigator object.
        """
        pass

    def CreateSignificantWhitespace(self, data):
        """
        CreateSignificantWhitespace(self: ConfigXmlDocument, data: str) -> XmlSignificantWhitespace
        
            Creates white spaces.
        
            data: The data to use.
            Returns: The System.Xml.XmlSignificantWhitespace value.
        """
        pass

    def CreateTextNode(self, text):
        """
        CreateTextNode(self: ConfigXmlDocument, text: str) -> XmlText
        
            Create a text node.
        
            text: The text to use.
            Returns: The System.Xml.XmlText value.
        """
        pass

    def CreateWhitespace(self, data):
        """
        CreateWhitespace(self: ConfigXmlDocument, data: str) -> XmlWhitespace
        
            Creates white space.
        
            data: The data to use.
            Returns: The System.Xml.XmlWhitespace value.
        """
        pass

    def Load(self, *__args):
        """
        Load(self: ConfigXmlDocument, filename: str)
            Loads the configuration file.
        
            filename: The name of the file.
        """
        pass

    def LoadSingleElement(self, filename, sourceReader):
        """
        LoadSingleElement(self: ConfigXmlDocument, filename: str, sourceReader: XmlTextReader)
            Loads a single configuration element.
        
            filename: The name of the file.
            sourceReader: The source for the reader.
        """
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

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the configuration file name.

Get: Filename(self: ConfigXmlDocument) -> str

"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current node line number.

Get: LineNumber(self: ConfigXmlDocument) -> int

"""



class DefaultSettingValueAttribute(Attribute, _Attribute):
    """
    Specifies the default value for an application settings property.
    
    DefaultSettingValueAttribute(value: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default value for the application settings property.

Get: Value(self: DefaultSettingValueAttribute) -> str

"""



class DictionarySectionHandler(object, IConfigurationSectionHandler):
    """
    Provides key/value pair configuration information from a configuration section.
    
    DictionarySectionHandler()
    """
    def Create(self, parent, context, section):
        """
        Create(self: DictionarySectionHandler, parent: object, context: object, section: XmlNode) -> object
        
            Creates a new configuration handler and adds it to the section-handler collection based on the 
             specified parameters.
        
        
            parent: Parent object.
            context: Configuration context object.
            section: Section XML node.
            Returns: A configuration object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    KeyAttributeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the XML attribute name to use as the key in a key/value pair.

"""

    ValueAttributeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the XML attribute name to use as the value in a key/value pair.

"""



class IApplicationSettingsProvider:
    """ Defines extended capabilities for client-based application settings providers. """
    def GetPreviousVersion(self, context, property):
        """
        GetPreviousVersion(self: IApplicationSettingsProvider, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue
        
            Returns the value of the specified settings property for the previous version of the same 
             application.
        
        
            context: A System.Configuration.SettingsContext describing the current application usage.
            property: The System.Configuration.SettingsProperty whose value is to be returned.
            Returns: A System.Configuration.SettingsPropertyValue containing the value of the specified property 
             setting as it was last set in the previous version of the application; or null if the setting 
             cannot be found.
        """
        pass

    def Reset(self, context):
        """
        Reset(self: IApplicationSettingsProvider, context: SettingsContext)
            Resets the application settings associated with the specified application to their default 
             values.
        
        
            context: A System.Configuration.SettingsContext describing the current application usage.
        """
        pass

    def Upgrade(self, context, properties):
        """
        Upgrade(self: IApplicationSettingsProvider, context: SettingsContext, properties: SettingsPropertyCollection)
            Indicates to the provider that the application has been upgraded. This offers the provider an 
             opportunity to upgrade its stored settings as appropriate.
        
        
            context: A System.Configuration.SettingsContext describing the current application usage.
            properties: A System.Configuration.SettingsPropertyCollection containing the settings property group whose 
             values are to be retrieved.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IConfigurationSectionHandler:
    """ Handles the access to certain configuration sections. """
    def Create(self, parent, configContext, section):
        """
        Create(self: IConfigurationSectionHandler, parent: object, configContext: object, section: XmlNode) -> object
        
            Creates a configuration section handler.
        
            parent: Parent object.
            configContext: Configuration context object.
            section: Section XML node.
            Returns: The created section handler object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IConfigurationSystem:
    """ Provides standard configuration methods. """
    def GetConfig(self, configKey):
        """
        GetConfig(self: IConfigurationSystem, configKey: str) -> object
        
            Gets the specified configuration.
        
            configKey: The configuration key.
            Returns: The object representing the configuration.
        """
        pass

    def Init(self):
        """
        Init(self: IConfigurationSystem)
            Used for initialization.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IdnElement(ConfigurationElement):
    """
    Provides the configuration setting for International Domain Name (IDN) processing in the System.Uri class.
    
    IdnElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the System.Configuration.IdnElement configuration setting.

Get: Enabled(self: IdnElement) -> UriIdnScope

Set: Enabled(self: IdnElement) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IgnoreSectionHandler(object, IConfigurationSectionHandler):
    """
    Provides a legacy section-handler definition for configuration sections that are not handled by the System.Configuration types.
    
    IgnoreSectionHandler()
    """
    def Create(self, parent, configContext, section):
        """
        Create(self: IgnoreSectionHandler, parent: object, configContext: object, section: XmlNode) -> object
        
            Creates a new configuration handler and adds the specified configuration object to the 
             section-handler collection.
        
        
            parent: The configuration settings in a corresponding parent configuration section.
            configContext: The virtual path for which the configuration section handler computes configuration values. 
             Normally this parameter is reserved and is null.
        
            section: An System.Xml.XmlNode that contains the configuration information to be handled. Provides direct 
             access to the XML contents of the configuration section.
        
            Returns: The created configuration handler object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IPersistComponentSettings:
    """ Defines standard functionality for controls or libraries that store and retrieve application settings. """
    def LoadComponentSettings(self):
        """
        LoadComponentSettings(self: IPersistComponentSettings)
            Reads the control's application settings into their corresponding properties and updates the 
             control's state.
        """
        pass

    def ResetComponentSettings(self):
        """
        ResetComponentSettings(self: IPersistComponentSettings)
            Resets the control's application settings properties to their default values.
        """
        pass

    def SaveComponentSettings(self):
        """
        SaveComponentSettings(self: IPersistComponentSettings)
            Persists the control's application settings properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SaveSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the control should automatically persist its application settings properties.

Get: SaveSettings(self: IPersistComponentSettings) -> bool

Set: SaveSettings(self: IPersistComponentSettings) = value
"""

    SettingsKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the application settings key for the current instance of the control.

Get: SettingsKey(self: IPersistComponentSettings) -> str

Set: SettingsKey(self: IPersistComponentSettings) = value
"""



class IriParsingElement(ConfigurationElement):
    """
    Provides the configuration setting for International Resource Identifier (IRI) processing in the System.Uri class.
    
    IriParsingElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the System.Configuration.IriParsingElement configuration setting.

Get: Enabled(self: IriParsingElement) -> bool

Set: Enabled(self: IriParsingElement) = value
"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ISettingsProviderService:
    """ Provides an interface for defining an alternate application settings provider. """
    def GetSettingsProvider(self, property):
        """
        GetSettingsProvider(self: ISettingsProviderService, property: SettingsProperty) -> SettingsProvider
        
            Returns the settings provider compatible with the specified settings property.
        
            property: The System.Configuration.SettingsProperty that requires serialization.
            Returns: If found, the System.Configuration.SettingsProvider that can persist the specified settings 
             property; otherwise, null.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SettingsProvider(ProviderBase):
    """ Acts as a base class for deriving custom settings providers in the application settings architecture. """
    def GetPropertyValues(self, context, collection):
        """
        GetPropertyValues(self: SettingsProvider, context: SettingsContext, collection: SettingsPropertyCollection) -> SettingsPropertyValueCollection
        
            Returns the collection of settings property values for the specified application instance and 
             settings property group.
        
        
            context: A System.Configuration.SettingsContext describing the current application use.
            collection: A System.Configuration.SettingsPropertyCollection containing the settings property group whose 
             values are to be retrieved.
        
            Returns: A System.Configuration.SettingsPropertyValueCollection containing the values for the specified 
             settings property group.
        """
        pass

    def SetPropertyValues(self, context, collection):
        """
        SetPropertyValues(self: SettingsProvider, context: SettingsContext, collection: SettingsPropertyValueCollection)
            Sets the values of the specified group of property settings.
        
            context: A System.Configuration.SettingsContext describing the current application usage.
            collection: A System.Configuration.SettingsPropertyValueCollection representing the group of property 
             settings to set.
        """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the currently running application.

Get: ApplicationName(self: SettingsProvider) -> str

Set: ApplicationName(self: SettingsProvider) = value
"""



class LocalFileSettingsProvider(SettingsProvider, IApplicationSettingsProvider):
    """
    Provides persistence for application settings classes.
    
    LocalFileSettingsProvider()
    """
    def GetPreviousVersion(self, context, property):
        """
        GetPreviousVersion(self: LocalFileSettingsProvider, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue
        
            Returns the value of the named settings property for the previous version of the same 
             application.
        
        
            context: A System.Configuration.SettingsContext that describes where the application settings property is 
             used.
        
            property: The System.Configuration.SettingsProperty whose value is to be returned.
            Returns: A System.Configuration.SettingsPropertyValue representing the application setting if found; 
             otherwise, null.
        """
        pass

    def GetPropertyValues(self, context, properties):
        """
        GetPropertyValues(self: LocalFileSettingsProvider, context: SettingsContext, properties: SettingsPropertyCollection) -> SettingsPropertyValueCollection
        
            Returns the collection of setting property values for the specified application instance and 
             settings property group.
        
        
            context: A System.Configuration.SettingsContext describing the current application usage.
            properties: A System.Configuration.SettingsPropertyCollection containing the settings property group whose 
             values are to be retrieved.
        
            Returns: A System.Configuration.SettingsPropertyValueCollection containing the values for the specified 
             settings property group.
        """
        pass

    def Initialize(self, name, values):
        """
        Initialize(self: LocalFileSettingsProvider, name: str, values: NameValueCollection)
            name: The name of the provider.
            values: The values for initialization.
        """
        pass

    def Reset(self, context):
        """
        Reset(self: LocalFileSettingsProvider, context: SettingsContext)
            Resets all application settings properties associated with the specified application to their 
             default values.
        
        
            context: A System.Configuration.SettingsContext describing the current application usage.
        """
        pass

    def SetPropertyValues(self, context, values):
        """
        SetPropertyValues(self: LocalFileSettingsProvider, context: SettingsContext, values: SettingsPropertyValueCollection)
            Sets the values of the specified group of property settings.
        
            context: A System.Configuration.SettingsContext describing the current application usage.
            values: A System.Configuration.SettingsPropertyValueCollection representing the group of property 
             settings to set.
        """
        pass

    def Upgrade(self, context, properties):
        """
        Upgrade(self: LocalFileSettingsProvider, context: SettingsContext, properties: SettingsPropertyCollection)
            Attempts to migrate previous user-scoped settings from a previous version of the same 
             application.
        
        
            context: A System.Configuration.SettingsContext describing the current application usage.
            properties: A System.Configuration.SettingsPropertyCollection containing the settings property group whose 
             values are to be retrieved.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ApplicationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the currently running application.

Get: ApplicationName(self: LocalFileSettingsProvider) -> str

Set: ApplicationName(self: LocalFileSettingsProvider) = value
"""



class NameValueFileSectionHandler(object, IConfigurationSectionHandler):
    """
    Provides access to a configuration file. This type supports the .NET Framework configuration infrastructure and is not intended to be used directly from your code.
    
    NameValueFileSectionHandler()
    """
    def Create(self, parent, configContext, section):
        """
        Create(self: NameValueFileSectionHandler, parent: object, configContext: object, section: XmlNode) -> object
        
            Creates a new configuration handler and adds it to the section-handler collection based on the 
             specified parameters.
        
        
            parent: The parent object.
            configContext: The configuration context object.
            section: The section XML node.
            Returns: A configuration object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class NameValueSectionHandler(object, IConfigurationSectionHandler):
    """
    Provides name/value-pair configuration information from a configuration section.
    
    NameValueSectionHandler()
    """
    def Create(self, parent, context, section):
        """
        Create(self: NameValueSectionHandler, parent: object, context: object, section: XmlNode) -> object
        
            Creates a new configuration handler and adds it to the section-handler collection based on the 
             specified parameters.
        
        
            parent: Parent object.
            context: Configuration context object.
            section: Section XML node.
            Returns: A configuration object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    KeyAttributeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the XML attribute name to use as the key in a key/value pair.

"""

    ValueAttributeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the XML attribute name to use as the value in a key/value pair.

"""



class NoSettingsVersionUpgradeAttribute(Attribute, _Attribute):
    """
    Specifies that a settings provider should disable any logic that gets invoked when an application upgrade is detected. This class cannot be inherited.
    
    NoSettingsVersionUpgradeAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SchemeSettingElement(ConfigurationElement):
    """
    Represents an element in a System.Configuration.SchemeSettingElementCollection class.
    
    SchemeSettingElement()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    GenericUriParserOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the GenericUriParserOptions entry from a System.Configuration.SchemeSettingElement instance.

Get: GenericUriParserOptions(self: SchemeSettingElement) -> GenericUriParserOptions

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the Name entry from a System.Configuration.SchemeSettingElement instance.

Get: Name(self: SchemeSettingElement) -> str

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SchemeSettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    Represents a collection of System.Configuration.SchemeSettingElement objects.
    
    SchemeSettingElementCollection()
    """
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

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: SchemeSettingElementCollection) -> ConfigurationElement
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
        """ GetElementKey(self: SchemeSettingElementCollection, element: ConfigurationElement) -> object """
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
        IndexOf(self: SchemeSettingElementCollection, element: SchemeSettingElement) -> int
        
            The index of the specified System.Configuration.SchemeSettingElement.
        
            element: The System.Configuration.SchemeSettingElement for the specified index location.
            Returns: The index of the specified System.Configuration.SchemeSettingElement; otherwise, -1.
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

    def set_Item(self, *args): #cannot find CLR method
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

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    AddElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ClearElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    CollectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default collection type of System.Configuration.SchemeSettingElementCollection.

Get: CollectionType(self: SchemeSettingElementCollection) -> ConfigurationElementCollectionType

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



class SettingChangingEventArgs(CancelEventArgs):
    """
    Provides data for the System.Configuration.ApplicationSettingsBase.SettingChanging event.
    
    SettingChangingEventArgs(settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, settingName, settingClass, settingKey, newValue, cancel):
        """ __new__(cls: type, settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool) """
        pass

    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new value being assigned to the application settings property.

Get: NewValue(self: SettingChangingEventArgs) -> object

"""

    SettingClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the application settings property category.

Get: SettingClass(self: SettingChangingEventArgs) -> str

"""

    SettingKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the application settings key associated with the property.

Get: SettingKey(self: SettingChangingEventArgs) -> str

"""

    SettingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the application setting associated with the application settings property.

Get: SettingName(self: SettingChangingEventArgs) -> str

"""



class SettingChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Configuration.ApplicationSettingsBase.SettingChanging event.
    
    SettingChangingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SettingChangingEventHandler, sender: object, e: SettingChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SettingChangingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SettingChangingEventHandler, sender: object, e: SettingChangingEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SettingElement(ConfigurationElement):
    """
    Represents a simplified configuration element used for updating elements in the configuration. This class cannot be inherited.
    
    SettingElement()
    SettingElement(name: str, serializeAs: SettingsSerializeAs)
    """
    def Equals(self, settings):
        """
        Equals(self: SettingElement, settings: object) -> bool
        
            Compares the current System.Configuration.SettingElement instance to the specified object.
        
            settings: The object to compare with.
            Returns: true if the System.Configuration.SettingElement instance is equal to the specified object; 
             otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SettingElement) -> int
        
            Gets a unique value representing the System.Configuration.SettingElement current instance.
            Returns: A unique value representing the System.Configuration.SettingElement current instance.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, serializeAs=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, serializeAs: SettingsSerializeAs)
        """
        pass

    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.SettingElement object.

Get: Name(self: SettingElement) -> str

Set: Name(self: SettingElement) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SerializeAs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the serialization mechanism used to persist the values of the System.Configuration.SettingElement object.

Get: SerializeAs(self: SettingElement) -> SettingsSerializeAs

Set: SerializeAs(self: SettingElement) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of a System.Configuration.SettingElement object by using a System.Configuration.SettingValueElement object.

Get: Value(self: SettingElement) -> SettingValueElement

Set: Value(self: SettingElement) = value
"""



class SettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """
    Contains a collection of System.Configuration.SettingElement objects. This class cannot be inherited.
    
    SettingElementCollection()
    """
    def Add(self, element):
        """
        Add(self: SettingElementCollection, element: SettingElement)
            Adds a System.Configuration.SettingElement object to the collection.
        
            element: The System.Configuration.SettingElement object to add to the collection.
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
        Clear(self: SettingElementCollection)
            Removes all System.Configuration.SettingElement objects from the collection.
        """
        pass

    def CreateNewElement(self, *args): #cannot find CLR method
        """
        CreateNewElement(self: SettingElementCollection) -> ConfigurationElement
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

    def Get(self, elementKey):
        """
        Get(self: SettingElementCollection, elementKey: str) -> SettingElement
        
            Gets a System.Configuration.SettingElement object from the collection.
        
            elementKey: A string value representing the System.Configuration.SettingElement object in the collection.
            Returns: A System.Configuration.SettingElement object.
        """
        pass

    def GetElementKey(self, *args): #cannot find CLR method
        """ GetElementKey(self: SettingElementCollection, element: ConfigurationElement) -> object """
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

    def get_Item(self, *args): #cannot find CLR method
        """
        get_Item(self: ConfigurationElement, propertyName: str) -> object
        get_Item(self: ConfigurationElement, prop: ConfigurationProperty) -> object
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

    def Remove(self, element):
        """
        Remove(self: SettingElementCollection, element: SettingElement)
            Removes a System.Configuration.SettingElement object from the collection.
        
            element: A System.Configuration.SettingElement object.
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

    def set_Item(self, *args): #cannot find CLR method
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    AddElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    ClearElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class.

"""

    CollectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the configuration collection.

Get: CollectionType(self: SettingElementCollection) -> ConfigurationElementCollectionType

"""

    ElementName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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



class SettingsAttributeDictionary(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
    """
    Represents a collection of key/value pairs used to describe a configuration object as well as a System.Configuration.SettingsProperty object.
    
    SettingsAttributeDictionary()
    SettingsAttributeDictionary(attributes: SettingsAttributeDictionary)
    """
    def GetHash(self, *args): #cannot find CLR method
        """
        GetHash(self: Hashtable, key: object) -> int
        
            Returns the hash code for the specified key.
        
            key: The System.Object for which a hash code is to be returned.
            Returns: The hash code for key.
        """
        pass

    def KeyEquals(self, *args): #cannot find CLR method
        """
        KeyEquals(self: Hashtable, item: object, key: object) -> bool
        
            Compares a specific System.Object with a specific key in the System.Collections.Hashtable.
        
            item: The System.Object to compare with key.
            key: The key in the System.Collections.Hashtable to compare with item.
            Returns: true if item and key are equal; otherwise, false.
        """
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

    @staticmethod # known case of __new__
    def __new__(self, attributes=None):
        """
        __new__(cls: type)
        __new__(cls: type, attributes: SettingsAttributeDictionary)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Collections.IComparer to use for the System.Collections.Hashtable.

"""

    EqualityComparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.IEqualityComparer to use for the System.Collections.Hashtable.

"""

    hcp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that can dispense hash codes.

"""



class SettingsContext(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
    """
    Provides contextual information that the provider can use when persisting settings.
    
    SettingsContext()
    """
    def GetHash(self, *args): #cannot find CLR method
        """
        GetHash(self: Hashtable, key: object) -> int
        
            Returns the hash code for the specified key.
        
            key: The System.Object for which a hash code is to be returned.
            Returns: The hash code for key.
        """
        pass

    def KeyEquals(self, *args): #cannot find CLR method
        """
        KeyEquals(self: Hashtable, item: object, key: object) -> bool
        
            Compares a specific System.Object with a specific key in the System.Collections.Hashtable.
        
            item: The System.Object to compare with key.
            key: The key in the System.Collections.Hashtable to compare with item.
            Returns: true if item and key are equal; otherwise, false.
        """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Collections.IComparer to use for the System.Collections.Hashtable.

"""

    EqualityComparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Collections.IEqualityComparer to use for the System.Collections.Hashtable.

"""

    hcp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that can dispense hash codes.

"""



class SettingsDescriptionAttribute(Attribute, _Attribute):
    """
    Provides a string that describes an individual configuration property. This class cannot be inherited.
    
    SettingsDescriptionAttribute(description: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the descriptive text for the associated configuration property.

Get: Description(self: SettingsDescriptionAttribute) -> str

"""



class SettingsGroupDescriptionAttribute(Attribute, _Attribute):
    """
    Provides a string that describes an application settings property group. This class cannot be inherited.
    
    SettingsGroupDescriptionAttribute(description: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The descriptive text for the application settings properties group.

Get: Description(self: SettingsGroupDescriptionAttribute) -> str

"""



class SettingsGroupNameAttribute(Attribute, _Attribute):
    """
    Specifies a name for application settings property group. This class cannot be inherited.
    
    SettingsGroupNameAttribute(groupName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, groupName):
        """ __new__(cls: type, groupName: str) """
        pass

    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the application settings property group.

Get: GroupName(self: SettingsGroupNameAttribute) -> str

"""



class SettingsLoadedEventArgs(EventArgs):
    """
    Provides data for the System.Configuration.ApplicationSettingsBase.SettingsLoaded event.
    
    SettingsLoadedEventArgs(provider: SettingsProvider)
    """
    @staticmethod # known case of __new__
    def __new__(self, provider):
        """ __new__(cls: type, provider: SettingsProvider) """
        pass

    Provider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the settings provider used to store configuration settings.

Get: Provider(self: SettingsLoadedEventArgs) -> SettingsProvider

"""



class SettingsLoadedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Configuration.ApplicationSettingsBase.SettingsLoaded event.
    
    SettingsLoadedEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SettingsLoadedEventHandler, sender: object, e: SettingsLoadedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SettingsLoadedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SettingsLoadedEventHandler, sender: object, e: SettingsLoadedEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SettingsManageability(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides values to indicate which services should be made available to application settings.
    
    enum SettingsManageability, values: Roaming (0)
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

    Roaming = None
    value__ = None


class SettingsManageabilityAttribute(Attribute, _Attribute):
    """
    Specifies special services for application settings properties. This class cannot be inherited.
    
    SettingsManageabilityAttribute(manageability: SettingsManageability)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, manageability):
        """ __new__(cls: type, manageability: SettingsManageability) """
        pass

    Manageability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the set of special services that have been requested.

Get: Manageability(self: SettingsManageabilityAttribute) -> SettingsManageability

"""



class SettingsProperty(object):
    """
    Used internally as the class that represents metadata about an individual configuration property.
    
    SettingsProperty(name: str)
    SettingsProperty(name: str, propertyType: Type, provider: SettingsProvider, isReadOnly: bool, defaultValue: object, serializeAs: SettingsSerializeAs, attributes: SettingsAttributeDictionary, throwOnErrorDeserializing: bool, throwOnErrorSerializing: bool)
    SettingsProperty(propertyToCopy: SettingsProperty)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, propertyType: Type, provider: SettingsProvider, isReadOnly: bool, defaultValue: object, serializeAs: SettingsSerializeAs, attributes: SettingsAttributeDictionary, throwOnErrorDeserializing: bool, throwOnErrorSerializing: bool)
        __new__(cls: type, propertyToCopy: SettingsProperty)
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Configuration.SettingsAttributeDictionary object containing the attributes of the System.Configuration.SettingsProperty object.

Get: Attributes(self: SettingsProperty) -> SettingsAttributeDictionary

"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default value of the System.Configuration.SettingsProperty object.

Get: DefaultValue(self: SettingsProperty) -> object

Set: DefaultValue(self: SettingsProperty) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value specifying whether a System.Configuration.SettingsProperty object is read-only.

Get: IsReadOnly(self: SettingsProperty) -> bool

Set: IsReadOnly(self: SettingsProperty) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the System.Configuration.SettingsProperty.

Get: Name(self: SettingsProperty) -> str

Set: Name(self: SettingsProperty) = value
"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type for the System.Configuration.SettingsProperty.

Get: PropertyType(self: SettingsProperty) -> Type

Set: PropertyType(self: SettingsProperty) = value
"""

    Provider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the provider for the System.Configuration.SettingsProperty.

Get: Provider(self: SettingsProperty) -> SettingsProvider

Set: Provider(self: SettingsProperty) = value
"""

    SerializeAs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Configuration.SettingsSerializeAs object for the System.Configuration.SettingsProperty.

Get: SerializeAs(self: SettingsProperty) -> SettingsSerializeAs

Set: SerializeAs(self: SettingsProperty) = value
"""

    ThrowOnErrorDeserializing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value specifying whether an error will be thrown when the property is unsuccessfully deserialized.

Get: ThrowOnErrorDeserializing(self: SettingsProperty) -> bool

Set: ThrowOnErrorDeserializing(self: SettingsProperty) = value
"""

    ThrowOnErrorSerializing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value specifying whether an error will be thrown when the property is unsuccessfully serialized.

Get: ThrowOnErrorSerializing(self: SettingsProperty) -> bool

Set: ThrowOnErrorSerializing(self: SettingsProperty) = value
"""



class SettingsPropertyCollection(object, IEnumerable, ICloneable, ICollection):
    """
    Contains a collection of System.Configuration.SettingsProperty objects.
    
    SettingsPropertyCollection()
    """
    def Add(self, property):
        """
        Add(self: SettingsPropertyCollection, property: SettingsProperty)
            Adds a System.Configuration.SettingsProperty object to the collection.
        
            property: A System.Configuration.SettingsProperty object.
        """
        pass

    def Clear(self):
        """
        Clear(self: SettingsPropertyCollection)
            Removes all System.Configuration.SettingsProperty objects from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: SettingsPropertyCollection) -> object
        
            Creates a copy of the existing collection.
            Returns: A System.Configuration.SettingsPropertyCollection class.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: SettingsPropertyCollection, array: Array, index: int)
            Copies this System.Configuration.SettingsPropertyCollection object to an array.
        
            array: The array to copy the object to.
            index: The index at which to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SettingsPropertyCollection) -> IEnumerator
        
            Gets the System.Collections.IEnumerator object as it applies to the collection.
            Returns: The System.Collections.IEnumerator object as it applies to the collection.
        """
        pass

    def OnAdd(self, *args): #cannot find CLR method
        """
        OnAdd(self: SettingsPropertyCollection, property: SettingsProperty)
            Performs additional, custom processing when adding to the contents of the 
             System.Configuration.SettingsPropertyCollection instance.
        
        
            property: A System.Configuration.SettingsProperty object.
        """
        pass

    def OnAddComplete(self, *args): #cannot find CLR method
        """
        OnAddComplete(self: SettingsPropertyCollection, property: SettingsProperty)
            Performs additional, custom processing after adding to the contents of the 
             System.Configuration.SettingsPropertyCollection instance.
        
        
            property: A System.Configuration.SettingsProperty object.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: SettingsPropertyCollection)
            Performs additional, custom processing when clearing the contents of the 
             System.Configuration.SettingsPropertyCollection instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: SettingsPropertyCollection)
            Performs additional, custom processing after clearing the contents of the 
             System.Configuration.SettingsPropertyCollection instance.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: SettingsPropertyCollection, property: SettingsProperty)
            Performs additional, custom processing when removing the contents of the 
             System.Configuration.SettingsPropertyCollection instance.
        
        
            property: A System.Configuration.SettingsProperty object.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: SettingsPropertyCollection, property: SettingsProperty)
            Performs additional, custom processing after removing the contents of the 
             System.Configuration.SettingsPropertyCollection instance.
        
        
            property: A System.Configuration.SettingsProperty object.
        """
        pass

    def Remove(self, name):
        """
        Remove(self: SettingsPropertyCollection, name: str)
            Removes a System.Configuration.SettingsProperty object from the collection.
        
            name: The name of the System.Configuration.SettingsProperty object.
        """
        pass

    def SetReadOnly(self):
        """
        SetReadOnly(self: SettingsPropertyCollection)
            Sets the collection to be read-only.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies the number of System.Configuration.SettingsProperty objects in the collection.

Get: Count(self: SettingsPropertyCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the collection is synchronized (thread safe).

Get: IsSynchronized(self: SettingsPropertyCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object to synchronize access to the collection.

Get: SyncRoot(self: SettingsPropertyCollection) -> object

"""



class SettingsPropertyIsReadOnlyException(Exception, ISerializable, _Exception):
    """
    Provides an exception for read-only System.Configuration.SettingsProperty objects.
    
    SettingsPropertyIsReadOnlyException(message: str)
    SettingsPropertyIsReadOnlyException(message: str, innerException: Exception)
    SettingsPropertyIsReadOnlyException()
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class SettingsPropertyNotFoundException(Exception, ISerializable, _Exception):
    """
    Provides an exception for System.Configuration.SettingsProperty objects that are not found.
    
    SettingsPropertyNotFoundException(message: str)
    SettingsPropertyNotFoundException(message: str, innerException: Exception)
    SettingsPropertyNotFoundException()
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class SettingsPropertyValue(object):
    """
    Contains the value of a settings property that can be loaded and stored by an instance of System.Configuration.SettingsBase.
    
    SettingsPropertyValue(property: SettingsProperty)
    """
    @staticmethod # known case of __new__
    def __new__(self, property):
        """ __new__(cls: type, property: SettingsProperty) """
        pass

    Deserialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the value of a System.Configuration.SettingsProperty object has been deserialized.

Get: Deserialized(self: SettingsPropertyValue) -> bool

Set: Deserialized(self: SettingsPropertyValue) = value
"""

    IsDirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the value of a System.Configuration.SettingsProperty object has changed.

Get: IsDirty(self: SettingsPropertyValue) -> bool

Set: IsDirty(self: SettingsPropertyValue) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property from the associated System.Configuration.SettingsProperty object.

Get: Name(self: SettingsPropertyValue) -> str

"""

    Property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.SettingsProperty object.

Get: Property(self: SettingsPropertyValue) -> SettingsProperty

"""

    PropertyValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the System.Configuration.SettingsProperty object.

Get: PropertyValue(self: SettingsPropertyValue) -> object

Set: PropertyValue(self: SettingsPropertyValue) = value
"""

    SerializedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the serialized value of the System.Configuration.SettingsProperty object.

Get: SerializedValue(self: SettingsPropertyValue) -> object

Set: SerializedValue(self: SettingsPropertyValue) = value
"""

    UsingDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a Boolean value specifying whether the value of the System.Configuration.SettingsPropertyValue object is the default value as defined by the System.Configuration.SettingsProperty.DefaultValue property value on the associated System.Configuration.SettingsProperty object.

Get: UsingDefaultValue(self: SettingsPropertyValue) -> bool

"""



class SettingsPropertyValueCollection(object, IEnumerable, ICloneable, ICollection):
    """
    Contains a collection of settings property values that map System.Configuration.SettingsProperty objects to System.Configuration.SettingsPropertyValue objects.
    
    SettingsPropertyValueCollection()
    """
    def Add(self, property):
        """
        Add(self: SettingsPropertyValueCollection, property: SettingsPropertyValue)
            Adds a System.Configuration.SettingsPropertyValue object to the collection.
        
            property: A System.Configuration.SettingsPropertyValue object.
        """
        pass

    def Clear(self):
        """
        Clear(self: SettingsPropertyValueCollection)
            Removes all System.Configuration.SettingsPropertyValue objects from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: SettingsPropertyValueCollection) -> object
        
            Creates a copy of the existing collection.
            Returns: A System.Configuration.SettingsPropertyValueCollection class.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: SettingsPropertyValueCollection, array: Array, index: int)
            Copies this System.Configuration.SettingsPropertyValueCollection collection to an array.
        
            array: The array to copy the collection to.
            index: The index at which to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SettingsPropertyValueCollection) -> IEnumerator
        
            Gets the System.Collections.IEnumerator object as it applies to the collection.
            Returns: The System.Collections.IEnumerator object as it applies to the collection.
        """
        pass

    def Remove(self, name):
        """
        Remove(self: SettingsPropertyValueCollection, name: str)
            Removes a System.Configuration.SettingsPropertyValue object from the collection.
        
            name: The name of the System.Configuration.SettingsPropertyValue object.
        """
        pass

    def SetReadOnly(self):
        """
        SetReadOnly(self: SettingsPropertyValueCollection)
            Sets the collection to be read-only.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies the number of System.Configuration.SettingsPropertyValue objects in the collection.

Get: Count(self: SettingsPropertyValueCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the collection is synchronized (thread safe).

Get: IsSynchronized(self: SettingsPropertyValueCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object to synchronize access to the collection.

Get: SyncRoot(self: SettingsPropertyValueCollection) -> object

"""



class SettingsPropertyWrongTypeException(Exception, ISerializable, _Exception):
    """
    Provides an exception that is thrown when an invalid type is used with a System.Configuration.SettingsProperty object.
    
    SettingsPropertyWrongTypeException(message: str)
    SettingsPropertyWrongTypeException(message: str, innerException: Exception)
    SettingsPropertyWrongTypeException()
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
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class SettingsProviderAttribute(Attribute, _Attribute):
    """
    Specifies the settings provider used to provide storage for the current application settings class or property. This class cannot be inherited.
    
    SettingsProviderAttribute(providerTypeName: str)
    SettingsProviderAttribute(providerType: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, providerTypeName: str)
        __new__(cls: type, providerType: Type)
        """
        pass

    ProviderTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type name of the settings provider.

Get: ProviderTypeName(self: SettingsProviderAttribute) -> str

"""



class SettingsProviderCollection(ProviderCollection, IEnumerable, ICollection):
    """
    Represents a collection of application settings providers.
    
    SettingsProviderCollection()
    """
    def Add(self, provider):
        """
        Add(self: SettingsProviderCollection, provider: ProviderBase)
            Adds a new settings provider to the collection.
        
            provider: A System.Configuration.Provider.ProviderBase to add to the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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


class SettingsSavingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Configuration.ApplicationSettingsBase.SettingsSaving event.
    
    SettingsSavingEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: SettingsSavingEventHandler, sender: object, e: CancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SettingsSavingEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SettingsSavingEventHandler, sender: object, e: CancelEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SettingsSerializeAs(Enum, IComparable, IFormattable, IConvertible):
    """
    Determines the serialization scheme used to store application settings.
    
    enum SettingsSerializeAs, values: Binary (2), ProviderSpecific (3), String (0), Xml (1)
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

    Binary = None
    ProviderSpecific = None
    String = None
    value__ = None
    Xml = None


class SettingsSerializeAsAttribute(Attribute, _Attribute):
    """
    Specifies the serialization mechanism that the settings provider should use. This class cannot be inherited.
    
    SettingsSerializeAsAttribute(serializeAs: SettingsSerializeAs)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, serializeAs):
        """ __new__(cls: type, serializeAs: SettingsSerializeAs) """
        pass

    SerializeAs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.SettingsSerializeAs enumeration value that specifies the serialization scheme.

Get: SerializeAs(self: SettingsSerializeAsAttribute) -> SettingsSerializeAs

"""



class SettingValueElement(ConfigurationElement):
    """
    Contains the XML representing the serialized value of the setting. This class cannot be inherited.
    
    SettingValueElement()
    """
    def Equals(self, settingValue):
        """
        Equals(self: SettingValueElement, settingValue: object) -> bool
        
            Compares the current System.Configuration.SettingValueElement instance to the specified object.
        
            settingValue: The object to compare.
            Returns: true if the System.Configuration.SettingValueElement instance is equal to the specified object; 
             otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SettingValueElement) -> int
        
            Gets a unique value representing the System.Configuration.SettingValueElement current instance.
            Returns: A unique value representing the System.Configuration.SettingValueElement current instance.
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

    ValueXml = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of a System.Configuration.SettingValueElement object by using an System.Xml.XmlNode object.

Get: ValueXml(self: SettingValueElement) -> XmlNode

Set: ValueXml(self: SettingValueElement) = value
"""



class SingleTagSectionHandler(object, IConfigurationSectionHandler):
    """
    Handles configuration sections that are represented by a single XML tag in the .config file.
    
    SingleTagSectionHandler()
    """
    def Create(self, parent, context, section):
        """
        Create(self: SingleTagSectionHandler, parent: object, context: object, section: XmlNode) -> object
        
            Used internally to create a new instance of this object.
        
            parent: The parent of this object.
            context: The context of this object.
            section: The System.Xml.XmlNode object in the configuration.
            Returns: The created object handler.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SpecialSetting(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the special setting category of a application settings property.
    
    enum SpecialSetting, values: ConnectionString (0), WebServiceUrl (1)
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

    ConnectionString = None
    value__ = None
    WebServiceUrl = None


class SpecialSettingAttribute(Attribute, _Attribute):
    """
    Indicates that an application settings property has a special significance. This class cannot be inherited.
    
    SpecialSettingAttribute(specialSetting: SpecialSetting)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, specialSetting):
        """ __new__(cls: type, specialSetting: SpecialSetting) """
        pass

    SpecialSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value describing the special setting category of the application settings property.

Get: SpecialSetting(self: SpecialSettingAttribute) -> SpecialSetting

"""



class UriSection(ConfigurationSection):
    """
    Represents the Uri section within a configuration file.
    
    UriSection()
    """
    ElementProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself.

"""

    EvaluationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object.

"""

    HasContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Idn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Configuration.IdnElement object that contains the configuration setting for International Domain Name (IDN) processing in the System.Uri class.

Get: Idn(self: UriSection) -> IdnElement

"""

    IriParsing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Configuration.IriParsingElement object that contains the configuration setting for International Resource Identifiers (IRI) parsing in the System.Uri class.

Get: IriParsing(self: UriSection) -> IriParsingElement

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SchemeSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Configuration.SchemeSettingElementCollection object that contains the configuration settings for scheme parsing in the System.Uri class.

Get: SchemeSettings(self: UriSection) -> SchemeSettingElementCollection

"""



class UserScopedSettingAttribute(SettingAttribute, _Attribute):
    """
    Specifies that an application settings group or property contains distinct values for each user of an application. This class cannot be inherited.
    
    UserScopedSettingAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UserSettingsGroup(ConfigurationSectionGroup):
    """
    Represents a grouping of related user settings sections within a configuration file. This class cannot be inherited.
    
    UserSettingsGroup()
    """

# variables with complex values

