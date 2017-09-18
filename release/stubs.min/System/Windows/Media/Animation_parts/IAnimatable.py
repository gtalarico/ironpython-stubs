class IAnimatable:
 """ This type supports the WPF infrastructure and is not intended to be used directly from your code. To make a class animatable,it should derive from System.Windows.UIElement,System.Windows.ContentElement,or System.Windows.Media.Animation.Animatable. """
 def ApplyAnimationClock(self,dp,clock,handoffBehavior=None):
  """
  ApplyAnimationClock(self: IAnimatable,dp: DependencyProperty,clock: AnimationClock,handoffBehavior: HandoffBehavior)

   Applies the effect of a given System.Windows.Media.Animation.AnimationClock to a given 

    dependency property. The effect of the new System.Windows.Media.Animation.AnimationClock on any 

    current animations is determined by the value of the handoffBehavior parameter.

  

  

   dp: The System.Windows.DependencyProperty to animate.

   clock: The System.Windows.Media.Animation.AnimationClock that animates the property.

   handoffBehavior: Determines how the new System.Windows.Media.Animation.AnimationClock will transition from or 

    affect any current animations on the property.

  

  ApplyAnimationClock(self: IAnimatable,dp: DependencyProperty,clock: AnimationClock)

   Applies the effect of a given System.Windows.Media.Animation.AnimationClock to a given 

    dependency property.

  

  

   dp: The System.Windows.DependencyProperty to animate.

   clock: The System.Windows.Media.Animation.AnimationClock that animates the property.
  """
  pass
 def BeginAnimation(self,dp,animation,handoffBehavior=None):
  """
  BeginAnimation(self: IAnimatable,dp: DependencyProperty,animation: AnimationTimeline,handoffBehavior: HandoffBehavior)

   Initiates an animation sequence for the System.Windows.DependencyProperty.object,based on both 

    the specified System.Windows.Media.Animation.AnimationTimeline and 

    System.Windows.Media.Animation.HandoffBehavior.

  

  

   dp: The object to animate.

   animation: The timeline with the necessary functionality to tailor the new animation.

   handoffBehavior: The object specifying the manner in which to interact with all relevant animation sequences.

  BeginAnimation(self: IAnimatable,dp: DependencyProperty,animation: AnimationTimeline)

   Initiates an animation sequence for the System.Windows.DependencyProperty object,based on the 

    specified System.Windows.Media.Animation.AnimationTimeline.

  

  

   dp: The object to animate.

   animation: The timeline with the necessary functionality to animate the property.
  """
  pass
 def GetAnimationBaseValue(self,dp):
  """
  GetAnimationBaseValue(self: IAnimatable,dp: DependencyProperty) -> object

  

   Retrieves the base value of the specified System.Windows.DependencyProperty object.

  

   dp: The object for which the base value is being requested.

   Returns: The object representing the base value of Dp.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 HasAnimatedProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this instance has any animated properties.



Get: HasAnimatedProperties(self: IAnimatable) -> bool



"""


