# encoding: utf-8
# module System.Windows.Markup calls itself Markup
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ComponentResourceKeyConverter(ExpressionConverter):
    """
    Implements a type converter for System.Windows.ComponentResourceKey objects, which deliberately have no type conversion pathways. The type converter enforces and reports that behavior.
    
    ComponentResourceKeyConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ComponentResourceKeyConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.ComponentResourceKey, using the specified context. Always returns false.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: false in all cases.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ComponentResourceKeyConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.ComponentResourceKey can be converted to the specified type, using the specified context. Always returns false.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: false in all cases.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ComponentResourceKeyConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Attempts to convert the specified object to a System.Windows.ComponentResourceKey, using the specified context. Throws an exception in all cases.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            Returns: Throws an exception in all cases.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ComponentResourceKeyConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.ComponentResourceKey to the specified type, using the specified context. Throws an exception in all cases.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: Throws an exception in all cases.
        """
        pass


class DependencyPropertyConverter(TypeConverter):
    """
    Converts from a string to a System.Windows.DependencyProperty object.
    
    DependencyPropertyConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: DependencyPropertyConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.DependencyProperty.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: DependencyPropertyConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.DependencyProperty can be converted to the specified type.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: DependencyPropertyConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.DependencyProperty, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: The converted object. If the conversion is successful, this is a System.Windows.DependencyProperty.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: DependencyPropertyConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.DependencyProperty to the specified type, using the specified context. Always throws an exception.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: Always throws an exception.
        """
        pass


class DesignerSerializationOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how a property is to be serialized.
    
    enum (flags) DesignerSerializationOptions, values: SerializeAsAttribute (1)
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

    SerializeAsAttribute = None
    value__ = None


class DesignerSerializationOptionsAttribute(Attribute, _Attribute):
    """
    Specifies the serialization flags for a property.
    
    DesignerSerializationOptionsAttribute(designerSerializationOptions: DesignerSerializationOptions)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, designerSerializationOptions):
        """ __new__(cls: type, designerSerializationOptions: DesignerSerializationOptions) """
        pass

    DesignerSerializationOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Markup.DesignerSerializationOptions set on the attribute.

Get: DesignerSerializationOptions(self: DesignerSerializationOptionsAttribute) -> DesignerSerializationOptions

"""



class EventSetterHandlerConverter(TypeConverter):
    """
    Converts the string name of an event setter handler to a delegate representation.
    
    EventSetterHandlerConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: EventSetterHandlerConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns whether this converter can convert an object of one type to a System.Delegate.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A System.Type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: EventSetterHandlerConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: A System.Type that represents the type you want to convert to.
            Returns: Always returns false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: EventSetterHandlerConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            Converts the specified string to a new System.Delegate for the event handler.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            cultureInfo: The System.Globalization.CultureInfo to use as the current culture.
            source: The source string to convert.
            Returns: A new System.Delegate that represents the referenced event handler.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: EventSetterHandlerConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified value object to the specified type. Always throws an exception.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            cultureInfo: The System.Globalization.CultureInfo to use as the current culture.
            value: The value to convert.
            destinationType: The type to convert the value parameter to.
            Returns: Always throws an exception.
        """
        pass


class IAddChild:
    """ Provides a means to parse elements that permit mixtures of child elements or text. """
    def AddChild(self, value):
        """
        AddChild(self: IAddChild, value: object)
            Adds a child object.
        
            value: The child object to add.
        """
        pass

    def AddText(self, text):
        """
        AddText(self: IAddChild, text: str)
            Adds the text content of a node to the object.
        
            text: The text to add to the object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InternalTypeHelper(object):
    """ Abstract class used internally by the WPF XAML compiler to support the use of internal types. """
    def AddEventHandler(self, *args): #cannot find CLR method
        """
        AddEventHandler(self: InternalTypeHelper, eventInfo: EventInfo, target: object, handler: Delegate)
            When overridden in a derived (generated) class, attaches an event handler delegate to an internal event.
        
            eventInfo: The event information for the event (CLR reflection information).
            target: The target where the handler is attached.
            handler: The event handler.
        """
        pass

    def CreateDelegate(self, *args): #cannot find CLR method
        """
        CreateDelegate(self: InternalTypeHelper, delegateType: Type, target: object, handler: str) -> Delegate
        
            When overridden in a derived (generated) class, creates an event delegate referencing a non-public handler method.
        
            delegateType: The System.Type of the delegate.
            target: The target where the handler is attached.
            handler: The name of the handler implementation.
            Returns: The delegate reference.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: InternalTypeHelper, type: Type, culture: CultureInfo) -> object
        
            When overridden in a derived (generated) class, creates an instance of an internal type.
        
            type: The System.Type to create.
            culture: Culture specific information.
            Returns: The created instance.
        """
        pass

    def GetPropertyValue(self, *args): #cannot find CLR method
        """
        GetPropertyValue(self: InternalTypeHelper, propertyInfo: PropertyInfo, target: object, culture: CultureInfo) -> object
        
            When overridden in a derived (generated) class, gets the value of an internal property on the target object
        
            propertyInfo: Property information for the property to get.
            target: The object that holds the desired property value.
            culture: Culture specific information.
            Returns: The value of the property.
        """
        pass

    def SetPropertyValue(self, *args): #cannot find CLR method
        """
        SetPropertyValue(self: InternalTypeHelper, propertyInfo: PropertyInfo, target: object, value: object, culture: CultureInfo)
            When overridden in a derived (generated) class, sets the value on an internal property on the target object.
        
            propertyInfo: Property information for the property to set.
            target: The object that holds the desired property value.
            value: The value to set.
            culture: Culture specific information.
        """
        pass


class IReceiveMarkupExtension:
    """ Provides a mechanism whereby types can declare that they can receive an expression (or another class) from a markup extension, where the output is a different property type than the target property. Do not use for .NET Framework�4 implementations; see Remarks. """
    def ReceiveMarkupExtension(self, property, markupExtension, serviceProvider):
        """
        ReceiveMarkupExtension(self: IReceiveMarkupExtension, property: str, markupExtension: MarkupExtension, serviceProvider: IServiceProvider)
            Provides the handling for markup extensions that provide property values. Do not use for .NET Framework�4 implementations; see Remarks in System.Windows.Markup.IReceiveMarkupExtension.
        
            property: The name of the target property.
            markupExtension: The markup extension instance of the incoming data.
            serviceProvider: Can provide additional services that should be performed when processing the markup extension data for a property value.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStyleConnector:
    """ Provides methods used internally by the WPF XAML parser to attach events and event setters in compiled XAML. """
    def Connect(self, connectionId, target):
        """
        Connect(self: IStyleConnector, connectionId: int, target: object)
            Attaches events on event setters and templates in compiled content.
        
            connectionId: The unique connection ID for event wiring purposes.
            target: The target for event wiring.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class NamespaceMapEntry(object):
    """
    Provides information that the System.Windows.Markup.XamlTypeMapper uses for mapping between an XML namespace, a CLR namespace, and the assembly that contains the relevant types for that CLR namespace.
    
    NamespaceMapEntry()
    NamespaceMapEntry(xmlNamespace: str, assemblyName: str, clrNamespace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, xmlNamespace=None, assemblyName=None, clrNamespace=None):
        """
        __new__(cls: type)
        __new__(cls: type, xmlNamespace: str, assemblyName: str, clrNamespace: str)
        """
        pass

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the assembly name that contains the types in the CLR namespace.

Get: AssemblyName(self: NamespaceMapEntry) -> str

Set: AssemblyName(self: NamespaceMapEntry) = value
"""

    ClrNamespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the CLR namespace that contains the types being mapped.

Get: ClrNamespace(self: NamespaceMapEntry) -> str

Set: ClrNamespace(self: NamespaceMapEntry) = value
"""

    XmlNamespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the mapping prefix for the XML namespace being mapped to.

Get: XmlNamespace(self: NamespaceMapEntry) -> str

Set: XmlNamespace(self: NamespaceMapEntry) = value
"""



class ParserContext(object, IUriContext):
    """
    Provides context information required by a XAML parser.
    
    ParserContext()
    ParserContext(xmlParserContext: XmlParserContext)
    """
    @staticmethod
    def ToXmlParserContext(parserContext):
        """
        ToXmlParserContext(parserContext: ParserContext) -> XmlParserContext
        
            Converts an System.Windows.Markup.ParserContext to an System.Xml.XmlParserContext.
        
            parserContext: The context to convert to an System.Xml.XmlParserContext.
            Returns: The XML parser context.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, xmlParserContext=None):
        """
        __new__(cls: type)
        __new__(cls: type, xmlParserContext: XmlParserContext)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the base URI for this context.

Get: BaseUri(self: ParserContext) -> Uri

Set: BaseUri(self: ParserContext) = value
"""

    XamlTypeMapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Markup.XamlTypeMapper to use with this System.Windows.Markup.ParserContext.

Get: XamlTypeMapper(self: ParserContext) -> XamlTypeMapper

Set: XamlTypeMapper(self: ParserContext) = value
"""

    XmlLang = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the xml:lang string for this context.

Get: XmlLang(self: ParserContext) -> str

Set: XmlLang(self: ParserContext) = value
"""

    XmlnsDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the XAML namespace dictionary for this XAML parser context.

Get: XmlnsDictionary(self: ParserContext) -> XmlnsDictionary

"""

    XmlSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the character for xml:space or this context.

Get: XmlSpace(self: ParserContext) -> str

Set: XmlSpace(self: ParserContext) = value
"""



class ResourceReferenceExpressionConverter(ExpressionConverter):
    """
    Converts instances of ResourceReferenceExpression to and from other types.
    
    ResourceReferenceExpressionConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: ResourceReferenceExpressionConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns a value that indicates whether the converter can convert from a source object to a ResourceReferenceExpression object.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: The type to convert from.
            Returns: true if the converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: ResourceReferenceExpressionConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns a value that indicates whether the converter can convert a ResourceReferenceExpression object to the specified destination type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: The type to convert to.
            Returns: true if the converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: ResourceReferenceExpressionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object
        
            Converts the specified value to the ResourceReferenceExpression type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The object to convert.
            Returns: The converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: ResourceReferenceExpressionConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified ResourceReferenceExpression object to the specified type.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The object to convert.
            destinationType: The type to convert to.
            Returns: The converted value.
        """
        pass


class RoutedEventConverter(TypeConverter):
    """
    Converts a System.Windows.RoutedEvent object from a string.
    
    RoutedEventConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: RoutedEventConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.RoutedEvent.
        
            typeDescriptorContext: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: true if this converter can perform the operation; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: RoutedEventConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.RoutedEvent can be converted to the specified type.
        
            typeDescriptorContext: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: Always returns false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: RoutedEventConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object to a System.Windows.RoutedEvent object, using the specified context.
        
            typeDescriptorContext: A format context that provides information about the environment from which this converter is being invoked.
            cultureInfo: Culture specific information.
            source: The object to convert.
            Returns: The conversion result.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: RoutedEventConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.RoutedEvent to the specified type. Throws an exception in all cases.
        
            typeDescriptorContext: A format context that provides information about the environment from which this converter is being invoked.
            cultureInfo: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: Always throws an exception.
        """
        pass


class ServiceProviders(object, IServiceProvider):
    """
    Provides an implementation for the System.IServiceProvider interface with methods that enable adding services.
    
    ServiceProviders()
    """
    def AddService(self, serviceType, service):
        """
        AddService(self: ServiceProviders, serviceType: Type, service: object)
            Adds a service to the list.
        
            serviceType: Service type of the new service.
            service: The service implementation class.
        """
        pass

    def GetService(self, serviceType):
        """
        GetService(self: ServiceProviders, serviceType: Type) -> object
        
            Gets the service object of the specified type.
        
            serviceType: The type of service object to get.
            Returns: A service implementation for the type serviceType. May be null if there is no service stored for type serviceType.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SetterTriggerConditionValueConverter(TypeConverter):
    """
    Provides type conversion analogous behavior for System.Windows.Setter, System.Windows.Trigger and System.Windows.Condition types that deal with System.Windows.DependencyProperty values. This converter only supports ConvertFrom.
    
    SetterTriggerConditionValueConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: SetterTriggerConditionValueConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns a value that indicates whether the converter can convert from a source object to a side-effect-produced System.Windows.Setter, System.Windows.Trigger or System.Windows.Condition .
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: The type to convert from.
            Returns: true if the converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: SetterTriggerConditionValueConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns a value that indicates whether the converter can convert to the specified destination type. Always returns false.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: The type to convert to.
            Returns: Always returns false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: SetterTriggerConditionValueConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Converts the converted source value if an underlying type converter can be obtained from context. Otherwise returns an unconverted source.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            source: The object to convert.
            Returns: The converter object, or possibly an unconverted source.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: SetterTriggerConditionValueConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified object to the specified type. Always throws an exception.
        
            context: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            culture: The System.Globalization.CultureInfo to use as the current culture.
            value: The object to convert.
            destinationType: The type to convert to.
            Returns: Always throws an exception.
        """
        pass


class TemplateKeyConverter(TypeConverter):
    """
    Implements a type converter for System.Windows.TemplateKey objects, which deliberately have no type conversion pathways. The type converter enforces and reports that behavior.
    
    TemplateKeyConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: TemplateKeyConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Determines whether an object of the specified type can be converted to an instance of System.Windows.TemplateKey.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            sourceType: The type being evaluated for conversion.
            Returns: Always returns false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: TemplateKeyConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Determines whether an instance of System.Windows.TemplateKey can be converted to the specified type.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            destinationType: The type being evaluated for conversion.
            Returns: Always returns false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: TemplateKeyConverter, context: ITypeDescriptorContext, culture: CultureInfo, source: object) -> object
        
            Attempts to convert the specified object (string) to a System.Windows.TemplateKey.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            source: The object to convert.
            Returns: Always throws an exception.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: TemplateKeyConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object
        
            Attempts to convert a System.Windows.TemplateKey to the specified type, using the specified context.
        
            context: A format context that provides information about the environment from which this converter is being invoked.
            culture: Culture specific information.
            value: The object to convert.
            destinationType: The type to convert the object to.
            Returns: Always throws an exception.
        """
        pass


class ValueSerializerAttribute(Attribute, _Attribute):
    """
    ValueSerializerAttribute(valueSerializerType: Type)
    ValueSerializerAttribute(valueSerializerTypeName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, valueSerializerType: Type)
        __new__(cls: type, valueSerializerTypeName: str)
        """
        pass

    ValueSerializerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueSerializerType(self: ValueSerializerAttribute) -> Type

"""

    ValueSerializerTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueSerializerTypeName(self: ValueSerializerAttribute) -> str

"""



class XamlDesignerSerializationManager(ServiceProviders, IServiceProvider):
    """
    Provides services for XAML serialization by XAML designers or other callers that require advanced serialization.
    
    XamlDesignerSerializationManager(xmlWriter: XmlWriter)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, xmlWriter):
        """ __new__(cls: type, xmlWriter: XmlWriter) """
        pass

    XamlWriterMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the XAML writer mode.

Get: XamlWriterMode(self: XamlDesignerSerializationManager) -> XamlWriterMode

Set: XamlWriterMode(self: XamlDesignerSerializationManager) = value
"""



class XamlInstanceCreator(object):
    """ Abstract class that provides a means to store parser records for later instantiation. """
    def CreateObject(self):
        """
        CreateObject(self: XamlInstanceCreator) -> object
        
            When overridden in a derived class, creates a new object to store parser records.
            Returns: The created object.
        """
        pass


class XamlParseException(SystemException, ISerializable, _Exception):
    """
    Represents the exception class for parser-specific exceptions from a WPF XAML parser. This exception is used in XAML API or WPF XAML parser operations from .NET Framework 3.0 and .NET Framework 3.5, or for specific use of the WPF XAML parser by calling System.Windows.Markup.XamlReader API.
    
    XamlParseException()
    XamlParseException(message: str)
    XamlParseException(message: str, innerException: Exception)
    XamlParseException(message: str, lineNumber: int, linePosition: int)
    XamlParseException(message: str, lineNumber: int, linePosition: int, innerException: Exception)
    """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: XamlParseException, info: SerializationInfo, context: StreamingContext)
            Gets the data that is required to serialize the specified object by populating the specified System.Runtime.Serialization.SerializationInfo object.
        
            info: The serialization information object to add the serialization data to.
            context: The destination for this serialization.
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
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, lineNumber: int, linePosition: int)
        __new__(cls: type, message: str, lineNumber: int, linePosition: int, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseUri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets base URI information when the exception is thrown.

Get: BaseUri(self: XamlParseException) -> Uri

"""

    KeyContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key value of the item in a dictionary where the exception occurred.

Get: KeyContext(self: XamlParseException) -> object

"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the line number where the exception occurred.

Get: LineNumber(self: XamlParseException) -> int

"""

    LinePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position in the line where the exception occurred.

Get: LinePosition(self: XamlParseException) -> int

"""

    NameContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the XAML name of the object where the exception occurred.

Get: NameContext(self: XamlParseException) -> str

"""

    UidContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x:Uid Directive of the object where the exception occurred.

Get: UidContext(self: XamlParseException) -> str

"""



class XamlReader(object):
    """
    Reads XAML input and creates an object graph, using the WPF default XAML reader and an associated XAML object writer.
    
    XamlReader()
    """
    def CancelAsync(self):
        """
        CancelAsync(self: XamlReader)
            Aborts the current asynchronous load operation, if there is an asynchronous load operation pending.
        """
        pass

    @staticmethod
    def GetWpfSchemaContext():
        """
        GetWpfSchemaContext() -> XamlSchemaContext
        
            Returns a System.Xaml.XamlSchemaContext object that represents the WPF schema context settings for a System.Windows.Markup.XamlReader.
            Returns: A System.Xaml.XamlSchemaContext object that represents the WPF schema context settings for a System.Windows.Markup.XamlReader.
        """
        pass

    @staticmethod
    def Load(*__args):
        """
        Load(stream: Stream, parserContext: ParserContext) -> object
        
            Reads the XAML input in the specified System.IO.Stream and returns an object that is the root of the corresponding object tree.
        
            stream: The stream that contains the XAML input to load.
            parserContext: Context information used by the parser.
            Returns: The object that is the root of the created object tree.
        Load(reader: XamlReader) -> object
        
            Reads the XAML input through a provided System.Xaml.XamlReader and returns an object that is the root of the corresponding object tree.
        
            reader: A System.Xaml.XamlReader object. This is expected to be initialized with input XAML.
            Returns: The object that is the root of the created object tree.
        Load(stream: Stream) -> object
        
            Reads the XAML input in the specified System.IO.Stream and returns an System.Object that is the root of the corresponding object tree.
        
            stream: The XAML to load, in stream form.
            Returns: The object at the root of the created object tree.
        Load(reader: XmlReader) -> object
        
            Reads the XAML input in the specified System.Xml.XmlReader and returns an object that is the root of the corresponding object tree.
        
            reader: The System.Xml.XmlReader that has already loaded the XAML input to load in XML form.
            Returns: The object that is the root of the created object tree.
        """
        pass

    def LoadAsync(self, *__args):
        """
        LoadAsync(self: XamlReader, stream: Stream, parserContext: ParserContext) -> object
        
            Reads the XAML input in the specified System.IO.Stream and returns the root of the corresponding object tree.
        
            stream: A stream containing the XAML input to load.
            parserContext: Context information used by the parser.
            Returns: The root of the created object tree.
        LoadAsync(self: XamlReader, reader: XmlReader) -> object
        
            Reads the XAML input in the specified System.Xml.XmlReader and returns the root of the corresponding object tree.
        
            reader: An existing  System.Xml.XmlReader that has already loaded/read the XAML input.
            Returns: The root of the created object tree.
        LoadAsync(self: XamlReader, stream: Stream) -> object
        
            Reads the XAML input in the specified System.IO.Stream and returns the root of the corresponding object tree.
        
            stream: The stream containing the XAML input to load.
            Returns: The object that is the root of the created object tree.
        """
        pass

    @staticmethod
    def Parse(xamlText, parserContext=None):
        """
        Parse(xamlText: str, parserContext: ParserContext) -> object
        
            Reads the XAML markup in the specified text string (using a specified System.Windows.Markup.ParserContext) and returns an object that corresponds to the root of the specified markup.
        
            xamlText: The input XAML, as a single text string.
            parserContext: Context information used by the parser.
            Returns: The root of the created object tree.
        Parse(xamlText: str) -> object
        
            Reads the XAML input in the specified text string and returns an object that corresponds to the root of the specified markup.
        
            xamlText: The input XAML, as a single text string.
            Returns: The root of the created object tree.
        """
        pass

    LoadCompleted = None


class XamlTypeMapper(object):
    """
    Maps a XAML element name to the appropriate CLR System.Type in assemblies.
    
    XamlTypeMapper(assemblyNames: Array[str])
    XamlTypeMapper(assemblyNames: Array[str], namespaceMaps: Array[NamespaceMapEntry])
    """
    def AddMappingProcessingInstruction(self, xmlNamespace, clrNamespace, assemblyName):
        """
        AddMappingProcessingInstruction(self: XamlTypeMapper, xmlNamespace: str, clrNamespace: str, assemblyName: str)
            Defines a mapping between an XML namespace and CLR namespaces in assemblies, and adds these to the System.Windows.Markup.XamlTypeMapper information.
        
            xmlNamespace: The prefix for the XML namespace..
            clrNamespace: The CLR  namespace that contains the types to map.
            assemblyName: The assembly that contains the CLR  namespace.
        """
        pass

    def AllowInternalType(self, *args): #cannot find CLR method
        """
        AllowInternalType(self: XamlTypeMapper, type: Type) -> bool
        
            Requests permission for a System.Windows.Markup.XamlTypeMapper derived type that is called under full trust to access a specific internal type.
        
            type: The type to access.
            Returns: true if the internal type can be accessed; otherwise, false.
        """
        pass

    def GetType(self, xmlNamespace=None, localName=None):
        """
        GetType(self: XamlTypeMapper, xmlNamespace: str, localName: str) -> Type
        
            Gets the CLR System.Type that a given XAML element is mapped to, using the specified XML namespace prefix and element name.
        
            xmlNamespace: The specified XML namespace prefix.
            localName: The "local" name of the XAML element to obtain the mapped System.Type for. Local in this context means as mapped versus the provided xmlNamespace.
            Returns: The System.Type for the object, or null if no mapping could be resolved.
        """
        pass

    def SetAssemblyPath(self, assemblyName, assemblyPath):
        """
        SetAssemblyPath(self: XamlTypeMapper, assemblyName: str, assemblyPath: str)
            Specifies the path to use when loading an assembly.
        
            assemblyName: The short name of the assembly without an extension or path specified (equivalent to System.Reflection.AssemblyName.Name).
            assemblyPath: The file path of the assembly. The assembly path must be a full file path containing a file extension.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, assemblyNames, namespaceMaps=None):
        """
        __new__(cls: type, assemblyNames: Array[str])
        __new__(cls: type, assemblyNames: Array[str], namespaceMaps: Array[NamespaceMapEntry])
        """
        pass

    DefaultMapper = None


class XamlWriter(object):
    """ Provides a single static erload:System.Windows.Markup.XamlWriter.Save method (multiple overloads) that can be used for limited XAML serialization of provided run-time objects into XAML markup. """
    @staticmethod
    def Save(obj, *__args):
        """
        Save(obj: object, xmlWriter: XmlWriter)
            Saves XAML information as the source for a provided System.Xml.XmlWriter object. The output of the System.Xml.XmlWriter can then be used to serialize the provided object and its properties.
        
            obj: The element to be serialized. Typically, this is the root element of a page or application.
            xmlWriter: Writer to use to write the serialized XAML information.
        Save(obj: object, manager: XamlDesignerSerializationManager)
            Saves XAML information into a custom serializer. The output of the serializer can then be used to serialize the provided object and its properties.
        
            obj: The element to be serialized. Typically, this is the root element of a page or application.
            manager: A custom serialization implementation.
        Save(obj: object, stream: Stream)
            Saves XAML information into a specified stream to serialize the specified object and its properties.
        
            obj: The element to be serialized. Typically, this is the root element of a page or application.
            stream: Destination stream for the serialized XAML information.
        Save(obj: object) -> str
        
            Returns a XAML string that serializes the specified object and its properties.
        
            obj: The element to be serialized. Typically, this is the root element of a page or application.
            Returns: A XAML string that can be written to a stream or file. The logical tree of all elements that fall under the provided obj element will be serialized.
        Save(obj: object, writer: TextWriter)
            Saves XAML information as the source for a provided System.IO.TextWriter object. The output of the System.IO.TextWriter can then be used to serialize the provided object and its properties.
        
            obj: The element to be serialized. Typically, this is the root element of a page or application.
            writer: A System.IO.TextWriter instance as the destination where the serialized XAML information is written.
        """
        pass

    __all__ = [
        'Save',
    ]


class XamlWriterMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the XAML writer mode for serializing values that are expressions (such as binding declarations).
    
    enum XamlWriterMode, values: Expression (0), Value (1)
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

    Expression = None
    Value = None
    value__ = None


class XamlWriterState(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes possible writing states for a custom XAML writer.
    
    enum XamlWriterState, values: Finished (1), Starting (0)
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

    Finished = None
    Starting = None
    value__ = None


class XmlAttributeProperties(object):
    """ Encapsulates the XML language-related attributes of a System.Windows.DependencyObject. """
    @staticmethod
    def GetXmlNamespaceMaps(dependencyObject):
        """
        GetXmlNamespaceMaps(dependencyObject: DependencyObject) -> str
        
            Gets the value of the System.Windows.Markup.XmlAttributeProperties.XmlNamespaceMaps�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object to obtain the System.Windows.Markup.XmlAttributeProperties.XmlNamespaceMaps property from.
            Returns: The value of the System.Windows.Markup.XmlAttributeProperties.XmlNamespaceMaps property for the specified object.
        """
        pass

    @staticmethod
    def GetXmlnsDefinition(dependencyObject):
        """
        GetXmlnsDefinition(dependencyObject: DependencyObject) -> str
        
            Gets the value of the System.Windows.Markup.XmlAttributeProperties.XmlnsDefinition�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object to obtain the System.Windows.Markup.XmlAttributeProperties.XmlnsDefinition attached property value from.
            Returns: The value of the System.Windows.Markup.XmlAttributeProperties.XmlnsDefinition attached property for the specified object.
        """
        pass

    @staticmethod
    def GetXmlnsDictionary(dependencyObject):
        """
        GetXmlnsDictionary(dependencyObject: DependencyObject) -> XmlnsDictionary
        
            Gets the value of the System.Windows.Markup.XmlAttributeProperties.XmlnsDictionary�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object to obtain the System.Windows.Markup.XmlAttributeProperties.XmlnsDictionary attached property value from.
            Returns: The value of the System.Windows.Markup.XmlAttributeProperties.XmlnsDictionary attached property for the specified object.
        """
        pass

    @staticmethod
    def GetXmlSpace(dependencyObject):
        """
        GetXmlSpace(dependencyObject: DependencyObject) -> str
        
            Gets the value of the System.Windows.Markup.XmlAttributeProperties.XmlSpace�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object to obtain the System.Windows.Markup.XmlAttributeProperties.XmlSpace attached property value from.
            Returns: The value of the System.Windows.Markup.XmlAttributeProperties.XmlSpace attached property for the specified object.
        """
        pass

    @staticmethod
    def SetXmlNamespaceMaps(dependencyObject, value):
        """
        SetXmlNamespaceMaps(dependencyObject: DependencyObject, value: str)
            Sets the value of the System.Windows.Markup.XmlAttributeProperties.XmlNamespaceMaps�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object on which to set the System.Windows.Markup.XmlAttributeProperties.XmlNamespaceMaps attached property.
            value: The string value to set.
        """
        pass

    @staticmethod
    def SetXmlnsDefinition(dependencyObject, value):
        """
        SetXmlnsDefinition(dependencyObject: DependencyObject, value: str)
            Sets the value of the System.Windows.Markup.XmlAttributeProperties.XmlnsDefinition�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object on which to set the System.Windows.Markup.XmlAttributeProperties.XmlnsDefinition property.
            value: The XML namespace definition in string form.
        """
        pass

    @staticmethod
    def SetXmlnsDictionary(dependencyObject, value):
        """
        SetXmlnsDictionary(dependencyObject: DependencyObject, value: XmlnsDictionary)
            Sets the value of the System.Windows.Markup.XmlAttributeProperties.XmlnsDictionary�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object on which to set the System.Windows.Markup.XmlAttributeProperties.XmlnsDictionary attached property.
            value: The xmlns dictionary in string form.
        """
        pass

    @staticmethod
    def SetXmlSpace(dependencyObject, value):
        """
        SetXmlSpace(dependencyObject: DependencyObject, value: str)
            Sets the value of the System.Windows.Markup.XmlAttributeProperties.XmlSpace�attached property of the specified System.Windows.DependencyObject.
        
            dependencyObject: The object on which to set the System.Windows.Markup.XmlAttributeProperties.XmlSpace attached property.
            value: The string to use for an XML space.
        """
        pass

    XmlNamespaceMapsProperty = None
    XmlnsDefinitionProperty = None
    XmlnsDictionaryProperty = None
    XmlSpaceProperty = None


class XmlLanguage(object):
    """ Represents a language tag for use in XAML markup. """
    def GetEquivalentCulture(self):
        """
        GetEquivalentCulture(self: XmlLanguage) -> CultureInfo
        
            Returns the appropriate equivalent System.Globalization.CultureInfo for this System.Windows.Markup.XmlLanguage, if and only if such a System.Globalization.CultureInfo is registered for the 
             System.Windows.Markup.XmlLanguage.IetfLanguageTag value of this System.Windows.Markup.XmlLanguage
        
            Returns: A System.Globalization.CultureInfo that can be used for localization-globalization API calls that take that type as an argument.
        """
        pass

    @staticmethod
    def GetLanguage(ietfLanguageTag):
        """
        GetLanguage(ietfLanguageTag: str) -> XmlLanguage
        
            Returns a System.Windows.Markup.XmlLanguage instance, based on a string representing the language per RFC 3066.
        
            ietfLanguageTag: An RFC 3066 language string, or empty string.
            Returns: A new System.Windows.Markup.XmlLanguage with the provided string as its System.Windows.Markup.XmlLanguage.IetfLanguageTag value.
        """
        pass

    def GetSpecificCulture(self):
        """
        GetSpecificCulture(self: XmlLanguage) -> CultureInfo
        
            Returns the most-closely-related non-neutral System.Globalization.CultureInfo for this System.Windows.Markup.XmlLanguage.
            Returns: A System.Globalization.CultureInfo that can be used for localization-globalization API calls that take that type as an argument.
        """
        pass

    def ToString(self):
        """
        ToString(self: XmlLanguage) -> str
        
            Returns a System.String that represents the current System.Windows.Markup.XmlLanguage.
            Returns: A System.String that represents the current System.Windows.Markup.XmlLanguage.
        """
        pass

    IetfLanguageTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the string representation of the language tag.

Get: IetfLanguageTag(self: XmlLanguage) -> str

"""


    Empty = None


class XmlLanguageConverter(TypeConverter):
    """
    Provides type conversion for the System.Windows.Markup.XmlLanguage class.
    
    XmlLanguageConverter()
    """
    def CanConvertFrom(self, *__args):
        """
        CanConvertFrom(self: XmlLanguageConverter, typeDescriptorContext: ITypeDescriptorContext, sourceType: Type) -> bool
        
            Returns whether this converter can convert an object of one type to the System.Windows.Markup.XmlLanguage type supported by this converter.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            sourceType: A type that represents the type you want to convert from.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def CanConvertTo(self, *__args):
        """
        CanConvertTo(self: XmlLanguageConverter, typeDescriptorContext: ITypeDescriptorContext, destinationType: Type) -> bool
        
            Returns whether this converter can convert the object to the specified type.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            destinationType: The type you want to convert to.
            Returns: true if this converter can perform the conversion; otherwise, false.
        """
        pass

    def ConvertFrom(self, *__args):
        """
        ConvertFrom(self: XmlLanguageConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, source: object) -> object
        
            Converts the specified string value to the System.Windows.Markup.XmlLanguage type supported by this converter.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            cultureInfo: The System.Globalization.CultureInfo to use as the current culture.
            source: The string to convert.
            Returns: An object that represents the converted value.
        """
        pass

    def ConvertTo(self, *__args):
        """
        ConvertTo(self: XmlLanguageConverter, typeDescriptorContext: ITypeDescriptorContext, cultureInfo: CultureInfo, value: object, destinationType: Type) -> object
        
            Converts the specified System.Windows.Markup.XmlLanguage to the specified type.
        
            typeDescriptorContext: An System.ComponentModel.ITypeDescriptorContext that provides a format context.
            cultureInfo: The System.Globalization.CultureInfo to use as the current culture.
            value: The object to convert. This is expected to be type System.Windows.Markup.XmlLanguage.
            destinationType: A type that represents the type you want to convert to.
            Returns: An object that represents the converted value.
        """
        pass


class XmlnsDictionary(object, IDictionary, ICollection, IEnumerable, IXamlNamespaceResolver):
    """
    Represents a dictionary that contains xmlns mappings for XAML namespaces in WPF.
    
    XmlnsDictionary()
    XmlnsDictionary(xmlnsDictionary: XmlnsDictionary)
    """
    def Add(self, prefix, xmlNamespace):
        """
        Add(self: XmlnsDictionary, prefix: str, xmlNamespace: str)
            Adds a prefix-URI pair to this System.Windows.Markup.XmlnsDictionary.
        
            prefix: The prefix of this XML namespace.
            xmlNamespace: The XML namespace URI the prefix maps to.
        Add(self: XmlnsDictionary, prefix: object, xmlNamespace: object)
            Adds a prefix-URI pair to this System.Windows.Markup.XmlnsDictionary.
        
            prefix: The prefix of the XAML namespace to be added.
            xmlNamespace: The XAML namespace URI the prefix maps to.
        """
        pass

    def Clear(self):
        """
        Clear(self: XmlnsDictionary)
            Removes all entries from this System.Windows.Markup.XmlnsDictionary.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: XmlnsDictionary, key: object) -> bool
        
            Returns a value that indicates whether the specified prefix key is in this System.Windows.Markup.XmlnsDictionary.
        
            key: The prefix key to search for.
            Returns: true if the requested prefix key is in the dictionary; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: XmlnsDictionary, array: Array, index: int)
            Copies the entries in the System.Windows.Markup.XmlnsDictionary to the specified array.
        
            array: The array to copy the table data into.
            index: The zero-based index in the destination array where copying starts.
        CopyTo(self: XmlnsDictionary, array: Array[DictionaryEntry], index: int)
            Copies the entries in the System.Windows.Markup.XmlnsDictionary to the specified System.Collections.DictionaryEntry array.
        
            array: The array to copy the table data into.
            index: The zero-based index in the destination array where copying starts.
        """
        pass

    def DefaultNamespace(self):
        """
        DefaultNamespace(self: XmlnsDictionary) -> str
        
            Looks up the XAML namespace that corresponds to the default XAML namespace.
            Returns: The namespace that corresponds to the default XML namespace if one exists; otherwise, null.
        """
        pass

    def GetDictionaryEnumerator(self, *args): #cannot find CLR method
        """
        GetDictionaryEnumerator(self: XmlnsDictionary) -> IDictionaryEnumerator
        
            Returns a dictionary enumerator that iterates through this System.Windows.Markup.XmlnsDictionary.
            Returns: The dictionary enumerator for this dictionary.
        """
        pass

    def GetEnumerator(self, *args): #cannot find CLR method
        """
        GetEnumerator(self: XmlnsDictionary) -> IEnumerator
        
            Returns an enumerator that iterates through this System.Windows.Markup.XmlnsDictionary.
            Returns: The enumerator for this dictionary.
        """
        pass

    def GetNamespace(self, prefix):
        """
        GetNamespace(self: XmlnsDictionary, prefix: str) -> str
        
            Retrieves a XAML namespace for the provided prefix string.
        
            prefix: The prefix to retrieve the XAML namespace for.
            Returns: The requested XAML namespace URI.
        """
        pass

    def GetNamespacePrefixes(self):
        """
        GetNamespacePrefixes(self: XmlnsDictionary) -> IEnumerable[NamespaceDeclaration]
        
            Returns all possible prefix-XAML namespace mappings (System.Xaml.NamespaceDeclaration values) that are available in the active schema context.
            Returns: An enumerable set of System.Xaml.NamespaceDeclaration values. To get the prefix strings specifically, get the System.Xaml.NamespaceDeclaration.Prefix value from each value returned.
        """
        pass

    def LookupNamespace(self, prefix):
        """
        LookupNamespace(self: XmlnsDictionary, prefix: str) -> str
        
            Returns the XAML namespace URI that corresponds to the specified XML namespace prefix.
        
            prefix: The XAML namespace prefix to look up.
            Returns: The XAML namespace URI that corresponds to the specified prefix if it exists in this System.Windows.Markup.XmlnsDictionary; otherwise, null.
        """
        pass

    def LookupPrefix(self, xmlNamespace):
        """
        LookupPrefix(self: XmlnsDictionary, xmlNamespace: str) -> str
        
            Returns the prefix that corresponds to the specified XAML namespace URI.
        
            xmlNamespace: The XAML namespace URI to look up.
            Returns: The XML prefix that corresponds to the given namespace; otherwise, null.
        """
        pass

    def PopScope(self):
        """
        PopScope(self: XmlnsDictionary)
            Pops the scope of the System.Windows.Markup.XmlnsDictionary.
        """
        pass

    def PushScope(self):
        """
        PushScope(self: XmlnsDictionary)
            Pushes the scope of the System.Windows.Markup.XmlnsDictionary.
        """
        pass

    def Remove(self, prefix):
        """
        Remove(self: XmlnsDictionary, prefix: object)
            Removes the item with the specified prefix key from the System.Windows.Markup.XmlnsDictionary.
        
            prefix: The prefix key to remove.
        Remove(self: XmlnsDictionary, prefix: str)
            Removes the item with the specified prefix key from the System.Windows.Markup.XmlnsDictionary.
        
            prefix: The prefix key to remove.
        """
        pass

    def Seal(self):
        """
        Seal(self: XmlnsDictionary)
            Locks the dictionary so that it cannot be changed.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        Contains(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the specified key.
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, xmlnsDictionary=None):
        """
        __new__(cls: type)
        __new__(cls: type, xmlnsDictionary: XmlnsDictionary)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the System.Windows.Markup.XmlnsDictionary.

Get: Count(self: XmlnsDictionary) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the size of the System.Windows.Markup.XmlnsDictionary is fixed.

Get: IsFixedSize(self: XmlnsDictionary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Markup.XmlnsDictionary is read-only.

Get: IsReadOnly(self: XmlnsDictionary) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to this System.Windows.Markup.XmlnsDictionary is thread safe.

Get: IsSynchronized(self: XmlnsDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all the keys in the System.Windows.Markup.XmlnsDictionary.

Get: Keys(self: XmlnsDictionary) -> ICollection

"""

    Sealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Markup.XmlnsDictionary is sealed.

Get: Sealed(self: XmlnsDictionary) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Windows.Markup.XmlnsDictionary.

Get: SyncRoot(self: XmlnsDictionary) -> object

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all the values in the System.Windows.Markup.XmlnsDictionary.

Get: Values(self: XmlnsDictionary) -> ICollection

"""



# variables with complex values

