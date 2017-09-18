class TableLayoutControlCollection(ControlCollection,IList,ICollection,IEnumerable,ICloneable):
 """
 Represents a collection of child controls in a table layout container.

 

 TableLayoutControlCollection(container: TableLayoutPanel)
 """
 def Add(self,*__args):
  """
  Add(self: TableLayoutControlCollection,control: Control,column: int,row: int)

   Adds the specified control to the collection and positions it at the specified cell.

  

   control: The control to add.

   column: The column in which control will be placed.

   row: The row in which control will be placed.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,container):
  """ __new__(cls: type,container: TableLayoutPanel) """
  pass
 Container=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent System.Windows.Forms.TableLayoutPanel that contains the controls in the collection.



Get: Container(self: TableLayoutControlCollection) -> TableLayoutPanel



"""


