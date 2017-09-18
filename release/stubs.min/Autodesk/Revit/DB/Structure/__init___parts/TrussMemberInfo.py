class TrussMemberInfo(object):
 """
 Provides access to the information of a truss member in Autodesk Revit.
 
 TrussMemberInfo()
 """
 hostTrussId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The host truss' ElementId of the member.

Get: hostTrussId(self: TrussMemberInfo) -> ElementId

Set: hostTrussId(self: TrussMemberInfo)=value
"""

 lockedToTruss=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether the member is locked to the host truss.

Get: lockedToTruss(self: TrussMemberInfo) -> bool

Set: lockedToTruss(self: TrussMemberInfo)=value
"""

 memberTypeKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Kind of the member in the truss.

Get: memberTypeKey(self: TrussMemberInfo) -> TrussMemberType

Set: memberTypeKey(self: TrussMemberInfo)=value
"""


