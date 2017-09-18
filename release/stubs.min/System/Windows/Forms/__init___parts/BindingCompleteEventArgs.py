class BindingCompleteEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.Binding.BindingComplete event.

 

 BindingCompleteEventArgs(binding: Binding,state: BindingCompleteState,context: BindingCompleteContext,errorText: str,exception: Exception,cancel: bool)

 BindingCompleteEventArgs(binding: Binding,state: BindingCompleteState,context: BindingCompleteContext,errorText: str,exception: Exception)

 BindingCompleteEventArgs(binding: Binding,state: BindingCompleteState,context: BindingCompleteContext,errorText: str)

 BindingCompleteEventArgs(binding: Binding,state: BindingCompleteState,context: BindingCompleteContext)
 """
 @staticmethod
 def __new__(self,binding,state,context,errorText=None,exception=None,cancel=None):
  """
  __new__(cls: type,binding: Binding,state: BindingCompleteState,context: BindingCompleteContext,errorText: str,exception: Exception,cancel: bool)

  __new__(cls: type,binding: Binding,state: BindingCompleteState,context: BindingCompleteContext,errorText: str,exception: Exception)

  __new__(cls: type,binding: Binding,state: BindingCompleteState,context: BindingCompleteContext,errorText: str)

  __new__(cls: type,binding: Binding,state: BindingCompleteState,context: BindingCompleteContext)
  """
  pass
 Binding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the binding associated with this occurrence of a System.Windows.Forms.Binding.BindingComplete event.



Get: Binding(self: BindingCompleteEventArgs) -> Binding



"""

 BindingCompleteContext=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction of the binding operation.



Get: BindingCompleteContext(self: BindingCompleteEventArgs) -> BindingCompleteContext



"""

 BindingCompleteState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the completion state of the binding operation.



Get: BindingCompleteState(self: BindingCompleteEventArgs) -> BindingCompleteState



"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text description of the error that occurred during the binding operation.



Get: ErrorText(self: BindingCompleteEventArgs) -> str



"""

 Exception=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the exception that occurred during the binding operation.



Get: Exception(self: BindingCompleteEventArgs) -> Exception



"""


