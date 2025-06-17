# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeleteDialog.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        if not DeleteDialog.objectName():
            DeleteDialog.setObjectName(u"DeleteDialog")
        DeleteDialog.resize(420, 180)
        DeleteDialog.setMinimumSize(QSize(420, 180))
        self.buttonBox = QDialogButtonBox(DeleteDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(240, 120, 159, 44))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)
        self.iconlabel = QLabel(DeleteDialog)
        self.iconlabel.setObjectName(u"iconlabel")
        self.iconlabel.setGeometry(QRect(20, 35, 71, 101))
        self.messageLabel = QLabel(DeleteDialog)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setGeometry(QRect(110, 30, 291, 81))
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.iconLabel = QLabel(DeleteDialog)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setGeometry(QRect(10, 10, 16, 16))
        self.iconLabel.setPixmap(QPixmap(u":/qt-project.org/styles/commonstyle/images/standardbutton-question-32.png"))
        self.iconLabel.setAlignment(Qt.AlignTop)

        self.retranslateUi(DeleteDialog)

        QMetaObject.connectSlotsByName(DeleteDialog)
    # setupUi

    def retranslateUi(self, DeleteDialog):
        DeleteDialog.setWindowTitle(QCoreApplication.translate("DeleteDialog", u"Confirm Delete", None))
        self.iconlabel.setText("")
        self.messageLabel.setText(QCoreApplication.translate("DeleteDialog", u"Are you sure you want to delete \"filename.txt\"?\n"
"\n"
"This action cannot be undone.", None))
    # retranslateUi

