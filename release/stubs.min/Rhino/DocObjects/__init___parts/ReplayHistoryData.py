class ReplayHistoryData(object,IDisposable):
 # no doc
 def Dispose(self):
  """ Dispose(self: ReplayHistoryData) """
  pass
 def GetRhinoObjRef(self,id):
  """
  GetRhinoObjRef(self: ReplayHistoryData,id: int) -> ObjRef

  

   In ReplayHistory,use GetRhinoObjRef to convert the information

     in a history record 

    into the ObjRef that has up to date

     RhinoObject pointers

  

  

   id: HistoryRecord value id

   Returns: ObjRef on success,null if not successful
  """
  pass
 def TryGetBool(self,id,value):
  """ TryGetBool(self: ReplayHistoryData,id: int) -> (bool,bool) """
  pass
 def TryGetColor(self,id,value):
  """ TryGetColor(self: ReplayHistoryData,id: int) -> (bool,Color) """
  pass
 def TryGetDouble(self,id,value):
  """ TryGetDouble(self: ReplayHistoryData,id: int) -> (bool,float) """
  pass
 def TryGetGuid(self,id,value):
  """ TryGetGuid(self: ReplayHistoryData,id: int) -> (bool,Guid) """
  pass
 def TryGetInt(self,id,value):
  """ TryGetInt(self: ReplayHistoryData,id: int) -> (bool,int) """
  pass
 def TryGetPoint3d(self,id,value):
  """ TryGetPoint3d(self: ReplayHistoryData,id: int) -> (bool,Point3d) """
  pass
 def TryGetString(self,id,value):
  """ TryGetString(self: ReplayHistoryData,id: int) -> (bool,str) """
  pass
 def TryGetTransform(self,id,value):
  """ TryGetTransform(self: ReplayHistoryData,id: int) -> (bool,Transform) """
  pass
 def TryGetVector3d(self,id,value):
  """ TryGetVector3d(self: ReplayHistoryData,id: int) -> (bool,Vector3d) """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The document this record belongs to



Get: Document(self: ReplayHistoryData) -> RhinoDoc



"""

 HistoryVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """ReplayHistory overrides check the version number to insure the information

   saved in the history record is compatible with the current implementation

   of ReplayHistory



Get: HistoryVersion(self: ReplayHistoryData) -> int



"""

 RecordId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Each history record has a unique id that Rhino assigns when it adds the

   history record to the history record table



Get: RecordId(self: ReplayHistoryData) -> Guid



"""

 Results=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Results(self: ReplayHistoryData) -> Array[ReplayHistoryResult]



"""


