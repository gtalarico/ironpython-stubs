class InlineCollection(TextElementCollection[Inline],IList,ICollection,IEnumerable,ICollection[Inline],IEnumerable[Inline]):
 """ Represents a collection of System.Windows.Documents.Inline elements. System.Windows.Documents.InlineCollection defines the allowable child content of the System.Windows.Documents.Paragraph,System.Windows.Documents.Span,and System.Windows.Controls.TextBlock elements. """
 def Add(self,*__args):
  """
  Add(self: InlineCollection,uiElement: UIElement)
   Adds an implicit System.Windows.Documents.InlineUIContainer with the supplied 
    System.Windows.UIElement already in it.
  
  
   uiElement: System.Windows.UIElement set as the 
    System.Windows.Documents.InlineUIContainer.Child property for the implicit 
    System.Windows.Documents.InlineUIContainer.
  
  Add(self: InlineCollection,text: str)
   Adds an implicit System.Windows.Documents.Run element with the given text,
    supplied as a System.String.
  
  
   text: Text set as the System.Windows.Documents.Run.Text property for the implicit 
    System.Windows.Documents.Run.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 FirstInline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the first System.Windows.Documents.Inline element within this instance of System.Windows.Documents.InlineCollection.

Get: FirstInline(self: InlineCollection) -> Inline

"""

 LastInline=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last System.Windows.Documents.Inline element within this instance of System.Windows.Documents.InlineCollection.

Get: LastInline(self: InlineCollection) -> Inline

"""


