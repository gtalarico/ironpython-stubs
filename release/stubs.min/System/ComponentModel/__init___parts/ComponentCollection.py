class ComponentCollection(ReadOnlyCollectionBase,ICollection,IEnumerable):
 """
 Provides a read-only container for a collection of System.ComponentModel.IComponent objects.

 

 ComponentCollection(components: Array[IComponent])
 """
 def CopyTo(self,array,index):
  """
  CopyTo(self: ComponentCollection,array: Array[IComponent],index: int)

   Copies the entire collection to an array,starting writing at the specified array index.

  

   array: An System.ComponentModel.IComponent array to copy the objects in the collection to.

   index: The index of the array at which copying to should begin.
  """
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
 def __new__(self,components):
  """ __new__(cls: type,components: Array[IComponent]) """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.



"""


