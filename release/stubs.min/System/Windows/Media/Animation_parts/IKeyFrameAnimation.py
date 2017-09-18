class IKeyFrameAnimation:
 """ An System.Windows.Media.Animation.IKeyFrameAnimation interface implementation provides untyped access to key frame collection members. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 KeyFrames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an ordered collection System.Windows.Media.Animation.IKeyFrameAnimation.KeyFrames associated with this animation sequence.



Get: KeyFrames(self: IKeyFrameAnimation) -> IList



Set: KeyFrames(self: IKeyFrameAnimation)=value

"""


