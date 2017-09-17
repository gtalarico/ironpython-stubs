class EventManager(object):
 """ Provides event-related utility methods that register routed events for class owners and add class handlers. """
 @staticmethod
 def GetRoutedEvents():
  """
  GetRoutedEvents() -> Array[RoutedEvent]
  
   Returns identifiers for routed events that have been registered to the event 
    system.
  
   Returns: An array of type System.Windows.RoutedEvent that contains the registered 
    objects.
  """
  pass
 @staticmethod
 def GetRoutedEventsForOwner(ownerType):
  """
  GetRoutedEventsForOwner(ownerType: Type) -> Array[RoutedEvent]
  
   Finds all routed event identifiers for events that are registered with the 
    provided owner type.
  
  
   ownerType: The type to start the search with. Base classes are included in the search.
   Returns: An array of matching routed event identifiers if any match is found; otherwise,
    null.
  """
  pass
 @staticmethod
 def RegisterClassHandler(classType,routedEvent,handler,handledEventsToo=None):
  """
  RegisterClassHandler(classType: Type,routedEvent: RoutedEvent,handler: Delegate,handledEventsToo: bool)
   Registers a class handler for a particular routed event,with the option to 
    handle events where event data is already marked handled.
  
  
   classType: The type of the class that is declaring class handling.
   routedEvent: The routed event identifier of the event to handle.
   handler: A reference to the class handler implementation.
   handledEventsToo: true to invoke this class handler even if arguments of the routed event have 
    been marked as handled; false to retain the default behavior of not invoking 
    the handler on any marked-handled event.
  
  RegisterClassHandler(classType: Type,routedEvent: RoutedEvent,handler: Delegate)
   Registers a class handler for a particular routed event.
  
   classType: The type of the class that is declaring class handling.
   routedEvent: The routed event identifier of the event to handle.
   handler: A reference to the class handler implementation.
  """
  pass
 @staticmethod
 def RegisterRoutedEvent(name,routingStrategy,handlerType,ownerType):
  """
  RegisterRoutedEvent(name: str,routingStrategy: RoutingStrategy,handlerType: Type,ownerType: Type) -> RoutedEvent
  
   Registers a new routed event with the Windows Presentation Foundation (WPF) 
    event system.
  
  
   name: The name of the routed event. The name must be unique within the owner type and 
    cannot be null or an empty string.
  
   routingStrategy: The routing strategy of the event as a value of the enumeration.
   handlerType: The type of the event handler. This must be a delegate type and cannot be null.
   ownerType: The owner class type of the routed event. This cannot be null.
   Returns: The identifier for the newly registered routed event. This identifier object 
    can now be stored as a static field in a class and then used as a parameter for 
    methods that attach handlers to the event. The routed event identifier is also 
    used for other event system APIs.
  """
  pass
 __all__=[
  'GetRoutedEvents',
  'GetRoutedEventsForOwner',
  'RegisterClassHandler',
  'RegisterRoutedEvent',
 ]

