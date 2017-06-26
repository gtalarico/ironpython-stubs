# encoding: utf-8
# module RevitServices.Elements calls itself Elements
# from RevitServices,Version=1.2.1.3083,Culture=neutral,PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class DisposeLogic(object):
 """ DisposeLogic() """
 IsClosingHomeworkspace=False
 IsShuttingDown=False


class ElementDeleteDelegate(MulticastDelegate,ICloneable,ISerializable):
 """ ElementDeleteDelegate(object: object,method: IntPtr) """
 def BeginInvoke(self,document,deleted,callback,object):
  """ BeginInvoke(self: ElementDeleteDelegate,document: Document,deleted: IEnumerable[ElementId],callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null,if the method represented by the current delegate does not require arguments.
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: ElementDeleteDelegate,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,document,deleted):
  """ Invoke(self: ElementDeleteDelegate,document: Document,deleted: IEnumerable[ElementId]) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without value in its invocation list; otherwise,this instance with its original invocation list.
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

class ElementTypeSpecificUpdater(object,IUpdater):
 # no doc
 def Execute(self,data):
  """ Execute(self: ElementTypeSpecificUpdater,data: UpdaterData) """
  pass
 def GetAdditionalInformation(self):
  """ GetAdditionalInformation(self: ElementTypeSpecificUpdater) -> str """
  pass
 def GetChangePriority(self):
  """ GetChangePriority(self: ElementTypeSpecificUpdater) -> ChangePriority """
  pass
 def GetUpdaterId(self):
  """ GetUpdaterId(self: ElementTypeSpecificUpdater) -> UpdaterId """
  pass
 def GetUpdaterName(self):
  """ GetUpdaterName(self: ElementTypeSpecificUpdater) -> str """
  pass
 def OnUpdated(self,*args):
  """ OnUpdated(self: ElementTypeSpecificUpdater,args: UpdaterArgs) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,id: AddInId) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Updated=None


class ElementUpdateDelegate(MulticastDelegate,ICloneable,ISerializable):
 """ ElementUpdateDelegate(object: object,method: IntPtr) """
 def BeginInvoke(self,updated,callback,object):
  """ BeginInvoke(self: ElementUpdateDelegate,updated: IEnumerable[str],callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null,if the method represented by the current delegate does not require arguments.
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: ElementUpdateDelegate,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,updated):
  """ Invoke(self: ElementUpdateDelegate,updated: IEnumerable[str]) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without value in its invocation list; otherwise,this instance with its original invocation list.
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

class ElementUpdateDelegateElementId(MulticastDelegate,ICloneable,ISerializable):
 """ ElementUpdateDelegateElementId(object: object,method: IntPtr) """
 def BeginInvoke(self,document,updated,callback,object):
  """ BeginInvoke(self: ElementUpdateDelegateElementId,document: Document,updated: IEnumerable[ElementId],callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null,if the method represented by the current delegate does not require arguments.
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: ElementUpdateDelegateElementId,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,document,updated):
  """ Invoke(self: ElementUpdateDelegateElementId,document: Document,updated: IEnumerable[ElementId]) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without value in its invocation list; otherwise,this instance with its original invocation list.
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

class ElementUpdateEventArgs(EventArgs):
 """ ElementUpdateEventArgs(doc: Document,elements: IEnumerable[ElementId],transactions: IEnumerable[str],operation: UpdateType) """
 def GetUniqueIds(self):
  """ GetUniqueIds(self: ElementUpdateEventArgs) -> IEnumerable[str] """
  pass
 @staticmethod
 def __new__(self,doc,elements,transactions,operation):
  """ __new__(cls: type,doc: Document,elements: IEnumerable[ElementId],transactions: IEnumerable[str],operation: UpdateType) """
  pass
 Elements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Elements(self: ElementUpdateEventArgs) -> IEnumerable[ElementId]

"""

 Operation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Operation(self: ElementUpdateEventArgs) -> UpdateType

"""

 RevitDocument=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RevitDocument(self: ElementUpdateEventArgs) -> Document

"""

 Transactions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Transactions(self: ElementUpdateEventArgs) -> IEnumerable[str]

"""


 UpdateType=None


class ElementUtils(object):
 # no doc
 @staticmethod
 def AllElementsOfType(document):
  """ AllElementsOfType[T](document: Document) -> IEnumerable[Element] """
  pass
 @staticmethod
 def TryGetElement(document,*__args):
# Error generating skeleton for function TryGetElement: Method must be called on a Type for which Type.IsGenericParameter is false.

 __all__=[
  'AllElementsOfType',
  'TryGetElement',
 ]


class RevitServicesUpdater(object):
 # no doc
 def AddUpdater(self,updater):
  """ AddUpdater(self: RevitServicesUpdater,updater: IUpdater) """
  pass
 def ApplicationDocumentChanged(self,sender,args):
  """ ApplicationDocumentChanged(self: RevitServicesUpdater,sender: object,args: DocumentChangedEventArgs) """
  pass
 @staticmethod
 def DisposeInstance():
  """ DisposeInstance() """
  pass
 @staticmethod
 def Initialize(updaters):
  """ Initialize(updaters: IEnumerable[IUpdater]) """
  pass
 def OnElementIdsAdded(self,*args):
  """ OnElementIdsAdded(self: RevitServicesUpdater,e: ElementUpdateEventArgs) """
  pass
 def OnElementsAdded(self,*args):
  """ OnElementsAdded(self: RevitServicesUpdater,e: ElementUpdateEventArgs) """
  pass
 def OnElementsDeleted(self,*args):
  """ OnElementsDeleted(self: RevitServicesUpdater,e: ElementUpdateEventArgs) """
  pass
 def OnElementsModified(self,*args):
  """ OnElementsModified(self: RevitServicesUpdater,e: ElementUpdateEventArgs) """
  pass
 def RemoveUpdater(self,updater):
  """ RemoveUpdater(self: RevitServicesUpdater,updater: IUpdater) """
  pass
 def RollBack(self,doc,deleted):
  """ RollBack(self: RevitServicesUpdater,doc: Document,deleted: ICollection[ElementId]) """
  pass
 def UnRegisterAllChangeHooks(self):
  """ UnRegisterAllChangeHooks(self: RevitServicesUpdater) """
  pass
 DocumentToWatch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DocumentToWatch(self: RevitServicesUpdater) -> Document

"""


 ElementAddedForID=None
 ElementsAdded=None
 ElementsDeleted=None
 ElementsModified=None
 ElementsUpdated=None
 IsInitialized=False


class SunPathUpdater(ElementTypeSpecificUpdater,IUpdater):
 """ SunPathUpdater(id: AddInId) """
 def Execute(self,data):
  """ Execute(self: SunPathUpdater,data: UpdaterData) """
  pass
 def GetAdditionalInformation(self):
  """ GetAdditionalInformation(self: SunPathUpdater) -> str """
  pass
 def GetUpdaterName(self):
  """ GetUpdaterName(self: SunPathUpdater) -> str """
  pass
 def OnUpdated(self,*args):
  """ OnUpdated(self: ElementTypeSpecificUpdater,args: UpdaterArgs) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,id):
  """ __new__(cls: type,id: AddInId) """
  pass

class UpdaterArgs(EventArgs):
 """ UpdaterArgs(added: ICollection[ElementId],modified: ICollection[ElementId],deleted: ICollection[ElementId]) """
 @staticmethod
 def __new__(self,added,modified,deleted):
  """ __new__(cls: type,added: ICollection[ElementId],modified: ICollection[ElementId],deleted: ICollection[ElementId]) """
  pass
 Added=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Added(self: UpdaterArgs) -> ICollection[ElementId]

Set: Added(self: UpdaterArgs)=value
"""

 Deleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Deleted(self: UpdaterArgs) -> ICollection[ElementId]

Set: Deleted(self: UpdaterArgs)=value
"""

 Modified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Modified(self: UpdaterArgs) -> ICollection[ElementId]

Set: Modified(self: UpdaterArgs)=value
"""



class UpdaterHandler(MulticastDelegate,ICloneable,ISerializable):
 """ UpdaterHandler(object: object,method: IntPtr) """
 def BeginInvoke(self,sender,args,callback,object):
  """ BeginInvoke(self: UpdaterHandler,sender: object,args: UpdaterArgs,callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- null,if the method represented by the current delegate does not require arguments.
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: UpdaterHandler,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,sender,args):
  """ Invoke(self: UpdaterHandler,sender: object,args: UpdaterArgs) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified delegate.
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without value in its invocation list; otherwise,this instance with its original invocation list.
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

