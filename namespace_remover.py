#!/usr/bin/env python2.7

"""
Removes all namespaces. may need to be run multiple times for stacked namespaces

__author__: James Chan
"""

import maya.cmds as cmds


def namespace_remover():
    cmds.namespace(setNamespace=':')
    namespaces = cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True)
    if namespaces:
        namespaces.remove("UI")
        namespaces.remove("shared")
    for i in namespacesAll:
        cmds.namespace(removeNamespace=i, mergeNamespaceWithRoot=True)


jc_namespaceRemover()
