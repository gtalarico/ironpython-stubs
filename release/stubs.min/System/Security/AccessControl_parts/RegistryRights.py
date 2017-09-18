class RegistryRights(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the access control rights that can be applied to registry objects.

 

 enum (flags) RegistryRights,values: ChangePermissions (262144),CreateLink (32),CreateSubKey (4),Delete (65536),EnumerateSubKeys (8),ExecuteKey (131097),FullControl (983103),Notify (16),QueryValues (1),ReadKey (131097),ReadPermissions (131072),SetValue (2),TakeOwnership (524288),WriteKey (131078)
 """
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
 ChangePermissions=None
 CreateLink=None
 CreateSubKey=None
 Delete=None
 EnumerateSubKeys=None
 ExecuteKey=None
 FullControl=None
 Notify=None
 QueryValues=None
 ReadKey=None
 ReadPermissions=None
 SetValue=None
 TakeOwnership=None
 value__=None
 WriteKey=None

