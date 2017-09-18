class StructuralAsset(object,IDisposable):
 """
 Represents the properties of a material pertinent to structural analysis.

 

 StructuralAsset(name: str,structuralAssetClass: StructuralAssetClass)
 """
 def Copy(self):
  """
  Copy(self: StructuralAsset) -> StructuralAsset

  

   Produces a copy of the asset.

   Returns: A copy of the asset.
  """
  pass
 def Dispose(self):
  """ Dispose(self: StructuralAsset) """
  pass
 def Equals(self,*__args):
  """
  Equals(self: StructuralAsset,other: StructuralAsset) -> bool

  

   Determines whether this structural asset is equal to another.

  

   other: The structural asset with which to compare this structural asset.

   Returns: True if the given structural asset is equal to this one,otherwise false.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: StructuralAsset,disposing: bool) """
  pass
 def SetPoissonRatio(self,poissonRatio):
  """
  SetPoissonRatio(self: StructuralAsset,poissonRatio: float)

   Sets the Poisson ratio of the asset.
  """
  pass
 def SetShearModulus(self,shearModulus):
  """
  SetShearModulus(self: StructuralAsset,shearModulus: float)

   Sets the shear modulus of the asset.
  """
  pass
 def SetThermalExpansionCoefficient(self,thermalExpCoeff):
  """
  SetThermalExpansionCoefficient(self: StructuralAsset,thermalExpCoeff: float)

   Sets the thermal expansion coefficient of the asset.
  """
  pass
 def SetYoungModulus(self,youngModulus):
  """
  SetYoungModulus(self: StructuralAsset,youngModulus: float)

   Sets the Young's modulus of the asset.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,name,structuralAssetClass):
  """ __new__(cls: type,name: str,structuralAssetClass: StructuralAssetClass) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Behavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Flag indicating whether elements of this material behave isotropically or orthotropically.



Get: Behavior(self: StructuralAsset) -> StructuralBehavior



Set: Behavior(self: StructuralAsset)=value

"""

 ConcreteBendingReinforcement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bending reinforcement of the asset.



Get: ConcreteBendingReinforcement(self: StructuralAsset) -> float



Set: ConcreteBendingReinforcement(self: StructuralAsset)=value

"""

 ConcreteCompression=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The compression strength of concrete-based assets.



Get: ConcreteCompression(self: StructuralAsset) -> float



Set: ConcreteCompression(self: StructuralAsset)=value

"""

 ConcreteShearReinforcement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shear reinforcement of the asset.



Get: ConcreteShearReinforcement(self: StructuralAsset) -> float



Set: ConcreteShearReinforcement(self: StructuralAsset)=value

"""

 ConcreteShearStrengthReduction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shear strength reduction of the asset.



Get: ConcreteShearStrengthReduction(self: StructuralAsset) -> float



Set: ConcreteShearStrengthReduction(self: StructuralAsset)=value

"""

 DampingRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The damping ratio of the asset.



Get: DampingRatio(self: StructuralAsset) -> float



Set: DampingRatio(self: StructuralAsset)=value

"""

 Density=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The density of the asset.



Get: Density(self: StructuralAsset) -> float



Set: Density(self: StructuralAsset)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: StructuralAsset) -> bool



"""

 Lightweight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Flag indicating whether the asset describes a material that is light-weight or not.



Get: Lightweight(self: StructuralAsset) -> bool



Set: Lightweight(self: StructuralAsset)=value

"""

 MetalReductionFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The reduction factor of the asset.



Get: MetalReductionFactor(self: StructuralAsset) -> float



Set: MetalReductionFactor(self: StructuralAsset)=value

"""

 MetalResistanceCalculationStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The resistance calculation strength of the asset.



Get: MetalResistanceCalculationStrength(self: StructuralAsset) -> float



Set: MetalResistanceCalculationStrength(self: StructuralAsset)=value

"""

 MinimumTensileStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The minimum tensile strength of the asset.



Get: MinimumTensileStrength(self: StructuralAsset) -> float



Set: MinimumTensileStrength(self: StructuralAsset)=value

"""

 MinimumYieldStress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The minimum yield stress of the asset.



Get: MinimumYieldStress(self: StructuralAsset) -> float



Set: MinimumYieldStress(self: StructuralAsset)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the structural asset.



Get: Name(self: StructuralAsset) -> str



Set: Name(self: StructuralAsset)=value

"""

 PoissonRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Poisson ratio of the asset.



Get: PoissonRatio(self: StructuralAsset) -> XYZ



Set: PoissonRatio(self: StructuralAsset)=value

"""

 ShearModulus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The shear modulus of the asset.



Get: ShearModulus(self: StructuralAsset) -> XYZ



Set: ShearModulus(self: StructuralAsset)=value

"""

 StructuralAssetClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of material that this structural asset describes (e.g. wood,concrete,metal.)



Get: StructuralAssetClass(self: StructuralAsset) -> StructuralAssetClass



"""

 SubClass=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The sub-class of the asset.



Get: SubClass(self: StructuralAsset) -> str



Set: SubClass(self: StructuralAsset)=value

"""

 ThermalExpansionCoefficient=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The thermal expansion coefficient of the asset.



Get: ThermalExpansionCoefficient(self: StructuralAsset) -> XYZ



Set: ThermalExpansionCoefficient(self: StructuralAsset)=value

"""

 WoodBendingStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The bending strength of the asset.



Get: WoodBendingStrength(self: StructuralAsset) -> float



Set: WoodBendingStrength(self: StructuralAsset)=value

"""

 WoodGrade=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The grade of wood used in a wood-based asset.



Get: WoodGrade(self: StructuralAsset) -> str



Set: WoodGrade(self: StructuralAsset)=value

"""

 WoodParallelCompressionStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The parallel compression strength of the asset.



Get: WoodParallelCompressionStrength(self: StructuralAsset) -> float



Set: WoodParallelCompressionStrength(self: StructuralAsset)=value

"""

 WoodParallelShearStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The parallel shear strength of the asset.



Get: WoodParallelShearStrength(self: StructuralAsset) -> float



Set: WoodParallelShearStrength(self: StructuralAsset)=value

"""

 WoodPerpendicularCompressionStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The perpendicular compression strength of the asset.



Get: WoodPerpendicularCompressionStrength(self: StructuralAsset) -> float



Set: WoodPerpendicularCompressionStrength(self: StructuralAsset)=value

"""

 WoodPerpendicularShearStrength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The perpendicular shear strength of the asset.



Get: WoodPerpendicularShearStrength(self: StructuralAsset) -> float



Set: WoodPerpendicularShearStrength(self: StructuralAsset)=value

"""

 WoodSpecies=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The species of wood used in a wood-based asset.



Get: WoodSpecies(self: StructuralAsset) -> str



Set: WoodSpecies(self: StructuralAsset)=value

"""

 YoungModulus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Young's modulus of the asset.



Get: YoungModulus(self: StructuralAsset) -> XYZ



Set: YoungModulus(self: StructuralAsset)=value

"""


