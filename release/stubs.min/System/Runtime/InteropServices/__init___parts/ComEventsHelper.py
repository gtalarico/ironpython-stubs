class ComEventsHelper(object):
 """ Provides methods that enable .NET Framework delegates that handle events to be added and removed from COM objects. """
 @staticmethod
 def Combine(rcw,iid,dispid,d):
  """
  Combine(rcw: object,iid: Guid,dispid: int,d: Delegate)

   Adds a delegate to the invocation list of events originating from a COM object.

  

   rcw: The COM object that triggers the events the caller would like to respond to.

   iid: The identifier of the source interface used by the COM object to trigger events.

   dispid: The dispatch identifier of the method on the source interface.

   d: The delegate to invoke when the COM event is fired.
  """
  pass
 @staticmethod
 def Remove(rcw,iid,dispid,d):
  """
  Remove(rcw: object,iid: Guid,dispid: int,d: Delegate) -> Delegate

  

   Removes a delegate from the invocation list of events originating from a COM object.

  

   rcw: The COM object the delegate is attached to.

   iid: The identifier of the source interface used by the COM object to trigger events.

   dispid: The dispatch identifier of the method on the source interface.

   d: The delegate to remove from the invocation list.

   Returns: The delegate that was removed from the invocation list.
  """
  pass
 __all__=[
  'Combine',
  'Remove',
 ]

