class ElectricalLoadClassification(Element,IDisposable):
 """
 The ElectricalLoadClassification class represents a serialized version of an instance of

    load classification.
 """
 @staticmethod
 def Create(ADoc,strName):
  """
  Create(ADoc: Document,strName: str) -> ElectricalLoadClassification

  

   Creates a new instance of load classification and adds it to the document.

  

   ADoc: The document where the element will be created and added.

   strName: The name of the electrical load classification to be created.

   Returns: The newly created load classification element.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ActualElectricalLoadLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name template for the actual load parameter on the load classification.



Get: ActualElectricalLoadLabel(self: ElectricalLoadClassification) -> str



Set: ActualElectricalLoadLabel(self: ElectricalLoadClassification)=value

"""

 DemandFactorId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The demand factor definition this load classification element uses.



Get: DemandFactorId(self: ElectricalLoadClassification) -> ElementId



Set: DemandFactorId(self: ElectricalLoadClassification)=value

"""

 LoadSummaryDemandFactorLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name template for the demand factor parameter of the load classification.



Get: LoadSummaryDemandFactorLabel(self: ElectricalLoadClassification) -> str



Set: LoadSummaryDemandFactorLabel(self: ElectricalLoadClassification)=value

"""

 Motor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if this load classification is to be used for motors.



Get: Motor(self: ElectricalLoadClassification) -> bool



"""

 PanelConnectedCurrentLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name template for the connected current parameter on the load classification.



Get: PanelConnectedCurrentLabel(self: ElectricalLoadClassification) -> str



Set: PanelConnectedCurrentLabel(self: ElectricalLoadClassification)=value

"""

 PanelConnectedLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name template for the connected load parameter of the load classification.



Get: PanelConnectedLabel(self: ElectricalLoadClassification) -> str



Set: PanelConnectedLabel(self: ElectricalLoadClassification)=value

"""

 PanelEstimatedCurrentLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name template for the estimated current parameter on the load classification.



Get: PanelEstimatedCurrentLabel(self: ElectricalLoadClassification) -> str



Set: PanelEstimatedCurrentLabel(self: ElectricalLoadClassification)=value

"""

 PanelEstimatedLabel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name template for the estimated demand parameter on the load classification.



Get: PanelEstimatedLabel(self: ElectricalLoadClassification) -> str



Set: PanelEstimatedLabel(self: ElectricalLoadClassification)=value

"""

 SpaceLoadClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The electrical load class associated with a space.



Get: SpaceLoadClass(self: ElectricalLoadClassification) -> ElectricalLoadClassificationSpace



Set: SpaceLoadClass(self: ElectricalLoadClassification)=value

"""


