# encoding: utf-8
# module NCrontab
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CrontabException:
 """
 CrontabException()
 CrontabException(message: str)
 CrontabException(message: str,innerException: Exception)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class CrontabField:
 # no doc
 def Contains(self,value):
  """ Contains(self: CrontabField,value: int) -> bool """
  pass
 @staticmethod
 def Days(expression):
  """ Days(expression: str) -> CrontabField """
  pass
 @staticmethod
 def DaysOfWeek(expression):
  """ DaysOfWeek(expression: str) -> CrontabField """
  pass
 def Format(self,writer,noNames=None):
  """ Format(self: CrontabField,writer: TextWriter)Format(self: CrontabField,writer: TextWriter,noNames: bool) """
  pass
 def GetFirst(self):
  """ GetFirst(self: CrontabField) -> int """
  pass
 @staticmethod
 def Hours(expression):
  """ Hours(expression: str) -> CrontabField """
  pass
 @staticmethod
 def Minutes(expression):
  """ Minutes(expression: str) -> CrontabField """
  pass
 @staticmethod
 def Months(expression):
  """ Months(expression: str) -> CrontabField """
  pass
 def Next(self,start):
  """ Next(self: CrontabField,start: int) -> int """
  pass
 @staticmethod
 def Parse(kind,expression):
  """ Parse(kind: CrontabFieldKind,expression: str) -> CrontabField """
  pass
 def ToString(self,format=None):
  """
  ToString(self: CrontabField) -> str
  ToString(self: CrontabField,format: str) -> str
  """
  pass
 @staticmethod
 def TryParse(kind,expression,onError=None):
  """
  TryParse(kind: CrontabFieldKind,expression: str) -> ValueOrError[CrontabField]
  TryParse(kind: CrontabFieldKind,expression: str,onError: ExceptionHandler) -> ValueOrError[CrontabField]
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass

class CrontabFieldAccumulator:
 """ CrontabFieldAccumulator(object: object,method: IntPtr) """
 def BeginInvoke(self,start,end,interval,onError,callback,object):
  """ BeginInvoke(self: CrontabFieldAccumulator,start: int,end: int,interval: int,onError: ExceptionHandler,callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the 
    current delegate.-or- null,if the method represented by the current delegate does not 
    require arguments.
  
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: CrontabFieldAccumulator,result: IAsyncResult) -> ExceptionProvider """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,start,end,interval,onError):
  """ Invoke(self: CrontabFieldAccumulator,start: int,end: int,interval: int,onError: ExceptionHandler) -> ExceptionProvider """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is 
    equal to the specified delegate.
  
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate 
    without value in its invocation list; otherwise,this instance with its original 
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

class CrontabFieldImpl:
 # no doc
 def Format(self,field,writer,noNames=None):
  """ Format(self: CrontabFieldImpl,field: ICrontabField,writer: TextWriter)Format(self: CrontabFieldImpl,field: ICrontabField,writer: TextWriter,noNames: bool) """
  pass
 @staticmethod
 def FromKind(kind):
  """ FromKind(kind: CrontabFieldKind) -> CrontabFieldImpl """
  pass
 def Parse(self,str,acc):
  """ Parse(self: CrontabFieldImpl,str: str,acc: CrontabFieldAccumulator) """
  pass
 def TryParse(self,str,acc,onError):
  """ TryParse(self: CrontabFieldImpl,str: str,acc: CrontabFieldAccumulator,onError: ExceptionHandler) -> ExceptionProvider """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Kind=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Kind(self: CrontabFieldImpl) -> CrontabFieldKind

"""

 MaxValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaxValue(self: CrontabFieldImpl) -> int

"""

 MinValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MinValue(self: CrontabFieldImpl) -> int

"""

 ValueCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ValueCount(self: CrontabFieldImpl) -> int

"""


 Day=None
 DayOfWeek=None
 Hour=None
 Minute=None
 Month=None


class CrontabFieldKind:
 """ enum CrontabFieldKind,values: Day (2),DayOfWeek (4),Hour (1),Minute (0),Month (3) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Day=None
 DayOfWeek=None
 Hour=None
 Minute=None
 Month=None
 value__=None


class CrontabSchedule:
 # no doc
 def GetNextOccurrence(self,baseTime,endTime=None):
  """
  GetNextOccurrence(self: CrontabSchedule,baseTime: DateTime) -> DateTime
  GetNextOccurrence(self: CrontabSchedule,baseTime: DateTime,endTime: DateTime) -> DateTime
  """
  pass
 def GetNextOccurrences(self,baseTime,endTime):
  """ GetNextOccurrences(self: CrontabSchedule,baseTime: DateTime,endTime: DateTime) -> IEnumerable[DateTime] """
  pass
 @staticmethod
 def Parse(expression):
  """ Parse(expression: str) -> CrontabSchedule """
  pass
 def ToString(self):
  """ ToString(self: CrontabSchedule) -> str """
  pass
 @staticmethod
 def TryParse(expression):
  """ TryParse(expression: str) -> ValueOrError[CrontabSchedule] """
  pass

class ExceptionHandler:
 """ ExceptionHandler(object: object,method: IntPtr) """
 def BeginInvoke(self,e,callback,object):
  """ BeginInvoke(self: ExceptionHandler,e: Exception,callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the 
    current delegate.-or- null,if the method represented by the current delegate does not 
    require arguments.
  
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: ExceptionHandler,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,e):
  """ Invoke(self: ExceptionHandler,e: Exception) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is 
    equal to the specified delegate.
  
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate 
    without value in its invocation list; otherwise,this instance with its original 
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

class ExceptionProvider:
 """ ExceptionProvider(object: object,method: IntPtr) """
 def BeginInvoke(self,callback,object):
  """ BeginInvoke(self: ExceptionProvider,callback: AsyncCallback,object: object) -> IAsyncResult """
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
  
   args: An array of objects that are the arguments to pass to the method represented by the 
    current delegate.-or- null,if the method represented by the current delegate does not 
    require arguments.
  
   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: ExceptionProvider,result: IAsyncResult) -> Exception """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self):
  """ Invoke(self: ExceptionProvider) -> Exception """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate
  
   Removes an element from the invocation list of this System.MulticastDelegate that is 
    equal to the specified delegate.
  
  
   value: The delegate to search for in the invocation list.
   Returns: If value is found in the invocation list for this instance,then a new System.Delegate 
    without value in its invocation list; otherwise,this instance with its original 
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

class ICrontabField:
 # no doc
 def Contains(self,value):
  """ Contains(self: ICrontabField,value: int) -> bool """
  pass
 def GetFirst(self):
  """ GetFirst(self: ICrontabField) -> int """
  pass
 def Next(self,start):
  """ Next(self: ICrontabField,start: int) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class ValueOrError:
 """
 ValueOrError[T](value: T)
 ValueOrError[T](error: Exception)
 ValueOrError[T](provider: ExceptionProvider)
 """
 def ToString(self):
  """ ToString(self: ValueOrError[T]) -> str """
  pass
 def TryGetValue(self,errorValue):
  """ TryGetValue(self: ValueOrError[T],errorValue: T) -> T """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,value: T)
  __new__(cls: type,error: Exception)
  __new__(cls: type,provider: ExceptionProvider)
  __new__[ValueOrError`1]() -> ValueOrError[T]
  """
  pass
 Error=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Error(self: ValueOrError[T]) -> Exception

"""

 ErrorProvider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ErrorProvider(self: ValueOrError[T]) -> ExceptionProvider

"""

 HasValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasValue(self: ValueOrError[T]) -> bool

"""

 IsError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsError(self: ValueOrError[T]) -> bool

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Value(self: ValueOrError[T]) -> T

"""



