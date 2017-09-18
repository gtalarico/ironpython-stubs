class InstanceObject(RhinoObject):
 # no doc
 def Explode(self,explodeNestedInstances,pieces,pieceAttributes,pieceTransforms):
  """
  Explode(self: InstanceObject,explodeNestedInstances: bool) -> (Array[RhinoObject],Array[ObjectAttributes],Array[Transform])

  

   Explodes the instance reference into pieces.

  

   explodeNestedInstances: If true,then nested instance references are recursively exploded into pieces

     until 

    actual geometry is found. If false,an InstanceObject is added to

     the pieces out 

    parameter when this InstanceObject has nested references.
  """
  pass
 def UsesDefinition(self,definitionIndex,nestingLevel):
  """
  UsesDefinition(self: InstanceObject,definitionIndex: int) -> (bool,int)

  

   Determine if this reference uses an instance definition

   Returns: true or false depending on if the deifinition is used
  """
  pass
 InsertionPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Basepoint coordinates of a block.



Get: InsertionPoint(self: InstanceObject) -> Point3d



"""

 InstanceDefinition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """instance definition that this object uses.



Get: InstanceDefinition(self: InstanceObject) -> InstanceDefinition



"""

 InstanceXform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """transformation applied to an instance definition for this object.



Get: InstanceXform(self: InstanceObject) -> Transform



"""


