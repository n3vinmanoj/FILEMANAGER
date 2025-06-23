# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PropertiesDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGroupBox, QLabel,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget,QHBoxLayout,QFormLayout,QSpacerItem)
from Utils.icons import get_icon

class Ui_PropertiesDialog(object):
    def setupUi(self, PropertiesDialog):
        if not PropertiesDialog.objectName():
            PropertiesDialog.setObjectName(u"PropertiesDialog")
        PropertiesDialog.resize(465, 400)  # Increased height
        PropertiesDialog.setModal(True)
        
        self.verticalLayout = QVBoxLayout(PropertiesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(10)
        
        self.tab_widget = QTabWidget(PropertiesDialog)
        self.tab_widget.setObjectName(u"tab_widget")
        
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        self.general_layout = QVBoxLayout(self.general_tab)
        self.general_layout.setContentsMargins(10, 10, 10, 10)
        self.general_layout.setSpacing(10)
        
        # Name and icon section
        self.name_icon_layout = QHBoxLayout()
        self.name_icon_layout.setSpacing(15)
        
        self.icon_label = QLabel(self.general_tab)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setFixedSize(48, 48)  # Larger icon
        self.name_icon_layout.addWidget(self.icon_label)
        
        self.name_label = QLabel(self.general_tab)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)
        self.name_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.name_icon_layout.addWidget(self.name_label, 1)  # Stretch factor
        
        self.general_layout.addLayout(self.name_icon_layout)
        
        # Separator
        self.line = QFrame(self.general_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet("color: #555;")
        self.general_layout.addWidget(self.line)
        
        # Properties form
        self.form_layout = QFormLayout()
        self.form_layout.setVerticalSpacing(8)
        self.form_layout.setHorizontalSpacing(15)
        
        # Type
        self.type_label = QLabel(self.general_tab)
        self.type_label.setObjectName(u"type_label")
        self.type_value = QLabel(self.general_tab)
        self.type_value.setObjectName(u"type_value")
        self.type_value.setWordWrap(True)
        self.form_layout.addRow(self.type_label, self.type_value)
        
        # Location
        self.location_label = QLabel(self.general_tab)
        self.location_label.setObjectName(u"location_label")
        self.location_value = QLabel(self.general_tab)
        self.location_value.setObjectName(u"location_value")
        self.location_value.setWordWrap(True)
        self.location_value.setStyleSheet("color: #aaa;")
        self.form_layout.addRow(self.location_label, self.location_value)
        
        # Size
        self.size_label = QLabel(self.general_tab)
        self.size_label.setObjectName(u"size_label")
        self.size_value = QLabel(self.general_tab)
        self.size_value.setObjectName(u"size_value")
        self.form_layout.addRow(self.size_label, self.size_value)
        
        # Modified
        self.modified_label = QLabel(self.general_tab)
        self.modified_label.setObjectName(u"modified_label")
        self.modified_value = QLabel(self.general_tab)
        self.modified_value.setObjectName(u"modified_value")
        self.form_layout.addRow(self.modified_label, self.modified_value)
        
        # Created
        self.created_label = QLabel(self.general_tab)
        self.created_label.setObjectName(u"created_label")
        self.created_value = QLabel(self.general_tab)
        self.created_value.setObjectName(u"created_value")
        self.form_layout.addRow(self.created_label, self.created_value)
        
        # Accessed
        self.accessed_label = QLabel(self.general_tab)
        self.accessed_label.setObjectName(u"accessed_label")
        self.accessed_value = QLabel(self.general_tab)
        self.accessed_value.setObjectName(u"accessed_value")
        self.form_layout.addRow(self.accessed_label, self.accessed_value)
        
        self.general_layout.addLayout(self.form_layout)
        
        # Spacer to push content up
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.general_layout.addItem(spacer)
        
        # Attributes group (hidden)
        self.attributes_group = QGroupBox(self.general_tab)
        self.attributes_group.setObjectName(u"attributes_group")
        self.attributes_layout = QVBoxLayout(self.attributes_group)
        self.readonly_cb = QCheckBox(self.attributes_group)
        self.hidden_cb = QCheckBox(self.attributes_group)
        self.attributes_layout.addWidget(self.readonly_cb)
        self.attributes_layout.addWidget(self.hidden_cb)
        self.attributes_group.hide()
        
        self.tab_widget.addTab(self.general_tab, "")
        self.verticalLayout.addWidget(self.tab_widget)
        
        # Button box
        self.button_box = QDialogButtonBox(PropertiesDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStandardButtons(QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.button_box)
        self.button_box.accepted.connect(PropertiesDialog.accept)

        self.retranslateUi(PropertiesDialog)
        self.tab_widget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(PropertiesDialog)

    def retranslateUi(self, PropertiesDialog):
        PropertiesDialog.setWindowTitle(QCoreApplication.translate("PropertiesDialog", u"Properties", None))
        self.type_label.setText(QCoreApplication.translate("PropertiesDialog", u"Type:", None))
        self.location_label.setText(QCoreApplication.translate("PropertiesDialog", u"Location:", None))
        self.size_label.setText(QCoreApplication.translate("PropertiesDialog", u"Size:", None))
        self.modified_label.setText(QCoreApplication.translate("PropertiesDialog", u"Modified:", None))
        self.created_label.setText(QCoreApplication.translate("PropertiesDialog", u"Created:", None))
        self.accessed_label.setText(QCoreApplication.translate("PropertiesDialog", u"Accessed:", None))
        self.readonly_cb.setText(QCoreApplication.translate("PropertiesDialog", u"Read-only", None))
        self.hidden_cb.setText(QCoreApplication.translate("PropertiesDialog", u"Hidden", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.general_tab), QCoreApplication.translate("PropertiesDialog", u"General", None))