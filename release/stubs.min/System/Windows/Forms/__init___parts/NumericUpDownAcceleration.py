class NumericUpDownAcceleration(object):
 """
 Provides information specifying how acceleration should be performed on a spin box (also known as an up-down control) when the up or down button is pressed for specified time period.

 

 NumericUpDownAcceleration(seconds: int,increment: Decimal)
 """
 @staticmethod
 def __new__(self,seconds,increment):
  """ __new__(cls: type,seconds: int,increment: Decimal) """
  pass
 Increment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the quantity to increment or decrement the displayed value during acceleration.



Get: Increment(self: NumericUpDownAcceleration) -> Decimal



Set: Increment(self: NumericUpDownAcceleration)=value

"""

 Seconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of seconds the up or down button must be pressed before the acceleration starts.



Get: Seconds(self: NumericUpDownAcceleration) -> int



Set: Seconds(self: NumericUpDownAcceleration)=value

"""


