class ServiceType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing all of the built-in parameter groups supported by Autodesk
    Revit.
    
    enum ServiceType, values: kActiveChilledBeams (22), kCentralHeatingConvectors (1), kCentralHeatingHotAir (3), kCentralHeatingRadiantFloor (2), kCentralHeatingRadiators (0), kConstantVolumeDualDuct (20), kConstantVolumeFixedOA (16), kConstantVolumeTerminalReheat (18), kConstantVolumeVariableOA (17), kFanCoilSystem (14), kForcedConvectionHeaterFlue (8), kForcedConvectionHeaterNoFlue (9), kInductionSystem (15), kMultizoneHotDeckColdDeck (19), kNoServiceType (-1), kOtherRoomHeater (4), kRadiantCooledCeilings (21), kRadiantHeaterFlue (5), kRadiantHeaterMultiburner (7), kRadiantHeaterNoFlue (6), kSplitSystemsWithMechanicalVentilation (26), kSplitSystemsWithMechanicalVentilationWithCooling (27), kSplitSystemsWithNaturalVentilation (25), kVariableRefrigerantFlow (24), kVAVDualDuct (11), kVAVIndoorPackagedCabinet (12), kVAVSingleDuct (10), kVAVTerminalReheat (13), kWaterLoopHeatPump (23)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    kActiveChilledBeams = None
    kCentralHeatingConvectors = None
    kCentralHeatingHotAir = None
    kCentralHeatingRadiantFloor = None
    kCentralHeatingRadiators = None
    kConstantVolumeDualDuct = None
    kConstantVolumeFixedOA = None
    kConstantVolumeTerminalReheat = None
    kConstantVolumeVariableOA = None
    kFanCoilSystem = None
    kForcedConvectionHeaterFlue = None
    kForcedConvectionHeaterNoFlue = None
    kInductionSystem = None
    kMultizoneHotDeckColdDeck = None
    kNoServiceType = None
    kOtherRoomHeater = None
    kRadiantCooledCeilings = None
    kRadiantHeaterFlue = None
    kRadiantHeaterMultiburner = None
    kRadiantHeaterNoFlue = None
    kSplitSystemsWithMechanicalVentilation = None
    kSplitSystemsWithMechanicalVentilationWithCooling = None
    kSplitSystemsWithNaturalVentilation = None
    kVariableRefrigerantFlow = None
    kVAVDualDuct = None
    kVAVIndoorPackagedCabinet = None
    kVAVSingleDuct = None
    kVAVTerminalReheat = None
    kWaterLoopHeatPump = None
    value__ = None

