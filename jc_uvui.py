import maya.cmds as cmds
import maya.mel as mel
import math


class uvui(object):
    windowName = "jc_UVUI_window"


    def show(self):
        # checks if window is already open, closes and recreates if it is
        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName, title="UV UI", minimizeButton=False,
                    maximizeButton=False, sizeable=True, rtf=True)
        self.buildUI()
        cmds.showWindow()
    def buildUI_bw(self):
        columnMain = cmds.columnLayout(columnWidth=200)
        widthb = 61
        widtha = 40
        widthc = 29
        widthe = 124

        white = [1,1,1]
        red = [.9,.5,.5]
        blue = [.5,.75,.9]
        green = [.4, .75, .4]
        yellow = [.9,.85,.45]
        orange = [.8,.3,.4]
        purple = [.6,.5,.8]

        cmds.rowLayout(numberOfColumns=3, columnAlign1="center", p=columnMain)
        cmds.button(label="Rot. L", width=widtha, bgc=white, command=self.rotateLeft)
        cmds.button(label="Orient", width=widtha, command=self.orientShells)
        cmds.button(label="Rot. R", width=widtha, bgc=white, command=self.rotateRight)
        cmds.rowLayout(numberOfColumns=2, columnAlign1="center", p=columnMain)
        cmds.button(label="Flip U", width=widthb, command=self.udimFlipU)
        cmds.button(label="Flip V", width=widthb, command=self.udimFlipV)

        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=5)

        cmds.rowLayout(numberOfColumns=3, columnAlign1="center", p=columnMain)
        cmds.text(label="", width=widtha)
        cmds.button(label="/\\", width=widtha, bgc=white, command=self.translateUp)
        cmds.text(label="", width=widtha)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="<", width=40, bgc=white, command=self.translateLeft)
        self.transDistance = cmds.floatField(ed=True,v=1.0, precision = 2,s=.25,w=40)
        cmds.button(label=">", width=40, bgc=white, command=self.translateRight)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.text(label="", width=40)
        cmds.button(label="V", width=40, bgc=white, command=self.translateDown)
        cmds.text(label="", width=40)
        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=5)

        ### arrows button ends, Layout buttons begin
        ###################################################################################################
        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Center", width=widthb, command=self.udimCenter)
        cmds.button(label="Maximize", width=widthb, command=self.udimMax)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Get TD", width=widthb, command=self.getTD)
        cmds.button(label="Set TD", width=widthb, command=self.setTD)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="Stack", width=widthb, command=self.stackShells)
        cmds.button(label="U", width=widthc, command=self.distributeU)
        cmds.button(label="V", width=widthc, command=self.distributeV)

        cmds.rowLayout(numberOfColumns=1, p=columnMain)
        cmds.button(label="Layout", width=widthe, bgc=white, command=self.layoutUnfold3d)
        cmds.rowColumnLayout(numberOfColumns=2, p=columnMain)
        self.layoutScaleBox=cmds.checkBox(label="Scale", value=True)
        self.layoutRotateBox=cmds.checkBox(label="Rotate")

        ### Layout button ends, UV edit buttons begin
        ###################################################################################################
        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=6)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="Unfold", width=widthb, command=self.unfoldUV)
        cmds.button(label="U", width=widthc, command=self.unfoldU)
        cmds.button(label="V", width=widthc, command=self.unfoldV)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="Straighten", width=widthb, command=self.straighten)
        cmds.button(label="U", width=widthc, command=self.straightenU)
        cmds.button(label="V", width=widthc, command=self.straightenV)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Symmetry", width=widthb, command=self.symmetrize)
        cmds.button(label="Mirror", width=widthb, command=self.distributeU)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="3D Cut", width=widthb, command=self.cutsew3d)
        cmds.button(label="To Obj", width=widthb, command=self.uvToObj)

        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=4)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.text(label="Transfer UVs", width=90, align="left")
        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Topo", width=widthb, command=self.transUVTopoMulti,
                    ann="Transfers UVs from the last selected object to the rest of your selected objects")
        cmds.button(label="World", width=widthb, command=self.transUVWorld)
        ### End
        ###################################################################################################


        # builds layout and buttons, hooks up to commands
    def buildUI(self):
        columnMain = cmds.columnLayout(columnWidth=200)
        widthb = 61
        widtha = 40
        widthc = 29
        widthe = 124

        white = [1,1,1]
        red = [.9,.5,.5]
        blue = [.5,.75,.9]
        green = [.4, .75, .4]
        yellow = [.9,.85,.45]
        orange = [.8,.3,.4]
        purple = [.65,.5,.85]

        cmds.rowLayout(numberOfColumns=3, columnAlign1="center", p=columnMain)
        cmds.button(label="Rot. L", width=widtha, bgc=white, command=self.rotateLeft)
        cmds.button(label="Orient", width=widtha, bgc=blue, command=self.orientShells)
        cmds.button(label="Rot. R", width=widtha, bgc=white, command=self.rotateRight)
        cmds.rowLayout(numberOfColumns=2, columnAlign1="center", p=columnMain)
        cmds.button(label="Flip U", width=widthb, bgc=red, command=self.udimFlipU)
        cmds.button(label="Flip V", width=widthb, bgc=red, command=self.udimFlipV)

        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=5)

        cmds.rowLayout(numberOfColumns=3, columnAlign1="center", p=columnMain)
        cmds.text(label="", width=widtha)
        cmds.button(label="/\\", width=widtha, bgc=white, command=self.translateUp)
        cmds.text(label="", width=widtha)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="<", width=40, bgc=white, command=self.translateLeft)
        self.transDistance = cmds.floatField(ed=True,v=1.0, precision = 2,s=.25,w=40)
        cmds.button(label=">", width=40, bgc=white, command=self.translateRight)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.text(label="", width=40)
        cmds.button(label="V", width=40, bgc=white, command=self.translateDown)
        cmds.text(label="", width=40)
        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=5)

        ### arrows button ends, Layout buttons begin
        ###################################################################################################
        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Center", width=widthb, bgc=green, command=self.udimCenter)
        cmds.button(label="Maximize", width=widthb, bgc=green, command=self.udimMax)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Get TD", width=widthb, bgc=yellow, command=self.getTD)
        cmds.button(label="Set TD", width=widthb, bgc=yellow, command=self.setTD)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="Stack", width=widthb, bgc=purple, command=self.stackShells)
        cmds.button(label="U", width=widthc, bgc=purple, command=self.distributeU)
        cmds.button(label="V", width=widthc, bgc=purple, command=self.distributeV)

        cmds.rowLayout(numberOfColumns=1, p=columnMain)
        cmds.button(label="Layout", width=widthe, bgc=white, command=self.layoutUnfold3d)
        cmds.rowColumnLayout(numberOfColumns=2, p=columnMain)
        self.layoutScaleBox=cmds.checkBox(label="Scale", value=True)
        self.layoutRotateBox=cmds.checkBox(label="Rotate")

        ### Layout button ends, UV edit buttons begin
        ###################################################################################################
        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=6)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="Unfold", width=widthb, bgc=blue, command=self.unfoldUV)
        cmds.button(label="U", width=widthc, bgc=blue, command=self.unfoldU)
        cmds.button(label="V", width=widthc, bgc=blue, command=self.unfoldV)

        cmds.rowLayout(numberOfColumns=3, p=columnMain)
        cmds.button(label="Straighten", width=widthb, bgc=red, command=self.straighten)
        cmds.button(label="U", width=widthc, bgc=red, command=self.straightenU)
        cmds.button(label="V", width=widthc, bgc=red,  command=self.straightenV)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Symmetry", width=widthb, bgc=yellow, command=self.symmetrize)
        cmds.button(label="Mirror", width=widthb, bgc=yellow, command=self.distributeU)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="3DCutSew", width=widthb, bgc=green, command=self.cutsew3d)
        cmds.button(label="AutoSeam", width=widthb, bgc=purple, command=self.autoSeams)

        cmds.rowLayout(numberOfColumns=1, p=columnMain, height=4)

        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.text(label="Transfer UVs", width=90, align="left")
        cmds.rowLayout(numberOfColumns=2, p=columnMain)
        cmds.button(label="Topo", width=widthb, bgc=white, command=self.transUVTopoMulti,
                    ann="Transfers UVs from the last selected object to the rest of your selected objects")
        cmds.button(label="World", width=widthb, bgc=white, command=self.transUVWorld)
        ### End
        ###################################################################################################


    def rotateLeft(self, *args):
        mel.eval('polyRotateUVs 45 1;')

    def rotateRight(self, *args):
        mel.eval('polyRotateUVs -45 1;')

    def translateUp(self, *args):
        distance = cmds.floatField(self.transDistance,q=True,v=True)
        cmds.polyEditUV(u=0, v=distance)
        mel.eval('texPivotCycle selection middle;')

    def translateRight(self, *args):
        distance = cmds.floatField(self.transDistance,q=True,v=True)
        cmds.polyEditUV(u=distance, v=0)
        mel.eval('texPivotCycle selection middle;')

    def translateLeft(self, *args):
        distance = cmds.floatField(self.transDistance,q=True,v=True)
        cmds.polyEditUV(u=-(distance), v=0)
        mel.eval('texPivotCycle selection middle;')

    def translateDown(self, *args):
        distance = cmds.floatField(self.transDistance,q=True,v=True)
        cmds.polyEditUV(u=0, v=-(distance))
        mel.eval('texPivotCycle selection middle;')

    def stackShells(self, *args):
        mel.eval('texStackShells {};')

    def orientShells(self, *args):
        mel.eval('texOrientShells;')

    def getTD(self, *args):
        mel.eval('uvTkDoGetTexelDensity;')

    def setTD(self, *args):
        mel.eval('uvTkDoSetTexelDensity;')

    def udimFlipU(self, *args):
        boundingBoxInfo = cmds.polyEvaluate(bc2=True)
        uminmax = boundingBoxInfo[0]
        ucenter = (uminmax[0] + uminmax[1])/2 # must add and divide by two to find center pivot
        tilecenter = (math.floor(ucenter))+.5
        cmds.polyEditUV(pivotU=tilecenter, scaleU=-1)
        mel.eval('texPivotCycle selection middle;')

    def udimFlipV(self, *args):
        boundingBoxInfo = cmds.polyEvaluate(bc2=True)
        vminmax = boundingBoxInfo[1]
        vcenter = (vminmax[0] + vminmax[1])/2 # must add and divide by two to find center pivot
        tilecenter = (math.floor(vcenter))+.5
        cmds.polyEditUV(pivotV=tilecenter, scaleV=-1)
        mel.eval('texPivotCycle selection middle;')

    def udimCenter(self, *args):
        boundingBoxInfo = cmds.polyEvaluate(bc2=True) #return tuple of UV boundinbox max and min for U and V
        uminmax = boundingBoxInfo[0] #separate u and v (max,min)
        vminmax = boundingBoxInfo[1]
        ucenter = (uminmax[0] + uminmax[1])/2 # must add and divide by two to find center pivot
        vcenter = (vminmax[0] + vminmax[1])/2
        utarget = (math.floor(ucenter))+.5 # find center of udim
        vtarget = (math.floor(vcenter))+.5
        cmds.polyEditUV(u=(utarget-ucenter), v=(vtarget-vcenter))
        mel.eval('texPivotCycle selection middle;')

    def udimMax(self, *args):
        boundingBoxInfo = cmds.polyEvaluate(bc2=True)
        uminmax = boundingBoxInfo[0]
        vminmax = boundingBoxInfo[1]
        ucenter = (uminmax[0] + uminmax[1])/2 # must add and divide by two to find center pivot
        vcenter = (vminmax[0] + vminmax[1])/2
        width = math.fabs(uminmax[0] - uminmax[1])
        height = math.fabs(vminmax[0] - vminmax[1])
        if (width > height):
            factor = .985/width
        else:
            factor = .985/height
        cmds.polyEditUV(pivotU=ucenter, pivotV=vcenter, scaleV=factor, scaleU=factor)
        mel.eval('texPivotCycle selection middle;')

    def symmetrize(self, *args):
        mel.eval('SymmetrizeUV;')

    def layoutUnfold3d(self, *args):
        cmds.u3dLayout(res=256, spc=0.015, mar=0.01)

    def layoutLegacy(self, *args):
        cmds.polyMultiLayoutUV(prescale=2, layoutMethod=1, rotateForBestFit=0,
                               flipReversed=True, percentageSpace=.5, layout=2,
                               gridU=2, gridV=2, scale=1, sizeU=1,
                               sizeV=1, offsetU=0, offsetV=0)

    def unfoldUV(self, *args):
        cmds.u3dUnfold(ite=1, p=0, bi=1, tf=1, ms=128, rs=0)

    def unfoldU(self, *args):
        cmds.unfold(i=5000, ss=0.001, gb=0, gmb=0.5, pub=0, ps=0, oa=2, us=False)

    def unfoldV(self, *args):
        cmds.unfold(i=5000, ss=0.001, gb=0, gmb=0.5, pub=0, ps=0, oa=1, us=False)

    def straighten(self, *args):
        mel.eval('texStraightenUVs "UV" 30;')

    def straightenU(self, *args):
        mel.eval('texStraightenUVs "U" 30;')

    def straightenV(self, *args):
        mel.eval('texStraightenUVs "V" 30;')

    def cutsew3d(self, *args):
        mel.eval('SetCutSewUVTool;')

    def transUVTopo(self, *args):
        cmds.transferAttributes(transferNormals=0, transferUVs=2,
                                sampleSpace=5, searchMethod=0)

    def transUVTopoMulti(self, *args):
        sel = cmds.list(sl=True)
        if len(sel) != 2:
            raise NameError('Must Select 2 groups!')

        source = sel[0]
        reference = sel[1]
        print source
        print reference
       # for obj in sel:
       #      cmds.transferAttributes(ref, obj, transferNormals=0,
       #                          transferUVs=2, sampleSpace=5)

    def transUVWorld(self, *args):
        cmds.transferAttributes(transferPositions=0, transferNormals=0,
                                transferUVs=2, sourceUvSpace="map1",
                                targetUvSpace="map1", sampleSpace=0, searchMethod=0)

    def uvToObj(self, *args):
        cmds.select(cmds.ls(sl=True, o=True))

    def distributeV(self, *args):
        mel.eval('texDistributeShells(0, 0.01, "up", {});')

    def distributeU(self, *args):
        mel.eval('texDistributeShells(0, 0.01, "right", {});')

    def autoSeams(self, *args):
        mel.eval('performPolyAutoSeamUV 0;')
