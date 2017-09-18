class RoutedEvent(object):
 """ Represents and identifies a routed event and declares its characteristics. """
 def AddOwner(self,ownerType):
  """
  AddOwner(self: RoutedEvent,ownerType: Type) -> RoutedEvent
  
   Associates another owner type with the routed event represented by a 
    System.Windows.RoutedEvent instance,and enables routing of the event and its 
    handling.
  
  
   ownerType: The type where the routed event is added.
   Returns: The identifier field for the event. This return value should be used to set a 
    public static read-only field that will store the identifier for the 
    representation of the routed event on the owning type. This field is typically 
    defined with public access,because user code must reference the field in order 
    to attach any instance handlers for the routed event when using the 
    System.Windows.UIElement.AddHandler(System.Windows.RoutedEvent,System.Delegate,S
    ystem.Boolean) utility method.
  """
  pass
 def ToString(self):
  """
  ToString(self: RoutedEvent) -> str
  
   Returns the string representation of this System.Windows.RoutedEvent.
   Returns: A string representation for this object,which is identical to the value 
    returned by System.Windows.RoutedEvent.Name.
  """
  pass
 HandlerType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handler type of the routed event.

Get: HandlerType(self: RoutedEvent) -> Type

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the identifying name of the routed event.

Get: Name(self: RoutedEvent) -> str

"""

 OwnerType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the registered owner type of the routed event.

Get: OwnerType(self: RoutedEvent) -> Type

"""

 RoutingStrategy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the routing strategy of the routed event.

Get: RoutingStrategy(self: RoutedEvent) -> RoutingStrategy

"""


