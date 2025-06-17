# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recycle_bin_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_RecycleBinDialog(object):
    def setupUi(self, RecycleBinDialog):
        if not RecycleBinDialog.objectName():
            RecycleBinDialog.setObjectName(u"RecycleBinDialog")
        RecycleBinDialog.resize(800, 500)
        RecycleBinDialog.setMinimumSize(QSize(800, 500))
        self.verticalLayout = QVBoxLayout(RecycleBinDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(RecycleBinDialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refreshButton = QPushButton(RecycleBinDialog)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout.addWidget(self.refreshButton)

        self.restoreButton = QPushButton(RecycleBinDialog)
        self.restoreButton.setObjectName(u"restoreButton")

        self.horizontalLayout.addWidget(self.restoreButton)

        self.deleteButton = QPushButton(RecycleBinDialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.emptyButton = QPushButton(RecycleBinDialog)
        self.emptyButton.setObjectName(u"emptyButton")

        self.horizontalLayout.addWidget(self.emptyButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(RecycleBinDialog)

        QMetaObject.connectSlotsByName(RecycleBinDialog)
    # setupUi

    def retranslateUi(self, RecycleBinDialog):
        RecycleBinDialog.setWindowTitle(QCoreApplication.translate("RecycleBinDialog", u"Recycle Bin", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RecycleBinDialog", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RecycleBinDialog", u"Original Path", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("RecycleBinDialog", u"Deleted At", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("RecycleBinDialog", u"Type", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("RecycleBinDialog", u"Size", None));
        self.refreshButton.setText(QCoreApplication.translate("RecycleBinDialog", u"Refresh", None))
        self.restoreButton.setText(QCoreApplication.translate("RecycleBinDialog", u"Restore Selected", None))
        self.deleteButton.setText(QCoreApplication.translate("RecycleBinDialog", u"Delete Permanently", None))
        self.emptyButton.setText(QCoreApplication.translate("RecycleBinDialog", u"Empty Recycle Bin", None))
    # retranslateUi

