class Random(object):
 """
 Represents a pseudo-random number generator,a device that produces a sequence of numbers that meet certain statistical requirements for randomness.

 

 Random()

 Random(Seed: int)
 """
 def Next(self,*__args):
  """
  Next(self: Random,maxValue: int) -> int

  

   Returns a nonnegative random number less than the specified maximum.

  

   maxValue: The exclusive upper bound of the random number to be generated. maxValue must be greater than or 

    equal to zero.

  

   Returns: A 32-bit signed integer greater than or equal to zero,and less than maxValue; that is,the 

    range of return values ordinarily includes zero but not maxValue. However,if maxValue equals 

    zero,maxValue is returned.

  

  Next(self: Random,minValue: int,maxValue: int) -> int

  

   Returns a random number within a specified range.

  

   minValue: The inclusive lower bound of the random number returned.

   maxValue: The exclusive upper bound of the random number returned. maxValue must be greater than or equal 

    to minValue.

  

   Returns: A 32-bit signed integer greater than or equal to minValue and less than maxValue; that is,the 

    range of return values includes minValue but not maxValue. If minValue equals maxValue,minValue 

    is returned.

  

  Next(self: Random) -> int

  

   Returns a nonnegative random number.

   Returns: A 32-bit signed integer greater than or equal to zero and less than System.Int32.MaxValue.
  """
  pass
 def NextBytes(self,buffer):
  """
  NextBytes(self: Random,buffer: Array[Byte])

   Fills the elements of a specified array of bytes with random numbers.

  

   buffer: An array of bytes to contain random numbers.
  """
  pass
 def NextDouble(self):
  """
  NextDouble(self: Random) -> float

  

   Returns a random number between 0.0 and 1.0.

   Returns: A double-precision floating point number greater than or equal to 0.0,and less than 1.0.
  """
  pass
 def Sample(self,*args):
  """
  Sample(self: Random) -> float

  

   Returns a random number between 0.0 and 1.0.

   Returns: A double-precision floating point number greater than or equal to 0.0,and less than 1.0.
  """
  pass
 @staticmethod
 def __new__(self,Seed=None):
  """
  __new__(cls: type)

  __new__(cls: type,Seed: int)
  """
  pass
