class Array(object,ICloneable,IList,ICollection,IEnumerable,IStructuralComparable,IStructuralEquatable):
 """ Provides methods for creating,manipulating,searching,and sorting arrays,thereby serving as the base class for all arrays in the common language runtime. """
 @staticmethod
 def AsReadOnly(array):
  """ AsReadOnly[T](array: Array[T]) -> ReadOnlyCollection[T] """
  pass
 @staticmethod
 def BinarySearch(array,*__args):
  """
  BinarySearch[T](array: Array[T],value: T,comparer: IComparer[T]) -> int

  BinarySearch[T](array: Array[T],value: T) -> int

  BinarySearch[T](array: Array[T],index: int,length: int,value: T,comparer: IComparer[T]) -> int

  BinarySearch[T](array: Array[T],index: int,length: int,value: T) -> int

  BinarySearch(array: Array,index: int,length: int,value: object) -> int

  

   Searches a range of elements in a one-dimensional sorted System.Array for a value,using the 

    System.IComparable interface implemented by each element of the System.Array and by the 

    specified value.

  

  

   array: The sorted one-dimensional System.Array to search.

   index: The starting index of the range to search.

   length: The length of the range to search.

   value: The object to search for.

   Returns: The index of the specified value in the specified array,if value is found. If value is not 

    found and value is less than one or more elements in array,a negative number which is the 

    bitwise complement of the index of the first element that is larger than value. If value is not 

    found and value is greater than any of the elements in array,a negative number which is the 

    bitwise complement of (the index of the last element plus 1).

  

  BinarySearch(array: Array,value: object) -> int

  

   Searches an entire one-dimensional sorted System.Array for a specific element,using the 

    System.IComparable interface implemented by each element of the System.Array and by the 

    specified object.

  

  

   array: The sorted one-dimensional System.Array to search.

   value: The object to search for.

   Returns: The index of the specified value in the specified array,if value is found. If value is not 

    found and value is less than one or more elements in array,a negative number which is the 

    bitwise complement of the index of the first element that is larger than value. If value is not 

    found and value is greater than any of the elements in array,a negative number which is the 

    bitwise complement of (the index of the last element plus 1).

  

  BinarySearch(array: Array,index: int,length: int,value: object,comparer: IComparer) -> int

  

   Searches a range of elements in a one-dimensional sorted System.Array for a value,using the 

    specified System.Collections.IComparer interface.

  

  

   array: The sorted one-dimensional System.Array to search.

   index: The starting index of the range to search.

   length: The length of the range to search.

   value: The object to search for.

   comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- null to use 

    the System.IComparable implementation of each element.

  

   Returns: The index of the specified value in the specified array,if value is found. If value is not 

    found and value is less than one or more elements in array,a negative number which is the 

    bitwise complement of the index of the first element that is larger than value. If value is not 

    found and value is greater than any of the elements in array,a negative number which is the 

    bitwise complement of (the index of the last element plus 1).

  

  BinarySearch(array: Array,value: object,comparer: IComparer) -> int

  

   Searches an entire one-dimensional sorted System.Array for a value using the specified 

    System.Collections.IComparer interface.

  

  

   array: The sorted one-dimensional System.Array to search.

   value: The object to search for.

   comparer: The System.Collections.IComparer implementation to use when comparing elements.-or- null to use 

    the System.IComparable implementation of each element.

  

   Returns: The index of the specified value in the specified array,if value is found. If value is not 

    found and value is less than one or more elements in array,a negative number which is the 

    bitwise complement of the index of the first element that is larger than value. If value is not 

    found and value is greater than any of the elements in array,a negative number which is the 

    bitwise complement of (the index of the last element plus 1).
  """
  pass
 @staticmethod
 def Clear(array,index,length):
  """
  Clear(array: Array,index: int,length: int)

   Sets a range of elements in the System.Array to zero,to false,or to null,depending on the 

    element type.

  

  

   array: The System.Array whose elements need to be cleared.

   index: The starting index of the range of elements to clear.

   length: The number of elements to clear.
  """
  pass
 def Clone(self):
  """
  Clone(self: Array) -> object

  

   Creates a shallow copy of the System.Array.

   Returns: A shallow copy of the System.Array.
  """
  pass
 @staticmethod
 def ConstrainedCopy(sourceArray,sourceIndex,destinationArray,destinationIndex,length):
  """
  ConstrainedCopy(sourceArray: Array,sourceIndex: int,destinationArray: Array,destinationIndex: int,length: int)

   Copies a range of elements from an System.Array starting at the specified source index and 

    pastes them to another System.Array starting at the specified destination index.  Guarantees 

    that all changes are undone if the copy does not succeed completely.

  

  

   sourceArray: The System.Array that contains the data to copy.

   sourceIndex: A 32-bit integer that represents the index in the sourceArray at which copying begins.

   destinationArray: The System.Array that receives the data.

   destinationIndex: A 32-bit integer that represents the index in the destinationArray at which storing begins.

   length: A 32-bit integer that represents the number of elements to copy.
  """
  pass
 @staticmethod
 def ConvertAll(array,converter):
  """ ConvertAll[(TInput,TOutput)](array: Array[TInput],converter: Converter[TInput,TOutput]) -> Array[TOutput] """
  pass
 @staticmethod
 def Copy(sourceArray,*__args):
  """
  Copy(sourceArray: Array,destinationArray: Array,length: Int64)

   Copies a range of elements from an System.Array starting at the first element and pastes them 

    into another System.Array starting at the first element. The length is specified as a 64-bit 

    integer.

  

  

   sourceArray: The System.Array that contains the data to copy.

   destinationArray: The System.Array that receives the data.

   length: A 64-bit integer that represents the number of elements to copy. The integer must be between 

    zero and System.Int32.MaxValue,inclusive.

  

  Copy(sourceArray: Array,sourceIndex: Int64,destinationArray: Array,destinationIndex: Int64,length: Int64)

   Copies a range of elements from an System.Array starting at the specified source index and 

    pastes them to another System.Array starting at the specified destination index. The length and 

    the indexes are specified as 64-bit integers.

  

  

   sourceArray: The System.Array that contains the data to copy.

   sourceIndex: A 64-bit integer that represents the index in the sourceArray at which copying begins.

   destinationArray: The System.Array that receives the data.

   destinationIndex: A 64-bit integer that represents the index in the destinationArray at which storing begins.

   length: A 64-bit integer that represents the number of elements to copy. The integer must be between 

    zero and System.Int32.MaxValue,inclusive.

  

  Copy(sourceArray: Array,destinationArray: Array,length: int)

   Copies a range of elements from an System.Array starting at the first element and pastes them 

    into another System.Array starting at the first element. The length is specified as a 32-bit 

    integer.

  

  

   sourceArray: The System.Array that contains the data to copy.

   destinationArray: The System.Array that receives the data.

   length: A 32-bit integer that represents the number of elements to copy.

  Copy(sourceArray: Array,sourceIndex: int,destinationArray: Array,destinationIndex: int,length: int)

   Copies a range of elements from an System.Array starting at the specified source index and 

    pastes them to another System.Array starting at the specified destination index. The length and 

    the indexes are specified as 32-bit integers.

  

  

   sourceArray: The System.Array that contains the data to copy.

   sourceIndex: A 32-bit integer that represents the index in the sourceArray at which copying begins.

   destinationArray: The System.Array that receives the data.

   destinationIndex: A 32-bit integer that represents the index in the destinationArray at which storing begins.

   length: A 32-bit integer that represents the number of elements to copy.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: Array,array: Array,index: Int64)

   Copies all the elements of the current one-dimensional System.Array to the specified 

    one-dimensional System.Array starting at the specified destination System.Array index. The index 

    is specified as a 64-bit integer.

  

  

   array: The one-dimensional System.Array that is the destination of the elements copied from the current 

    System.Array.

  

   index: A 64-bit integer that represents the index in array at which copying begins.

  CopyTo(self: Array,array: Array,index: int)

   Copies all the elements of the current one-dimensional System.Array to the specified 

    one-dimensional System.Array starting at the specified destination System.Array index. The index 

    is specified as a 32-bit integer.

  

  

   array: The one-dimensional System.Array that is the destination of the elements copied from the current 

    System.Array.

  

   index: A 32-bit integer that represents the index in array at which copying begins.
  """
  pass
 @staticmethod
 def CreateInstance(elementType,*__args):
  """
  CreateInstance(elementType: Type,*lengths: Array[int]) -> Array

  

   Creates a multidimensional System.Array of the specified System.Type and dimension lengths,with 

    zero-based indexing. The dimension lengths are specified in an array of 32-bit integers.

  

  

   elementType: The System.Type of the System.Array to create.

   lengths: An array of 32-bit integers that represent the size of each dimension of the System.Array to 

    create.

  

   Returns: A new multidimensional System.Array of the specified System.Type with the specified length for 

    each dimension,using zero-based indexing.

  

  CreateInstance(elementType: Type,*lengths: Array[Int64]) -> Array

  

   Creates a multidimensional System.Array of the specified System.Type and dimension lengths,with 

    zero-based indexing. The dimension lengths are specified in an array of 64-bit integers.

  

  

   elementType: The System.Type of the System.Array to create.

   lengths: An array of 64-bit integers that represent the size of each dimension of the System.Array to 

    create. Each integer in the array must be between zero and System.Int32.MaxValue,inclusive.

  

   Returns: A new multidimensional System.Array of the specified System.Type with the specified length for 

    each dimension,using zero-based indexing.

  

  CreateInstance(elementType: Type,lengths: Array[int],lowerBounds: Array[int]) -> Array

  

   Creates a multidimensional System.Array of the specified System.Type and dimension lengths,with 

    the specified lower bounds.

  

  

   elementType: The System.Type of the System.Array to create.

   lengths: A one-dimensional array that contains the size of each dimension of the System.Array to create.

   lowerBounds: A one-dimensional array that contains the lower bound (starting index) of each dimension of the 

    System.Array to create.

  

   Returns: A new multidimensional System.Array of the specified System.Type with the specified length and 

    lower bound for each dimension.

  

  CreateInstance(elementType: Type,length: int) -> Array

  

   Creates a one-dimensional System.Array of the specified System.Type and length,with zero-based 

    indexing.

  

  

   elementType: The System.Type of the System.Array to create.

   length: The size of the System.Array to create.

   Returns: A new one-dimensional System.Array of the specified System.Type with the specified length,using 

    zero-based indexing.

  

  CreateInstance(elementType: Type,length1: int,length2: int) -> Array

  

   Creates a two-dimensional System.Array of the specified System.Type and dimension lengths,with 

    zero-based indexing.

  

  

   elementType: The System.Type of the System.Array to create.

   length1: The size of the first dimension of the System.Array to create.

   length2: The size of the second dimension of the System.Array to create.

   Returns: A new two-dimensional System.Array of the specified System.Type with the specified length for 

    each dimension,using zero-based indexing.

  

  CreateInstance(elementType: Type,length1: int,length2: int,length3: int) -> Array

  

   Creates a three-dimensional System.Array of the specified System.Type and dimension lengths,

    with zero-based indexing.

  

  

   elementType: The System.Type of the System.Array to create.

   length1: The size of the first dimension of the System.Array to create.

   length2: The size of the second dimension of the System.Array to create.

   length3: The size of the third dimension of the System.Array to create.

   Returns: A new three-dimensional System.Array of the specified System.Type with the specified length for 

    each dimension,using zero-based indexing.
  """
  pass
 @staticmethod
 def Empty():
  """ Empty[T]() -> Array[T] """
  pass
 @staticmethod
 def Exists(array,match):
  """ Exists[T](array: Array[T],match: Predicate[T]) -> bool """
  pass
 @staticmethod
 def Find(array,match):
  """ Find[T](array: Array[T],match: Predicate[T]) -> T """
  pass
 @staticmethod
 def FindAll(array,match):
  """ FindAll[T](array: Array[T],match: Predicate[T]) -> Array[T] """
  pass
 @staticmethod
 def FindIndex(array,*__args):
  """
  FindIndex[T](array: Array[T],startIndex: int,count: int,match: Predicate[T]) -> int

  FindIndex[T](array: Array[T],startIndex: int,match: Predicate[T]) -> int

  FindIndex[T](array: Array[T],match: Predicate[T]) -> int
  """
  pass
 @staticmethod
 def FindLast(array,match):
  """ FindLast[T](array: Array[T],match: Predicate[T]) -> T """
  pass
 @staticmethod
 def FindLastIndex(array,*__args):
  """
  FindLastIndex[T](array: Array[T],startIndex: int,count: int,match: Predicate[T]) -> int

  FindLastIndex[T](array: Array[T],startIndex: int,match: Predicate[T]) -> int

  FindLastIndex[T](array: Array[T],match: Predicate[T]) -> int
  """
  pass
 @staticmethod
 def ForEach(array,action):
  """ ForEach[T](array: Array[T],action: Action[T]) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: Array) -> IEnumerator

  

   Returns an System.Collections.IEnumerator for the System.Array.

   Returns: An System.Collections.IEnumerator for the System.Array.
  """
  pass
 def GetLength(self,dimension):
  """
  GetLength(self: Array,dimension: int) -> int

  

   Gets a 32-bit integer that represents the number of elements in the specified dimension of the 

    System.Array.

  

  

   dimension: A zero-based dimension of the System.Array whose length needs to be determined.

   Returns: A 32-bit integer that represents the number of elements in the specified dimension.
  """
  pass
 def GetLongLength(self,dimension):
  """
  GetLongLength(self: Array,dimension: int) -> Int64

  

   Gets a 64-bit integer that represents the number of elements in the specified dimension of the 

    System.Array.

  

  

   dimension: A zero-based dimension of the System.Array whose length needs to be determined.

   Returns: A 64-bit integer that represents the number of elements in the specified dimension.
  """
  pass
 def GetLowerBound(self,dimension):
  """
  GetLowerBound(self: Array,dimension: int) -> int

  

   Gets the lower bound of the specified dimension in the System.Array.

  

   dimension: A zero-based dimension of the System.Array whose lower bound needs to be determined.

   Returns: The lower bound of the specified dimension in the System.Array.
  """
  pass
 def GetUpperBound(self,dimension):
  """
  GetUpperBound(self: Array,dimension: int) -> int

  

   Gets the upper bound of the specified dimension in the System.Array.

  

   dimension: A zero-based dimension of the System.Array whose upper bound needs to be determined.

   Returns: The upper bound of the specified dimension in the System.Array.
  """
  pass
 def GetValue(self,*__args):
  """
  GetValue(self: Array,index1: Int64,index2: Int64) -> object

  

   Gets the value at the specified position in the two-dimensional System.Array. The indexes are 

    specified as 64-bit integers.

  

  

   index1: A 64-bit integer that represents the first-dimension index of the System.Array element to get.

   index2: A 64-bit integer that represents the second-dimension index of the System.Array element to get.

   Returns: The value at the specified position in the two-dimensional System.Array.

  GetValue(self: Array,index: Int64) -> object

  

   Gets the value at the specified position in the one-dimensional System.Array. The index is 

    specified as a 64-bit integer.

  

  

   index: A 64-bit integer that represents the position of the System.Array element to get.

   Returns: The value at the specified position in the one-dimensional System.Array.

  GetValue(self: Array,*indices: Array[Int64]) -> object

  

   Gets the value at the specified position in the multidimensional System.Array. The indexes are 

    specified as an array of 64-bit integers.

  

  

   indices: A one-dimensional array of 64-bit integers that represent the indexes specifying the position of 

    the System.Array element to get.

  

   Returns: The value at the specified position in the multidimensional System.Array.

  GetValue(self: Array,index1: Int64,index2: Int64,index3: Int64) -> object

  

   Gets the value at the specified position in the three-dimensional System.Array. The indexes are 

    specified as 64-bit integers.

  

  

   index1: A 64-bit integer that represents the first-dimension index of the System.Array element to get.

   index2: A 64-bit integer that represents the second-dimension index of the System.Array element to get.

   index3: A 64-bit integer that represents the third-dimension index of the System.Array element to get.

   Returns: The value at the specified position in the three-dimensional System.Array.

  GetValue(self: Array,index: int) -> object

  

   Gets the value at the specified position in the one-dimensional System.Array. The index is 

    specified as a 32-bit integer.

  

  

   index: A 32-bit integer that represents the position of the System.Array element to get.

   Returns: The value at the specified position in the one-dimensional System.Array.

  GetValue(self: Array,*indices: Array[int]) -> object

  

   Gets the value at the specified position in the multidimensional System.Array. The indexes are 

    specified as an array of 32-bit integers.

  

  

   indices: A one-dimensional array of 32-bit integers that represent the indexes specifying the position of 

    the System.Array element to get.

  

   Returns: The value at the specified position in the multidimensional System.Array.

  GetValue(self: Array,index1: int,index2: int,index3: int) -> object

  

   Gets the value at the specified position in the three-dimensional System.Array. The indexes are 

    specified as 32-bit integers.

  

  

   index1: A 32-bit integer that represents the first-dimension index of the System.Array element to get.

   index2: A 32-bit integer that represents the second-dimension index of the System.Array element to get.

   index3: A 32-bit integer that represents the third-dimension index of the System.Array element to get.

   Returns: The value at the specified position in the three-dimensional System.Array.

  GetValue(self: Array,index1: int,index2: int) -> object

  

   Gets the value at the specified position in the two-dimensional System.Array. The indexes are 

    specified as 32-bit integers.

  

  

   index1: A 32-bit integer that represents the first-dimension index of the System.Array element to get.

   index2: A 32-bit integer that represents the second-dimension index of the System.Array element to get.

   Returns: The value at the specified position in the two-dimensional System.Array.
  """
  pass
 @staticmethod
 def IndexOf(array,value,startIndex=None,count=None):
  """
  IndexOf[T](array: Array[T],value: T) -> int

  IndexOf[T](array: Array[T],value: T,startIndex: int) -> int

  IndexOf[T](array: Array[T],value: T,startIndex: int,count: int) -> int

  IndexOf(array: Array,value: object) -> int

  

   Searches for the specified object and returns the index of the first occurrence within the 

    entire one-dimensional System.Array.

  

  

   array: The one-dimensional System.Array to search.

   value: The object to locate in array.

   Returns: The index of the first occurrence of value within the entire array,if found; otherwise,the 

    lower bound of the array minus 1.

  

  IndexOf(array: Array,value: object,startIndex: int) -> int

  

   Searches for the specified object and returns the index of the first occurrence within the range 

    of elements in the one-dimensional System.Array that extends from the specified index to the 

    last element.

  

  

   array: The one-dimensional System.Array to search.

   value: The object to locate in array.

   startIndex: The starting index of the search. 0 (zero) is valid in an empty array.

   Returns: The index of the first occurrence of value within the range of elements in array that extends 

    from startIndex to the last element,if found; otherwise,the lower bound of the array minus 1.

  

  IndexOf(array: Array,value: object,startIndex: int,count: int) -> int

  

   Searches for the specified object and returns the index of the first occurrence within the range 

    of elements in the one-dimensional System.Array that starts at the specified index and contains 

    the specified number of elements.

  

  

   array: The one-dimensional System.Array to search.

   value: The object to locate in array.

   startIndex: The starting index of the search. 0 (zero) is valid in an empty array.

   count: The number of elements in the section to search.

   Returns: The index of the first occurrence of value within the range of elements in array that starts at 

    startIndex and contains the number of elements specified in count,if found; otherwise,the 

    lower bound of the array minus 1.
  """
  pass
 def Initialize(self):
  """
  Initialize(self: Array)

   Initializes every element of the value-type System.Array by calling the default constructor of 

    the value type.
  """
  pass
 @staticmethod
 def LastIndexOf(array,value,startIndex=None,count=None):
  """
  LastIndexOf[T](array: Array[T],value: T) -> int

  LastIndexOf[T](array: Array[T],value: T,startIndex: int) -> int

  LastIndexOf[T](array: Array[T],value: T,startIndex: int,count: int) -> int

  LastIndexOf(array: Array,value: object) -> int

  

   Searches for the specified object and returns the index of the last occurrence within the entire 

    one-dimensional System.Array.

  

  

   array: The one-dimensional System.Array to search.

   value: The object to locate in array.

   Returns: The index of the last occurrence of value within the entire array,if found; otherwise,the 

    lower bound of the array minus 1.

  

  LastIndexOf(array: Array,value: object,startIndex: int) -> int

  

   Searches for the specified object and returns the index of the last occurrence within the range 

    of elements in the one-dimensional System.Array that extends from the first element to the 

    specified index.

  

  

   array: The one-dimensional System.Array to search.

   value: The object to locate in array.

   startIndex: The starting index of the backward search.

   Returns: The index of the last occurrence of value within the range of elements in array that extends 

    from the first element to startIndex,if found; otherwise,the lower bound of the array minus 1.

  

  LastIndexOf(array: Array,value: object,startIndex: int,count: int) -> int

  

   Searches for the specified object and returns the index of the last occurrence within the range 

    of elements in the one-dimensional System.Array that contains the specified number of elements 

    and ends at the specified index.

  

  

   array: The one-dimensional System.Array to search.

   value: The object to locate in array.

   startIndex: The starting index of the backward search.

   count: The number of elements in the section to search.

   Returns: The index of the last occurrence of value within the range of elements in array that contains 

    the number of elements specified in count and ends at startIndex,if found; otherwise,the lower 

    bound of the array minus 1.
  """
  pass
 @staticmethod
 def Resize(array,newSize):
  """ Resize[T](array: Array[T],newSize: int) -> Array[T] """
  pass
 @staticmethod
 def Reverse(array,index=None,length=None):
  """
  Reverse(array: Array,index: int,length: int)

   Reverses the sequence of the elements in a range of elements in the one-dimensional System.Array.

  

   array: The one-dimensional System.Array to reverse.

   index: The starting index of the section to reverse.

   length: The number of elements in the section to reverse.

  Reverse(array: Array)

   Reverses the sequence of the elements in the entire one-dimensional System.Array.

  

   array: The one-dimensional System.Array to reverse.
  """
  pass
 def SetValue(self,value,*__args):
  """
  SetValue(self: Array,value: object,index1: Int64,index2: Int64)

   Sets a value to the element at the specified position in the two-dimensional System.Array. The 

    indexes are specified as 64-bit integers.

  

  

   value: The new value for the specified element.

   index1: A 64-bit integer that represents the first-dimension index of the System.Array element to set.

   index2: A 64-bit integer that represents the second-dimension index of the System.Array element to set.

  SetValue(self: Array,value: object,index: Int64)

   Sets a value to the element at the specified position in the one-dimensional System.Array. The 

    index is specified as a 64-bit integer.

  

  

   value: The new value for the specified element.

   index: A 64-bit integer that represents the position of the System.Array element to set.

  SetValue(self: Array,value: object,*indices: Array[Int64])

   Sets a value to the element at the specified position in the multidimensional System.Array. The 

    indexes are specified as an array of 64-bit integers.

  

  

   value: The new value for the specified element.

   indices: A one-dimensional array of 64-bit integers that represent the indexes specifying the position of 

    the element to set.

  

  SetValue(self: Array,value: object,index1: Int64,index2: Int64,index3: Int64)

   Sets a value to the element at the specified position in the three-dimensional System.Array. The 

    indexes are specified as 64-bit integers.

  

  

   value: The new value for the specified element.

   index1: A 64-bit integer that represents the first-dimension index of the System.Array element to set.

   index2: A 64-bit integer that represents the second-dimension index of the System.Array element to set.

   index3: A 64-bit integer that represents the third-dimension index of the System.Array element to set.

  SetValue(self: Array,value: object,index1: int,index2: int)

   Sets a value to the element at the specified position in the two-dimensional System.Array. The 

    indexes are specified as 32-bit integers.

  

  

   value: The new value for the specified element.

   index1: A 32-bit integer that represents the first-dimension index of the System.Array element to set.

   index2: A 32-bit integer that represents the second-dimension index of the System.Array element to set.

  SetValue(self: Array,value: object,index: int)

   Sets a value to the element at the specified position in the one-dimensional System.Array. The 

    index is specified as a 32-bit integer.

  

  

   value: The new value for the specified element.

   index: A 32-bit integer that represents the position of the System.Array element to set.

  SetValue(self: Array,value: object,*indices: Array[int])

   Sets a value to the element at the specified position in the multidimensional System.Array. The 

    indexes are specified as an array of 32-bit integers.

  

  

   value: The new value for the specified element.

   indices: A one-dimensional array of 32-bit integers that represent the indexes specifying the position of 

    the element to set.

  

  SetValue(self: Array,value: object,index1: int,index2: int,index3: int)

   Sets a value to the element at the specified position in the three-dimensional System.Array. The 

    indexes are specified as 32-bit integers.

  

  

   value: The new value for the specified element.

   index1: A 32-bit integer that represents the first-dimension index of the System.Array element to set.

   index2: A 32-bit integer that represents the second-dimension index of the System.Array element to set.

   index3: A 32-bit integer that represents the third-dimension index of the System.Array element to set.
  """
  pass
 @staticmethod
 def Sort(*__args):
  """
  Sort[(TKey,TValue)](keys: Array[TKey],items: Array[TValue],index: int,length: int)Sort[T](array: Array[T],comparer: IComparer[T])Sort[(TKey,TValue)](keys: Array[TKey],items: Array[TValue])Sort[T](array: Array[T],index: int,length: int)Sort[(TKey,TValue)](keys: Array[TKey],items: Array[TValue],index: int,length: int,comparer: IComparer[TKey])Sort[T](array: Array[T],comparison: Comparison[T])Sort[(TKey,TValue)](keys: Array[TKey],items: Array[TValue],comparer: IComparer[TKey])Sort[T](array: Array[T],index: int,length: int,comparer: IComparer[T])Sort[T](array: Array[T])Sort(array: Array,index: int,length: int)

   Sorts the elements in a range of elements in a one-dimensional System.Array using the 

    System.IComparable implementation of each element of the System.Array.

  

  

   array: The one-dimensional System.Array to sort.

   index: The starting index of the range to sort.

   length: The number of elements in the range to sort.

  Sort(keys: Array,items: Array,index: int,length: int)

   Sorts a range of elements in a pair of one-dimensional System.Array objects (one contains the 

    keys and the other contains the corresponding items) based on the keys in the first System.Array 

    using the System.IComparable implementation of each key.

  

  

   keys: The one-dimensional System.Array that contains the keys to sort.

   items: The one-dimensional System.Array that contains the items that correspond to each of the keys in 

    the keysSystem.Array.-or-null to sort only the keysSystem.Array.

  

   index: The starting index of the range to sort.

   length: The number of elements in the range to sort.

  Sort(array: Array)

   Sorts the elements in an entire one-dimensional System.Array using the System.IComparable 

    implementation of each element of the System.Array.

  

  

   array: The one-dimensional System.Array to sort.

  Sort(keys: Array,items: Array)

   Sorts a pair of one-dimensional System.Array objects (one contains the keys and the other 

    contains the corresponding items) based on the keys in the first System.Array using the 

    System.IComparable implementation of each key.

  

  

   keys: The one-dimensional System.Array that contains the keys to sort.

   items: The one-dimensional System.Array that contains the items that correspond to each of the keys in 

    the keysSystem.Array.-or-null to sort only the keysSystem.Array.

  

  Sort(array: Array,index: int,length: int,comparer: IComparer)

   Sorts the elements in a range of elements in a one-dimensional System.Array using the specified 

    System.Collections.IComparer.

  

  

   array: The one-dimensional System.Array to sort.

   index: The starting index of the range to sort.

   length: The number of elements in the range to sort.

   comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-null to use 

    the System.IComparable implementation of each element.

  

  Sort(keys: Array,items: Array,index: int,length: int,comparer: IComparer)

   Sorts a range of elements in a pair of one-dimensional System.Array objects (one contains the 

    keys and the other contains the corresponding items) based on the keys in the first System.Array 

    using the specified System.Collections.IComparer.

  

  

   keys: The one-dimensional System.Array that contains the keys to sort.

   items: The one-dimensional System.Array that contains the items that correspond to each of the keys in 

    the keysSystem.Array.-or-null to sort only the keysSystem.Array.

  

   index: The starting index of the range to sort.

   length: The number of elements in the range to sort.

   comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-null to use 

    the System.IComparable implementation of each element.

  

  Sort(array: Array,comparer: IComparer)

   Sorts the elements in a one-dimensional System.Array using the specified 

    System.Collections.IComparer.

  

  

   array: The one-dimensional System.Array to sort.

   comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-null to use 

    the System.IComparable implementation of each element.

  

  Sort(keys: Array,items: Array,comparer: IComparer)

   Sorts a pair of one-dimensional System.Array objects (one contains the keys and the other 

    contains the corresponding items) based on the keys in the first System.Array using the 

    specified System.Collections.IComparer.

  

  

   keys: The one-dimensional System.Array that contains the keys to sort.

   items: The one-dimensional System.Array that contains the items that correspond to each of the keys in 

    the keysSystem.Array.-or-null to sort only the keysSystem.Array.

  

   comparer: The System.Collections.IComparer implementation to use when comparing elements.-or-null to use 

    the System.IComparable implementation of each element.
  """
  pass
 @staticmethod
 def TrueForAll(array,match):
  """ TrueForAll[T](array: Array[T],match: Predicate[T]) -> bool """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool

  

   Determines whether the System.Collections.IList contains a specific value.

  

   value: The object to locate in the System.Collections.IList.

   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __hash__(self,*args):
  """ x.__hash__() <==> hash(x) """
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
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(pythonType: type,items: object) -> object

  __new__(pythonType: type,items: ICollection) -> object
  """
  pass
 def __ne__(self,*args):
  pass
 def __radd__(self,*args):
  """ __radd__(data1: Array,data2: Array) -> Array """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: Array) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]=x.__setitem__(i,y) <==> x[i]=x.__setitem__(i,y) <==> x[i]= """
  pass
 IsFixedSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Array has a fixed size.



Get: IsFixedSize(self: Array) -> bool



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Array is read-only.



Get: IsReadOnly(self: Array) -> bool



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether access to the System.Array is synchronized (thread safe).



Get: IsSynchronized(self: Array) -> bool



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a 32-bit integer that represents the total number of elements in all the dimensions of the System.Array.



Get: Length(self: Array) -> int



"""

 LongLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a 64-bit integer that represents the total number of elements in all the dimensions of the System.Array.



Get: LongLength(self: Array) -> Int64



"""

 Rank=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rank (number of dimensions) of the System.Array.



Get: Rank(self: Array) -> int



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that can be used to synchronize access to the System.Array.



Get: SyncRoot(self: Array) -> object



"""


