class DependencyObject(DispatcherObject):
    """
    Represents an object that participates in the dependency property system.
    
    DependencyObject()
    """
    def ClearValue(self, *__args):
        """
        ClearValue(self: DependencyObject, key: DependencyPropertyKey)
            Clears the local value of a read-only property. The property to be cleared is specified by a System.Windows.DependencyPropertyKey.
        
            key: The key for the dependency property to be cleared.
        ClearValue(self: DependencyObject, dp: DependencyProperty)
            Clears the local value of a property. The property to be cleared is specified by a System.Windows.DependencyProperty identifier.
        
            dp: The dependency property to be cleared, identified by a System.Windows.DependencyProperty object reference.
        """
        pass

    def CoerceValue(self, dp):
        """
        CoerceValue(self: DependencyObject, dp: DependencyProperty)
            Coerces the value of the specified dependency property. This is accomplished by invoking any System.Windows.CoerceValueCallback function specified in property metadata for the dependency property as it 
             exists on the calling System.Windows.DependencyObject.
        
        
            dp: The identifier for the dependency property to coerce.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DependencyObject, obj: object) -> bool
        
            Determines whether a provided System.Windows.DependencyObject is equivalent to the current System.Windows.DependencyObject.
        
            obj: The System.Windows.DependencyObject  to compare to the current instance.
            Returns: true if the two instances are the same; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DependencyObject) -> int
        
            Gets a hash code for this System.Windows.DependencyObject.
            Returns: A signed 32-bit integer hash code.
        """
        pass

    def GetLocalValueEnumerator(self):
        """
        GetLocalValueEnumerator(self: DependencyObject) -> LocalValueEnumerator
        
            Creates a specialized enumerator for determining which dependency properties have locally set values on this System.Windows.DependencyObject.
            Returns: A specialized local value enumerator.
        """
        pass

    def GetValue(self, dp):
        """
        GetValue(self: DependencyObject, dp: DependencyProperty) -> object
        
            Returns the current effective value of a dependency property on this instance of a System.Windows.DependencyObject.
        
            dp: The System.Windows.DependencyProperty identifier of the property to retrieve the value for.
            Returns: Returns the current effective value.
        """
        pass

    def InvalidateProperty(self, dp):
        """
        InvalidateProperty(self: DependencyObject, dp: DependencyProperty)
            Re-evaluates the effective value for the specified dependency property
        
            dp: The System.Windows.DependencyProperty identifier of the property to invalidate.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.DependencyObject has been updated. The specific dependency property that changed is reported in the event data.
        
            e: Event data that will contain the dependency property identifier of interest, the property metadata for the type, and old and new values.
        """
        pass

    def ReadLocalValue(self, dp):
        """
        ReadLocalValue(self: DependencyObject, dp: DependencyProperty) -> object
        
            Returns the local value of a dependency property, if it exists.
        
            dp: The System.Windows.DependencyProperty identifier of the property to retrieve the value for.
            Returns: Returns the local value, or returns the sentinel value System.Windows.DependencyProperty.UnsetValue if no local value is set.
        """
        pass

    def SetCurrentValue(self, dp, value):
        """
        SetCurrentValue(self: DependencyObject, dp: DependencyProperty, value: object)
            Sets the value of a dependency property without changing its value source.
        
            dp: The identifier of the dependency property to set.
            value: The new local value.
        """
        pass

    def SetValue(self, *__args):
        """
        SetValue(self: DependencyObject, key: DependencyPropertyKey, value: object)
            Sets the local value of a read-only dependency property, specified by the System.Windows.DependencyPropertyKey identifier of the dependency property.
        
            key: The System.Windows.DependencyPropertyKey identifier of the property to set.
            value: The new local value.
        SetValue(self: DependencyObject, dp: DependencyProperty, value: object)
            Sets the local value of a dependency property, specified by its dependency property identifier.
        
            dp: The identifier of the dependency property to set.
            value: The new local value.
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

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DependencyObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.DependencyObjectType that wraps the CLR type of this instance.

Get: DependencyObjectType(self: DependencyObject) -> DependencyObjectType

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this instance is currently sealed (read-only).

Get: IsSealed(self: DependencyObject) -> bool

"""


