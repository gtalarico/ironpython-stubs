class EventTrigger(TriggerBase, IAddChild):
    """
    Represents a trigger that applies a set of actions in response to an event.
    
    EventTrigger()
    EventTrigger(routedEvent: RoutedEvent)
    """
    def AddChild(self, *args): #cannot find CLR method
        """
        AddChild(self: EventTrigger, value: object)
            Adds the specified object to the System.Windows.EventTrigger.Actions collection of the current event trigger.
        
            value: A System.Windows.TriggerAction object to add to the System.Windows.EventTrigger.Actions collection of this trigger.
        """
        pass

    def AddText(self, *args): #cannot find CLR method
        """
        AddText(self: EventTrigger, text: str)
            This method is not supported and results in an exception.
        
            text: This parameter is not used.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.DependencyObject has been updated. The specific dependency property that changed is reported in the event data.
        
            e: Event data that will contain the dependency property identifier of interest, the property metadata for the type, and old and new values.
        """
        pass

    def ShouldSerializeActions(self):
        """
        ShouldSerializeActions(self: EventTrigger) -> bool
        
            Returns whether serialization processes should serialize the effective value of the System.Windows.EventTrigger.Actions property on instances of this class.
            Returns: Returns true if the System.Windows.EventTrigger.Actions property value should be serialized; otherwise, false.
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
    def __new__(self, routedEvent=None):
        """
        __new__(cls: type)
        __new__(cls: type, routedEvent: RoutedEvent)
        """
        pass

    Actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of actions to apply when the event occurs.

Get: Actions(self: EventTrigger) -> TriggerActionCollection

"""

    RoutedEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.RoutedEvent that will activate this trigger.

Get: RoutedEvent(self: EventTrigger) -> RoutedEvent

Set: RoutedEvent(self: EventTrigger) = value
"""

    SourceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the object with the event that activates this trigger. This is only used by element triggers or template triggers.

Get: SourceName(self: EventTrigger) -> str

Set: SourceName(self: EventTrigger) = value
"""


