class ValueSource(object):
    """ Reports the information returned from System.Windows.DependencyPropertyHelper.GetValueSource(System.Windows.DependencyObject,System.Windows.DependencyProperty). """
    def Equals(self, o):
        """
        Equals(self: ValueSource, o: object) -> bool
        
            Returns a value indicating whether this System.Windows.ValueSource is equal to a specified object.
        
            o: The object to compare with this System.Windows.ValueSource.
            Returns: true if the provided object is equivalent to the current System.Windows.ValueSource; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ValueSource) -> int
        
            Returns the hash code for this System.Windows.ValueSource.
            Returns: A 32-bit unsigned integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BaseValueSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value of the System.Windows.BaseValueSource enumeration, which reports the source that provided the dependency property system with a value.

Get: BaseValueSource(self: ValueSource) -> BaseValueSource

"""

    IsAnimated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that declares whether the property is being animated.

Get: IsAnimated(self: ValueSource) -> bool

"""

    IsCoerced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that declares whether this value resulted from a System.Windows.CoerceValueCallback implementation applied to a dependency property.

Get: IsCoerced(self: ValueSource) -> bool

"""

    IsCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether the value was set by the System.Windows.DependencyObject.SetCurrentValue(System.Windows.DependencyProperty,System.Object) method.

Get: IsCurrent(self: ValueSource) -> bool

"""

    IsExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that declares whether this value resulted from an evaluated expression. This might be a System.Windows.Data.BindingExpression supporting a binding, or an internal expression such as those that support the DynamicResource Markup Extension.

Get: IsExpression(self: ValueSource) -> bool

"""


