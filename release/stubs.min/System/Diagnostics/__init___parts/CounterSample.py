class CounterSample(object):
 """
 Defines a structure that holds the raw data for a performance counter.

 

 CounterSample(rawValue: Int64,baseValue: Int64,counterFrequency: Int64,systemFrequency: Int64,timeStamp: Int64,timeStamp100nSec: Int64,counterType: PerformanceCounterType)

 CounterSample(rawValue: Int64,baseValue: Int64,counterFrequency: Int64,systemFrequency: Int64,timeStamp: Int64,timeStamp100nSec: Int64,counterType: PerformanceCounterType,counterTimeStamp: Int64)
 """
 @staticmethod
 def Calculate(counterSample,nextCounterSample=None):
  """
  Calculate(counterSample: CounterSample,nextCounterSample: CounterSample) -> Single

  

   Calculates the performance data of the counter,using two sample points. This method is 

    generally used for calculated performance counter types,such as averages.

  

  

   counterSample: The System.Diagnostics.CounterSample structure to use as a base point for calculating 

    performance data.

  

   nextCounterSample: The System.Diagnostics.CounterSample structure to use as an ending point for calculating 

    performance data.

  

   Returns: The calculated performance value.

  Calculate(counterSample: CounterSample) -> Single

  

   Calculates the performance data of the counter,using a single sample point. This method is 

    generally used for uncalculated performance counter types.

  

  

   counterSample: The System.Diagnostics.CounterSample structure to use as a base point for calculating 

    performance data.

  

   Returns: The calculated performance value.
  """
  pass
 def Equals(self,*__args):
  """
  Equals(self: CounterSample,sample: CounterSample) -> bool

  

   Indicates whether the specified System.Diagnostics.CounterSample structure is equal to the 

    current System.Diagnostics.CounterSample structure.

  

  

   sample: The System.Diagnostics.CounterSample structure to be compared with this instance.

   Returns: true if sample is equal to the current instance; otherwise,false.

  Equals(self: CounterSample,o: object) -> bool

  

   Indicates whether the specified structure is a System.Diagnostics.CounterSample structure and is 

    identical to the current System.Diagnostics.CounterSample structure.

  

  

   o: The System.Diagnostics.CounterSample structure to be compared with the current structure.

   Returns: true if o is a System.Diagnostics.CounterSample structure and is identical to the current 

    instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CounterSample) -> int

  

   Gets a hash code for the current counter sample.

   Returns: A hash code for the current counter sample.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,rawValue,baseValue,counterFrequency,systemFrequency,timeStamp,timeStamp100nSec,counterType,counterTimeStamp=None):
  """
  __new__[CounterSample]() -> CounterSample

  

  __new__(cls: type,rawValue: Int64,baseValue: Int64,counterFrequency: Int64,systemFrequency: Int64,timeStamp: Int64,timeStamp100nSec: Int64,counterType: PerformanceCounterType)

  __new__(cls: type,rawValue: Int64,baseValue: Int64,counterFrequency: Int64,systemFrequency: Int64,timeStamp: Int64,timeStamp100nSec: Int64,counterType: PerformanceCounterType,counterTimeStamp: Int64)
  """
  pass
 def __ne__(self,*args):
  pass
 BaseValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an optional,base raw value for the counter.



Get: BaseValue(self: CounterSample) -> Int64



"""

 CounterFrequency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw counter frequency.



Get: CounterFrequency(self: CounterSample) -> Int64



"""

 CounterTimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the counter's time stamp.



Get: CounterTimeStamp(self: CounterSample) -> Int64



"""

 CounterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the performance counter type.



Get: CounterType(self: CounterSample) -> PerformanceCounterType



"""

 RawValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw value of the counter.



Get: RawValue(self: CounterSample) -> Int64



"""

 SystemFrequency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw system frequency.



Get: SystemFrequency(self: CounterSample) -> Int64



"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw time stamp.



Get: TimeStamp(self: CounterSample) -> Int64



"""

 TimeStamp100nSec=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw,high-fidelity time stamp.



Get: TimeStamp100nSec(self: CounterSample) -> Int64



"""


 Empty=None

