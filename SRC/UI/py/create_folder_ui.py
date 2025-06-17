# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateFolder.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget,QVBoxLayout,QFormLayout)

class Ui_CreateFolderDialog(object):
    def setupUi(self, CreateFolderDialog):
        if not CreateFolderDialog.objectName():
            CreateFolderDialog.setObjectName(u"CreateFolderDialog")
        CreateFolderDialog.resize(300, 120)
        CreateFolderDialog.setModal(True)
        
        self.verticalLayout = QVBoxLayout(CreateFolderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        
        self.label = QLabel(CreateFolderDialog)
        self.label.setObjectName(u"label")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)
        
        self.folder_name_input = QLineEdit(CreateFolderDialog)
        self.folder_name_input.setObjectName(u"folder_name_input")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.folder_name_input)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        self.button_box = QDialogButtonBox(CreateFolderDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(CreateFolderDialog)
        QMetaObject.connectSlotsByName(CreateFolderDialog)

    def retranslateUi(self, CreateFolderDialog):
        CreateFolderDialog.setWindowTitle(QCoreApplication.translate("CreateFolderDialog", u"Create New Folder", None))
        self.label.setText(QCoreApplication.translate("CreateFolderDialog", u"Folder name:", None))
        self.folder_name_input.setPlaceholderText(QCoreApplication.translate("CreateFolderDialog", u"New folder name...", None))
    # retranslateUi

