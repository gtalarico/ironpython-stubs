class InertiaTranslationBehavior(object):
 """
 Controls deceleration on a translation manipulation during inertia.
 
 InertiaTranslationBehavior()
 """
 DesiredDeceleration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rate the linear movement slows in device-independent units (1/96th inch per unit) per squared millisecond.

Get: DesiredDeceleration(self: InertiaTranslationBehavior) -> float

Set: DesiredDeceleration(self: InertiaTranslationBehavior)=value
"""

 DesiredDisplacement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the linear movement of the manipulation at the end of inertia.

Get: DesiredDisplacement(self: InertiaTranslationBehavior) -> float

Set: DesiredDisplacement(self: InertiaTranslationBehavior)=value
"""

 InitialVelocity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial rate of linear movement at the start of the inertia phase.

Get: InitialVelocity(self: InertiaTranslationBehavior) -> Vector

Set: InitialVelocity(self: InertiaTranslationBehavior)=value
"""


