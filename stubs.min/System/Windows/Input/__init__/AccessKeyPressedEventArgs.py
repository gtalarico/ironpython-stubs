class AccessKeyPressedEventArgs(RoutedEventArgs):
    """
    Provides data for the System.Windows.Input.AccessKeyManager�routed event.
    
    AccessKeyPressedEventArgs()
    AccessKeyPressedEventArgs(key: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, key=None):
        """
        __new__(cls: type)
        __new__(cls: type, key: str)
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a string representation of the access key that was pressed

Get: Key(self: AccessKeyPressedEventArgs) -> str

"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the scope for the element that raised this event.

Get: Scope(self: AccessKeyPressedEventArgs) -> object

Set: Scope(self: AccessKeyPressedEventArgs) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target for the event.

Get: Target(self: AccessKeyPressedEventArgs) -> UIElement

Set: Target(self: AccessKeyPressedEventArgs) = value
"""


