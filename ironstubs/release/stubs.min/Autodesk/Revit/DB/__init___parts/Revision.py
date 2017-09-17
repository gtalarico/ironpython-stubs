class Revision(Element,IDisposable):
 """ Represents a single revision in the project. """
 @staticmethod
 def CombineWithNext(document,revisionId):
  """
  CombineWithNext(document: Document,revisionId: ElementId) -> ISet[ElementId]
  
   Combines the specified Revision with the next Revision.
  
   document: The Document containing the Revisions.
   revisionId: The Revision that should have its clouds and tags associated with the next 
    Revision.
  
   Returns: The ids of all RevisionClouds that were reassigned to the next Revision.
  """
  pass
 @staticmethod
 def CombineWithPrevious(document,revisionId):
  """
  CombineWithPrevious(document: Document,revisionId: ElementId) -> ISet[ElementId]
  
   Combines the specified Revision with the previous Revision.
  
   document: The Document containing the Revisions.
   revisionId: The Revision that should have its clouds and tags associated with the previous 
    Revision.
  
   Returns: The ids of all RevisionClouds that were reassigned to the previous Revision.
  """
  pass
 @staticmethod
 def Create(document):
  """
  Create(document: Document) -> Revision
  
   Creates a new Revision in the project.
  
   document: The document of the new Revision.
   Returns: The newly created Revision.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 @staticmethod
 def GetAllRevisionIds(document):
  """
  GetAllRevisionIds(document: Document) -> IList[ElementId]
  
   Returns the ids of all Revisions in the project ordered by sequence number.
  
   document: The document containing the Revisions.
   Returns: The ids of all the Revisions in the document ordered by sequence number.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 @staticmethod
 def ReorderRevisionSequence(document,newSequence):
  """ ReorderRevisionSequence(document: Document,newSequence: IList[ElementId]) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description of this Revision.

Get: Description(self: Revision) -> str

Set: Description(self: Revision)=value
"""

 Issued=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this Revision has been issued.

Get: Issued(self: Revision) -> bool

Set: Issued(self: Revision)=value
"""

 IssuedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates who has issued or will issue this Revision.

Get: IssuedBy(self: Revision) -> str

Set: IssuedBy(self: Revision)=value
"""

 IssuedTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates to whom this Revision was or will be issued.

Get: IssuedTo(self: Revision) -> str

Set: IssuedTo(self: Revision)=value
"""

 NumberType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates what number type the Revision Number for this Revision should use.

Get: NumberType(self: Revision) -> RevisionNumberType

Set: NumberType(self: Revision)=value
"""

 RevisionDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The date of this Revision.

Get: RevisionDate(self: Revision) -> str

Set: RevisionDate(self: Revision)=value
"""

 RevisionNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Revision number of this revision.

Get: RevisionNumber(self: Revision) -> str

"""

 SequenceNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Sequence Number of this Revision.

Get: SequenceNumber(self: Revision) -> int

"""

 Visibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Controls the visibility of revision clouds and revision tags related to this Revision.

Get: Visibility(self: Revision) -> RevisionVisibility

Set: Visibility(self: Revision)=value
"""


