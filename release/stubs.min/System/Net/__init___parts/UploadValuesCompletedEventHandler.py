class UploadValuesCompletedEventHandler(MulticastDelegate):
 """
 Represents the method that will handle the System.Net.WebClient.UploadValuesCompleted event of a System.Net.WebClient.
 
 UploadValuesCompletedEventHandler(object: object,method: IntPtr)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UploadValuesCompletedEventHandler()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def BeginInvoke(self,sender,e,callback,object):
  """ BeginInvoke(self: UploadValuesCompletedEventHandler,sender: object,e: UploadValuesCompletedEventArgs,callback: AsyncCallback,object: object) -> IAsyncResult """
  pass
 def CombineImpl(self,*args):
  """
  CombineImpl(self: MulticastDelegate,follow: Delegate) -> Delegate
  
   Combines this System.Delegate with the specified System.Delegate to form a new delegate.
  
   follow: The delegate to combine with this delegate.
   Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
  """
  pass
 def DynamicInvokeImpl(self,*args):
  """
  DynamicInvokeImpl(self: Delegate,args: Array[object]) -> object
  
   Dynamically invokes (late-bound) the method represented by the current delegate.
  
   args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null,if the method represented by the current delegate does not 
    require arguments.
  
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: UploadValuesCompletedEventHandler,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,sender,e):
  """ Invoke(self: UploadValuesCompletedEventHandler,sender: object,e: UploadValuesCompletedEventArgs) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without value in its invocation list; otherwise,this instance with its original 
    invocation list.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,object,method):
  """ __new__(cls: type,object: object,method: IntPtr) """
  pass
 def __reduce_ex__(self,*args):
  pass
