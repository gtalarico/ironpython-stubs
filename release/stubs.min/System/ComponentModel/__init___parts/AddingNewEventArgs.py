class AddingNewEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.BindingSource.AddingNew event.

 

 AddingNewEventArgs()

 AddingNewEventArgs(newObject: object)
 """
 @staticmethod
 def __new__(self,newObject=None):
  """
  __new__(cls: type)

  __new__(cls: type,newObject: object)
  """
  pass
 NewObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object to be added to the binding list.



Get: NewObject(self: AddingNewEventArgs) -> object



Set: NewObject(self: AddingNewEventArgs)=value

"""


