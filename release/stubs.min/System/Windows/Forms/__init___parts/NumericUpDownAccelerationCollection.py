class NumericUpDownAccelerationCollection(MarshalByRefObject,ICollection[NumericUpDownAcceleration],IEnumerable[NumericUpDownAcceleration],IEnumerable):
 """
 Represents a sorted collection of System.Windows.Forms.NumericUpDownAcceleration objects in the System.Windows.Forms.NumericUpDown control.

 

 NumericUpDownAccelerationCollection()
 """
 def Add(self,acceleration):
  """
  Add(self: NumericUpDownAccelerationCollection,acceleration: NumericUpDownAcceleration)

   Adds a new System.Windows.Forms.NumericUpDownAcceleration to the 

    System.Windows.Forms.NumericUpDownAccelerationCollection.

  

  

   acceleration: The System.Windows.Forms.NumericUpDownAcceleration to add to the 

    System.Windows.Forms.NumericUpDownAccelerationCollection.
  """
  pass
 def AddRange(self,accelerations):
  """
  AddRange(self: NumericUpDownAccelerationCollection,*accelerations: Array[NumericUpDownAcceleration])

   Adds the elements of the specified array to the 

    System.Windows.Forms.NumericUpDownAccelerationCollection,keeping the collection sorted.

  

  

   accelerations: An array of type System.Windows.Forms.NumericUpDownAcceleration  containing the objects to add 

    to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: NumericUpDownAccelerationCollection)

   Removes all elements from the System.Windows.Forms.NumericUpDownAccelerationCollection.
  """
  pass
 def Contains(self,acceleration):
  """
  Contains(self: NumericUpDownAccelerationCollection,acceleration: NumericUpDownAcceleration) -> bool

  

   Determines whether the System.Windows.Forms.NumericUpDownAccelerationCollection contains a 

    specific System.Windows.Forms.NumericUpDownAcceleration.

  

  

   acceleration: The System.Windows.Forms.NumericUpDownAcceleration to locate in the 

    System.Windows.Forms.NumericUpDownAccelerationCollection.

  

   Returns: true if the System.Windows.Forms.NumericUpDownAcceleration is found in the 

    System.Windows.Forms.NumericUpDownAccelerationCollection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: NumericUpDownAccelerationCollection,array: Array[NumericUpDownAcceleration],index: int)

   Copies the System.Windows.Forms.NumericUpDownAccelerationCollection values to a one-dimensional 

    System.Windows.Forms.NumericUpDownAcceleration instance at the specified index.

  

  

   array: The one-dimensional System.Windows.Forms.NumericUpDownAcceleration that is the destination of 

    the values copied from System.Windows.Forms.NumericUpDownAccelerationCollection.

  

   index: The index in array where copying begins.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def Remove(self,acceleration):
  """
  Remove(self: NumericUpDownAccelerationCollection,acceleration: NumericUpDownAcceleration) -> bool

  

   Removes the first occurrence of the specified System.Windows.Forms.NumericUpDownAcceleration 

    from the System.Windows.Forms.NumericUpDownAccelerationCollection.

  

  

   acceleration: The System.Windows.Forms.NumericUpDownAcceleration to remove from the collection.

   Returns: true if the System.Windows.Forms.NumericUpDownAcceleration is removed from 

    System.Windows.Forms.NumericUpDownAccelerationCollection; otherwise,false.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__(self: ICollection[NumericUpDownAcceleration],item: NumericUpDownAcceleration) -> bool """
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
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of objects in the System.Windows.Forms.NumericUpDownAccelerationCollection.



Get: Count(self: NumericUpDownAccelerationCollection) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.NumericUpDownAccelerationCollection is read-only.



Get: IsReadOnly(self: NumericUpDownAccelerationCollection) -> bool



"""


