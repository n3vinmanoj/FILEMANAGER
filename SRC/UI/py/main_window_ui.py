# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        
        # Make main window resizable and set minimum size
        MainWindow.setMinimumSize(QSize(800, 600))
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Main layout with proper margins and spacing
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(8)
        
        # Toolbar layout
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.toolbarLayout.setSpacing(5)
        
        self.new_folder_button = QPushButton(self.centralwidget)
        self.new_folder_button.setObjectName(u"new_folder_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_folder_button.sizePolicy().hasHeightForWidth())
        self.new_folder_button.setSizePolicy(sizePolicy)
        self.new_folder_button.setMinimumSize(QSize(110, 35))
        self.new_folder_button.setMaximumSize(QSize(110, 35))

        self.toolbarLayout.addWidget(self.new_folder_button)

        self.refresh_button = QPushButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setMinimumSize(QSize(90, 35))
        self.refresh_button.setMaximumSize(QSize(90, 35))

        self.toolbarLayout.addWidget(self.refresh_button)

        self.toolbar_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.toolbarLayout.addItem(self.toolbar_spacer)

        self.mainLayout.addLayout(self.toolbarLayout)

        # Address layout - make components responsive
        self.addressLayout = QHBoxLayout()
        self.addressLayout.setObjectName(u"addressLayout")
        self.addressLayout.setSpacing(5)
        
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(40, 30))
        self.homeButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.addressLayout.addWidget(self.homeButton)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(40, 30))
        self.backButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.addressLayout.addWidget(self.backButton)

        # Address input stretches to fill available space
        self.address_input = QLineEdit(self.centralwidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.address_input.setMinimumHeight(30)

        self.addressLayout.addWidget(self.address_input)

        self.go_button = QPushButton(self.centralwidget)
        self.go_button.setObjectName(u"go_button")
        self.go_button.setMinimumSize(QSize(50, 30))
        self.go_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.addressLayout.addWidget(self.go_button)

        self.mainLayout.addLayout(self.addressLayout)

        # Search layout - make components responsive
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setSpacing(5)
        
        # Search input stretches to fill most space
        self.search_input = QLineEdit(self.centralwidget)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.search_input.setMinimumHeight(30)

        self.searchLayout.addWidget(self.search_input)

        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(70, 30))
        self.search_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.searchLayout.addWidget(self.search_button)

        self.clear_search_button = QPushButton(self.centralwidget)
        self.clear_search_button.setObjectName(u"clear_search_button")
        self.clear_search_button.setMinimumSize(QSize(60, 30))
        self.clear_search_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.searchLayout.addWidget(self.clear_search_button)

        self.mainLayout.addLayout(self.searchLayout)

        # File list table - fully responsive with proper column sizing
        self.file_list = QTableWidget(self.centralwidget)
        if (self.file_list.columnCount() < 4):
            self.file_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.file_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.file_list.setObjectName(u"file_list")
        
        # Make table expand to fill available space
        self.file_list.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Configure column resize behavior for optimal spacing
        header = self.file_list.horizontalHeader()
        # Name column takes up most space and stretches
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        # Type column fits content but has minimum width
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setMinimumSectionSize(80)
        # Size column fits content
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        # Modified column is interactive (user can resize) with reasonable default
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)
        
        # Set initial column widths (these will adjust responsively)
        self.file_list.setColumnWidth(1, 100)  # Type
        self.file_list.setColumnWidth(2, 80)   # Size  
        self.file_list.setColumnWidth(3, 150)  # Modified
        
        # Enable sorting and selection
        self.file_list.setSortingEnabled(True)
        self.file_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.file_list.setAlternatingRowColors(True)

        # Add table to layout with stretch factor to take up most space
        self.mainLayout.addWidget(self.file_list, 1)  # Stretch factor of 1

        MainWindow.setCentralWidget(self.centralwidget)
        
        # Status bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)  # Enable resize grip
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"File Manager", None))
        self.new_folder_button.setText(QCoreApplication.translate("MainWindow", u"📁 New Folder", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"🔄 Refresh", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"🏠", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"←", None))
        self.go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search files and folders...", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.clear_search_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        ___qtablewidgetitem = self.file_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.file_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.file_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem3 = self.file_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Modified", None));
    # retranslateUi