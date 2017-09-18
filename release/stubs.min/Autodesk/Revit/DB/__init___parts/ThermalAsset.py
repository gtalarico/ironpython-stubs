class ThermalAsset(object,IDisposable):
 """
 Represents the properties of a material pertinent to energy analysis.

 

 ThermalAsset(name: str,materialType: ThermalMaterialType)
 """
 def Copy(self):
  """
  Copy(self: ThermalAsset) -> ThermalAsset

  

   Produces a copy of the asset.

   Returns: A copy of the asset.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ThermalAsset) """
  pass
 def Equals(self,*__args):
  """
  Equals(self: ThermalAsset,other: ThermalAsset) -> bool

  

   Determines whether this thermal asset is equal to another.

  

   other: The thermal asset to compare with this one.

   Returns: True if the given thermal asset is equal to this one,otherwise false.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ThermalAsset,disposing: bool) """
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
 def __new__(self,name,materialType):
  """ __new__(cls: type,name: str,materialType: ThermalMaterialType) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Behavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Flag indicating whether elements of this material behave isotropically or orthotropically.



Get: Behavior(self: ThermalAsset) -> StructuralBehavior



Set: Behavior(self: ThermalAsset)=value

"""

 Compressibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The compressibility of the asset.



Get: Compressibility(self: ThermalAsset) -> float



Set: Compressibility(self: ThermalAsset)=value

"""

 Density=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The density of the asset.



Get: Density(self: ThermalAsset) -> float



Set: Density(self: ThermalAsset)=value

"""

 ElectricalResistivity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The electrical resistivity of the asset.



Get: ElectricalResistivity(self: ThermalAsset) -> float



Set: ElectricalResistivity(self: ThermalAsset)=value

"""

 Emissivity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The emissivity of the asset.



Get: Emissivity(self: ThermalAsset) -> float



Set: Emissivity(self: ThermalAsset)=value

"""

 GasViscosity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The gas viscosity of the asset.



Get: GasViscosity(self: ThermalAsset) -> float



Set: GasViscosity(self: ThermalAsset)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ThermalAsset) -> bool



"""

 LiquidViscosity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The liquid viscosity of the asset.



Get: LiquidViscosity(self: ThermalAsset) -> float



Set: LiquidViscosity(self: ThermalAsset)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the thermal asset.



Get: Name(self: ThermalAsset) -> str



Set: Name(self: ThermalAsset)=value

"""

 Permeability=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The permeability of the asset.



Get: Permeability(self: ThermalAsset) -> float



Set: Permeability(self: ThermalAsset)=value

"""

 Porosity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The porosity of the asset.



Get: Porosity(self: ThermalAsset) -> float



Set: Porosity(self: ThermalAsset)=value

"""

 Reflectivity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The reflectivity of the asset.



Get: Reflectivity(self: ThermalAsset) -> float



Set: Reflectivity(self: ThermalAsset)=value

"""

 SpecificHeat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The specific heat of the asset.



Get: SpecificHeat(self: ThermalAsset) -> float



Set: SpecificHeat(self: ThermalAsset)=value

"""

 SpecificHeatOfVaporization=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The specific heat of vaporization of the asset.



Get: SpecificHeatOfVaporization(self: ThermalAsset) -> float



Set: SpecificHeatOfVaporization(self: ThermalAsset)=value

"""

 ThermalConductivity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The thermal conductivity of the asset.



Get: ThermalConductivity(self: ThermalAsset) -> float



Set: ThermalConductivity(self: ThermalAsset)=value

"""

 ThermalMaterialType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of material that this thermal asset describes (e.g. solid,liquid,gas.)



Get: ThermalMaterialType(self: ThermalAsset) -> ThermalMaterialType



"""

 TransmitsLight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A boolean flag that indicates whether or not the asset transmits light.



Get: TransmitsLight(self: ThermalAsset) -> bool



Set: TransmitsLight(self: ThermalAsset)=value

"""

 VaporPressure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The vapor pressure of the asset.



Get: VaporPressure(self: ThermalAsset) -> float



Set: VaporPressure(self: ThermalAsset)=value

"""


