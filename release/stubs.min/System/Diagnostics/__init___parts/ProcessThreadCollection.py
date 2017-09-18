class ProcessThreadCollection(ReadOnlyCollectionBase,ICollection,IEnumerable):
 """
 Provides a strongly typed collection of System.Diagnostics.ProcessThread objects.

 

 ProcessThreadCollection(processThreads: Array[ProcessThread])
 """
 def Add(self,thread):
  """
  Add(self: ProcessThreadCollection,thread: ProcessThread) -> int

  

   Appends a process thread to the collection.

  

   thread: The thread to add to the collection.

   Returns: The zero-based index of the thread in the collection.
  """
  pass
 def Contains(self,thread):
  """
  Contains(self: ProcessThreadCollection,thread: ProcessThread) -> bool

  

   Determines whether the specified process thread exists in the collection.

  

   thread: A System.Diagnostics.ProcessThread instance that indicates the thread to find in this collection.

   Returns: true if the thread exists in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ProcessThreadCollection,array: Array[ProcessThread],index: int)

   Copies an array of System.Diagnostics.ProcessThread instances to the collection,at the 

    specified index.

  

  

   array: An array of System.Diagnostics.ProcessThread instances to add to the collection.

   index: The location at which to add the new instances.
  """
  pass
 def IndexOf(self,thread):
  """
  IndexOf(self: ProcessThreadCollection,thread: ProcessThread) -> int

  

   Provides the location of a specified thread within the collection.

  

   thread: The System.Diagnostics.ProcessThread whose index is retrieved.

   Returns: The zero-based index that defines the location of the thread within the 

    System.Diagnostics.ProcessThreadCollection.
  """
  pass
 def Insert(self,index,thread):
  """
  Insert(self: ProcessThreadCollection,index: int,thread: ProcessThread)

   Inserts a process thread at the specified location in the collection.

  

   index: The zero-based index indicating the location at which to insert the thread.

   thread: The thread to insert into the collection.
  """
  pass
 def Remove(self,thread):
  """
  Remove(self: ProcessThreadCollection,thread: ProcessThread)

   Deletes a process thread from the collection.

  

   thread: The thread to remove from the collection.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
 @staticmethod
 def __new__(self,processThreads):
  """
  __new__(cls: type)

  __new__(cls: type,processThreads: Array[ProcessThread])
  """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.



"""


