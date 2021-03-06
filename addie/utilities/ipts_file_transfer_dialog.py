from PyQt4 import QtGui, QtCore
from addie.ui_iptsFileTransfer import Ui_Dialog as UiDialog
from addie.utilities.job_status_handler import JobStatusHandler
import os


class IptsFileTransferDialog(QtGui.QDialog):
    
    ipts_folder = '/SNS/NOM'
    script = '/SNS/NOM/shared/autoNOM/stable/copystuff.py'
    
    def __init__(self, parent=None):
        self.parent = parent
        
        QtGui.QDialog.__init__(self, parent=parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)
        
    def transfer_clicked(self):
        _input_ipts = str(self.ui.source_ipts_value.text())
        _input_autonom = str(self.ui.source_autonom_value.text())
        _target_autonom = str(self.ui.target_autonom_value.text())
    
        _full_script = self.script + " -i " + _input_ipts
        _full_script += " -f " + _input_autonom
        _full_script += " -t " + _target_autonom

        print(_full_script)

        job_handler = JobStatusHandler(parent = self.parent,
                                       script_to_run=_full_script,
                                       job_name='IPTS File Transfer')
    
        self.close()

    def cancel_clicked(self):
        self.close()
        
    def source_ipts_clicked(self):
        _ipts_folder = QtGui.QFileDialog.getExistingDirectory(caption="Select Input IPTS Folder ...", 
                                                      directory=self.ipts_folder, 
                                                      options=QtGui.QFileDialog.ShowDirsOnly)
        if _ipts_folder:
            self.ipts_folder = _ipts_folder
            _ipts_folder = os.path.basename(_ipts_folder)
            _ipts_number = _ipts_folder.split('-')[1]
            self.ui.source_ipts_value.setText(str(_ipts_number))
            self.check_status_transfer_button()
    
    def source_autonom_clicked(self):
        _autonom_folder = QtGui.QFileDialog.getExistingDirectory(caption="Select Input autoNOM Folder ...", 
                                                      directory=self.ipts_folder,
                                                      options=QtGui.QFileDialog.ShowDirsOnly)
        if _autonom_folder:
            _autonom_folder = os.path.basename(_autonom_folder)
            self.ui.source_autonom_value.setText(str(_autonom_folder))
            self.check_status_transfer_button()
    
    def target_autonom_clicked(self):
        _autonom_folder = QtGui.QFileDialog.getExistingDirectory(caption="Select Output autoNOM Folder ...", 
                                                      directory=self.parent.current_folder,
                                                      options=QtGui.QFileDialog.ShowDirsOnly)
        if _autonom_folder:
            _autonom_folder = os.path.basename(_autonom_folder)
            self.ui.target_autonom_value.setText(str(_autonom_folder))
            self.check_status_transfer_button()
    
    def check_status_transfer_button(self):
        _source_ipts = str(self.ui.source_ipts_value.text())
        if _source_ipts == 'N/A':
            self.set_transfer_button_status(status='disable')
            return
        
        _source_autonom = str(self.ui.source_autonom_value.text())
        if _source_autonom == 'N/A':
            self.set_transfer_button_status(status='disable')
            return
        
        _target_autonom = str(self.ui.target_autonom_value.text())
        if _target_autonom == 'N/A':
            self.set_transfer_button_status(status='disable')
            return
        
        self.set_transfer_button_status(status='enable')
        
    def set_transfer_button_status(self, status='enable'):
        if status == 'enable':
            self.ui.transfer_button.setEnabled(True)
        else:
            self.ui.transfer_button.setEnabled(False)
            
        
