class ToolStripProfessionalRenderer(ToolStripRenderer):
 """
 Handles the painting functionality for System.Windows.Forms.ToolStrip objects,applying a custom palette and a streamlined style.

 

 ToolStripProfessionalRenderer()

 ToolStripProfessionalRenderer(professionalColorTable: ProfessionalColorTable)
 """
 @staticmethod
 def __new__(self,professionalColorTable=None):
  """
  __new__(cls: type)

  __new__(cls: type,professionalColorTable: ProfessionalColorTable)
  """
  pass
 ColorTable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the color palette used for painting.



Get: ColorTable(self: ToolStripProfessionalRenderer) -> ProfessionalColorTable



"""

 RoundedEdges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether edges of controls have a rounded rather than a square or sharp appearance.



Get: RoundedEdges(self: ToolStripProfessionalRenderer) -> bool



Set: RoundedEdges(self: ToolStripProfessionalRenderer)=value

"""


