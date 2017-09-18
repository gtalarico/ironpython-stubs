# encoding: utf-8
# module System.Windows.Markup.Localizer calls itself Localizer
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BamlLocalizabilityResolver(object):
    """ Resolves localizable settings for classes and properties in binary XAML (BAML). """
    def GetElementLocalizability(self, assembly, className):
        """
        GetElementLocalizability(self: BamlLocalizabilityResolver, assembly: str, className: str) -> ElementLocalizability
        
            Returns a value that indicates whether a specified type of element can be localized and, if so, 
             whether it can be formatted inline.
        
        
            assembly: The full name of the assembly that contains BAML to be localized.
            className: The full class name of the element that you want to retrieve localizability information for.
            Returns: An object that contains the localizability information for the specified assembly and element.
        """
        pass

    def GetPropertyLocalizability(self, assembly, className, property):
        """
        GetPropertyLocalizability(self: BamlLocalizabilityResolver, assembly: str, className: str, property: str) -> LocalizabilityAttribute
        
            Returns a value that indicates whether a specified property of a specified type of element can 
             be localized.
        
        
            assembly: The full name of the assembly that contains BAML to be localized.
            className: The full class name of the element that you want to retrieve localizability information for.
            property: The name of the property that you want to retrieve localizability information for.
            Returns: An object that specifies whether and how the property can be localized.
        """
        pass

    def ResolveAssemblyFromClass(self, className):
        """
        ResolveAssemblyFromClass(self: BamlLocalizabilityResolver, className: str) -> str
        
            Returns the full name of the assembly that contains the specified class.
        
            className: The full class name.
            Returns: The full name of the assembly that contains the class.
        """
        pass

    def ResolveFormattingTagToClass(self, formattingTag):
        """
        ResolveFormattingTagToClass(self: BamlLocalizabilityResolver, formattingTag: str) -> str
        
            Returns the full class name of a XAML tag that has not been encountered in BAML.
        
            formattingTag: The name of the tag.
            Returns: The full class name associated with the tag.
        """
        pass


class BamlLocalizableResource(object):
    """
    Represents a localizable resource in a BAML stream.
    
    BamlLocalizableResource()
    BamlLocalizableResource(content: str, comments: str, category: LocalizationCategory, modifiable: bool, readable: bool)
    """
    def Equals(self, other):
        """
        Equals(self: BamlLocalizableResource, other: object) -> bool
        
            Determines whether a specified System.Windows.Markup.Localizer.BamlLocalizableResource object is 
             equal to this object.
        
        
            other: The System.Windows.Markup.Localizer.BamlLocalizableResource object test for equality.
            Returns: true if other is equal to this object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: BamlLocalizableResource) -> int
        
            Returns an integer hash code representing this instance.
            Returns: An integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, content=None, comments=None, category=None, modifiable=None, readable=None):
        """
        __new__(cls: type)
        __new__(cls: type, content: str, comments: str, category: LocalizationCategory, modifiable: bool, readable: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the localization category of a resource.

Get: Category(self: BamlLocalizableResource) -> LocalizationCategory

Set: Category(self: BamlLocalizableResource) = value
"""

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the localization comments associated with a resource.

Get: Comments(self: BamlLocalizableResource) -> str

Set: Comments(self: BamlLocalizableResource) = value
"""

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the localizable content.

Get: Content(self: BamlLocalizableResource) -> str

Set: Content(self: BamlLocalizableResource) = value
"""

    Modifiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the localizable resource is modifiable.

Get: Modifiable(self: BamlLocalizableResource) -> bool

Set: Modifiable(self: BamlLocalizableResource) = value
"""

    Readable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the resource is visible for translation.

Get: Readable(self: BamlLocalizableResource) -> bool

Set: Readable(self: BamlLocalizableResource) = value
"""



class BamlLocalizableResourceKey(object):
    """
    Represents a key that is used to identify localizable resources in a System.Windows.Markup.Localizer.BamlLocalizationDictionary.
    
    BamlLocalizableResourceKey(uid: str, className: str, propertyName: str)
    """
    def Equals(self, other):
        """
        Equals(self: BamlLocalizableResourceKey, other: object) -> bool
        
            Compares an object to an instance of System.Windows.Markup.Localizer.BamlLocalizableResourceKey 
             for equality.
        
        
            other: The object to compare for equality.
            Returns: true if the two instances are equal; otherwise, false.
        Equals(self: BamlLocalizableResourceKey, other: BamlLocalizableResourceKey) -> bool
        
            Compares two instances of System.Windows.Markup.Localizer.BamlLocalizableResourceKey for 
             equality.
        
        
            other: The other instance of System.Windows.Markup.Localizer.BamlLocalizableResourceKey to compare for 
             equality.
        
            Returns: true if the two instances are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: BamlLocalizableResourceKey) -> int
        
            Returns an integer hash code representing this instance.
            Returns: An integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, uid, className, propertyName):
        """ __new__(cls: type, uid: str, className: str, propertyName: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the assembly that defines the type of the localizable resource as declared by its System.Windows.Markup.Localizer.BamlLocalizableResourceKey.ClassName.

Get: AssemblyName(self: BamlLocalizableResourceKey) -> str

"""

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class name component of this System.Windows.Markup.Localizer.BamlLocalizableResourceKey.

Get: ClassName(self: BamlLocalizableResourceKey) -> str

"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property name component of this System.Windows.Markup.Localizer.BamlLocalizableResourceKey.

Get: PropertyName(self: BamlLocalizableResourceKey) -> str

"""

    Uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Uid component of this System.Windows.Markup.Localizer.BamlLocalizableResourceKey.

Get: Uid(self: BamlLocalizableResourceKey) -> str

"""



class BamlLocalizationDictionary(object, IDictionary, ICollection, IEnumerable):
    """
    Contains all the localizable resources in a BAML record.
    
    BamlLocalizationDictionary()
    """
    def Add(self, key, value):
        """
        Add(self: BamlLocalizationDictionary, key: BamlLocalizableResourceKey, value: BamlLocalizableResource)
            Adds an item with the provided key and value to the 
             System.Windows.Markup.Localizer.BamlLocalizationDictionary.
        
        
            key: A key for the resource.
            value: An object that contains the resource.
        """
        pass

    def Clear(self):
        """
        Clear(self: BamlLocalizationDictionary)
            Deletes all resources from the System.Windows.Markup.Localizer.BamlLocalizationDictionary object.
        """
        pass

    def Contains(self, key):
        """
        Contains(self: BamlLocalizationDictionary, key: BamlLocalizableResourceKey) -> bool
        
            Determines whether a System.Windows.Markup.Localizer.BamlLocalizationDictionary object contains 
             a resource with a specified key.
        
        
            key: The resource key to find.
            Returns: true if the System.Windows.Markup.Localizer.BamlLocalizationDictionary object contains a 
             resource with the specified key; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: BamlLocalizationDictionary, array: Array[DictionaryEntry], arrayIndex: int)
            Copies the contents of a System.Windows.Markup.Localizer.BamlLocalizationDictionary object to a 
             one-dimensional array of System.Collections.DictionaryEntry objects, starting at a specified 
             index.
        
        
            array: An array of objects to hold the data.
            arrayIndex: The starting index value.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BamlLocalizationDictionary) -> BamlLocalizationDictionaryEnumerator
        
            Returns an enumerator that iterates through the 
             System.Windows.Markup.Localizer.BamlLocalizationDictionary.
        
            Returns: A specialized System.Windows.Markup.Localizer.BamlLocalizationDictionaryEnumerator that can 
             iterate the contents of the dictionary.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: BamlLocalizationDictionary, key: BamlLocalizableResourceKey)
            Removes a specified localizable resource from the 
             System.Windows.Markup.Localizer.BamlLocalizationDictionary.
        
        
            key: The key for the resource to be removed.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: true if the System.Collections.IDictionary contains an element with the key; otherwise, false.
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of localizable resources in the System.Windows.Markup.Localizer.BamlLocalizationDictionary.

Get: Count(self: BamlLocalizationDictionary) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Markup.Localizer.BamlLocalizationDictionary object has a fixed size.

Get: IsFixedSize(self: BamlLocalizationDictionary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.Windows.Markup.Localizer.BamlLocalizationDictionary object is read-only.

Get: IsReadOnly(self: BamlLocalizationDictionary) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection that contains all the keys in the System.Windows.Markup.Localizer.BamlLocalizationDictionary object.

Get: Keys(self: BamlLocalizationDictionary) -> ICollection

"""

    RootElementKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key of the root element, if it is localizable.

Get: RootElementKey(self: BamlLocalizationDictionary) -> BamlLocalizableResourceKey

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection that contains all the values in the System.Windows.Markup.Localizer.BamlLocalizationDictionary.

Get: Values(self: BamlLocalizationDictionary) -> ICollection

"""



class BamlLocalizationDictionaryEnumerator(object, IDictionaryEnumerator, IEnumerator):
    """ Defines a specialized enumerator that can enumerate over the content of a System.Windows.Markup.Localizer.BamlLocalizationDictionary object. """
    def MoveNext(self):
        """
        MoveNext(self: BamlLocalizationDictionaryEnumerator) -> bool
        
            Moves to the next item in the collection.
            Returns: true if the enumerator successfully advances to the next element. If there are no remaining 
             elements, this method returns false.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: BamlLocalizationDictionaryEnumerator)
            Returns the enumerator to its initial position, which is before the first object in the 
             collection.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current object in the collection.

Get: Current(self: BamlLocalizationDictionaryEnumerator) -> DictionaryEntry

"""

    Entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current position's System.Collections.DictionaryEntry object.

Get: Entry(self: BamlLocalizationDictionaryEnumerator) -> DictionaryEntry

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key of the current entry.

Get: Key(self: BamlLocalizationDictionaryEnumerator) -> BamlLocalizableResourceKey

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the current entry.

Get: Value(self: BamlLocalizationDictionaryEnumerator) -> BamlLocalizableResource

"""



class BamlLocalizer(object):
    """
    Extracts resources from a BAML file and generates a localized version of a BAML source.
    
    BamlLocalizer(source: Stream)
    BamlLocalizer(source: Stream, resolver: BamlLocalizabilityResolver)
    BamlLocalizer(source: Stream, resolver: BamlLocalizabilityResolver, comments: TextReader)
    """
    def ExtractResources(self):
        """
        ExtractResources(self: BamlLocalizer) -> BamlLocalizationDictionary
        
            Extracts all localizable resources from a BAML stream.
            Returns: A copy of the localizable resources from a BAML stream, in the form of a 
             System.Windows.Markup.Localizer.BamlLocalizationDictionary.
        """
        pass

    def OnErrorNotify(self, *args): #cannot find CLR method
        """
        OnErrorNotify(self: BamlLocalizer, e: BamlLocalizerErrorNotifyEventArgs)
            Raises the System.Windows.Markup.Localizer.BamlLocalizer.ErrorNotify event.
        
            e: Required event arguments.
        """
        pass

    def UpdateBaml(self, target, updates):
        """
        UpdateBaml(self: BamlLocalizer, target: Stream, updates: BamlLocalizationDictionary)
            Applies resource updates to the BAML source and writes the updated version to a specified stream 
             in order to create a localized version of the source BAML.
        
        
            target: The stream that will receive the updated BAML.
            updates: The resource updates to be applied to the source BAML.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source, resolver=None, comments=None):
        """
        __new__(cls: type, source: Stream)
        __new__(cls: type, source: Stream, resolver: BamlLocalizabilityResolver)
        __new__(cls: type, source: Stream, resolver: BamlLocalizabilityResolver, comments: TextReader)
        """
        pass

    ErrorNotify = None


class BamlLocalizerError(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies error conditions that may be encountered by the System.Windows.Markup.Localizer.BamlLocalizer.
    
    enum BamlLocalizerError, values: DuplicateElement (1), DuplicateUid (0), IncompleteElementPlaceholder (2), InvalidCommentingXml (3), InvalidLocalizationAttributes (4), InvalidLocalizationComments (5), InvalidUid (6), MismatchedElements (7), SubstitutionAsPlaintext (8), UidMissingOnChildElement (9), UnknownFormattingTag (10)
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

    DuplicateElement = None
    DuplicateUid = None
    IncompleteElementPlaceholder = None
    InvalidCommentingXml = None
    InvalidLocalizationAttributes = None
    InvalidLocalizationComments = None
    InvalidUid = None
    MismatchedElements = None
    SubstitutionAsPlaintext = None
    UidMissingOnChildElement = None
    UnknownFormattingTag = None
    value__ = None


class BamlLocalizerErrorNotifyEventArgs(EventArgs):
    """ Provides required event data for the System.Windows.Markup.Localizer.BamlLocalizer.ErrorNotify event. """
    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the specific error condition encountered by System.Windows.Markup.Localizer.BamlLocalizer.

Get: Error(self: BamlLocalizerErrorNotifyEventArgs) -> BamlLocalizerError

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the key associated with the resource that generated the error condition.

Get: Key(self: BamlLocalizerErrorNotifyEventArgs) -> BamlLocalizableResourceKey

"""



class BamlLocalizerErrorNotifyEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that will handle the System.Windows.Markup.Localizer.BamlLocalizer.ErrorNotify event.
    
    BamlLocalizerErrorNotifyEventHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: BamlLocalizerErrorNotifyEventHandler, sender: object, e: BamlLocalizerErrorNotifyEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: BamlLocalizerErrorNotifyEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BamlLocalizerErrorNotifyEventHandler, sender: object, e: BamlLocalizerErrorNotifyEventArgs) """
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


class ElementLocalizability(object):
    """
    Represents localizability settings for an element in BAML.
    
    ElementLocalizability()
    ElementLocalizability(formattingTag: str, attribute: LocalizabilityAttribute)
    """
    @staticmethod # known case of __new__
    def __new__(self, formattingTag=None, attribute=None):
        """
        __new__(cls: type)
        __new__(cls: type, formattingTag: str, attribute: LocalizabilityAttribute)
        """
        pass

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the associated element's localizability attribute.

Get: Attribute(self: ElementLocalizability) -> LocalizabilityAttribute

Set: Attribute(self: ElementLocalizability) = value
"""

    FormattingTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the associated element's formatting tag.

Get: FormattingTag(self: ElementLocalizability) -> str

Set: FormattingTag(self: ElementLocalizability) = value
"""



