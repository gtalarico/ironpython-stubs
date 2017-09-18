class SlabShapeEditor(object):
 """ An object used for Slab Shape Editing. """
 def DrawPoint(self,location):
  """
  DrawPoint(self: SlabShapeEditor,location: XYZ) -> SlabShapeVertex
  
   Adds a point to the corresponding slab,roof or floor.
  
   location: The location of the point.
   Returns: The newly created vertex.
  """
  pass
 def DrawSplitLine(self,startVertex,endVertex):
  """
  DrawSplitLine(self: SlabShapeEditor,startVertex: SlabShapeVertex,endVertex: SlabShapeVertex) -> SlabShapeCreaseArray
  
   Draws a split line on the corresponding slab,roof or floor.
  
   startVertex: The vertex to start the split line.
   endVertex: The vertex to end the split line.
   Returns: The newly created creases.
  """
  pass
 def Enable(self):
  """
  Enable(self: SlabShapeEditor)
   Enables the slab shape editing functionality.
  """
  pass
 def ModifySubElement(self,*__args):
  """
  ModifySubElement(self: SlabShapeEditor,vertex: SlabShapeVertex,offset: float)
   Manipulates the vertex on the corresponding slab,roof or floor.
  
   vertex: The vertex.
   offset: The new value of the vertex offset.
  ModifySubElement(self: SlabShapeEditor,crease: SlabShapeCrease,offset: float)
   Manipulates the crease on the corresponding slab,roof or floor.
  
   crease: The crease.
   offset: The new value of the crease offset,which is the average of offsets of its ends.
  """
  pass
 def PickSupport(self,gLine):
  """
  PickSupport(self: SlabShapeEditor,gLine: Line)
   Picks an element to support the slab.  This method will define split lines and 
    create constant bearing lines for the slab.
  
  
   gLine: A line from a support element such as a beam.
  """
  pass
 def ResetSlabShape(self):
  """
  ResetSlabShape(self: SlabShapeEditor)
   Removes the modifications made during editing and resets the element geometry 
    back to the unmodified state.
  """
  pass
 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the slab shape editing functionality is enabled.

Get: IsEnabled(self: SlabShapeEditor) -> bool

"""

 SlabShapeCreases=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """All of the creases that can be edited.

Get: SlabShapeCreases(self: SlabShapeEditor) -> SlabShapeCreaseArray

"""

 SlabShapeVertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """All of the vertices that can be edited.

Get: SlabShapeVertices(self: SlabShapeEditor) -> SlabShapeVertexArray

"""


