# encoding: utf-8
# module Grasshopper.Kernel.Undo calls itself Undo
# from Grasshopper,Version=1.0.0.20,Culture=neutral,PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_UndoAction(object,IGH_UndoAction,GH_ISerializable):
 # no doc
 def Internal_Redo(self,*args):
  """ Internal_Redo(self: GH_UndoAction,doc: GH_Document) """
  pass
 def Internal_Undo(self,*args):
  """ Internal_Undo(self: GH_UndoAction,doc: GH_Document) """
  pass
 def Read(self,reader):
  """ Read(self: GH_UndoAction,reader: GH_IReader) -> bool """
  pass
 def Redo(self,doc):
  """ Redo(self: GH_UndoAction,doc: GH_Document) """
  pass
 def Undo(self,doc):
  """ Undo(self: GH_UndoAction,doc: GH_Document) """
  pass
 def Write(self,writer):
  """ Write(self: GH_UndoAction,writer: GH_IWriter) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ExpiresDisplay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiresDisplay(self: GH_UndoAction) -> bool



"""

 ExpiresSolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiresSolution(self: GH_UndoAction) -> bool



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: State(self: GH_UndoAction) -> GH_UndoState



"""



class GH_ArchivedUndoAction(GH_UndoAction,IGH_UndoAction,GH_ISerializable):
 # no doc
 def Deserialize(self,*args):
  """ Deserialize(self: GH_ArchivedUndoAction,obj: GH_ISerializable) """
  pass
 def Internal_Redo(self,*args):
  """ Internal_Redo(self: GH_UndoAction,doc: GH_Document) """
  pass
 def Internal_Undo(self,*args):
  """ Internal_Undo(self: GH_UndoAction,doc: GH_Document) """
  pass
 def Read(self,reader):
  """ Read(self: GH_ArchivedUndoAction,reader: GH_IReader) -> bool """
  pass
 def Serialize(self,*args):
  """ Serialize(self: GH_ArchivedUndoAction,obj: GH_ISerializable) """
  pass
 def SerializeToByteArray(self,*args):
  """ SerializeToByteArray(self: GH_ArchivedUndoAction,obj: GH_ISerializable) -> Array[Byte] """
  pass
 def Write(self,writer):
  """ Write(self: GH_ArchivedUndoAction,writer: GH_IWriter) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 m_data=None


class GH_ObjectUndoAction(GH_UndoAction,IGH_UndoAction,GH_ISerializable):
 # no doc
 def Internal_Redo(self,*args):
  """ Internal_Redo(self: GH_ObjectUndoAction,doc: GH_Document) """
  pass
 def Internal_Undo(self,*args):
  """ Internal_Undo(self: GH_ObjectUndoAction,doc: GH_Document) """
  pass
 def Object_Redo(self,*args):
  """ Object_Redo(self: GH_ObjectUndoAction,doc: GH_Document,obj: IGH_DocumentObject) """
  pass
 def Object_Undo(self,*args):
  """ Object_Undo(self: GH_ObjectUndoAction,doc: GH_Document,obj: IGH_DocumentObject) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,object_id: Guid) """
  pass

class GH_UndoException(Exception,ISerializable,_Exception):
 """
 GH_UndoException(message: str)

 GH_UndoException(message: str,*args: Array[object])
 """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message,args=None):
  """
  __new__(cls: type,message: str)

  __new__(cls: type,message: str,*args: Array[object])
  """
  pass
 def __str__(self,*args):
  pass

class GH_UndoRecord(object):
 """
 GH_UndoRecord()

 GH_UndoRecord(name: str)

 GH_UndoRecord(name: str,action: IGH_UndoAction)

 GH_UndoRecord(name: str,*actions: Array[IGH_UndoAction])

 GH_UndoRecord(name: str,actions: IEnumerable[IGH_UndoAction])
 """
 def AddAction(self,action):
  """ AddAction(self: GH_UndoRecord,action: IGH_UndoAction) """
  pass
 def Redo(self,doc):
  """ Redo(self: GH_UndoRecord,doc: GH_Document) """
  pass
 def Undo(self,doc):
  """ Undo(self: GH_UndoRecord,doc: GH_Document) """
  pass
 @staticmethod
 def __new__(self,name=None,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,name: str)

  __new__(cls: type,name: str,action: IGH_UndoAction)

  __new__(cls: type,name: str,*actions: Array[IGH_UndoAction])

  __new__(cls: type,name: str,actions: IEnumerable[IGH_UndoAction])
  """
  pass
 ActionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ActionCount(self: GH_UndoRecord) -> int



"""

 Actions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Actions(self: GH_UndoRecord) -> IList[IGH_UndoAction]



"""

 ExpiresDisplay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiresDisplay(self: GH_UndoRecord) -> bool



"""

 ExpiresSolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiresSolution(self: GH_UndoRecord) -> bool



"""

 Guid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Guid(self: GH_UndoRecord) -> Guid



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: GH_UndoRecord) -> str



Set: Name(self: GH_UndoRecord)=value

"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: State(self: GH_UndoRecord) -> GH_UndoState



"""

 Time=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Time(self: GH_UndoRecord) -> DateTime



"""



class GH_UndoServer(object,IGH_DebugDescription):
 """ GH_UndoServer(nOwner: GH_Document) """
 def AppendToDebugLog(self,writer):
  """ AppendToDebugLog(self: GH_UndoServer,writer: GH_DebugDescriptionWriter) """
  pass
 def Clear(self):
  """ Clear(self: GH_UndoServer) """
  pass
 def ClearRedo(self):
  """ ClearRedo(self: GH_UndoServer) """
  pass
 def ClearUndo(self):
  """ ClearUndo(self: GH_UndoServer) """
  pass
 def PerformRedo(self):
  """ PerformRedo(self: GH_UndoServer) """
  pass
 def PerformUndo(self):
  """ PerformUndo(self: GH_UndoServer) """
  pass
 def PushUndoRecord(self,*__args):
  """
  PushUndoRecord(self: GH_UndoServer,name: str,action: GH_UndoAction) -> Guid

  PushUndoRecord(self: GH_UndoServer,record: GH_UndoRecord)
  """
  pass
 def RemoveRecord(self,id):
  """ RemoveRecord(self: GH_UndoServer,id: Guid) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,nOwner):
  """ __new__(cls: type,nOwner: GH_Document) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FirstRedoName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FirstRedoName(self: GH_UndoServer) -> str



"""

 FirstUndoName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FirstUndoName(self: GH_UndoServer) -> str



"""

 MaxRecords=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaxRecords(self: GH_UndoServer) -> int



Set: MaxRecords(self: GH_UndoServer)=value

"""

 RedoCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RedoCount(self: GH_UndoServer) -> int



"""

 RedoGuids=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RedoGuids(self: GH_UndoServer) -> List[Guid]



"""

 RedoNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RedoNames(self: GH_UndoServer) -> List[str]



"""

 UndoCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UndoCount(self: GH_UndoServer) -> int



"""

 UndoGuids=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UndoGuids(self: GH_UndoServer) -> List[Guid]



"""

 UndoNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UndoNames(self: GH_UndoServer) -> List[str]



"""



class GH_UndoState(Enum,IComparable,IFormattable,IConvertible):
 """ enum GH_UndoState,values: redo (1),undo (0) """
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
 redo=None
 undo=None
 value__=None


class IGH_UndoAction(GH_ISerializable):
 # no doc
 def Redo(self,doc):
  """ Redo(self: IGH_UndoAction,doc: GH_Document) """
  pass
 def Undo(self,doc):
  """ Undo(self: IGH_UndoAction,doc: GH_Document) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ExpiresDisplay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiresDisplay(self: IGH_UndoAction) -> bool



"""

 ExpiresSolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExpiresSolution(self: IGH_UndoAction) -> bool



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: State(self: IGH_UndoAction) -> GH_UndoState



"""



# variables with complex values

