class TraversalRequest(object):
 """
 Represents a request to move focus to another control.
 
 TraversalRequest(focusNavigationDirection: FocusNavigationDirection)
 """
 @staticmethod
 def __new__(self,focusNavigationDirection):
  """ __new__(cls: type,focusNavigationDirection: FocusNavigationDirection) """
  pass
 FocusNavigationDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the traversal direction.

Get: FocusNavigationDirection(self: TraversalRequest) -> FocusNavigationDirection

"""

 Wrapped=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether focus traversal has reached the end of child elements that can have focus.

Get: Wrapped(self: TraversalRequest) -> bool

Set: Wrapped(self: TraversalRequest)=value
"""



# variables with complex values

