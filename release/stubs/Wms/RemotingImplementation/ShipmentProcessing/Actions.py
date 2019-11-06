from Wms.RemotingObjects.ShippingLayers import State
# encoding: utf-8
# module Wms.RemotingImplementation.ShipmentProcessing.Actions calls itself Actions
# from Wms.RemotingImplementation, Version=1.24.1.1, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BaseState(State):
    """ BaseState() """
    def Next(self):
        """ Next(self: BaseState) -> State """
        pass

    def Run(self, args):
        """ Run(self: BaseState, *args: Array[object]) -> Array[object] """
        pass

    CacheKeyOfTransportPackages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKeyOfTransportPackages(self: BaseState) -> CacheKey

Set: CacheKeyOfTransportPackages(self: BaseState) = value
"""

    DfObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DfObject(self: BaseState) -> DataFlowObject[ProcessShipmentArgs]

Set: DfObject(self: BaseState) = value
"""

    Shipment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shipment(self: BaseState) -> ShipmentBase

Set: Shipment(self: BaseState) = value
"""

    TransportPackages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransportPackages(self: BaseState) -> TransportPackages

Set: TransportPackages(self: BaseState) = value
"""


    Instance = BaseState()
    """hardcoded/returns an instance of the class"""

class FinalizeState(BaseState):
    """ FinalizeState() """
    def Next(self):
        """ Next(self: FinalizeState) -> State """
        pass

    def Run(self, args):
        """ Run(self: FinalizeState, *args: Array[object]) -> Array[object] """
        pass

    Instance = FinalizeState()
    """hardcoded/returns an instance of the class"""

