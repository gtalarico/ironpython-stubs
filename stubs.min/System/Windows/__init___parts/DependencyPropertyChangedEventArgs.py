class DependencyPropertyChangedEventArgs(object):
    """
    Provides data for various property changed events. Typically these events report effective value changes in the value of a read-only dependency property. Another usage is as part of a System.Windows.PropertyChangedCallback implementation.
    
    DependencyPropertyChangedEventArgs(property: DependencyProperty, oldValue: object, newValue: object)
    """
    def Equals(self, *__args):
        """
        Equals(self: DependencyPropertyChangedEventArgs, args: DependencyPropertyChangedEventArgs) -> bool
        
            Determines whether the provided System.Windows.DependencyPropertyChangedEventArgs is equivalent to the current System.Windows.DependencyPropertyChangedEventArgs.
        
            args: The System.Windows.DependencyPropertyChangedEventArgs to compare to the current System.Windows.DependencyPropertyChangedEventArgs
            Returns: true if the provided System.Windows.DependencyPropertyChangedEventArgs is equivalent to the current System.Windows.DependencyPropertyChangedEventArgs; otherwise, false.
        Equals(self: DependencyPropertyChangedEventArgs, obj: object) -> bool
        
            Determines whether the provided object is equivalent to the current System.Windows.DependencyPropertyChangedEventArgs.
        
            obj: The object to compare to the current System.Windows.DependencyPropertyChangedEventArgs.
            Returns: true if the provided object is equivalent to the current System.Windows.DependencyPropertyChangedEventArgs; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DependencyPropertyChangedEventArgs) -> int
        
            Gets a hash code  for this System.Windows.DependencyPropertyChangedEventArgs.
            Returns: A signed 32-bit integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, property, oldValue, newValue):
        """
        __new__(cls: type, property: DependencyProperty, oldValue: object, newValue: object)
        __new__[DependencyPropertyChangedEventArgs]() -> DependencyPropertyChangedEventArgs
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the property after the change.

Get: NewValue(self: DependencyPropertyChangedEventArgs) -> object

"""

    OldValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the property before the change.

Get: OldValue(self: DependencyPropertyChangedEventArgs) -> object

"""

    Property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the identifier for the dependency property where the value change occurred.

Get: Property(self: DependencyPropertyChangedEventArgs) -> DependencyProperty

"""


