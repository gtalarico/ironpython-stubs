class FBXExportOptions(object):
 """
 3D-Studio Max (FBX) Export options.

 

 FBXExportOptions()
 """
 LevelsOfDetailValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The value of the levels of detail.



Get: LevelsOfDetailValue(self: FBXExportOptions) -> int



Set: LevelsOfDetailValue(self: FBXExportOptions)=value

"""

 StopOnError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether export process should stop when a view fails to export.



Get: StopOnError(self: FBXExportOptions) -> bool



Set: StopOnError(self: FBXExportOptions)=value

"""

 UseLevelsOfDetail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to use levels of detail,false otherwise.



Get: UseLevelsOfDetail(self: FBXExportOptions) -> bool



Set: UseLevelsOfDetail(self: FBXExportOptions)=value

"""

 WithoutBoundaryEdges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True to export without boundary edges,false otherwise.



Get: WithoutBoundaryEdges(self: FBXExportOptions) -> bool



Set: WithoutBoundaryEdges(self: FBXExportOptions)=value

"""


