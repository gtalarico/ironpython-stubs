class PointCloudItem(object):
 """
 Represents a single item in a pointcloud. A PointCloud item 

    always has a location,but it has an optional normal vector and color.
 """
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of this point cloud item.



Get: Color(self: PointCloudItem) -> Color



Set: Color(self: PointCloudItem)=value

"""

 Hidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the hidden flag of this point cloud item.



Get: Hidden(self: PointCloudItem) -> bool



Set: Hidden(self: PointCloudItem)=value

"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of this point cloud item.



Get: Index(self: PointCloudItem) -> int



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the location of this point cloud item.



Get: Location(self: PointCloudItem) -> Point3d



Set: Location(self: PointCloudItem)=value

"""

 Normal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the normal vector for this point cloud item.



Get: Normal(self: PointCloudItem) -> Vector3d



Set: Normal(self: PointCloudItem)=value

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X component of this point cloud item location.



Get: X(self: PointCloudItem) -> float



Set: X(self: PointCloudItem)=value

"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y component of this point cloud item location.



Get: Y(self: PointCloudItem) -> float



Set: Y(self: PointCloudItem)=value

"""

 Z=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Z component of this point cloud item location.



Get: Z(self: PointCloudItem) -> float



Set: Z(self: PointCloudItem)=value

"""


