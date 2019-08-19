# encoding: utf-8
# module Wms.RemotingImplementation.Shipments calls itself Shipments
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ShipmentMetaDataHelper():
    # no doc
    @staticmethod
    def CreateMetaDataForPackingSlip(shipment, packages, shipper, serviceLevel):
        """ CreateMetaDataForPackingSlip(shipment: HistoryShipment, packages: TransportPackages, shipper: IShipper, serviceLevel: ServiceBase) -> SerializableDictionary[str, str] """
        pass

    @staticmethod
    def GetMetaDataOfPackingSlip(shipmentId):
        """ GetMetaDataOfPackingSlip(shipmentId: int) -> SerializableDictionary[str, str] """
        pass

    __all__ = [
        'CreateMetaDataForPackingSlip',
        'GetMetaDataOfPackingSlip',
    ]

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ShipmentMetaDataHelper()

