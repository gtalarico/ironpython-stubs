class InertiaExpansionBehavior(object):
 """
 Controls the deceleration of a resizing manipulation during inertia.
 
 InertiaExpansionBehavior()
 """
 DesiredDeceleration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rate that resizing slows in device-independent units (1/96th inch per unit) per square milliseconds.

Get: DesiredDeceleration(self: InertiaExpansionBehavior) -> float

Set: DesiredDeceleration(self: InertiaExpansionBehavior)=value
"""

 DesiredExpansion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the amount the element resizes at the end of inertia.

Get: DesiredExpansion(self: InertiaExpansionBehavior) -> Vector

Set: DesiredExpansion(self: InertiaExpansionBehavior)=value
"""

 InitialRadius=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial average radius.

Get: InitialRadius(self: InertiaExpansionBehavior) -> float

Set: InitialRadius(self: InertiaExpansionBehavior)=value
"""

 InitialVelocity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial rate the element resizes at the start of inertia.

Get: InitialVelocity(self: InertiaExpansionBehavior) -> Vector

Set: InitialVelocity(self: InertiaExpansionBehavior)=value
"""


