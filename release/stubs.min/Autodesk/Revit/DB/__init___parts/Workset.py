class Workset(WorksetPreview,IDisposable):
 """ Represents a workset in the document. """
 @staticmethod
 def Create(document,name):
  """
  Create(document: Document,name: str) -> Workset

  

   Creates a new workset.

  

   document: The document in which the new instance is created.

   name: The workset name.

   Returns: Returns the newly created workset.
  """
  pass
 def Dispose(self):
  """ Dispose(self: WorksetPreview,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WorksetPreview,disposing: bool) """
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
 IsEditable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the workset is editable.



Get: IsEditable(self: Workset) -> bool



"""

 IsOpen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the workset is open (rather than closed).



Get: IsOpen(self: Workset) -> bool



"""

 IsVisibleByDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the workset is visible by default.



Get: IsVisibleByDefault(self: Workset) -> bool



"""

 Kind=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Kind of the workset.



Get: Kind(self: Workset) -> WorksetKind



"""


