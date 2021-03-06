# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2017 OpenLP Developers                                   #
# Copyright (c) 2018 John Kirkland                                            #
# --------------------------------------------------------------------------- #
# This program is free software; you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation; version 2 of the License.                              #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program; if not, write to the Free Software Foundation, Inc., 59  #
# Temple Place, Suite 330, Boston, MA 02111-1307 USA                          #
###############################################################################
"""
The :mod:`~openlp.plugins.planningcenter.forms.editauthdialog` module contains the user interface code for the EditAuthDialog
"""

from PyQt5 import QtWidgets
from openlp.core.lib import translate

class Ui_EditAuthDialog(object):
    """
    This is the dialog that collect the Planning Center application ID and secret codes
    """
    def setup_ui(self, planningcenter_dialog_auth):
        planningcenter_dialog_auth.setObjectName('planningcenter_dialog_auth')
        planningcenter_dialog_auth.resize(700, 350)

        self.auth_layout = QtWidgets.QFormLayout(planningcenter_dialog_auth)
        self.auth_layout.setContentsMargins(20, 40, 20, 40)
        self.auth_layout.setSpacing(8)
        self.auth_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        
        self.notice_label = QtWidgets.QLabel(planningcenter_dialog_auth)
        self.notice_label.setWordWrap(True)
        self.auth_layout.addRow(self.notice_label)
        
        self.instructions_label = QtWidgets.QLabel(planningcenter_dialog_auth)
        self.instructions_label.setWordWrap(True)
        self.auth_layout.addRow(self.instructions_label)
        
        # Application ID GUI Elements
        self.application_id_label = QtWidgets.QLabel(planningcenter_dialog_auth)
        self.application_id_line_edit = QtWidgets.QLineEdit(planningcenter_dialog_auth)
        self.application_id_line_edit.setMaxLength(64)
        self.auth_layout.addRow(self.application_id_label, self.application_id_line_edit)
        self.application_id_line_edit.setFocus()
        
        # Secret GUI Elements (shhhh... it's a secret...)
        self.secret_label = QtWidgets.QLabel(planningcenter_dialog_auth)
        self.secret_line_edit = QtWidgets.QLineEdit(planningcenter_dialog_auth)
        self.secret_line_edit.setMaxLength(64)
        self.auth_layout.addRow(self.secret_label, self.secret_line_edit)
        
        # Buttons
        self.button_layout = QtWidgets.QDialogButtonBox(planningcenter_dialog_auth)
        self.save_credentials_button = QtWidgets.QPushButton(planningcenter_dialog_auth)
        self.button_layout.addButton(self.save_credentials_button, QtWidgets.QDialogButtonBox.AcceptRole)
        self.test_credentials_button = QtWidgets.QPushButton(planningcenter_dialog_auth)
        self.button_layout.addButton(self.test_credentials_button, QtWidgets.QDialogButtonBox.AcceptRole)
        self.delete_credentials_button = QtWidgets.QPushButton(planningcenter_dialog_auth)
        self.button_layout.addButton(self.delete_credentials_button, QtWidgets.QDialogButtonBox.ActionRole)
        self.auth_layout.addRow(self.button_layout)
        
        
        self.retranslate_ui(planningcenter_dialog_auth)
        
    def retranslate_ui(self, planningcenter_dialog_auth):
        """
        Translate the GUI.
        """
        planningcenter_dialog_auth.setWindowTitle(translate('PlanningCenterPlugin.PlanningCenterAuthForm', 'Planning Center Online Authentication'))
        self.notice_label.setText(
            translate('PlanningCenterPlugin.PlanningCenterForm', '<strong>Note:</strong> '
                      'An Internet connection and a Planning Center Online Account are required in order to import plans from Planning Center Online.')    
        )
        self.instructions_label.setText(
            translate('PlanningCenterPlugin.PlanningCenterAuthForm',\
"""Enter your <b>Planning Center Online</b> <i>Personal Access Token</i> details in the text boxes \
below.  Personal Access Tokens are created by doing the following:
<ol>
  <li>Login to your Planning Center Online account at<br>
      <a href=https://api.planningcenteronline.com/oauth/applications>
      https://api.planningcenteronline.com/oauth/applications</a></li>
  <li>Click the "New Personal Access Token" button at the bottom of the screen.</li>
  <li>Enter a description of your use case (eg. "OpenLP Integration")</li>
  <li>Copy and paste the provided Application ID and Secret values below.</li>
</ol>"""))
        self.application_id_label.setText(translate('PlanningCenterPlugin.PlanningCenterAuthForm', "Application ID"))
        self.secret_label.setText(translate('PlanningCenterPlugin.PlanningCenterAuthForm', "Secret"))
        self.test_credentials_button.setText(translate('PlanningCenterPlugin.PlanningCenterAuthForm','Test Credentials'))
        self.save_credentials_button.setText(translate('PlanningCenterPlugin.PlanningCenterAuthForm','Save Credentials'))
        self.delete_credentials_button.setText(translate('PlanningCenterPlugin.PlanningCenterAuthForm','Delete Credentials'))
        
