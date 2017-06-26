class BlockCollection(TextElementCollection[Block],IList,ICollection,IEnumerable,ICollection[Block],IEnumerable[Block]):
 """ Represents a collection of System.Windows.Documents.Block elements. System.Windows.Documents.BlockCollection defines the allowable child content of the System.Windows.Documents.FlowDocument,System.Windows.Documents.Section,System.Windows.Documents.ListItem,System.Windows.Documents.TableCell,System.Windows.Documents.Floater,and System.Windows.Documents.Figure elements. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 FirstBlock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first System.Windows.Documents.Block element within this instance of System.Windows.Documents.BlockCollection.

Get: FirstBlock(self: BlockCollection) -> Block

"""

 LastBlock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last System.Windows.Documents.Block element within this instance of System.Windows.Documents.BlockCollection.

Get: LastBlock(self: BlockCollection) -> Block

"""


