class ConversionLink(object):
 """ ConversionLink(partId: int) """
 def Delete(self):
  """ Delete(self: ConversionLink) -> bool """
  pass
 def Insert(self):
  """ Insert(self: ConversionLink) -> bool """
  pass
 def Modify(self):
  """ Modify(self: ConversionLink) -> bool """
  pass
 def Select(self):
  """ Select(self: ConversionLink) -> bool """
  pass
 @staticmethod
 def __new__(self,partId):
  """ __new__(cls: type,partId: int) """
  pass
 ApprovalStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ApprovalStatus(self: ConversionLink) -> ApprovalStatusEnum

Set: ApprovalStatus(self: ConversionLink)=value
"""

 ConversionStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ConversionStatus(self: ConversionLink) -> ConversionStatusEnum

Set: ConversionStatus(self: ConversionLink)=value
"""

 PartId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PartId(self: ConversionLink) -> int

"""

 RefModelId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RefModelId(self: ConversionLink) -> int

Set: RefModelId(self: ConversionLink)=value
"""

 RefModelObjectId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RefModelObjectId(self: ConversionLink) -> int

Set: RefModelObjectId(self: ConversionLink)=value
"""


 ApprovalStatusEnum=None
 ConversionStatusEnum=None

