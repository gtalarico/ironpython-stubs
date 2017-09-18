class CounterCreationData(object):
 """
 Defines the counter type,name,and Help string for a custom counter.

 

 CounterCreationData(counterName: str,counterHelp: str,counterType: PerformanceCounterType)

 CounterCreationData()
 """
 @staticmethod
 def __new__(self,counterName=None,counterHelp=None,counterType=None):
  """
  __new__(cls: type)

  __new__(cls: type,counterName: str,counterHelp: str,counterType: PerformanceCounterType)
  """
  pass
 CounterHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the custom counter's description.



Get: CounterHelp(self: CounterCreationData) -> str



Set: CounterHelp(self: CounterCreationData)=value

"""

 CounterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the custom counter.



Get: CounterName(self: CounterCreationData) -> str



Set: CounterName(self: CounterCreationData)=value

"""

 CounterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the performance counter type of the custom counter.



Get: CounterType(self: CounterCreationData) -> PerformanceCounterType



Set: CounterType(self: CounterCreationData)=value

"""


