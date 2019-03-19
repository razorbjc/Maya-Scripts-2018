# given a a complete edge loop or enclosure of edges, 
# will select all faces within the edge perimeter

import maya.cmds as cmds
import maya.mel as mel

def jc_faceCut():
    # collect selected edges and obj name
    edgeSel = cmds.ls(sl=True)
    objs = cmds.ls(sl=True, o=True)
	
	#creates extra uv set to work in
    cmds.polyUVSet(create=True, uvSet="facecut")
    cmds.polyUVSet(currentLastUVSet=True)
	
	# runs planar projection for basic UVs, then cuts the selected edges, 
    projection= cmds.polyProjection(objs[0], type='Planar', md='p')
    cut=cmds.polyMapCut(edgeSel)
	
	#selects a face and converts to shell selection
    firstFace = (objs[0] + ".map[0]")
    cmds.select(firstFace, r=True)
    cmds.ConvertSelectionToUVShell()
    cmds.ConvertSelectionToFaces()
	cmds.polyUVSet(delete=True)
    cmds.delete(cut)
    cmds.delete(projection)
    # mel.eval('InvertSelection;')