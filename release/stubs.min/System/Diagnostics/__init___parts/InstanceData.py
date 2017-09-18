class InstanceData(object):
 """
 Holds instance data associated with a performance counter sample.

 

 InstanceData(instanceName: str,sample: CounterSample)
 """
 @staticmethod
 def __new__(self,instanceName,sample):
  """ __new__(cls: type,instanceName: str,sample: CounterSample) """
  pass
 InstanceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the instance name associated with this instance data.



Get: InstanceName(self: InstanceData) -> str



"""

 RawValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the raw data value associated with the performance counter sample.



Get: RawValue(self: InstanceData) -> Int64



"""

 Sample=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the performance counter sample that generated this data.



Get: Sample(self: InstanceData) -> CounterSample



"""


