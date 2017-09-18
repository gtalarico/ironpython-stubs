class ConstructionPlane(object):
 """
 Represents a contruction plane inside the document.

    Use Rhino.DocObjects.Tables.NamedConstructionPlaneTable

    methods and indexers to add and access a Rhino.DocObjects.ConstructionPlane.

 

 ConstructionPlane()
 """
 DepthBuffered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the grid is drawn on top of geometry.

   false=grid is always drawn behind 3d geometrytrue=grid is drawn at its depth as a 3d plane and grid lines obscure things behind the grid.



Get: DepthBuffered(self: ConstructionPlane) -> bool



Set: DepthBuffered(self: ConstructionPlane)=value

"""

 GridLineCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the total amount of grid lines in each direction.



Get: GridLineCount(self: ConstructionPlane) -> int



Set: GridLineCount(self: ConstructionPlane)=value

"""

 GridSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance between grid lines.



Get: GridSpacing(self: ConstructionPlane) -> float



Set: GridSpacing(self: ConstructionPlane)=value

"""

 GridXColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the grid X-axis mark.



Get: GridXColor(self: ConstructionPlane) -> Color



Set: GridXColor(self: ConstructionPlane)=value

"""

 GridYColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the grid Y-axis mark.



Get: GridYColor(self: ConstructionPlane) -> Color



Set: GridYColor(self: ConstructionPlane)=value

"""

 GridZColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the grid Z-axis mark.



Get: GridZColor(self: ConstructionPlane) -> Color



Set: GridZColor(self: ConstructionPlane)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the grid.



Get: Name(self: ConstructionPlane) -> str



"""

 Plane=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the geometric plane to use for construction.



Get: Plane(self: ConstructionPlane) -> Plane



Set: Plane(self: ConstructionPlane)=value

"""

 ShowAxes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the axes of the grid shuld be visible.



Get: ShowAxes(self: ConstructionPlane) -> bool



Set: ShowAxes(self: ConstructionPlane)=value

"""

 ShowGrid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the grid itself should be visible.



Get: ShowGrid(self: ConstructionPlane) -> bool



Set: ShowGrid(self: ConstructionPlane)=value

"""

 SnapSpacing=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """when "grid snap" is enabled,the distance between snap points.

   Typically this is the same distance as grid spacing.



Get: SnapSpacing(self: ConstructionPlane) -> float



Set: SnapSpacing(self: ConstructionPlane)=value

"""

 ThickLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the thicker,wider line.



Get: ThickLineColor(self: ConstructionPlane) -> Color



Set: ThickLineColor(self: ConstructionPlane)=value

"""

 ThickLineFrequency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the recurrence of a wider line on the grid.

   0: No lines are thick,all are drawn thin.1: All lines are thick.2: Every other line is thick.3: One line in three lines is thick (and two are thin).4: ...



Get: ThickLineFrequency(self: ConstructionPlane) -> int



Set: ThickLineFrequency(self: ConstructionPlane)=value

"""

 ThinLineColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of the thinner,less prominent line.



Get: ThinLineColor(self: ConstructionPlane) -> Color



Set: ThinLineColor(self: ConstructionPlane)=value

"""


