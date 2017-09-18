class EventHandlerList(object,IDisposable):
 """
 Provides a simple list of delegates. This class cannot be inherited.

 

 EventHandlerList()
 """
 def AddHandler(self,key,value):
  """
  AddHandler(self: EventHandlerList,key: object,value: Delegate)

   Adds a delegate to the list.

  

   key: The object that owns the event.

   value: The delegate to add to the list.
  """
  pass
 def AddHandlers(self,listToAddFrom):
  """
  AddHandlers(self: EventHandlerList,listToAddFrom: EventHandlerList)

   Adds a list of delegates to the current list.

  

   listToAddFrom: The list to add.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: EventHandlerList)

   Disposes the delegate list.
  """
  pass
 def RemoveHandler(self,key,value):
  """
  RemoveHandler(self: EventHandlerList,key: object,value: Delegate)

   Removes a delegate from the list.

  

   key: The object that owns the event.

   value: The delegate to remove from the list.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
