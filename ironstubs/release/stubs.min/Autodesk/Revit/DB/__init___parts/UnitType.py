class UnitType(Enum,IComparable,IFormattable,IConvertible):
 """
 The type of physical quantity to be measured,for example length or force.
 
 enum UnitType,values: UT_Acceleration (92),UT_Angle (3),UT_Area (1),UT_AreaForce (28),UT_AreaForcePerLength (54),UT_AreaForceScale (32),UT_Bar_Diameter (93),UT_Color_Temperature (75),UT_Crack_Width (94),UT_Currency (72),UT_Custom (-1),UT_DecSheetLength (76),UT_Displacement_Deflection (95),UT_Electrical_Apparent_Power (34),UT_Electrical_CableTraySize (82),UT_Electrical_ConduitSize (83),UT_Electrical_Current (19),UT_Electrical_Demand_Factor (86),UT_Electrical_Efficacy (73),UT_Electrical_Frequency (21),UT_Electrical_Illuminance (22),UT_Electrical_Luminance (78),UT_Electrical_Luminous_Flux (23),UT_Electrical_Luminous_Intensity (77),UT_Electrical_Potential (20),UT_Electrical_Power (24),UT_Electrical_Power_Density (35),UT_Electrical_Resistivity (121),UT_Electrical_Temperature (81),UT_Electrical_TemperatureDifference (129),UT_Electrical_Wattage (74),UT_Energy (96),UT_Force (26),UT_ForceLengthPerAngle (51),UT_ForcePerLength (50),UT_ForceScale (30),UT_HVAC_Airflow (15),UT_HVAC_Airflow_Density (58),UT_HVAC_Airflow_Divided_By_Cooling_Load (67),UT_HVAC_Airflow_Divided_By_Volume (66),UT_HVAC_Area_Divided_By_Cooling_Load (68),UT_HVAC_Area_Divided_By_Heating_Load (79),UT_HVAC_CoefficientOfHeatTransfer (57),UT_HVAC_Cooling_Load (60),UT_HVAC_Cooling_Load_Divided_By_Area (61),UT_HVAC_Cooling_Load_Divided_By_Volume (62),UT_HVAC_CrossSection (17),UT_HVAC_Density (7),UT_HVAC_DuctInsulationThickness (87),UT_HVAC_DuctLiningThickness (88),UT_HVAC_DuctSize (16),UT_HVAC_Energy (8),UT_HVAC_Factor (80),UT_HVAC_Friction (9),UT_HVAC_HeatGain (18),UT_HVAC_Heating_Load (63),UT_HVAC_Heating_Load_Divided_By_Area (64),UT_HVAC_Heating_Load_Divided_By_Volume (65),UT_HVAC_Permeability (120),UT_HVAC_Power (10),UT_HVAC_Power_Density (11),UT_HVAC_Pressure (12),UT_HVAC_Roughness (25),UT_HVAC_Slope (70),UT_HVAC_SpecificHeat (118),UT_HVAC_SpecificHeatOfVaporization (119),UT_HVAC_Temperature (13),UT_HVAC_TemperatureDifference (127),UT_HVAC_ThermalConductivity (117),UT_HVAC_ThermalMass (91),UT_HVAC_ThermalResistance (90),UT_HVAC_Velocity (14),UT_HVAC_Viscosity (56),UT_Length (0),UT_LinearForce (27),UT_LinearForceLengthPerAngle (53),UT_LinearForcePerLength (52),UT_LinearForceScale (31),UT_LinearMoment (48),UT_LinearMomentScale (49),UT_Mass (98),UT_Mass_per_Unit_Length (99),UT_MassDensity (122),UT_MassPerUnitArea (123),UT_Moment (29),UT_Moment_of_Inertia (100),UT_MomentScale (33),UT_Number (4),UT_Period (102),UT_Pipe_Dimension (124),UT_PipeInsulationThickness (89),UT_PipeMass (125),UT_PipeMassPerUnitLength (126),UT_PipeSize (43),UT_Piping_Density (36),UT_Piping_Flow (37),UT_Piping_Friction (38),UT_Piping_Pressure (39),UT_Piping_Roughness (44),UT_Piping_Slope (71),UT_Piping_Temperature (40),UT_Piping_TemperatureDifference (128),UT_Piping_Velocity (41),UT_Piping_Viscosity (42),UT_Piping_Volume (55),UT_Pulsation (103),UT_Reinforcement_Area (104),UT_Reinforcement_Area_per_Unit_Length (105),UT_Reinforcement_Cover (106),UT_Reinforcement_Length (85),UT_Reinforcement_Spacing (107),UT_Reinforcement_Volume (84),UT_Rotation (108),UT_Section_Area (109),UT_Section_Dimension (110),UT_Section_Modulus (111),UT_Section_Property (112),UT_SheetLength (5),UT_SiteAngle (6),UT_Slope (59),UT_Stress (45),UT_Structural_Frequency (97),UT_Structural_Velocity (113),UT_Surface_Area (101),UT_ThermalExpansion (47),UT_Undefined (-2),UT_UnitWeight (46),UT_Volume (2),UT_Warping_Constant (114),UT_Weight (115),UT_Weight_per_Unit_Length (116),UT_WireSize (69)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 UT_Acceleration=None
 UT_Angle=None
 UT_Area=None
 UT_AreaForce=None
 UT_AreaForcePerLength=None
 UT_AreaForceScale=None
 UT_Bar_Diameter=None
 UT_Color_Temperature=None
 UT_Crack_Width=None
 UT_Currency=None
 UT_Custom=None
 UT_DecSheetLength=None
 UT_Displacement_Deflection=None
 UT_Electrical_Apparent_Power=None
 UT_Electrical_CableTraySize=None
 UT_Electrical_ConduitSize=None
 UT_Electrical_Current=None
 UT_Electrical_Demand_Factor=None
 UT_Electrical_Efficacy=None
 UT_Electrical_Frequency=None
 UT_Electrical_Illuminance=None
 UT_Electrical_Luminance=None
 UT_Electrical_Luminous_Flux=None
 UT_Electrical_Luminous_Intensity=None
 UT_Electrical_Potential=None
 UT_Electrical_Power=None
 UT_Electrical_Power_Density=None
 UT_Electrical_Resistivity=None
 UT_Electrical_Temperature=None
 UT_Electrical_TemperatureDifference=None
 UT_Electrical_Wattage=None
 UT_Energy=None
 UT_Force=None
 UT_ForceLengthPerAngle=None
 UT_ForcePerLength=None
 UT_ForceScale=None
 UT_HVAC_Airflow=None
 UT_HVAC_Airflow_Density=None
 UT_HVAC_Airflow_Divided_By_Cooling_Load=None
 UT_HVAC_Airflow_Divided_By_Volume=None
 UT_HVAC_Area_Divided_By_Cooling_Load=None
 UT_HVAC_Area_Divided_By_Heating_Load=None
 UT_HVAC_CoefficientOfHeatTransfer=None
 UT_HVAC_Cooling_Load=None
 UT_HVAC_Cooling_Load_Divided_By_Area=None
 UT_HVAC_Cooling_Load_Divided_By_Volume=None
 UT_HVAC_CrossSection=None
 UT_HVAC_Density=None
 UT_HVAC_DuctInsulationThickness=None
 UT_HVAC_DuctLiningThickness=None
 UT_HVAC_DuctSize=None
 UT_HVAC_Energy=None
 UT_HVAC_Factor=None
 UT_HVAC_Friction=None
 UT_HVAC_HeatGain=None
 UT_HVAC_Heating_Load=None
 UT_HVAC_Heating_Load_Divided_By_Area=None
 UT_HVAC_Heating_Load_Divided_By_Volume=None
 UT_HVAC_Permeability=None
 UT_HVAC_Power=None
 UT_HVAC_Power_Density=None
 UT_HVAC_Pressure=None
 UT_HVAC_Roughness=None
 UT_HVAC_Slope=None
 UT_HVAC_SpecificHeat=None
 UT_HVAC_SpecificHeatOfVaporization=None
 UT_HVAC_Temperature=None
 UT_HVAC_TemperatureDifference=None
 UT_HVAC_ThermalConductivity=None
 UT_HVAC_ThermalMass=None
 UT_HVAC_ThermalResistance=None
 UT_HVAC_Velocity=None
 UT_HVAC_Viscosity=None
 UT_Length=None
 UT_LinearForce=None
 UT_LinearForceLengthPerAngle=None
 UT_LinearForcePerLength=None
 UT_LinearForceScale=None
 UT_LinearMoment=None
 UT_LinearMomentScale=None
 UT_Mass=None
 UT_MassDensity=None
 UT_MassPerUnitArea=None
 UT_Mass_per_Unit_Length=None
 UT_Moment=None
 UT_MomentScale=None
 UT_Moment_of_Inertia=None
 UT_Number=None
 UT_Period=None
 UT_PipeInsulationThickness=None
 UT_PipeMass=None
 UT_PipeMassPerUnitLength=None
 UT_PipeSize=None
 UT_Pipe_Dimension=None
 UT_Piping_Density=None
 UT_Piping_Flow=None
 UT_Piping_Friction=None
 UT_Piping_Pressure=None
 UT_Piping_Roughness=None
 UT_Piping_Slope=None
 UT_Piping_Temperature=None
 UT_Piping_TemperatureDifference=None
 UT_Piping_Velocity=None
 UT_Piping_Viscosity=None
 UT_Piping_Volume=None
 UT_Pulsation=None
 UT_Reinforcement_Area=None
 UT_Reinforcement_Area_per_Unit_Length=None
 UT_Reinforcement_Cover=None
 UT_Reinforcement_Length=None
 UT_Reinforcement_Spacing=None
 UT_Reinforcement_Volume=None
 UT_Rotation=None
 UT_Section_Area=None
 UT_Section_Dimension=None
 UT_Section_Modulus=None
 UT_Section_Property=None
 UT_SheetLength=None
 UT_SiteAngle=None
 UT_Slope=None
 UT_Stress=None
 UT_Structural_Frequency=None
 UT_Structural_Velocity=None
 UT_Surface_Area=None
 UT_ThermalExpansion=None
 UT_Undefined=None
 UT_UnitWeight=None
 UT_Volume=None
 UT_Warping_Constant=None
 UT_Weight=None
 UT_Weight_per_Unit_Length=None
 UT_WireSize=None
 value__=None

