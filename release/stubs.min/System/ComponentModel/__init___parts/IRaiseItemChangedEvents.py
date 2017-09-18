class IRaiseItemChangedEvents:
 """ Indicates whether a class converts property change events to System.ComponentModel.IBindingList.ListChanged events. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 RaisesItemChangedEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.ComponentModel.IRaiseItemChangedEvents object raises System.ComponentModel.IBindingList.ListChanged events.



Get: RaisesItemChangedEvents(self: IRaiseItemChangedEvents) -> bool



"""


