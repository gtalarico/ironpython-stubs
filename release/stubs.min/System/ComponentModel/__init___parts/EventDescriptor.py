class EventDescriptor(MemberDescriptor):
 """ Provides information about an event. """
 def AddEventHandler(self,component,value):
  """
  AddEventHandler(self: EventDescriptor,component: object,value: Delegate)

   When overridden in a derived class,binds the event to the component.

  

   component: A component that provides events to the delegate.

   value: A delegate that represents the method that handles the event.
  """
  pass
 def RemoveEventHandler(self,component,value):
  """
  RemoveEventHandler(self: EventDescriptor,component: object,value: Delegate)

   When overridden in a derived class,unbinds the delegate from the component so that the delegate 

    will no longer receive events from the component.

  

  

   component: The component that the delegate is bound to.

   value: The delegate to unbind from the component.
  """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,name: str,attrs: Array[Attribute])

  __new__(cls: type,descr: MemberDescriptor)

  __new__(cls: type,descr: MemberDescriptor,attrs: Array[Attribute])
  """
  pass
 AttributeArray=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an array of attributes.



"""

 ComponentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the type of component this event is bound to.



Get: ComponentType(self: EventDescriptor) -> Type



"""

 EventType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets the type of delegate for the event.



Get: EventType(self: EventDescriptor) -> Type



"""

 IsMulticast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When overridden in a derived class,gets a value indicating whether the event delegate is a multicast delegate.



Get: IsMulticast(self: EventDescriptor) -> bool



"""

 NameHashCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the hash code for the name of the member,as specified in System.String.GetHashCode.



"""


