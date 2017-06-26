class TraversalRequest(object):
    """
    Represents a request to move focus to another control.
    
    TraversalRequest(focusNavigationDirection: FocusNavigationDirection)
    """
    @staticmethod # known case of __new__
    def __new__(self, focusNavigationDirection):
        """ __new__(cls: type, focusNavigationDirection: FocusNavigationDirection) """
        pass

    FocusNavigationDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the traversal direction.

Get: FocusNavigationDirection(self: TraversalRequest) -> FocusNavigationDirection

"""

    Wrapped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether focus traversal has reached the end of child elements that can have focus.

Get: Wrapped(self: TraversalRequest) -> bool

Set: Wrapped(self: TraversalRequest) = value
"""



# variables with complex values

