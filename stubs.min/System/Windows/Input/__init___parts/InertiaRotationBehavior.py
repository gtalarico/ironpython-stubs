class InertiaRotationBehavior(object):
    """
    Controls the deceleration of a rotation manipulation during inertia.
    
    InertiaRotationBehavior()
    """
    DesiredDeceleration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rate the rotation slows in degrees per squared millisecond.

Get: DesiredDeceleration(self: InertiaRotationBehavior) -> float

Set: DesiredDeceleration(self: InertiaRotationBehavior) = value
"""

    DesiredRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation, in degrees, at the end of the inertial movement.

Get: DesiredRotation(self: InertiaRotationBehavior) -> float

Set: DesiredRotation(self: InertiaRotationBehavior) = value
"""

    InitialVelocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initial rate of the rotation at the start of the inertia phase.

Get: InitialVelocity(self: InertiaRotationBehavior) -> float

Set: InitialVelocity(self: InertiaRotationBehavior) = value
"""


