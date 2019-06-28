# encoding: utf-8
# module Wms.RemotingImplementation.ColliRegistration.Picking calls itself Picking
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PickReferenceExtensions:
 # no doc
 @staticmethod
 def AddOrUpdate(this,reference,type,warehouseCode,warehouseLocationCode,itemCode,itemId,quantity,parent,orderNumber):
  """ AddOrUpdate(this: List[ColloReference],reference: str,type: ReferenceType,warehouseCode: str,warehouseLocationCode: str,itemCode: str,itemId: str,quantity: Decimal,parent: str,orderNumber: str) """
  pass
 @staticmethod
 def FindPairs(this,*__args):
  """
  FindPairs(this: List[ColloReference],itemCode: str,warehouseCode: str,warehouseLocationCode: str,itemId: str) -> IEnumerable[ValueTuple[ColloReference,ColloReference]]
  FindPairs(this: List[ColloReference]) -> IEnumerable[ColloReferencePair]
  FindPairs(this: List[ColloReference],predicate: Func[ColloReference,bool]) -> IEnumerable[ColloReferencePair]
  FindPairs(this: List[ColloReference],innerReference: str,outerReference: str) -> IEnumerable[ColloReferencePair]
  FindPairs(this: List[ColloReference],itemCode: str,warehouseCode: str,locationCode: str,innerReference: str,outerReference: str,orderNumber: str,itemId: str) -> IEnumerable[ColloReferencePair]
  """
  pass
 __all__=[
  'AddOrUpdate',
  'FindPairs',
 ]


