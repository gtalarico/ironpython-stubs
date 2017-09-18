class StairsEditScope(EditScope,IDisposable):
 """
 StairsEditScope allows user to maintain a stairs-editing session.

 

 StairsEditScope(document: Document,transactionName: str)
 """
 def Dispose(self):
  """ Dispose(self: EditScope,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: EditScope,disposing: bool) """
  pass
 def Start(self,*__args):
  """
  Start(self: StairsEditScope,baseLevelId: ElementId,topLevelId: ElementId) -> ElementId

  

   Creates a new empty stairs element with a default stairs type in the specified 

    levels

     and then starts stairs edit mode and editing the new stairs.

  

  

   baseLevelId: The base level on which the stairs is to be placed.

   topLevelId: The top level where the stairs is to reach.

   Returns: ElementId of the new stairs.

  Start(self: StairsEditScope,stairsId: ElementId) -> ElementId

  

   Starts an stairs edit mode for an existing Stairs element

  

   stairsId: The stairs element to be edited.

   Returns: ElementId of the editing stairs. It should be the same as the input stairsId
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
 @staticmethod
 def __new__(self,document,transactionName):
  """ __new__(cls: type,document: Document,transactionName: str) """
  pass
 IsPermitted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Tells if the StairsEditScope is permitted to start.



Get: IsPermitted(self: StairsEditScope) -> bool



"""


