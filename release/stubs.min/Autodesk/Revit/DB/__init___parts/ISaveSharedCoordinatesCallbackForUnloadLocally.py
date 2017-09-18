class ISaveSharedCoordinatesCallbackForUnloadLocally:
 """
 An interface that is used to control Revit when trying to unload

    locally a Revit link with changes in shared coordinates.
 """
 def GetSaveModifiedLinksOptionForUnloadLocally(self,link):
  """
  GetSaveModifiedLinksOptionForUnloadLocally(self: ISaveSharedCoordinatesCallbackForUnloadLocally,link: RevitLinkType) -> SaveModifiedLinksOptionsForUnloadLocally

  

   Determines whether Revit should save the link or not prior

     to unloading the 

    link locally.

  

  

   link: The Revit link which has modified shared coordinates.

   Returns: The saving option when unloading locally a linked file which has been modified

  

    in-memory by shared coordinates operations.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
