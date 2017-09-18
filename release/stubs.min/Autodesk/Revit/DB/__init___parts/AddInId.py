class AddInId(object,IDisposable):
 """
 Identifies an AddIn registered with Revit

 

 AddInId(val: Guid)
 """
 def Dispose(self):
  """ Dispose(self: AddInId) """
  pass
 def GetAddInName(self):
  """
  GetAddInName(self: AddInId) -> str

  

   name of addin associated with this AddInId

     Attempts to obtain the name from 

    loaded Third Party AddIns

  

   Returns: name of addin
  """
  pass
 def GetAddInNameFromDocument(self,aDoc):
  """
  GetAddInNameFromDocument(self: AddInId,aDoc: Document) -> str

  

   name of application associated with this ApplicationId

     First attempts to 

    obtain the name from AddInIds stored in the document.

     If unsuccessful,

    attempts to obtain the name from loaded Third Party AddIns.

  

  

   aDoc: target document

   Returns: name of application
  """
  pass
 def GetGUID(self):
  """
  GetGUID(self: AddInId) -> Guid

  

   value of the AddInId as a GUID

   Returns: GUID value of the AddInId
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: AddInId,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,val):
  """ __new__(cls: type,val: Guid) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: AddInId) -> bool



"""


