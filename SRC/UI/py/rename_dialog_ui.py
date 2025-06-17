# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RenameDialog.ui'
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
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_RenameDialog(object):
    def setupUi(self, RenameDialog):
        if not RenameDialog.objectName():
            RenameDialog.setObjectName(u"RenameDialog")
        RenameDialog.resize(300, 120)
        RenameDialog.setMinimumSize(QSize(300, 120))
        RenameDialog.setMaximumSize(QSize(300, 120))
        self.verticalLayout = QVBoxLayout(RenameDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.New_Name = QLabel(RenameDialog)
        self.New_Name.setObjectName(u"New_Name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.New_Name)

        self.nameInput = QLineEdit(RenameDialog)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(RenameDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(RenameDialog)

        QMetaObject.connectSlotsByName(RenameDialog)
    # setupUi

    def retranslateUi(self, RenameDialog):
        RenameDialog.setWindowTitle(QCoreApplication.translate("RenameDialog", u"Rename Item", None))
        self.New_Name.setText(QCoreApplication.translate("RenameDialog", u"New name:", None))
    # retranslateUi

