class AnimationException(SystemException,ISerializable,_Exception):
 """ The exception that is thrown when an error occurs while animating a property. """
 def add_SerializeObjectState(self,*args):
  """ add_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def remove_SerializeObjectState(self,*args):
  """ remove_SerializeObjectState(self: Exception,value: EventHandler[SafeSerializationEventArgs]) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Clock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the clock that generates the animated values.



Get: Clock(self: AnimationException) -> AnimationClock



"""

 Property=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the animated dependency property.



Get: Property(self: AnimationException) -> DependencyProperty



"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the animated object.



Get: Target(self: AnimationException) -> IAnimatable



"""


