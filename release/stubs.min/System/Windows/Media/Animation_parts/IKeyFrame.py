class IKeyFrame:
 """ An System.Windows.Media.Animation.IKeyFrame interface implementation provides un-typed access to System.Windows.Media.Animation.KeyTime properties. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 KeyTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets System.Windows.Media.Animation.IKeyFrame.KeyTime values associated with a KeyFrame object.



Get: KeyTime(self: IKeyFrame) -> KeyTime



Set: KeyTime(self: IKeyFrame)=value

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value associated with a System.Windows.Media.Animation.KeyTime instance.



Get: Value(self: IKeyFrame) -> object



Set: Value(self: IKeyFrame)=value

"""


