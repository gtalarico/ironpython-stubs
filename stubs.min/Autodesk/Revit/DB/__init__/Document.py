class Document(object, IDisposable):
    """ An object that represents an open Autodesk Revit project. """
    def AutoJoinElements(self):
        """
        AutoJoinElements(self: Document)
            Forces the elements in the Revit document to automatically join to their 
             neighbors where appropriate.
        """
        pass

    def CanEnableWorksharing(self):
        """
        CanEnableWorksharing(self: Document) -> bool
        
            Checks if worksharing can be enabled in the document.
            Returns: True if worksharing can be enabled in the document, False otherwise.
        """
        pass

    def Close(self, saveModified=None):
        """
        Close(self: Document, saveModified: bool) -> bool
        
            Closes the document with the option to save.
        
            saveModified: Indicates if the current document should be saved before close operation.
            Returns: False if closing procedure fails or if saving of a modified document was 
             requested (saveModified = True) but failed. 
        Also returns False if closing is 
             cancelled by an external application during 'DocumentClosing' event. 
        When 
             function succeeds, True is returned.
        
        Close(self: Document) -> bool
        
            Closes the document, save the changes if there are.
            Returns: False if either closing procedure fails or if saving of a modified document 
             failed. 
        Also returns False if closing is cancelled by an external application 
             during 'DocumentClosing' event. 
        When function succeeds, True is returned.
        """
        pass

    def CombineElements(self, members):
        """
        CombineElements(self: Document, members: CombinableElementArray) -> GeomCombination
        
            Combine a set of combinable elements into a geometry combination.
        
            members: A list of combinable elements to be combined.
            Returns: If successful, the newly created geometry combination is returned, otherwise an
             
        exception with error information will be thrown.
        """
        pass

    def ConvertDetailToModelCurves(self, view, detailCurves):
        """
        ConvertDetailToModelCurves(self: Document, view: View, detailCurves: DetailCurveArray) -> ModelCurveArray
        
            Converts a group of DetailCurves to equivalent ModelCurves.
        
            view: The view where the new lines will be created.
        The lines are projected on the 
             view workplane.
        The view workplane must be parallel to the view plane.
        
            detailCurves: The detail curve array to be converted.
        """
        pass

    def ConvertModelToDetailCurves(self, view, modelCurves):
        """
        ConvertModelToDetailCurves(self: Document, view: View, modelCurves: ModelCurveArray) -> DetailCurveArray
        
            Converts a group of ModelCurves to equivalent DetailCurves.
        
            view: The view where the new lines will be created.  
        The lines are projected on the 
             view plane.
        If the lines are not parallel to the view plane, lines are 
             foreshortened and arcs are converted to ellipses.
        Splines are modified.
        
            modelCurves: The model curve array to be converted.
        """
        pass

    def ConvertModelToSymbolicCurves(self, view, modelCurves):
        """
        ConvertModelToSymbolicCurves(self: Document, view: View, modelCurves: ModelCurveArray) -> SymbolicCurveArray
        
            Converts a group of ModelCurves to equivalent SymbolicCurves.
        
            view: The view where the new lines will be created. 
        The lines are projected on the 
             view workplane.
        The view workplane must be parallel to the view plane.
        If the 
             lines are not parallel to the view plane, lines are foreshortened and arcs are 
             converted to ellipses.
        Splines are modified.
        
            modelCurves: The model curve array to be converted.
        """
        pass

    def ConvertSymbolicToModelCurves(self, view, symbolicCurve):
        """
        ConvertSymbolicToModelCurves(self: Document, view: View, symbolicCurve: SymbolicCurveArray) -> ModelCurveArray
        
            Converts a group of SymbolicCurves to equivalent ModelCurves.
        
            view: The view where the new lines will be created.
        The lines are projected on the 
             view workplane.
        The view workplane must be parallel to the view plane.
        
            symbolicCurve: The symbolic curve array to be converted.
        """
        pass

    def Delete(self, *__args):
        """
        Delete(self: Document, elementId: ElementId) -> ICollection[ElementId]
        
            Deletes an element from the document given the id of that element.
        
            elementId: Id of the element to delete.
            Returns: The deleted element id set.
        Delete(self: Document, elementIds: ICollection[ElementId]) -> ICollection[ElementId]
        """
        pass

    def Dispose(self):
        """ Dispose(self: Document) """
        pass

    def EditFamily(self, loadedFamily):
        """
        EditFamily(self: Document, loadedFamily: Family) -> Document
        
            Gets the document of a loaded family to edit.
        
            loadedFamily: The loaded family in current document.
            Returns: Reference of the document of the family.
        """
        pass

    def EnableWorksharing(self, worksetNameGridLevel, worksetName):
        """
        EnableWorksharing(self: Document, worksetNameGridLevel: str, worksetName: str)
            Enables worksharing in the document.
        
            worksetNameGridLevel: Name of workset for grids and levels.
            worksetName: Name of workset for all other elements.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Document, obj: object) -> bool
        
            Determines whether the specified System.Object equals to this System.Object.
        """
        pass

    def Export(self, folder, name, *__args):
        """
        Export(self: Document, folder: str, name: str, views: ViewSet, options: FBXExportOptions) -> bool
        
            Exports the document in 3D-Studio Max (FBX) format.
        
            folder: Output folder, into which file(s) will be exported. The folder must exist.
            name: Either the name of a single file or a prefix for a set of files.
                      
                  If ll or empty, automatic naming will be used.
        
            views: Selection of views to be exported.Only 3D views are allowed.
            options: Options applicable to the FBX format.
            Returns: Function returns true only if all specified views are exported successfully. 
        
             The function returns False if exporting of any view fails, even if some views 
             might have been exported successfully.
        
        Export(self: Document, folder: str, name: str, views: ICollection[ElementId], options: DWGExportOptions) -> bool
        Export(self: Document, folder: str, name: str, views: ICollection[ElementId], options: DXFExportOptions) -> bool
        Export(self: Document, folder: str, name: str, view: View3D, grossAreaPlan: ViewPlan, options: BuildingSiteExportOptions) -> bool
        
            Exports the document in the format of Civil Engineering design applications.
        
            folder: Output folder, into which file will be exported. The folder must exist.
            name: The name for the exported civil file. 
                           If ll or empty, 
             automatic naming will be used."
        
            view: 3D View to be exported.
            grossAreaPlan: All the areas on the view plan will be exported, it must be 'Gross Building' 
             area plan. It must not be ll.
                                    To check whether its 
             area scheme is Gross Building, use IsGrossBuildingArea property of 
             Autodesk.Revit.DB.AreaScheme.
        
            options: Various options applicable to the format of Civil Engineering design 
             applications.
                              If ll, all options will be set to their 
             respective default values.
        
            Returns: True if successful, otherwise False.
        Export(self: Document, folder: str, name: str, views: ViewSet, options: DWFExportOptions) -> bool
        
            Exports the current view or a selection of views in DWF format.
        
            folder: Output folder, into which file(s) will be exported. The folder must exist.
            name: Either the name of a single file or a prefix for a set of files.
                      
                  If ll or empty, automatic naming will be used.
        
            views: Selection of views to be exported.
            options: Various options applicable to the DWF format.
                           If ll, all 
             options will be set to their respective default values.
        
            Returns: Function returns true only if all specified views are exported successfully. 
             Returns False if exporting of any view fails, 
        even if some views might have 
             been exported successfully.
        
        Export(self: Document, folder: str, name: str, views: ViewSet, options: DWFXExportOptions) -> bool
        
            Exports the current view or a selection of views in DWFX format.
        
            folder: Output folder, into which file(s) will be exported. The folder must exist.
            name: Either the name of a single file or a prefix for a set of files.
                      
                  If ll or empty, automatic naming will be used.
        
            views: Selection of views to be exported.
            options: Various options applicable to the DWFX format.
                           If ll, all 
             options will be set to their respective default values.
        
            Returns: Function returns true only if all specified views are exported successfully.
        
             The function returns False if exporting of any view fails, even if some views 
             might have been exported successfully.
        
        Export(self: Document, folder: str, name: str, options: NavisworksExportOptions)
            Exports a Revit project to the Navisworks .nwc format.
        
            folder: The name of the folder for the exported file.
            name: The name of the exported file.  If it doesn't end in '.nwc', this extension 
             will be added automatically.
        
            options: Options which control the contents of the export.
        Export(self: Document, folder: str, name: str, options: MassGBXMLExportOptions)
            Exports a gbXML file from a mass model document.
        
            folder: Indicates the path of a folder where to export the gbXML file.
            name: Indicates the name of the gbXML file to export. If it doesn't end with ".xml", 
             extension ".xml" will be added automatically. The name cannot contain any of 
             the following characters: \/:*?"<>|. Empty name is not acceptable.
        
            options: Options which control the contents of the export.
        Export(self: Document, folder: str, name: str, options: GBXMLExportOptions) -> bool
        
            Export the model in gbXML (green-building) format.
        
            folder: Indicates the path of a folder where to export the gbXML file.
            name: Indicates the name of the gbXML file to export. If it doesn't end with ".xml", 
             extension ".xml" will be added automatically. The name cannot contain any of 
             the following characters: \/:*?"<>|. Empty name is not acceptable.
        
            options: Options which control the contents of the export.
            Returns: True if successful, otherwise False.
        Export(self: Document, folder: str, name: str, views: ICollection[ElementId], options: DGNExportOptions) -> bool
        Export(self: Document, folder: str, name: str, views: ICollection[ElementId], options: SATExportOptions) -> bool
        Export(self: Document, folder: str, name: str, options: IFCExportOptions) -> bool
        
            Exports the document to the Industry Standard Classes (IFC) format.
        
            folder: Output folder into which the file will be exported. The folder must exist.
            name: Either the name of a single file or a prefix for a set of files.
           If empty, 
             automatic naming will be used.
        
            options: Various options applicable to the IFC format.
           If ll, all options will be 
             set to their respective default values.
        
            Returns: True if successful, otherwise False.
        """
        pass

    def ExportImage(self, options):
        """
        ExportImage(self: Document, options: ImageExportOptions)
            Exports a view or set of views into an image file.
        
            options: The options which govern the image export.
        """
        pass

    def GetDefaultElementTypeId(self, defaultTypeId):
        """
        GetDefaultElementTypeId(self: Document, defaultTypeId: ElementTypeGroup) -> ElementId
        
            Gets the default element type id with the given DefaultElementType id.
        
            defaultTypeId: The default element type id.
            Returns: The element type id.
        """
        pass

    def GetDefaultFamilyTypeId(self, familyCategoryId):
        """
        GetDefaultFamilyTypeId(self: Document, familyCategoryId: ElementId) -> ElementId
        
            Gets the default family type id with the given family category id.
        
            familyCategoryId: The family category id.
            Returns: The default family type id.
        """
        pass

    def GetDocumentPreviewSettings(self):
        """
        GetDocumentPreviewSettings(self: Document) -> DocumentPreviewSettings
        
            Returns the preview settings for the given document.
            Returns: The preview settings.
        """
        pass

    @staticmethod
    def GetDocumentVersion(doc):
        """
        GetDocumentVersion(doc: Document) -> DocumentVersion
        
            Gets the DocumentVersion that corresponds to a document.
        
            doc: The document whose DocumentVersion will be returned.
            Returns: The DocumentVersion corresponding to the given document.
        """
        pass

    def GetElement(self, *__args):
        """
        GetElement(self: Document, reference: Reference) -> Element
        
            Gets the Element referenced by the input reference.
        
            reference: The reference, whose referenced Element will be retrieved from the model.
            Returns: The element referenced by the input argument.
        GetElement(self: Document, uniqueId: str) -> Element
        
            Gets the Element referenced by a unique id string.
        
            uniqueId: The element unique id, whose referenced Element will be retrieved from the 
             model.
           Autodesk.Revit.DB.Element.UniqueId
        
            Returns: The element referenced by the input argument.
        GetElement(self: Document, id: ElementId) -> Element
        
            Gets the Element referenced by the input string name.
        
            id: The ElementId, whose referenced Element will be retrieved from the model.
            Returns: The element referenced by the input argument.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Document) -> int
        
            Gets the hash code of this document instance.
        """
        pass

    def GetPaintedMaterial(self, elementId, face):
        """
        GetPaintedMaterial(self: Document, elementId: ElementId, face: Face) -> ElementId
        
            Get the material painted on the element's face. Returns invalidElementId if the 
             face is not painted.
        
        
            elementId: The element that the face belongs to.
            face: The painted element's face.
            Returns: The material's Id painted on the element's face.
        """
        pass

    def GetPrintSettingIds(self):
        """
        GetPrintSettingIds(self: Document) -> ICollection[ElementId]
        
            Retrieves all Print Settings of current project.
            Returns: The ElementIds of all print setting elements
        """
        pass

    def GetRoomAtPoint(self, point, phase=None):
        """
        GetRoomAtPoint(self: Document, point: XYZ, phase: Phase) -> Room
        
            Gets a room containing the point.
        
            point: Point to be checked.
            phase: Phase in which the room exists.
            Returns: The room containing the point.
        GetRoomAtPoint(self: Document, point: XYZ) -> Room
        
            Gets a room containing the point.
        
            point: Point to be checked.
            Returns: The room containing the point.
        """
        pass

    def GetSpaceAtPoint(self, point, phase=None):
        """
        GetSpaceAtPoint(self: Document, point: XYZ, phase: Phase) -> Space
        
            Gets a space containing the point.
        
            point: Point to be checked.
            phase: Phase in which the space exists.
            Returns: The space containing the point.
        GetSpaceAtPoint(self: Document, point: XYZ) -> Space
        
            Gets a space containing the point.
        
            point: Point to be checked.
            Returns: The space containing the point.
        """
        pass

    def GetUnits(self):
        """
        GetUnits(self: Document) -> Units
        
            Gets the Units object.
            Returns: The Units object.
        """
        pass

    def GetWorksetId(self, id):
        """
        GetWorksetId(self: Document, id: ElementId) -> WorksetId
        
            Get Id of the Workset which owns the element.
        
            id: Id of the element.
            Returns: Id of the Workset which owns the element.
        """
        pass

    def GetWorksetTable(self):
        """
        GetWorksetTable(self: Document) -> WorksetTable
        
            Get the WorksetTable of this document.
            Returns: The WorksetTable of this document.
        """
        pass

    def GetWorksharingCentralModelPath(self):
        """
        GetWorksharingCentralModelPath(self: Document) -> ModelPath
        
            Gets the central model path of the worksharing model.
            Returns: The central model path, or null if the document is not workshared.
        """
        pass

    def HasAllChangesFromCentral(self):
        """
        HasAllChangesFromCentral(self: Document) -> bool
        
            Returns whether the model in the current session is up to date with central.
            Returns: True means up to date; false means out of date.
            If central is locked but 
             Revit can determine that
           the model in the current session is out of date
          
              without opening central, this method will return false
           instead of throwing 
             CentralModelContentionException.
        """
        pass

    def Import(self, file, options, *__args):
        """
        Import(self: Document, file: str, options: DWGImportOptions, pDBView: View) -> (bool, ElementId)
        
            Imports a DWG or DXF file to the document.
        
            file: Full path of the file to import. File must exist and must be a valid DWG or DXF 
             file.
        
            options: Various options applicable to the DWG or DXF format. If ll, all options will be 
             set to their respective default values.
        
            pDBView: The view into which the file wil be imported.
            Returns: True if successful, otherwise False.
        Import(self: Document, file: str, options: GBXMLImportOptions) -> bool
        
            Imports a Green-Building XML file into the document.
        
            file: Full path of the file to import. File must exist.
            options: Various options applicable to GBXml import. If ll, all options will be set to 
             their respective default values.
        
            Returns: True if successful, otherwise False.
        Import(self: Document, file: str, options: ImageImportOptions, view: View) -> (bool, Element)
        
            Imports an image (a bitmap) into the document.
        
            file: Full path of the file to import. File must exist.
            options: Various options applicable to an image.
        If ll, all options will be set to 
             their respective default values.
        
            view: The view into which the image is going to be imported.
            Returns: True if successful, otherwise False.
        Import(self: Document, file: str, options: DGNImportOptions, pDBView: View) -> (bool, ElementId)
        
            Imports a DGN file to the document.
        
            file: Full path of the file to import. File must exist and must be a valid DGN file.
            options: Various options applicable to the DGN format. If ll, all options will be set to 
             their respective default values.
        
            pDBView: The view into which the file will be imported.
            Returns: True if successful, otherwise False.
        Import(self: Document, file: str, options: SKPImportOptions, pDBView: View) -> ElementId
        
            Imports an SKP file into the document.
        
            file: Full path of the file to link. File must exist and must be a valid SAT file.
            options: Various import options applicable to the SKP format. If ll, all options will be 
             set to their respective default values.
        
            pDBView: The view into which the file will be linked.
            Returns: Returns the element Id of the linked instance.
        Import(self: Document, file: str, options: SATImportOptions, pDBView: View) -> ElementId
        
            Imports an SAT file into the document.
        
            file: Full path of the file to link. File must exist and must be a valid SAT file.
            options: Various import options applicable to the SAT format. If ll, all options will be 
             set to their respective default values.
        
            pDBView: The view into which the file will be linked.
            Returns: Returns the element Id of the linked instance.
        """
        pass

    def IsDefaultElementTypeIdValid(self, defaultTypeId, typeId):
        """
        IsDefaultElementTypeIdValid(self: Document, defaultTypeId: ElementTypeGroup, typeId: ElementId) -> bool
        
            Checks whether the element type id is valid for the give DefaultElmentType id.
        
            defaultTypeId: The default element type id.
            typeId: The element type id.
            Returns: True if the element type id is valid for the give DefaultElmentType id, false 
             otherwise.
        """
        pass

    def IsDefaultFamilyTypeIdValid(self, familyCategoryId, familyTypeId):
        """
        IsDefaultFamilyTypeIdValid(self: Document, familyCategoryId: ElementId, familyTypeId: ElementId) -> bool
        
            Checks whether the family type id is valid for the give family category.
        
            familyCategoryId: The family category id.
            familyTypeId: The default family type id.
            Returns: True if the family type id is valid for the give family category, false 
             otherwise.
        """
        pass

    def IsPainted(self, elementId, face):
        """
        IsPainted(self: Document, elementId: ElementId, face: Face) -> bool
        
            Checks if the element's face is painted with a material.
        
            elementId: The element that the face belongs to.
            face: The painted element's face.
            Returns: True if the element's face is painted.
        """
        pass

    def Link(self, file, options, pDBView=None, elementId=None):
        """
        Link(self: Document, file: str, options: SATImportOptions, pDBView: View) -> ElementId
        
            Links an SAT file into the document.
        
            file: Full path of the file to link. File must exist and must be a valid SAT file.
            options: Various import options applicable to the SAT format. If ll, all options will be 
             set to their respective default values.
        
            pDBView: The view into which the file will be linked.
            Returns: Returns the element Id of the linked instance.
        Link(self: Document, file: str, options: DWGImportOptions, pDBView: View) -> (bool, ElementId)
        
            Links a DWG or DXF file to the document.
        
            file: Full path of the file to link. File must exist and must be a valid DWG or DXF 
             file.
        
            options: Various import options applicable to the DWG or DXF format. If ll, all options 
             will be set to their respective default values.
        
            pDBView: The view into which the file will be linked.
            Returns: True if successful, otherwise False.
        Link(self: Document, file: str, options: SKPImportOptions, pDBView: View) -> ElementId
        
            Links an SKP file into the document.
        
            file: Full path of the file to link. File must exist and must be a valid SAT file.
            options: Various import options applicable to the SKP format. If ll, all options will be 
             set to their respective default values.
        
            pDBView: The view into which the file will be linked.
            Returns: Returns the element Id of the linked instance.
        Link(self: Document, file: str, options: DWFImportOptions) -> IList[ElementId]
        
            Links Markups in a DWF file to the document.
        
            file: Full path of the file to link. File must exist and must be a valid DWF file.
            options: Various link options applicable to the DWF format.
            Returns: A collection of link instance element ids created by the markup link.
        Link(self: Document, file: str, options: DGNImportOptions, pDBView: View) -> (bool, ElementId)
        
            Links a DGN file to the document.
        
            file: Full path of the file to link. File must exist and must be a valid DGN file.
            options: Various import options applicable to the DGN format. If ll, all options will be 
             set to their respective default values.
        
            pDBView: The view into which the file will be linked.
            Returns: True if successful, otherwise False.
        """
        pass

    def LoadFamily(self, *__args):
        """
        LoadFamily(self: Document, filename: str) -> (bool, Family)
        
            Loads an entire family and all its types/symbols into the document and provides 
             a reference
        to the loaded family.
        
        
            filename: The fully qualified filename of the Family file, usually ending in .rfa.
            Returns: True if the entire family was loaded successfully into the project, otherwise 
             False.
        
        LoadFamily(self: Document, filename: str) -> bool
        
            Loads an entire family and all its types/symbols into the document.
        
            filename: The fully qualified filename of the Family file, usually ending in .rfa.
            Returns: True if the entire family was loaded successfully into the project, otherwise 
             False.
        
        LoadFamily(self: Document, filename: str, familyLoadOptions: IFamilyLoadOptions) -> (bool, Family)
        
            Loads an entire family and all its types/symbols into the document and provides 
             a reference
        to the loaded family.
        
        
            filename: The fully qualified filename of the Family file, usually ending in .rfa.
            familyLoadOptions: The interface implementation to use when loading a family into the document.
            Returns: True if the entire family was loaded successfully into the project, otherwise 
             False.
        
        LoadFamily(self: Document, targetDocument: Document, familyLoadOptions: IFamilyLoadOptions) -> Family
        
            Loads the contents of this family document into another document.
        
            targetDocument: The target document which the family will be loaded into.
            familyLoadOptions: The interface implementation to use when responding to conflicts during the 
             load operation.
        
            Returns: Reference of the family in the target document.
        LoadFamily(self: Document, targetDocument: Document) -> Family
        
            Loads the contents of this family document into another document.
        
            targetDocument: The target document where the family will be loaded.
            Returns: Reference of the family in the target document.
        """
        pass

    def LoadFamilySymbol(self, filename, name, *__args):
        """
        LoadFamilySymbol(self: Document, filename: str, name: str) -> bool
        
            Loads only a specified family type/symbol from a family file into the document.
        
            filename: The fully qualified filename of the Family file, usually ending in .rfa.
            name: The name of the type/symbol to be loaded, such as "W11x14".
            Returns: True if the family type/symbol was loaded successfully into the project, 
             otherwise False.
        
        LoadFamilySymbol(self: Document, filename: str, name: str) -> (bool, FamilySymbol)
        
            Loads only the specified family type/symbol from a family file into the 
             document and
        provides a reference to the loaded family symbol.
        
        
            filename: The fully qualified filename of the Family file, usually ending in .rfa.
            name: The name of the type/symbol to be loaded, such as "W11x14".
            Returns: True if the family type/symbol was loaded successfully into the project, 
             otherwise False.
        
        LoadFamilySymbol(self: Document, filename: str, name: str, familyLoadOptions: IFamilyLoadOptions) -> (bool, FamilySymbol)
        
            Loads only the specified family type/symbol from a family file into the 
             document and
        provides a reference to the loaded family symbol.
        
        
            filename: The fully qualified filename of the Family file, usually ending in .rfa.
            name: The name of the type/symbol to be loaded, such as "W11x14".
            familyLoadOptions: The interface implementation to use when loading a family into the document.
            Returns: True if the family type/symbol was loaded successfully into the project, 
             otherwise False.
        """
        pass

    def MakeTransientElements(self, maker):
        """
        MakeTransientElements(self: Document, maker: ITransientElementMaker)
            This method encapsulates the process of creating transient elements in the 
             document.
        
        
            maker: An instance of a class that implements the  
             Autodesk.Revit.DB.ITransientElementMaker interface.
           The maker will be 
             called to create element(s) which would become transient.
        """
        pass

    def Paint(self, elementId, face, *__args):
        """
        Paint(self: Document, elementId: ElementId, face: Face, familyParameter: FamilyParameter)
            Paint the element's face with specified material.
        
            elementId: The element that the face belongs to.
            face: The painted element's face.
            familyParameter: The family parameter associated with a material.
        Paint(self: Document, elementId: ElementId, face: Face, materialId: ElementId)
            Paint the element's face with specified material.
        
            elementId: The element that the face belongs to.
            face: The painted element's face.
            materialId: The material to be painted on the face
        """
        pass

    def PostFailure(self, failure):
        """
        PostFailure(self: Document, failure: FailureMessage) -> FailureMessageKey
        
            Posts a failure to be displayed to the user at the end of transaction.
        
            failure: The failure to be posted.
            Returns: A unique key that identifies posted failure message in a document. If exactly 
             the same error is posted more than once,
           and not removed between the 
             postings, returned key will be the same every time.
        """
        pass

    def Print(self, views, *__args):
        """
        Print(self: Document, views: ViewSet, useCurrentPrintSettings: bool)
            Prints a set of views with default view template and default print settings.
        
            views: The set of views which need to be printed.
            useCurrentPrintSettings: If true, print the view with the current print setting,
        otherwise with the 
             print setting of the document of the view.
        
        Print(self: Document, views: ViewSet)
            Prints a set of views with default view template and default print settings.
        
            views: The set of views which need to be printed.
        Print(self: Document, views: ViewSet, viewTemplate: View, useCurrentPrintSettings: bool)
            Prints a set of views with a specified view template and default print settings.
        
            views: The set of views which need to be printed.
            viewTemplate: The view template which apply to the set of views.
            useCurrentPrintSettings: If true, print the view with the current print setting,
        otherwise with the 
             print setting of the document of the view.
        
        Print(self: Document, views: ViewSet, viewTemplate: View)
            Prints a set of views with a specified view template and default print settings.
        
            views: The set of views which need to be printed.
            viewTemplate: The view template which apply to the set of views.
        """
        pass

    def Regenerate(self):
        """
        Regenerate(self: Document)
            Updates the elements in the Revit document to reflect all changes.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Document, disposing: bool) """
        pass

    def ReleaseUnmanagedResources_(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources_(self: Document, disposing: bool) """
        pass

    def ReloadLatest(self, reloadOptions):
        """
        ReloadLatest(self: Document, reloadOptions: ReloadLatestOptions)
            Fetches changes from central (due to one or more synchronizations with central)
             
           and merges them into the current session.
        
        
            reloadOptions: Various options to control behavior of reloadLatest.
        """
        pass

    def RemovePaint(self, elementId, face):
        """
        RemovePaint(self: Document, elementId: ElementId, face: Face)
            Remove the material painted on the element's face.
           If the face is currently 
             not painted,it will do nothing.
        
        
            elementId: The element that the painted face belongs to.
            face: The painted element's face.
        """
        pass

    def Save(self, options=None):
        """
        Save(self: Document)
            Saves the document.
        Save(self: Document, options: SaveOptions)
            Saves the document.
        
            options: Options to control the Save operation.
        """
        pass

    def SaveAs(self, *__args):
        """
        SaveAs(self: Document, filepath: str)
            Saves the document to a given file path.
        
            filepath: File name and path to be saved as. Either a relative or absolute path can be 
             provided.
        
        SaveAs(self: Document, filepath: str, options: SaveAsOptions)
            Saves the document to a given file path.
        
            filepath: File name and path to be saved as. Either a relative or absolute path can be 
             provided.
        
            options: Options to govern the SaveAs operation.
        SaveAs(self: Document, path: ModelPath, options: SaveAsOptions)
            Saves the document to a given path.
        
            path: Name and path to be saved as. For a file path, either a relative or absolute 
             path can be provided.
        
            options: Options to govern the SaveAs operation.
        """
        pass

    def SaveToProjectAsImage(self, options):
        """
        SaveToProjectAsImage(self: Document, options: ImageExportOptions) -> ElementId
        
            Creates an image view from the currently active view.
        
            options: The options which govern the image creation.
            Returns: Id of the newly created view if the operation succeeded, invalid element id 
             otherwise.
        """
        pass

    def SeparateElements(self, members):
        """
        SeparateElements(self: Document, members: CombinableElementArray)
            Separate a set of combinable elements out of combinations they currently belong 
             to.
        
        
            members: A list of combinable elements to be separated.
        """
        pass

    def SetDefaultElementTypeId(self, defaultTypeId, typeId):
        """
        SetDefaultElementTypeId(self: Document, defaultTypeId: ElementTypeGroup, typeId: ElementId)
            Sets the default element type id of the given DefaultElementType id.
        
            defaultTypeId: The default element type id.
            typeId: The element type id.
        """
        pass

    def SetDefaultFamilyTypeId(self, familyCategoryId, familyTypeId):
        """
        SetDefaultFamilyTypeId(self: Document, familyCategoryId: ElementId, familyTypeId: ElementId)
            Sets the default family type id for the given family category.
        
            familyCategoryId: The family category id.
            familyTypeId: The default family type id.
        """
        pass

    def SetUnits(self, units):
        """
        SetUnits(self: Document, units: Units)
            Sets the units.
        
            units: The units.
        """
        pass

    def SynchronizeWithCentral(self, transactOptions, syncOptions):
        """
        SynchronizeWithCentral(self: Document, transactOptions: TransactWithCentralOptions, syncOptions: SynchronizeWithCentralOptions)
            Performs reload latest until the model in the current session is up to date and 
             then saves changes back to central.
           A save to central is performed even if 
             no changes were made.
        
        
            transactOptions: Options to customize behavior accessing the central model.
            syncOptions: Options to customize behavior of SynchronizeWithCentral.
        """
        pass

    def UnpostFailure(self, messageKey):
        """
        UnpostFailure(self: Document, messageKey: FailureMessageKey)
            Deletes the posted failure message associated with a given FailureMessageKey.
        
            messageKey: The key of the FailureMessage to be deleted.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActiveProjectLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the active project location.

Get: ActiveProjectLocation(self: Document) -> ProjectLocation

Set: ActiveProjectLocation(self: Document) = value
"""

    ActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document's active view.

Get: ActiveView(self: Document) -> View

"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Application in which the Document resides.

Get: Application(self: Document) -> Application

"""

    Create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object that can be used to create new instances of Autodesk Revit API elements
within a project.

Get: Create(self: Document) -> Document

"""

    DisplayUnitSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides access to display unit type with in the document.

Get: DisplayUnitSystem(self: Document) -> DisplayUnit

"""

    FamilyCreate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object that can be used to create new instances of Autodesk Revit API elements
within a family document.

Get: FamilyCreate(self: Document) -> FamilyItemFactory

"""

    FamilyManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The family manager object provides access to family types and parameters.

Get: FamilyManager(self: Document) -> FamilyManager

"""

    IsDetached = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if a workshared document is detached.
   Also, see Autodesk.Revit.DB.Document.IsWorkshared

Get: IsDetached(self: Document) -> bool

"""

    IsFamilyDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the current document is a family document.

Get: IsFamilyDocument(self: Document) -> bool

"""

    IsLinked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if a document is a linked RVT.

Get: IsLinked(self: Document) -> bool

"""

    IsModifiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document's state of modifiability.

Get: IsModifiable(self: Document) -> bool

"""

    IsModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of changes made to the document.

Get: IsModified(self: Document) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if the document is read-only or can possibly be modified.

Get: IsReadOnly(self: Document) -> bool

"""

    IsReadOnlyFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signals whether the document was opened from a read-only file.

Get: IsReadOnlyFile(self: Document) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Document) -> bool

"""

    IsWorkshared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if worksharing (i.e. editing permissions and multiple worksets) have been enabled in the document.
   Also, see Autodesk.Revit.DB.Document.IsDetached

Get: IsWorkshared(self: Document) -> bool

"""

    MassDisplayTemporaryOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This setting controls temporary display in views of objects with mass category or subcategories.

Get: MassDisplayTemporaryOverride(self: Document) -> MassDisplayTemporaryOverrideType

Set: MassDisplayTemporaryOverride(self: Document) = value
"""

    MullionTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property is used to retrieve all the mullion types in current system.

Get: MullionTypes(self: Document) -> MullionTypeSet

"""

    OwnerFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Family of this Family Document.

Get: OwnerFamily(self: Document) -> Family

"""

    PanelTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves a set of PanelType objects that contains all the panel types that are currently loaded into the
project.

Get: PanelTypes(self: Document) -> PanelTypeSet

"""

    ParameterBindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object from which mappings between parameter definitions and categories can
be found.

Get: ParameterBindings(self: Document) -> BindingMap

"""

    PathName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fully qualified path of the document's disk file.

Get: PathName(self: Document) -> str

"""

    Phases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves all the object that represent phases within the project.

Get: Phases(self: Document) -> PhaseArray

"""

    PrintManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the PrintManager of current project.

Get: PrintManager(self: Document) -> PrintManager

"""

    ProjectInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the Project Information of the current project.

Get: ProjectInformation(self: Document) -> ProjectInfo

"""

    ProjectLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve all the project locations associated with this project

Get: ProjectLocations(self: Document) -> ProjectLocationSet

"""

    ReactionsAreUpToDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reports if the analytical model has regenerated in a document with reaction loads.

Get: ReactionsAreUpToDate(self: Document) -> bool

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides access to general application settings, such as Categories.

Get: Settings(self: Document) -> Settings

"""

    SiteLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the site location information.

Get: SiteLocation(self: Document) -> SiteLocation

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The document's title.

Get: Title(self: Document) -> str

"""

    WorksharingCentralGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The central GUID of the server-based model.

Get: WorksharingCentralGUID(self: Document) -> Guid

"""


    DocumentClosing = None
    DocumentPrinted = None
    DocumentPrinting = None
    DocumentSaved = None
    DocumentSavedAs = None
    DocumentSaving = None
    DocumentSavingAs = None
    ViewPrinted = None
    ViewPrinting = None

