class RefreshEventArgs(EventArgs):
 """
 Provides data for the System.ComponentModel.TypeDescriptor.Refreshed event.

 

 RefreshEventArgs(componentChanged: object)

 RefreshEventArgs(typeChanged: Type)
 """
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,componentChanged: object)

  __new__(cls: type,typeChanged: Type)
  """
  pass
 ComponentChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the component that changed its properties,events,or extenders.



Get: ComponentChanged(self: RefreshEventArgs) -> object



"""

 TypeChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Type that changed its properties or events.



Get: TypeChanged(self: RefreshEventArgs) -> Type



"""


