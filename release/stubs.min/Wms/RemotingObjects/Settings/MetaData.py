# encoding: utf-8
# module Wms.RemotingObjects.Settings.MetaData calls itself MetaData
# from Wms.RemotingObjects,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GetValidValues:
 """ GetValidValues(object: object,method: IntPtr) """
 def BeginInvoke(self,callback,object):
  """ BeginInvoke(self: GetValidValues,callback: AsyncCallback,object: object) -> IAsyncResult """
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
  """ EndInvoke(self: GetValidValues,result: IAsyncResult) -> Hashtable """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo
  
   Returns a static method represented by the current System.MulticastDelegate.
   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self):
  """ Invoke(self: GetValidValues) -> Hashtable """
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

class ISystemSettingsAttribute:
 # no doc
 def UpdateInfo(self,row):
  """ UpdateInfo(self: ISystemSettingsAttribute,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class Group:
 """ Group(sortKey: str,name: str) """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: Group,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,sortKey,name):
  """ __new__(cls: type,sortKey: str,name: str) """
  pass
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: Group) -> str

Set: Name(self: Group)=value
"""

 SortKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SortKey(self: Group) -> str

Set: SortKey(self: Group)=value
"""



class Label:
 """ Label(value: str) """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: Label,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value):
  """ __new__(cls: type,value: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Value(self: Label) -> str

Set: Value(self: Label)=value
"""



class MachineSetting:
 """ MachineSetting() """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: MachineSetting,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class MaxLength:
 """ MaxLength(value: int) """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: MaxLength,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value):
  """ __new__(cls: type,value: int) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Value(self: MaxLength) -> int

Set: Value(self: MaxLength)=value
"""



class Renderer:
 """ Renderer(value: RenderingTypes) """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: Renderer,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value):
  """ __new__(cls: type,value: RenderingTypes) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Value(self: Renderer) -> RenderingTypes

Set: Value(self: Renderer)=value
"""



class RenderingTypes:
 """ enum RenderingTypes,values: Auto (0),PlainTextArea (2),RichTextArea (1),WarehouseCombo (3) """
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
 Auto=None
 PlainTextArea=None
 RichTextArea=None
 value__=None
 WarehouseCombo=None


class SettingAttributesHelper:
 """ SettingAttributesHelper() """
 @staticmethod
 def ConvertToTable(settings,topLevelOnly):
  """ ConvertToTable(settings: SystemSettings,topLevelOnly: bool) -> SystemSettingsTable """
  pass
 @staticmethod
 def GetMemberValue(settingsObject,member):
  """ GetMemberValue(settingsObject: object,member: MemberInfo) -> object """
  pass

class UserSetting:
 """ UserSetting() """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: UserSetting,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class ValidValuePattern:
 """
 ValidValuePattern(regex: str)
 ValidValuePattern(regex: str,errorMessage: str)
 """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: ValidValuePattern,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,regex,errorMessage=None):
  """
  __new__(cls: type,regex: str)
  __new__(cls: type,regex: str,errorMessage: str)
  """
  pass

class ValidValues:
 """ ValidValues(delegateName: str) """
 def UpdateInfo(self,row):
  """ UpdateInfo(self: ValidValues,row: SystemSettingsTableRow) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,delegateName):
  """ __new__(cls: type,delegateName: str) """
  pass
 DelegateName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DelegateName(self: ValidValues) -> str

Set: DelegateName(self: ValidValues)=value
"""



