class JournalEntry(DependencyObject, ISerializable):
    """ Represents an entry in either back or forward navigation history. """
    @staticmethod
    def GetKeepAlive(dependencyObject):
        """
        GetKeepAlive(dependencyObject: DependencyObject) -> bool
        
            Returns the System.Windows.Navigation.JournalEntry.KeepAlive�attached property of the journal entry for the specified element.
        
            dependencyObject: The element from which to get the attached property value.
            Returns: The value of the System.Windows.Navigation.JournalEntry.KeepAlive�attached property of the journal entry for the specified element.
        """
        pass

    @staticmethod
    def GetName(dependencyObject):
        """
        GetName(dependencyObject: DependencyObject) -> str
        
            Gets the System.Windows.Navigation.JournalEntry.Name�attached property of the journal entry for the specified element.
        
            dependencyObject: The element from which to get the attached property value.
            Returns: The System.Windows.Navigation.JournalEntry.Name�attached property of the journal entry for the specified element.
        """
        pass

    def GetObjectData(self, info, context):
        """
        GetObjectData(self: JournalEntry, info: SerializationInfo, context: StreamingContext)
            Called when this object is serialized.
        
            info: The data that is required to serialize the target object.
            context: The streaming context.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.DependencyObject has been updated. The specific dependency property that changed is reported in the event data.
        
            e: Event data that will contain the dependency property identifier of interest, the property metadata for the type, and old and new values.
        """
        pass

    @staticmethod
    def SetKeepAlive(dependencyObject, keepAlive):
        """
        SetKeepAlive(dependencyObject: DependencyObject, keepAlive: bool)
            Sets the System.Windows.Navigation.JournalEntry.KeepAlive�attached property of the specified element.
        
            dependencyObject: The element on which to set the attached property value.
            keepAlive: true to keep the journal entry in memory; otherwise, false.
        """
        pass

    @staticmethod
    def SetName(dependencyObject, name):
        """
        SetName(dependencyObject: DependencyObject, name: str)
            Sets the System.Windows.Navigation.JournalEntry.Name�attached property of the specified element.
        
            dependencyObject: The element on which to set the attached property value.
            name: The name to be assigned to the attached property.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CustomContentState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Navigation.CustomContentState object that is associated with this journal entry.

Get: CustomContentState(self: JournalEntry) -> CustomContentState

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the journal entry.

Get: Name(self: JournalEntry) -> str

Set: Name(self: JournalEntry) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the URI of the content that was navigated to.

Get: Source(self: JournalEntry) -> Uri

Set: Source(self: JournalEntry) = value
"""


    KeepAliveProperty = None
    NameProperty = None

