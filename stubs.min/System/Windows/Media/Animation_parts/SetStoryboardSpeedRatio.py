class SetStoryboardSpeedRatio(ControllableStoryboardAction):
 """
 A trigger action that changes the speed of a System.Windows.Media.Animation.Storyboard.
 
 SetStoryboardSpeedRatio()
 """
 SpeedRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a new System.Windows.Media.Animation.Storyboard animation speed as a ratio of the old animation speed.

Get: SpeedRatio(self: SetStoryboardSpeedRatio) -> float

Set: SpeedRatio(self: SetStoryboardSpeedRatio)=value
"""


