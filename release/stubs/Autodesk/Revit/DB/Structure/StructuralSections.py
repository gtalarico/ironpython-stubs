# encoding: utf-8
# module Autodesk.Revit.DB.Structure.StructuralSections calls itself StructuralSections
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StructuralSection(object, IDisposable):
    """ The base class for StructuralSection specific classes, designed to provide common parameters and ability to differentiate between different structural section shapes. """
    def Dispose(self):
        """ Dispose(self: StructuralSection) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: StructuralSection) -> bool

"""

    SectionNameKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A parameter in structural families which allows for family type identification.
   This will be used for data mapping during model exchange with another program, namely Advance Steel.

Get: SectionNameKey(self: StructuralSection) -> str

Set: SectionNameKey(self: StructuralSection) = value
"""

    StructuralSectionShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of structural section shape.

Get: StructuralSectionShape(self: StructuralSection) -> StructuralSectionShape

"""

    StructuralSectionShapeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A human readable string representing the structural section shape.

Get: StructuralSectionShapeName(self: StructuralSection) -> str

"""



class StructuralSectionRectangular(StructuralSection, IDisposable):
    """ Defines common set of parameters for structural section rectangular contour. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CentroidHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the left extremites along horizontal axis.

Get: CentroidHorizontal(self: StructuralSectionRectangular) -> float

Set: CentroidHorizontal(self: StructuralSectionRectangular) = value
"""

    CentroidVertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the upper extremites along vertical axis.

Get: CentroidVertical(self: StructuralSectionRectangular) -> float

Set: CentroidVertical(self: StructuralSectionRectangular) = value
"""

    ElasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main strong axis for calculation of bending stresses.

Get: ElasticModulusStrongAxis(self: StructuralSectionRectangular) -> float

Set: ElasticModulusStrongAxis(self: StructuralSectionRectangular) = value
"""

    ElasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main weak axis for calculation of bending stresses.

Get: ElasticModulusWeakAxis(self: StructuralSectionRectangular) -> float

Set: ElasticModulusWeakAxis(self: StructuralSectionRectangular) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section height, depth.

Get: Height(self: StructuralSectionRectangular) -> float

Set: Height(self: StructuralSectionRectangular) = value
"""

    MomentOfInertiaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main strong axis (I).

Get: MomentOfInertiaStrongAxis(self: StructuralSectionRectangular) -> float

Set: MomentOfInertiaStrongAxis(self: StructuralSectionRectangular) = value
"""

    MomentOfInertiaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main weak axis (I).

Get: MomentOfInertiaWeakAxis(self: StructuralSectionRectangular) -> float

Set: MomentOfInertiaWeakAxis(self: StructuralSectionRectangular) = value
"""

    NameKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name Key

Get: NameKey(self: StructuralSectionRectangular) -> str

Set: NameKey(self: StructuralSectionRectangular) = value
"""

    NominalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unit weight (not mass) per unit length, for self-weight calculation or quantity survey.

Get: NominalWeight(self: StructuralSectionRectangular) -> float

Set: NominalWeight(self: StructuralSectionRectangular) = value
"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Painting surface of the unit length.

Get: Perimeter(self: StructuralSectionRectangular) -> float

Set: Perimeter(self: StructuralSectionRectangular) = value
"""

    PlasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main strong axis (Z, Wpl)

Get: PlasticModulusStrongAxis(self: StructuralSectionRectangular) -> float

Set: PlasticModulusStrongAxis(self: StructuralSectionRectangular) = value
"""

    PlasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main weak axis.

Get: PlasticModulusWeakAxis(self: StructuralSectionRectangular) -> float

Set: PlasticModulusWeakAxis(self: StructuralSectionRectangular) = value
"""

    PrincipalAxesAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rotation angle between the principal axes and cross section reference planes.

Get: PrincipalAxesAngle(self: StructuralSectionRectangular) -> float

Set: PrincipalAxesAngle(self: StructuralSectionRectangular) = value
"""

    SectionArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cross section area.

Get: SectionArea(self: StructuralSectionRectangular) -> float

Set: SectionArea(self: StructuralSectionRectangular) = value
"""

    ShearAreaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq).

Get: ShearAreaStrongAxis(self: StructuralSectionRectangular) -> float

Set: ShearAreaStrongAxis(self: StructuralSectionRectangular) = value
"""

    ShearAreaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of weak axis (Wq).

Get: ShearAreaWeakAxis(self: StructuralSectionRectangular) -> float

Set: ShearAreaWeakAxis(self: StructuralSectionRectangular) = value
"""

    TorsionalModulus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section modulus for calculations of torsion stresses (Ct)

Get: TorsionalModulus(self: StructuralSectionRectangular) -> float

Set: TorsionalModulus(self: StructuralSectionRectangular) = value
"""

    TorsionalMomentOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation

Get: TorsionalMomentOfInertia(self: StructuralSectionRectangular) -> float

Set: TorsionalMomentOfInertia(self: StructuralSectionRectangular) = value
"""

    WarpingConstant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Warping constant (Cw, Iomega, H)

Get: WarpingConstant(self: StructuralSectionRectangular) -> float

Set: WarpingConstant(self: StructuralSectionRectangular) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section width.

Get: Width(self: StructuralSectionRectangular) -> float

Set: Width(self: StructuralSectionRectangular) = value
"""



class StructuralSectionColdFormed(StructuralSectionRectangular, IDisposable):
    """ Defines parameters for Hot Formed structural section. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    InnerFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Fillet - Corner fillet inner radius.

Get: InnerFillet(self: StructuralSectionColdFormed) -> float

Set: InnerFillet(self: StructuralSectionColdFormed) = value
"""

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of rectangle.

Get: WallDesignThickness(self: StructuralSectionColdFormed) -> float

Set: WallDesignThickness(self: StructuralSectionColdFormed) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of rectangle.

Get: WallNominalThickness(self: StructuralSectionColdFormed) -> float

Set: WallNominalThickness(self: StructuralSectionColdFormed) = value
"""



class StructuralSectionConcreteCross(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized concrete cross structural section.
    
    StructuralSectionConcreteCross(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, cantileverLength, cantileverHeight):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float) """
        pass

    CantileverHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever thickness.

Get: CantileverHeight(self: StructuralSectionConcreteCross) -> float

Set: CantileverHeight(self: StructuralSectionConcreteCross) = value
"""

    CantileverLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever length.

Get: CantileverLength(self: StructuralSectionConcreteCross) -> float

Set: CantileverLength(self: StructuralSectionConcreteCross) = value
"""



class StructuralSectionConcreteRectangle(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized concrete rectangle structural section.
    
    StructuralSectionConcreteRectangle(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionConcreteRectangleCut(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized concrete rectangle cut structural section.
    
    StructuralSectionConcreteRectangleCut(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, topCutWidth: float, topCutHeight: float, bottomCutWidth: float, bottomCutHeight: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, topCutWidth, topCutHeight, bottomCutWidth, bottomCutHeight):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, topCutWidth: float, topCutHeight: float, bottomCutWidth: float, bottomCutHeight: float) """
        pass

    BottomCutHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section height left Cut.

Get: BottomCutHeight(self: StructuralSectionConcreteRectangleCut) -> float

Set: BottomCutHeight(self: StructuralSectionConcreteRectangleCut) = value
"""

    BottomCutWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section width left Cut.

Get: BottomCutWidth(self: StructuralSectionConcreteRectangleCut) -> float

Set: BottomCutWidth(self: StructuralSectionConcreteRectangleCut) = value
"""

    TopCutHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section height right Cut.

Get: TopCutHeight(self: StructuralSectionConcreteRectangleCut) -> float

Set: TopCutHeight(self: StructuralSectionConcreteRectangleCut) = value
"""

    TopCutWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section width right Cut.

Get: TopCutWidth(self: StructuralSectionConcreteRectangleCut) -> float

Set: TopCutWidth(self: StructuralSectionConcreteRectangleCut) = value
"""



class StructuralSectionRound(StructuralSection, IDisposable):
    """ Defines common set of  parameters for structural section round contour. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CentroidHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the left extremites along horizontal axis.

Get: CentroidHorizontal(self: StructuralSectionRound) -> float

Set: CentroidHorizontal(self: StructuralSectionRound) = value
"""

    CentroidVertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Distance from centroid to the upper extremites along vertical axis.

Get: CentroidVertical(self: StructuralSectionRound) -> float

Set: CentroidVertical(self: StructuralSectionRound) = value
"""

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pipe Diameter.

Get: Diameter(self: StructuralSectionRound) -> float

Set: Diameter(self: StructuralSectionRound) = value
"""

    ElasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main strong axis for calculation of bending stresses.

Get: ElasticModulusStrongAxis(self: StructuralSectionRound) -> float

Set: ElasticModulusStrongAxis(self: StructuralSectionRound) = value
"""

    ElasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Elastic section modulus about main weak axis for calculation of bending stresses.

Get: ElasticModulusWeakAxis(self: StructuralSectionRound) -> float

Set: ElasticModulusWeakAxis(self: StructuralSectionRound) = value
"""

    MomentOfInertiaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main strong axis (I).

Get: MomentOfInertiaStrongAxis(self: StructuralSectionRound) -> float

Set: MomentOfInertiaStrongAxis(self: StructuralSectionRound) = value
"""

    MomentOfInertiaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Moment of Inertia about main weak axis (I).

Get: MomentOfInertiaWeakAxis(self: StructuralSectionRound) -> float

Set: MomentOfInertiaWeakAxis(self: StructuralSectionRound) = value
"""

    NameKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name Key

Get: NameKey(self: StructuralSectionRound) -> str

Set: NameKey(self: StructuralSectionRound) = value
"""

    NominalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unit weight (not mass) per unit length, for self-weight calculation or quantity survey.

Get: NominalWeight(self: StructuralSectionRound) -> float

Set: NominalWeight(self: StructuralSectionRound) = value
"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Painting surface of the unit length.

Get: Perimeter(self: StructuralSectionRound) -> float

Set: Perimeter(self: StructuralSectionRound) = value
"""

    PlasticModulusStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main strong axis (Z, Wpl)

Get: PlasticModulusStrongAxis(self: StructuralSectionRound) -> float

Set: PlasticModulusStrongAxis(self: StructuralSectionRound) = value
"""

    PlasticModulusWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Plastic section modulus in bending about main weak axis.

Get: PlasticModulusWeakAxis(self: StructuralSectionRound) -> float

Set: PlasticModulusWeakAxis(self: StructuralSectionRound) = value
"""

    PrincipalAxesAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rotation angle between the principal axes and cross section reference planes.

Get: PrincipalAxesAngle(self: StructuralSectionRound) -> float

Set: PrincipalAxesAngle(self: StructuralSectionRound) = value
"""

    SectionArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cross section area.

Get: SectionArea(self: StructuralSectionRound) -> float

Set: SectionArea(self: StructuralSectionRound) = value
"""

    ShearAreaStrongAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq).

Get: ShearAreaStrongAxis(self: StructuralSectionRound) -> float

Set: ShearAreaStrongAxis(self: StructuralSectionRound) = value
"""

    ShearAreaWeakAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shear area (reduced extreme shear stress coefficient) in the direction of weak axis (Wq).

Get: ShearAreaWeakAxis(self: StructuralSectionRound) -> float

Set: ShearAreaWeakAxis(self: StructuralSectionRound) = value
"""

    TorsionalModulus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Section modulus for calculations of torsion stresses (Ct)

Get: TorsionalModulus(self: StructuralSectionRound) -> float

Set: TorsionalModulus(self: StructuralSectionRound) = value
"""

    TorsionalMomentOfInertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation

Get: TorsionalMomentOfInertia(self: StructuralSectionRound) -> float

Set: TorsionalMomentOfInertia(self: StructuralSectionRound) = value
"""

    WarpingConstant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Warping constant (Cw, Iomega, H)

Get: WarpingConstant(self: StructuralSectionRound) -> float

Set: WarpingConstant(self: StructuralSectionRound) = value
"""



class StructuralSectionConcreteRound(StructuralSectionRound, IDisposable):
    """
    Creates a new instance of Structural Section Concrete Round shape with the associated set of parameters,
       used to attach to structural element.
    
    StructuralSectionConcreteRound(diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionConcreteT(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized concrete T structural section.
    
    StructuralSectionConcreteT(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, cantileverLength, cantileverHeight):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, cantileverLength: float, cantileverHeight: float) """
        pass

    CantileverHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever thickness.

Get: CantileverHeight(self: StructuralSectionConcreteT) -> float

Set: CantileverHeight(self: StructuralSectionConcreteT) = value
"""

    CantileverLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange cantilever length.

Get: CantileverLength(self: StructuralSectionConcreteT) -> float

Set: CantileverLength(self: StructuralSectionConcreteT) = value
"""



class StructuralSectionHotRolled(StructuralSectionRectangular, IDisposable):
    """ Defines parameters for hot rolled structural sections. """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    FlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Thickness.

Get: FlangeThickness(self: StructuralSectionHotRolled) -> float

Set: FlangeThickness(self: StructuralSectionHotRolled) = value
"""

    WebFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Fillet - fillet radius between web and flange.

Get: WebFillet(self: StructuralSectionHotRolled) -> float

Set: WebFillet(self: StructuralSectionHotRolled) = value
"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Thickness.

Get: WebThickness(self: StructuralSectionHotRolled) -> float

Set: WebThickness(self: StructuralSectionHotRolled) = value
"""



class StructuralSectionCParallelFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for C-channel Parallel Flange structural section.
    
    StructuralSectionCParallelFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionCParallelFlange) -> float

Set: BoltDiameter(self: StructuralSectionCParallelFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionCParallelFlange) -> float

Set: BoltSpacing(self: StructuralSectionCParallelFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionCParallelFlange) -> float

Set: ClearWebHeight(self: StructuralSectionCParallelFlange) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionCParallelFlange) -> float

Set: FlangeToeOfFillet(self: StructuralSectionCParallelFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionCParallelFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionCParallelFlange) = value
"""



class StructuralSectionCProfile(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for C Profile structural section.
    
    StructuralSectionCProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionCProfileWithFold(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for C Profile with fold structural section.
    
    StructuralSectionCProfileWithFold(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, foldLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength, foldLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, foldLength: float) """
        pass

    FoldLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fold segment length.

Get: FoldLength(self: StructuralSectionCProfileWithFold) -> float

Set: FoldLength(self: StructuralSectionCProfileWithFold) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionCProfileWithFold) -> float

Set: LipLength(self: StructuralSectionCProfileWithFold) = value
"""



class StructuralSectionCProfileWithLips(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for C Profile with lips structural section.
    
    StructuralSectionCProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float) """
        pass

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionCProfileWithLips) -> float

Set: LipLength(self: StructuralSectionCProfileWithLips) = value
"""



class StructuralSectionCSlopedFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for C-channel Sloped Flange structural section.
    
    StructuralSectionCSlopedFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionCSlopedFlange) -> float

Set: BoltDiameter(self: StructuralSectionCSlopedFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionCSlopedFlange) -> float

Set: BoltSpacing(self: StructuralSectionCSlopedFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionCSlopedFlange) -> float

Set: ClearWebHeight(self: StructuralSectionCSlopedFlange) = value
"""

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionCSlopedFlange) -> float

Set: FlangeFillet(self: StructuralSectionCSlopedFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionCSlopedFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionCSlopedFlange) = value
"""



class StructuralSectionIParallelFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for I-shape Parallel Flange structural section.
    
    StructuralSectionIParallelFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionIParallelFlange) -> float

Set: BoltDiameter(self: StructuralSectionIParallelFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionIParallelFlange) -> float

Set: BoltSpacing(self: StructuralSectionIParallelFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionIParallelFlange) -> float

Set: ClearWebHeight(self: StructuralSectionIParallelFlange) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionIParallelFlange) -> float

Set: FlangeToeOfFillet(self: StructuralSectionIParallelFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionIParallelFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionIParallelFlange) = value
"""



class StructuralSectionISlopedFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for I-shape Sloped Flange structural section.
    
    StructuralSectionISlopedFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionISlopedFlange) -> float

Set: BoltDiameter(self: StructuralSectionISlopedFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionISlopedFlange) -> float

Set: BoltSpacing(self: StructuralSectionISlopedFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionISlopedFlange) -> float

Set: ClearWebHeight(self: StructuralSectionISlopedFlange) = value
"""

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionISlopedFlange) -> float

Set: FlangeFillet(self: StructuralSectionISlopedFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionISlopedFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionISlopedFlange) = value
"""



class StructuralSectionISplitParallelFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for I-split Parallel Flange structural section.
    
    StructuralSectionISplitParallelFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionISplitParallelFlange) -> float

Set: BoltDiameter(self: StructuralSectionISplitParallelFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionISplitParallelFlange) -> float

Set: BoltSpacing(self: StructuralSectionISplitParallelFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionISplitParallelFlange) -> float

Set: ClearWebHeight(self: StructuralSectionISplitParallelFlange) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionISplitParallelFlange) -> float

Set: FlangeToeOfFillet(self: StructuralSectionISplitParallelFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionISplitParallelFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionISplitParallelFlange) = value
"""



class StructuralSectionISplitSlopedFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for I-split Sloped Flange structural section.
    
    StructuralSectionISplitSlopedFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, webToeOfFillet, boltSpacing, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, webToeOfFillet: float, boltSpacing: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionISplitSlopedFlange) -> float

Set: BoltDiameter(self: StructuralSectionISplitSlopedFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionISplitSlopedFlange) -> float

Set: BoltSpacing(self: StructuralSectionISplitSlopedFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionISplitSlopedFlange) -> float

Set: ClearWebHeight(self: StructuralSectionISplitSlopedFlange) = value
"""

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionISplitSlopedFlange) -> float

Set: FlangeFillet(self: StructuralSectionISplitSlopedFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionISplitSlopedFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionISplitSlopedFlange) = value
"""



class StructuralSectionIWelded(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for I-shape Welded structural section.
    
    StructuralSectionIWelded(width: float, height: float, topFlangeThickness: float, topFlangeWidth: float, bottomFlangeThickness: float, bottomFlangeWidth: float, webThickness: float, webHeight: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, topFlangeThickness, topFlangeWidth, bottomFlangeThickness, bottomFlangeWidth, webThickness, webHeight, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, topFlangeThickness: float, topFlangeWidth: float, bottomFlangeThickness: float, bottomFlangeWidth: float, webThickness: float, webHeight: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass

    BottomFlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange Thickness.

Get: BottomFlangeThickness(self: StructuralSectionIWelded) -> float

Set: BottomFlangeThickness(self: StructuralSectionIWelded) = value
"""

    BottomFlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange Width.

Get: BottomFlangeWidth(self: StructuralSectionIWelded) -> float

Set: BottomFlangeWidth(self: StructuralSectionIWelded) = value
"""

    TopFlangeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Flange Thickness.

Get: TopFlangeThickness(self: StructuralSectionIWelded) -> float

Set: TopFlangeThickness(self: StructuralSectionIWelded) = value
"""

    TopFlangeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Flange Width.

Get: TopFlangeWidth(self: StructuralSectionIWelded) -> float

Set: TopFlangeWidth(self: StructuralSectionIWelded) = value
"""

    WebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Height.

Get: WebHeight(self: StructuralSectionIWelded) -> float

Set: WebHeight(self: StructuralSectionIWelded) = value
"""

    WebThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Web Thickness.

Get: WebThickness(self: StructuralSectionIWelded) -> float

Set: WebThickness(self: StructuralSectionIWelded) = value
"""



class StructuralSectionIWideFlange(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for I-shape Wide Flange structural section.
    
    StructuralSectionIWideFlange(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltSpacingTwoRows: float, boltSpacingBetweenRows: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, clearWebHeight, flangeToeOfFillet, webToeOfFillet, boltSpacing, boltSpacingTwoRows, boltSpacingBetweenRows, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, clearWebHeight: float, flangeToeOfFillet: float, webToeOfFillet: float, boltSpacing: float, boltSpacingTwoRows: float, boltSpacingBetweenRows: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionIWideFlange) -> float

Set: BoltDiameter(self: StructuralSectionIWideFlange) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing, in. (mm)

Get: BoltSpacing(self: StructuralSectionIWideFlange) -> float

Set: BoltSpacing(self: StructuralSectionIWideFlange) = value
"""

    BoltSpacingBetweenRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing between rows, in. (mm)

Get: BoltSpacingBetweenRows(self: StructuralSectionIWideFlange) -> float

Set: BoltSpacingBetweenRows(self: StructuralSectionIWideFlange) = value
"""

    BoltSpacingTwoRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing for two rows , in. (mm)

Get: BoltSpacingTwoRows(self: StructuralSectionIWideFlange) -> float

Set: BoltSpacingTwoRows(self: StructuralSectionIWideFlange) = value
"""

    ClearWebHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing depth between the web toes of the fillets, in.(mm)

Get: ClearWebHeight(self: StructuralSectionIWideFlange) -> float

Set: ClearWebHeight(self: StructuralSectionIWideFlange) = value
"""

    FlangeToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from center of web to flange toe of fillet, in. (mm)

Get: FlangeToeOfFillet(self: StructuralSectionIWideFlange) -> float

Set: FlangeToeOfFillet(self: StructuralSectionIWideFlange) = value
"""

    WebToeOfFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Detailing distance from outer face of flange to web toe of fillet, in. (mm)

Get: WebToeOfFillet(self: StructuralSectionIWideFlange) -> float

Set: WebToeOfFillet(self: StructuralSectionIWideFlange) = value
"""



class StructuralSectionLAngle(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for L-angle Flange structural section.
    
    StructuralSectionLAngle(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing1LongerFlange: float, boltSpacing2LongerFlange: float, boltSpacingShorterFlange: float, boltDiameterLongerFlange: float, boltDiameterShorterFlange: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, boltSpacing1LongerFlange, boltSpacing2LongerFlange, boltSpacingShorterFlange, boltDiameterLongerFlange, boltDiameterShorterFlange):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing1LongerFlange: float, boltSpacing2LongerFlange: float, boltSpacingShorterFlange: float, boltDiameterLongerFlange: float, boltDiameterShorterFlange: float) """
        pass

    BoltDiameterLongerFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter in the longer flange, in. (mm)

Get: BoltDiameterLongerFlange(self: StructuralSectionLAngle) -> float

Set: BoltDiameterLongerFlange(self: StructuralSectionLAngle) = value
"""

    BoltDiameterShorterFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter in the shorter flange, in. (mm)

Get: BoltDiameterShorterFlange(self: StructuralSectionLAngle) -> float

Set: BoltDiameterShorterFlange(self: StructuralSectionLAngle) = value
"""

    BoltSpacing1LongerFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing first row in the longer flange, in. (mm)

Get: BoltSpacing1LongerFlange(self: StructuralSectionLAngle) -> float

Set: BoltSpacing1LongerFlange(self: StructuralSectionLAngle) = value
"""

    BoltSpacing2LongerFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing second row in the longer flange, in. (mm)

Get: BoltSpacing2LongerFlange(self: StructuralSectionLAngle) -> float

Set: BoltSpacing2LongerFlange(self: StructuralSectionLAngle) = value
"""

    BoltSpacingShorterFlange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing in the shorter flange, in. (mm)

Get: BoltSpacingShorterFlange(self: StructuralSectionLAngle) -> float

Set: BoltSpacingShorterFlange(self: StructuralSectionLAngle) = value
"""

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionLAngle) -> float

Set: FlangeFillet(self: StructuralSectionLAngle) = value
"""



class StructuralSectionLProfile(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for L profile structural section.
    
    StructuralSectionLProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionLProfileWithLips(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for L Profile with lips structural section.
    
    StructuralSectionLProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float) """
        pass

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionLProfileWithLips) -> float

Set: LipLength(self: StructuralSectionLProfileWithLips) = value
"""



class StructuralSectionPipeStandard(StructuralSectionRound, IDisposable):
    """
    Defines parameters for pipes also known as RoundHSS or HollowStructuralSection (HSS).
    
    StructuralSectionPipeStandard(diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, wallNominalThickness: float, wallDesignThickness: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, principalAxesAngle, wallNominalThickness, wallDesignThickness, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, wallNominalThickness: float, wallDesignThickness: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of rectangle.

Get: WallDesignThickness(self: StructuralSectionPipeStandard) -> float

Set: WallDesignThickness(self: StructuralSectionPipeStandard) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of rectangle.

Get: WallNominalThickness(self: StructuralSectionPipeStandard) -> float

Set: WallNominalThickness(self: StructuralSectionPipeStandard) = value
"""



class StructuralSectionRectangleHSS(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized rectangle HSS structural section.
    
    StructuralSectionRectangleHSS(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, outerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, outerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, outerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass

    InnerFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Inner Fillet - Corner fillet inner radius.

Get: InnerFillet(self: StructuralSectionRectangleHSS) -> float

Set: InnerFillet(self: StructuralSectionRectangleHSS) = value
"""

    OuterFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Outer Fillet - Corner fillet outer radius.

Get: OuterFillet(self: StructuralSectionRectangleHSS) -> float

Set: OuterFillet(self: StructuralSectionRectangleHSS) = value
"""

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of rectangle.

Get: WallDesignThickness(self: StructuralSectionRectangleHSS) -> float

Set: WallDesignThickness(self: StructuralSectionRectangleHSS) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of rectangle.

Get: WallNominalThickness(self: StructuralSectionRectangleHSS) -> float

Set: WallNominalThickness(self: StructuralSectionRectangleHSS) = value
"""



class StructuralSectionRectangleParameterized(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized rectangle structural section.
    
    StructuralSectionRectangleParameterized(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRectangularBar(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for Rectangular Bar structural section.
    
    StructuralSectionRectangularBar(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRoundBar(StructuralSectionRound, IDisposable):
    """
    Defines parameters for Round Bar structural section.
    
    StructuralSectionRoundBar(diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionRoundHSS(StructuralSectionRound, IDisposable):
    """
    Defines parameters for pipes known as Round HSS (HollowStructuralSection).
    
    StructuralSectionRoundHSS(diameter: float, wallNominalThickness: float, wallDesignThickness: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, diameter, wallNominalThickness, wallDesignThickness, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, diameter: float, wallNominalThickness: float, wallDesignThickness: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass

    WallDesignThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall design thickness of pipe.

Get: WallDesignThickness(self: StructuralSectionRoundHSS) -> float

Set: WallDesignThickness(self: StructuralSectionRoundHSS) = value
"""

    WallNominalThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents wall nominal thickness of pipe.

Get: WallNominalThickness(self: StructuralSectionRoundHSS) -> float

Set: WallNominalThickness(self: StructuralSectionRoundHSS) = value
"""



class StructuralSectionShape(Enum, IComparable, IFormattable, IConvertible):
    """
    Shapes for structural sections.
    
    enum StructuralSectionShape, values: ConcreteCross (34), ConcreteRectangle (31), ConcreteRectangleCut (32), ConcreteRound (35), ConcreteT (33), CParallelFlange (9), CProfile (20), CProfileWithFold (22), CProfileWithLips (21), CSlopedFlange (10), Invalid (-1), IParallelFlange (6), ISlopedFlange (7), ISplitParallelFlange (17), ISplitSlopedFlange (18), IWelded (16), IWideFlange (8), LAngle (11), LProfile (23), LProfileWithLips (24), NotDefined (0), PipeStandard (5), RectangleHSS (14), RectangleParameterized (2), RectangularBar (12), RoundBar (13), RoundHSS (15), SigmaProfile (27), SigmaProfileWithFold (29), SigmaProfileWithLips (28), StructuralTees (19), UserDefined (30), ZProfile (25), ZProfileWithLips (26)
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

    ConcreteCross = None
    ConcreteRectangle = None
    ConcreteRectangleCut = None
    ConcreteRound = None
    ConcreteT = None
    CParallelFlange = None
    CProfile = None
    CProfileWithFold = None
    CProfileWithLips = None
    CSlopedFlange = None
    Invalid = None
    IParallelFlange = None
    ISlopedFlange = None
    ISplitParallelFlange = None
    ISplitSlopedFlange = None
    IWelded = None
    IWideFlange = None
    LAngle = None
    LProfile = None
    LProfileWithLips = None
    NotDefined = None
    PipeStandard = None
    RectangleHSS = None
    RectangleParameterized = None
    RectangularBar = None
    RoundBar = None
    RoundHSS = None
    SigmaProfile = None
    SigmaProfileWithFold = None
    SigmaProfileWithLips = None
    StructuralTees = None
    UserDefined = None
    value__ = None
    ZProfile = None
    ZProfileWithLips = None


class StructuralSectionSigmaProfile(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for Sigma Profile structural section.
    
    StructuralSectionSigmaProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bendWidth: float, middleBendLength: float, topBendLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, bendWidth, middleBendLength, topBendLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bendWidth: float, middleBendLength: float, topBendLength: float) """
        pass

    BendWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend segment width.

Get: BendWidth(self: StructuralSectionSigmaProfile) -> float

Set: BendWidth(self: StructuralSectionSigmaProfile) = value
"""

    MiddleBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Middle Bend segment length.

Get: MiddleBendLength(self: StructuralSectionSigmaProfile) -> float

Set: MiddleBendLength(self: StructuralSectionSigmaProfile) = value
"""

    TopBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Bend segment length.

Get: TopBendLength(self: StructuralSectionSigmaProfile) -> float

Set: TopBendLength(self: StructuralSectionSigmaProfile) = value
"""



class StructuralSectionSigmaProfileWithFold(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for structural Sigma profile section with fold.
    
    StructuralSectionSigmaProfileWithFold(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, foldWidth: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, foldWidth, lipLength, bendWidth, middleBendLength, topBendLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, foldWidth: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float) """
        pass

    BendWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend segment width.

Get: BendWidth(self: StructuralSectionSigmaProfileWithFold) -> float

Set: BendWidth(self: StructuralSectionSigmaProfileWithFold) = value
"""

    FoldWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fold segment width.

Get: FoldWidth(self: StructuralSectionSigmaProfileWithFold) -> float

Set: FoldWidth(self: StructuralSectionSigmaProfileWithFold) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionSigmaProfileWithFold) -> float

Set: LipLength(self: StructuralSectionSigmaProfileWithFold) = value
"""

    MiddleBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Middle Bend segment length.

Get: MiddleBendLength(self: StructuralSectionSigmaProfileWithFold) -> float

Set: MiddleBendLength(self: StructuralSectionSigmaProfileWithFold) = value
"""

    TopBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Bend segment length.

Get: TopBendLength(self: StructuralSectionSigmaProfileWithFold) -> float

Set: TopBendLength(self: StructuralSectionSigmaProfileWithFold) = value
"""



class StructuralSectionSigmaProfileWithLips(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for structural Sigma Profile section with lips.
    
    StructuralSectionSigmaProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, lipLength, bendWidth, middleBendLength, topBendLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, lipLength: float, bendWidth: float, middleBendLength: float, topBendLength: float) """
        pass

    BendWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bend segment width.

Get: BendWidth(self: StructuralSectionSigmaProfileWithLips) -> float

Set: BendWidth(self: StructuralSectionSigmaProfileWithLips) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionSigmaProfileWithLips) -> float

Set: LipLength(self: StructuralSectionSigmaProfileWithLips) = value
"""

    MiddleBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Middle Bend segment length.

Get: MiddleBendLength(self: StructuralSectionSigmaProfileWithLips) -> float

Set: MiddleBendLength(self: StructuralSectionSigmaProfileWithLips) = value
"""

    TopBendLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top Bend segment length.

Get: TopBendLength(self: StructuralSectionSigmaProfileWithLips) -> float

Set: TopBendLength(self: StructuralSectionSigmaProfileWithLips) = value
"""



class StructuralSectionStructuralTees(StructuralSectionHotRolled, IDisposable):
    """
    Defines parameters for Structural Tees structural section.
    
    StructuralSectionStructuralTees(width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing: float, boltSpacingWeb: float, boltDiameter: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, flangeThickness, webThickness, webFillet, flangeFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, boltSpacing, boltSpacingWeb, boltDiameter):
        """ __new__(cls: type, width: float, height: float, flangeThickness: float, webThickness: float, webFillet: float, flangeFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, boltSpacing: float, boltSpacingWeb: float, boltDiameter: float) """
        pass

    BoltDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum bolt hole diameter, in. (mm)

Get: BoltDiameter(self: StructuralSectionStructuralTees) -> float

Set: BoltDiameter(self: StructuralSectionStructuralTees) = value
"""

    BoltSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing in the flange, in. (mm)

Get: BoltSpacing(self: StructuralSectionStructuralTees) -> float

Set: BoltSpacing(self: StructuralSectionStructuralTees) = value
"""

    BoltSpacingWeb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard bolt spacing in the web, in. (mm)

Get: BoltSpacingWeb(self: StructuralSectionStructuralTees) -> float

Set: BoltSpacingWeb(self: StructuralSectionStructuralTees) = value
"""

    FlangeFillet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flange Fillet - fillet radius at the flange end.

Get: FlangeFillet(self: StructuralSectionStructuralTees) -> float

Set: FlangeFillet(self: StructuralSectionStructuralTees) = value
"""



class StructuralSectionUserDefined(StructuralSectionRectangular, IDisposable):
    """
    Defines parameters for parameterized user defined structural section.
    
    StructuralSectionUserDefined(width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis):
        """ __new__(cls: type, width: float, height: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float) """
        pass


class StructuralSectionUtils(object):
    """ This class provides utilities related to Structural Section Properties. """
    @staticmethod
    def GetStructuralSection(document, familySymbolId):
        """
        GetStructuralSection(document: Document, familySymbolId: ElementId) -> StructuralSection
        
            Return structural section from element.
        
            document: The document that owns the family for beam, brace or structural column.
            familySymbolId: ID of family symbol for beam, brace or structural column.
            Returns: Structural section returned if element have one.
           For elements that do not 
             have structural section or can not have structural section ll will be returned.
        """
        pass

    @staticmethod
    def SetStructuralSection(document, familySymbolId, structuralSection):
        """
        SetStructuralSection(document: Document, familySymbolId: ElementId, structuralSection: StructuralSection) -> bool
        
            Set structural section in element.
        
            document: The document that owns the family for beam, brace or structural column.
            familySymbolId: ID of family symbol for beam, brace or structural column.
            structuralSection: Structural section with values that will be set.
            Returns: True is returned when requested shape with values was properly set. Return 
             false otherwise.
        """
        pass

    __all__ = [
        'GetStructuralSection',
        'SetStructuralSection',
    ]


class StructuralSectionZProfile(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for Z Profile structural section.
    
    StructuralSectionZProfile(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, bottomFlangeLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float) """
        pass

    BottomFlangeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange segment length.

Get: BottomFlangeLength(self: StructuralSectionZProfile) -> float

Set: BottomFlangeLength(self: StructuralSectionZProfile) = value
"""



class StructuralSectionZProfileWithLips(StructuralSectionColdFormed, IDisposable):
    """
    Defines parameters for Z Profile with lips structural section.
    
    StructuralSectionZProfileWithLips(width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float, lipLength: float)
    """
    def Dispose(self):
        """ Dispose(self: StructuralSection, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: StructuralSection, disposing: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, width, height, wallNominalThickness, wallDesignThickness, innerFillet, centroidHorizontal, centroidVertical, principalAxesAngle, sectionArea, perimeter, nominalWeight, momentOfInertiaStrongAxis, momentOfInertiaWeakAxis, elasticModulusStrongAxis, elasticModulusWeakAxis, plasticModulusStrongAxis, plasticModulusWeakAxis, torsionalMomentOfInertia, torsionalModulus, warpingConstant, shearAreaStrongAxis, shearAreaWeakAxis, bottomFlangeLength, lipLength):
        """ __new__(cls: type, width: float, height: float, wallNominalThickness: float, wallDesignThickness: float, innerFillet: float, centroidHorizontal: float, centroidVertical: float, principalAxesAngle: float, sectionArea: float, perimeter: float, nominalWeight: float, momentOfInertiaStrongAxis: float, momentOfInertiaWeakAxis: float, elasticModulusStrongAxis: float, elasticModulusWeakAxis: float, plasticModulusStrongAxis: float, plasticModulusWeakAxis: float, torsionalMomentOfInertia: float, torsionalModulus: float, warpingConstant: float, shearAreaStrongAxis: float, shearAreaWeakAxis: float, bottomFlangeLength: float, lipLength: float) """
        pass

    BottomFlangeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bottom Flange segment length.

Get: BottomFlangeLength(self: StructuralSectionZProfileWithLips) -> float

Set: BottomFlangeLength(self: StructuralSectionZProfileWithLips) = value
"""

    LipLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lip segment length.

Get: LipLength(self: StructuralSectionZProfileWithLips) -> float

Set: LipLength(self: StructuralSectionZProfileWithLips) = value
"""



