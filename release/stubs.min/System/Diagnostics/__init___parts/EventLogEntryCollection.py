class EventLogEntryCollection(object,ICollection,IEnumerable):
 """ Defines size and enumerators for a collection of System.Diagnostics.EventLogEntry instances. """
 def CopyTo(self,entries,index):
  """
  CopyTo(self: EventLogEntryCollection,entries: Array[EventLogEntry],index: int)

   Copies the elements of the System.Diagnostics.EventLogEntryCollection to an array of 

    System.Diagnostics.EventLogEntry instances,starting at a particular array index.

  

  

   entries: The one-dimensional array of System.Diagnostics.EventLogEntry instances that is the destination 

    of the elements copied from the collection. The array must have zero-based indexing.

  

   index: The zero-based index in the array at which copying begins.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: EventLogEntryCollection) -> IEnumerator

  

   Supports a simple iteration over the System.Diagnostics.EventLogEntryCollection object.

   Returns: An object that can be used to iterate over the collection.
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of entries in the event log (that is,the number of elements in the System.Diagnostics.EventLogEntry collection).



Get: Count(self: EventLogEntryCollection) -> int



"""


