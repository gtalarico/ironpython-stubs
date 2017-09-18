class ColumnAttachment(object,IDisposable):
 """
 An object representing the attachment of the top or bottom of a column to some target:
    a floor,roof,ceiling,beam,or brace.
 """
 @staticmethod
 def AddColumnAttachment(doc,column,target,baseOrTop,cutColumnStyle,justification,attachOffset):
  """
  AddColumnAttachment(doc: Document,column: FamilyInstance,target: Element,baseOrTop: int,cutColumnStyle: ColumnAttachmentCutStyle,justification: ColumnAttachmentJustification,attachOffset: float)
   Attaches the column to the target. If an attachment already
     exists with the 
    same "baseOrTop" value,no attachment is made.
  
  
   doc: The document containing column and target.
   column: A column.
   target: A target element.
   baseOrTop: 0 to attach the column base,1 to attach the column top.
   cutColumnStyle: Control the handling of columns that intersect their targets.
   justification: Control the column extent in cases where the target is not a uniform height.
   attachOffset: An additional offset for the bottom. If positive,the column base or top will
   
      be higher than the attachment point; if negative,lower.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ColumnAttachment) """
  pass
 @staticmethod
 def GetColumnAttachment(column,*__args):
  """
  GetColumnAttachment(column: FamilyInstance,baseOrTop: int) -> ColumnAttachment
  
   Look up a column attachment. There is at most one attachment on
     the base 
    and one on the top.
  
  
   column: A column.
   baseOrTop: 0 for base,1 for top.
   Returns: The column attachment for the base or top of the column,or ll if that end
     
    of the column is unattached.
  
  GetColumnAttachment(column: FamilyInstance,targetId: ElementId) -> ColumnAttachment
  
   Look up a column attachment by specifying the target id.
  
   column: A column.
   targetId: Id of a target element.
   Returns: The column attachment attaching the column to the target,or ll if there
     is 
    no such attachment.
  """
  pass
 @staticmethod
 def IsValidColumn(familyInstance):
  """
  IsValidColumn(familyInstance: FamilyInstance) -> bool
  
   Says whether a FamilyInstance supports column attachments.
  
   familyInstance: A column.
  """
  pass
 @staticmethod
 def IsValidTarget(*__args):
  """
  IsValidTarget(column: FamilyInstance,target: Element) -> bool
  
   Says whether the element can be used as a target for a new attachment.
  
   column: The column to attach. If the target is a beam or brace,the column
     will be 
    checked to see if it is slanted. Otherwise,this argument
     is not used and 
    may be omitted.
  
   target: A proposed target element for a column attachment.
  IsValidTarget(forSlantedColumn: bool,target: Element) -> bool
  
   Says whether the element can be used as a target for a new attachment.
  
   forSlantedColumn: If true,check whether the target is valid for a slanted column;
     if false,
    check whether the target is valid for a vertical column.
  
   target: A proposed target element for a column attachment.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ColumnAttachment,disposing: bool) """
  pass
 @staticmethod
 def RemoveColumnAttachment(column,*__args):
  """
  RemoveColumnAttachment(column: FamilyInstance,baseOrTop: int)
   Removes an attachment at the top or base of a column,if there is one.
  
   column: A column.
   baseOrTop: 0 for base,1 for top.
  RemoveColumnAttachment(column: FamilyInstance,targetId: ElementId)
   Removes any attachment of the column to the specified target.
  
   column: A column.
   targetId: Id of a target element.
  """
  pass
 def SetJustification(self,justification):
  """
  SetJustification(self: ColumnAttachment,justification: ColumnAttachmentJustification)
   Setter of ColumnAttachmentJustification
  """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AttachOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The offset of the column attachment.

Get: AttachOffset(self: ColumnAttachment) -> float

Set: AttachOffset(self: ColumnAttachment)=value
"""

 BaseOrTop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this ColumnAttachment is at the base or top of the column.

Get: BaseOrTop(self: ColumnAttachment) -> int

"""

 CutStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies whether the column,or the attached element should be cut (or if neither should be cut).

Get: CutStyle(self: ColumnAttachment) -> ColumnAttachmentCutStyle

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ColumnAttachment) -> bool

"""

 Justification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the type of justification to apply to this ColumnAttachment.

Get: Justification(self: ColumnAttachment) -> ColumnAttachmentJustification

"""

 TargetId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the element that is attached to the column and is described by this ColumnAttachment.

Get: TargetId(self: ColumnAttachment) -> ElementId

"""


