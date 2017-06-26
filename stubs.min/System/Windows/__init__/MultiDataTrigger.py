class MultiDataTrigger(TriggerBase, IAddChild):
    """
    Represents a trigger that applies property values or performs actions when the bound data meet a set of conditions.
    
    MultiDataTrigger()
    """
    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.DependencyObject has been updated. The specific dependency property that changed is reported in the event data.
        
            e: Event data that will contain the dependency property identifier of interest, the property metadata for the type, and old and new values.
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

    Conditions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Condition objects. Changes to property values are applied when all the conditions in the collection are met.

Get: Conditions(self: MultiDataTrigger) -> ConditionCollection

"""

    Setters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of System.Windows.Setter objects that describe the property values to apply when all the conditions of the System.Windows.MultiDataTrigger are met.

Get: Setters(self: MultiDataTrigger) -> SetterBaseCollection

"""


