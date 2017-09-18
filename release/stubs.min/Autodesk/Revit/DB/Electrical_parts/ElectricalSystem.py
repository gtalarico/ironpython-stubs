class ElectricalSystem(MEPSystem,IDisposable):
 """ Provides access to the Electrical System in Autodesk Revit MEP. """
 def AddToCircuit(self,components):
  """
  AddToCircuit(self: ElectricalSystem,components: ElementSet) -> bool

  

   Add a set of exist components to the Electrical System.

  

   components: The components added to the electrical system.

   Returns: If successful,all the components will add to the system. Otherwise ll is 

    returned.
  """
  pass
 def DisconnectPanel(self):
  """
  DisconnectPanel(self: ElectricalSystem)

   Disconnect the panel for the Electrical System.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def getElementsInNetwork(self,*args):
  """ getElementsInNetwork(self: MEPSystem) -> ElementSet """
  pass
 def getFlow(self,*args):
  """ getFlow(self: MEPSystem,param: BuiltInParameter) -> float """
  pass
 def getStaticPressure(self,*args):
  """ getStaticPressure(self: MEPSystem,param: BuiltInParameter) -> float """
  pass
 def NewWires(self,view,wiringType):
  """
  NewWires(self: ElectricalSystem,view: View,wiringType: WiringType) -> WireSet

  

   Create a bunch of wires for the electrical system.

  

   view: The view in which the wire is to be visible.

   wiringType: Specify the wiring type (Arc or Chamfer) that is to be applied to all newly 

    created wires.

  

   Returns: New created wires
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveFromCircuit(self,components):
  """
  RemoveFromCircuit(self: ElectricalSystem,components: ElementSet)

   remove a set of exist components from the Electrical System.

  

   components: The components removed from the electrical system.
  """
  pass
 def SelectPanel(self,panel):
  """
  SelectPanel(self: ElectricalSystem,panel: FamilyInstance)

   Set the panel for the Electrical System.

  

   panel: The panel of the electrical system.
  """
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
 ApparentCurrent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentCurrent value of the Electrical System.



Get: ApparentCurrent(self: ElectricalSystem) -> float



"""

 ApparentCurrentPhaseA=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentCurrentPhaseA value of the Electrical System.



Get: ApparentCurrentPhaseA(self: ElectricalSystem) -> float



"""

 ApparentCurrentPhaseB=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentCurrentPhaseB value of the Electrical System.



Get: ApparentCurrentPhaseB(self: ElectricalSystem) -> float



"""

 ApparentCurrentPhaseC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentCurrentPhaseC value of the Electrical System.



Get: ApparentCurrentPhaseC(self: ElectricalSystem) -> float



"""

 ApparentLoad=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentLoad value of the Electrical System.



Get: ApparentLoad(self: ElectricalSystem) -> float



"""

 ApparentLoadPhaseA=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentLoadPhaseA value of the Electrical System.



Get: ApparentLoadPhaseA(self: ElectricalSystem) -> float



"""

 ApparentLoadPhaseB=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentLoadPhaseB value of the Electrical System.



Get: ApparentLoadPhaseB(self: ElectricalSystem) -> float



"""

 ApparentLoadPhaseC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the ApparentLoadPhaseC value of the Electrical System.



Get: ApparentLoadPhaseC(self: ElectricalSystem) -> float



"""

 BalancedLoad=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Reports whether the BalancedLoad is on or off.



Get: BalancedLoad(self: ElectricalSystem) -> bool



"""

 CircuitNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the CircuitNumber of the Electrical System.



Get: CircuitNumber(self: ElectricalSystem) -> str



"""

 CircuitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the circuit type of the Electrical System.



Get: CircuitType(self: ElectricalSystem) -> CircuitType



"""

 GroundConductorsNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the GroundConductors Number of the Electrical System.



Get: GroundConductorsNumber(self: ElectricalSystem) -> int



"""

 HotConductorsNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the HotConductors Number of the Electrical System.



Get: HotConductorsNumber(self: ElectricalSystem) -> int



"""

 Length=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Length value of the Electrical System.



Get: Length(self: ElectricalSystem) -> float



"""

 LoadClassifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the LoadClassifications used in the Electrical System.



Get: LoadClassifications(self: ElectricalSystem) -> str



"""

 LoadName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get/Set the LoadName of the Electrical System.



Get: LoadName(self: ElectricalSystem) -> str



Set: LoadName(self: ElectricalSystem)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Name of the Electrical System.



Get: Name(self: ElectricalSystem) -> str



"""

 NeutralConductorsNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the NeutralConductors Number of the Electrical System.



Get: NeutralConductorsNumber(self: ElectricalSystem) -> int



"""

 PanelName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Panel name of the Electrical System.



Get: PanelName(self: ElectricalSystem) -> str



"""

 PolesNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Poles Number of the Electrical System.



Get: PolesNumber(self: ElectricalSystem) -> int



"""

 PowerFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the PowerFactor value of the Electrical System.



Get: PowerFactor(self: ElectricalSystem) -> float



"""

 PowerFactorState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the PowerFactorState type of the Electrical System.



Get: PowerFactorState(self: ElectricalSystem) -> PowerFactorStateType



"""

 Rating=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get/Set the Rating value of the Electrical System.



Get: Rating(self: ElectricalSystem) -> float



Set: Rating(self: ElectricalSystem)=value

"""

 RunsNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Runs Number of the Electrical System.



Get: RunsNumber(self: ElectricalSystem) -> int



"""

 StartSlot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get/Set the Start Slot where the Electrical System is located in its panel.



Get: StartSlot(self: ElectricalSystem) -> int



"""

 SystemType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Electrical System Type of the Electrical System.



Get: SystemType(self: ElectricalSystem) -> ElectricalSystemType



"""

 TrueCurrent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueCurrent value of the Electrical System.



Get: TrueCurrent(self: ElectricalSystem) -> float



"""

 TrueCurrentPhaseA=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueCurrentPhaseA value of the Electrical System.



Get: TrueCurrentPhaseA(self: ElectricalSystem) -> float



"""

 TrueCurrentPhaseB=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueCurrentPhaseB value of the Electrical System.



Get: TrueCurrentPhaseB(self: ElectricalSystem) -> float



"""

 TrueCurrentPhaseC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueCurrentPhaseC value of the Electrical System.



Get: TrueCurrentPhaseC(self: ElectricalSystem) -> float



"""

 TrueLoad=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueLoad value of the Electrical System.



Get: TrueLoad(self: ElectricalSystem) -> float



"""

 TrueLoadPhaseA=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueLoadPhaseA value of the Electrical System.



Get: TrueLoadPhaseA(self: ElectricalSystem) -> float



"""

 TrueLoadPhaseB=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueLoadPhaseB value of the Electrical System.



Get: TrueLoadPhaseB(self: ElectricalSystem) -> float



"""

 TrueLoadPhaseC=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the TrueLoadPhaseC value of the Electrical System.



Get: TrueLoadPhaseC(self: ElectricalSystem) -> float



"""

 Voltage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the Voltage value of the Electrical System.



Get: Voltage(self: ElectricalSystem) -> float



"""

 VoltageDrop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the VoltageDrop value of the Electrical System.



Get: VoltageDrop(self: ElectricalSystem) -> float



"""

 WireSizeString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the WireSize as a String of the Electrical System.



Get: WireSizeString(self: ElectricalSystem) -> str



"""

 WireType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get/Set the wire type of the Electrical System.



Get: WireType(self: ElectricalSystem) -> WireType



Set: WireType(self: ElectricalSystem)=value

"""


