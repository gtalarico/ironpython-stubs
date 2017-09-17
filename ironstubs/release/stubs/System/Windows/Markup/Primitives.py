# encoding: utf-8
# module System.Windows.Markup.Primitives calls itself Primitives
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MarkupObject(object):
    """ Abstract class that represents an object that can be used to navigate a tree of objects. """
    def AssignRootContext(self, context):
        """
        AssignRootContext(self: MarkupObject, context: IValueSerializerContext)
            When overridden in a derived class, assigns a root context for 
             System.Windows.Markup.ValueSerializer classes.
        
        
            context: The System.Windows.Markup.IValueSerializerContext to assign a root context for.
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the attributes associated with this System.Windows.Markup.Primitives.MarkupObject.

Get: Attributes(self: MarkupObject) -> AttributeCollection

"""

    Instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the instance of the object represented by this System.Windows.Markup.Primitives.MarkupObject.

Get: Instance(self: MarkupObject) -> object

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the type of the System.Windows.Markup.Primitives.MarkupObject instance.

Get: ObjectType(self: MarkupObject) -> Type

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the properties of this System.Windows.Markup.Primitives.MarkupObject instance that should be written to XAML.

Get: Properties(self: MarkupObject) -> IEnumerable[MarkupProperty]

"""



class MarkupProperty(object):
    """ Abstract class that provides a property description to be used while writing to markup which encapsulates access to properties and their values. """
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the attributes associated with this System.Windows.Markup.Primitives.MarkupProperty.

Get: Attributes(self: MarkupProperty) -> AttributeCollection

"""

    DependencyProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the System.Windows.DependencyProperty identifier for the markup property if the property is implemented as a dependency property

Get: DependencyProperty(self: MarkupProperty) -> DependencyProperty

"""

    IsAttached = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, determines whether this System.Windows.Markup.Primitives.MarkupProperty is an attached System.Windows.DependencyProperty.

Get: IsAttached(self: MarkupProperty) -> bool

"""

    IsComposite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, determines whether this System.Windows.Markup.Primitives.MarkupProperty is a composite property.

Get: IsComposite(self: MarkupProperty) -> bool

"""

    IsConstructorArgument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, determines whether this System.Windows.Markup.Primitives.MarkupProperty represents a constructor argument.

Get: IsConstructorArgument(self: MarkupProperty) -> bool

"""

    IsContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, determines whether this System.Windows.Markup.Primitives.MarkupProperty represents direct content of a collection.

Get: IsContent(self: MarkupProperty) -> bool

"""

    IsKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, determines whether this System.Windows.Markup.Primitives.MarkupProperty represents the key used by the System.Windows.Markup.Primitives.MarkupObject to store the item in a dictionary.

Get: IsKey(self: MarkupProperty) -> bool

"""

    IsValueAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, determines whether this System.Windows.Markup.Primitives.MarkupProperty represents text which is passed to a type converter to create an instance of the property or if a constructor should be used.

Get: IsValueAsString(self: MarkupProperty) -> bool

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the items that make up the value of this property.

Get: Items(self: MarkupProperty) -> IEnumerable[MarkupObject]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets a name that is used for diagnostics and error reporting.

Get: Name(self: MarkupProperty) -> str

"""

    PropertyDescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the System.ComponentModel.PropertyDescriptor for the markup property.

Get: PropertyDescriptor(self: MarkupProperty) -> PropertyDescriptor

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the CLR type of the property.

Get: PropertyType(self: MarkupProperty) -> Type

"""

    StringValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the string value of this System.Windows.Markup.Primitives.MarkupProperty.

Get: StringValue(self: MarkupProperty) -> str

"""

    TypeReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the set of types that this System.Windows.Markup.Primitives.MarkupProperty will reference when it serializes its value as a string.

Get: TypeReferences(self: MarkupProperty) -> IEnumerable[Type]

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the current value of this System.Windows.Markup.Primitives.MarkupProperty.

Get: Value(self: MarkupProperty) -> object

"""



class MarkupWriter(object, IDisposable):
    """ Provides methods to write an object to XAML format. """
    def Dispose(self):
        """
        Dispose(self: MarkupWriter)
            Releases the resources used by the 
             System.Windows.Markup.Primitives.MarkupWriter.
        """
        pass

    @staticmethod
    def GetMarkupObjectFor(instance, manager=None):
        """
        GetMarkupObjectFor(instance: object, manager: XamlDesignerSerializationManager) -> MarkupObject
        
            Creates an instance of a System.Windows.Markup.Primitives.MarkupObject from the 
             specified object and the specified serialization manager.
        
        
            instance: An object that will be the root of the serialized tree.
            manager: The serialization manager.
            Returns: A markup object that enables navigating through the tree of objects.
        GetMarkupObjectFor(instance: object) -> MarkupObject
        
            Creates an instance of a System.Windows.Markup.Primitives.MarkupObject from the 
             specified object.
        
        
            instance: An object that will be the root of the serialized tree.
            Returns: A markup object that enables navigating through the tree of objects.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


