from PyQt4 import QtGui, QtCore

from addie.ui_loadTableIntermediateStep import Ui_Dialog as UiDialog
from addie.utilities.gui_handler import GuiHandler


class loadTableIntermediateStepInterface(QtGui.QDialog):
    
    def __init__(self, parent=None):
        self.parent = parent
        
        QtGui.QDialog.__init__(self, parent=parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)
        self.parent.load_intermediate_step_ok = False
        
    def closeEvent(self, event=None):
        pass
    
    def ok_clicked(self):
        o_gui = GuiHandler(parent = self)
        _state_button = o_gui.radiobutton_get_state(widget_id=self.ui.remove_temperature_checkbox)
        self.parent.remove_dynamic_temperature_flag = _state_button
        self.parent.load_intermediate_step_ok = True
        self.close()
        self.parent.move_to_folder_step2()
    
    def cancel_clicked(self):
        self.close()
  
        
        
        
        
