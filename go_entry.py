# -----------------------------------------------------------------------
# This is an example illustrating how to use the Form class
# (c) Hex-Rays
#
import GO_Utils
idaapi.require("GO_Utils")
idaapi.require("GO_Utils.Gopclntab")
idaapi.require("GO_Utils.Utils")
idaapi.require("GO_Utils.Firstmoduledata")
idaapi.require("GO_Utils.Types")
idaapi.require("GO_Utils.GoStrings")

from idaapi import PluginForm
from PyQt5 import QtCore, QtGui, QtWidgets

GO_SETTINGS = GO_Utils.GoSettings()


class MyForm(PluginForm):
    def OnCreate(self, form):
        self.parent = self.FormToPyQtWidget(form)
        self.PopulateForm()


    def PopulateForm(self):
        self.cGoVers = 0
        layout = QtWidgets.QVBoxLayout()
        self.addbtnmoduledata = QtWidgets.QPushButton("Try to detemine go version based on moduledata") 
        self.addbtnmoduledata.clicked.connect(self.OnButton1)
        layout.addWidget(self.addbtnmoduledata, QtCore.Qt.AlignTop)
        self.addbtnversionstr = QtWidgets.QPushButton("Try to detemine go version based on version string") 
        self.addbtnversionstr.clicked.connect(self.OnButton2)
        layout.addWidget(self.addbtnversionstr)
        self.addbtnrename = QtWidgets.QPushButton("Rename functions") 
        self.addbtnrename.clicked.connect(self.OnButton3)
        layout.addWidget(self.addbtnrename)

        groupbox = QtWidgets.QGroupBox("Go  Versions")
        vbox = QtWidgets.QVBoxLayout()
        self.go_ver = ["Go1.2","Go1.4","Go1.5","Go1.6", "Go1.7", "Go1.8", "Go1.9", "Go1.10"]
        self.buttongroup = QtWidgets.QButtonGroup()
        for cc, gv in enumerate(self.go_ver):
            item_widget = QtWidgets.QRadioButton(gv)
            item_widget.toggled.connect(self.OnFormChange)
            if cc == 0:
                item_widget.setChecked(True)
            self.buttongroup.addButton(item_widget, cc)
            vbox.addWidget(item_widget, QtCore.Qt.AlignTop)
        groupbox.setLayout(vbox)
        layout.addWidget(groupbox)

        self.addbtnstdtype = QtWidgets.QPushButton("Add standard go types") 
        self.addbtnstdtype.clicked.connect(self.OnButton4)
        layout.addWidget(self.addbtnstdtype)
        self.addbttypemod = QtWidgets.QPushButton("Parse types by moduledata") 
        self.addbttypemod.clicked.connect(self.OnButton5)
        layout.addWidget(self.addbttypemod)
        self.parent.setLayout(layout)


    def OnButton1(self, code=0):
        global GO_SETTINGS
        GO_SETTINGS.findModuleData()
        print(GO_SETTINGS.tryFindGoVersion())


    def OnButton3(self, code=0):
        global GO_SETTINGS
        GO_SETTINGS.renameFunctions()

    def OnButton2(self, code=0):
        print(GO_SETTINGS.getVersionByString())

    def OnButton4(self, code=0):
        global GO_SETTINGS
        typ = self.cGoVers
        GO_SETTINGS.createTyper(typ)

    def OnButton5(self, code=0):
        global GO_SETTINGS
        typ = self.cGoVers
        GO_SETTINGS.typesModuleData(typ)


    def OnFormChange(self, fid):
        tt = self.buttongroup.checkedId()
        if tt == -1:
            tt = 0 
        self.cGoVers = tt

        
plg = MyForm()
plg.Show("GoLoader")