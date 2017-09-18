class PowerStatus(object):
 """ Indicates current system power status information. """
 BatteryChargeStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current battery charge status.



Get: BatteryChargeStatus(self: PowerStatus) -> BatteryChargeStatus



"""

 BatteryFullLifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the reported full charge lifetime of the primary battery power source in seconds.



Get: BatteryFullLifetime(self: PowerStatus) -> int



"""

 BatteryLifePercent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the approximate amount of full battery charge remaining.



Get: BatteryLifePercent(self: PowerStatus) -> Single



"""

 BatteryLifeRemaining=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the approximate number of seconds of battery time remaining.



Get: BatteryLifeRemaining(self: PowerStatus) -> int



"""

 PowerLineStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current system power status.



Get: PowerLineStatus(self: PowerStatus) -> PowerLineStatus



"""


