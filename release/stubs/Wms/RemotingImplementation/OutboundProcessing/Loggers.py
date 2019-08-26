# encoding: utf-8
# module Wms.RemotingImplementation.OutboundProcessing.Loggers calls itself Loggers
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DirectOrderLogger():
    """ DirectOrderLogger(orderMapper: ObjectsMapper[DirectOrder, DirectOrders], linesMapper: ObjectsMapper[DirectOrderLine, DirectOrderLines], detailsMapper: ObjectsMapper[ItemIdentification, DirectOrderLineDetails]) """
    def Log(self, directOrder):
        """ Log(self: DirectOrderLogger, directOrder: DirectOrder) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderMapper, linesMapper, detailsMapper):
        """ __new__(cls: type, orderMapper: ObjectsMapper[DirectOrder, DirectOrders], linesMapper: ObjectsMapper[DirectOrderLine, DirectOrderLines], detailsMapper: ObjectsMapper[ItemIdentification, DirectOrderLineDetails]) """
        pass

    Instance = DirectOrderLogger()
    """hardcoded/returns an instance of the class"""

