class StylusButtonCollection(ReadOnlyCollection[StylusButton],IList[StylusButton],ICollection[StylusButton],IEnumerable[StylusButton],IEnumerable,IList,ICollection,IReadOnlyList[StylusButton],IReadOnlyCollection[StylusButton]):
 """ Contains a collection of System.Windows.Input.StylusButton objects. """
 def GetStylusButtonByGuid(self,guid):
  """
  GetStylusButtonByGuid(self: StylusButtonCollection,guid: Guid) -> StylusButton
  
   Gets the System.Windows.Input.StylusButton that the specified GUID identifies.
  
   guid: The System.Guid that specifies the desired System.Windows.Input.StylusButton.
   Returns: The System.Windows.Input.StylusButton of the specified GUID.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the System.Collections.Generic.IList that the System.Collections.ObjectModel.ReadOnlyCollection wraps.

"""


