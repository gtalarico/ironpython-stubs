# encoding: utf-8
# module Wms.RemotingImplementation.Shipments calls itself Shipments
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ShipmentMetaDataHelper(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipmentMetaDataHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CreateMetaDataForPackingSlip(shipment,packages,shipper,serviceLevel):
  """ CreateMetaDataForPackingSlip(shipment: HistoryShipment,packages: TransportPackages,shipper: IShipper,serviceLevel: ServiceBase) -> SerializableDictionary[str,str] """
  pass
 @staticmethod
 def GetMetaDataOfPackingSlip(shipmentId):
  """ GetMetaDataOfPackingSlip(shipmentId: int) -> SerializableDictionary[str,str] """
  pass
 __all__=[
  'CreateMetaDataForPackingSlip',
  'GetMetaDataOfPackingSlip',
 ]


