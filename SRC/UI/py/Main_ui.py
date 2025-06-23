# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QAction)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget,QMenu)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(6)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.backButton = QToolButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setIconSize(QSize(16, 16))

        self.toolbarLayout.addWidget(self.backButton)

        self.forwardButton = QToolButton(self.centralwidget)
        self.forwardButton.setObjectName(u"forwardButton")
        self.forwardButton.setIconSize(QSize(16, 16))

        self.toolbarLayout.addWidget(self.forwardButton)

        self.upButton = QToolButton(self.centralwidget)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setIconSize(QSize(16, 16))

        self.toolbarLayout.addWidget(self.upButton)

        self.homeButton = QToolButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setIconSize(QSize(16, 16))

        self.toolbarLayout.addWidget(self.homeButton)

        self.address_input = QLineEdit(self.centralwidget)
        self.address_input.setObjectName(u"address_input")

        self.toolbarLayout.addWidget(self.address_input)

        self.go_button = QToolButton(self.centralwidget)
        self.go_button.setObjectName(u"go_button")

        self.toolbarLayout.addWidget(self.go_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolbarLayout.addItem(self.horizontalSpacer)

        self.search_input = QLineEdit(self.centralwidget)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(200, 0))

        self.toolbarLayout.addWidget(self.search_input)

        self.search_button = QToolButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setIconSize(QSize(16, 16))

        self.toolbarLayout.addWidget(self.search_button)

        self.new_folder_button = QToolButton(self.centralwidget)
        self.new_folder_button.setObjectName(u"new_folder_button")
        self.new_folder_button.setIconSize(QSize(16, 16))

        self.toolbarLayout.addWidget(self.new_folder_button)

        self.refresh_button = QToolButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setIconSize(QSize(16, 16))

        self.view_button = QToolButton(self.centralwidget)
        self.view_button.setObjectName(u"view_button")
        self.view_button.setPopupMode(QToolButton.InstantPopup)
        self.view_button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.view_button.setIconSize(QSize(16, 16))
        self.view_button.setFixedSize(24, 24)

        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setPen(QColor("#505050"))
# Draw 2x2 grid
        painter.drawLine(5, 3, 5, 13)
        painter.drawLine(10, 3, 10, 13)
        painter.drawLine(3, 5, 13, 5)
        painter.drawLine(3, 10, 13, 10)
        painter.end()
        self.view_button.setIcon(QIcon(pixmap))

        self.toolbarLayout.addWidget(self.view_button)

# View menu
        self.view_menu = QMenu(self.view_button)
        self.view_menu.setObjectName(u"view_menu")
        self.view_button.setMenu(self.view_menu)

# View actions
        self.actionList_View = QAction(MainWindow)
        self.actionList_View.setObjectName(u"actionList_View")
        self.actionList_View.setCheckable(True)
        self.actionList_View.setChecked(True)
        self.view_menu.addAction(self.actionList_View)

        self.actionIcon_View = QAction(MainWindow)
        self.actionIcon_View.setObjectName(u"actionIcon_View")
        self.actionIcon_View.setCheckable(True)
        self.view_menu.addAction(self.actionIcon_View)

        self.view_menu.addSeparator()

        self.actionSmall_Icons = QAction(MainWindow)
        self.actionSmall_Icons.setObjectName(u"actionSmall_Icons")
        self.actionSmall_Icons.setCheckable(True)
        self.view_menu.addAction(self.actionSmall_Icons)

        self.actionMedium_Icons = QAction(MainWindow)
        self.actionMedium_Icons.setObjectName(u"actionMedium_Icons")
        self.actionMedium_Icons.setCheckable(True)
        self.actionMedium_Icons.setChecked(True)
        self.view_menu.addAction(self.actionMedium_Icons)

        self.hidden_toggle = QToolButton(self.centralwidget)
        self.hidden_toggle.setObjectName(u"hidden_toggle")
        self.hidden_toggle.setCheckable(True)
        self.hidden_toggle.setToolTip("Show Hidden Files")
        self.hidden_toggle.setText("👁️")
        self.toolbarLayout.addWidget(self.hidden_toggle)

        self.toolbarLayout.addWidget(self.refresh_button)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setFrameShape(QFrame.StyledPanel)
        self.sidebarFrame.setFrameShadow(QFrame.Sunken)
        self.sidebarFrame.setMinimumWidth(180)
        self.sidebarFrame.setMaximumWidth(180)
        self.verticalLayout_2 = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout_2.setSpacing(2)  
        self.verticalLayout_2.setContentsMargins(6, 8, 6, 8) 
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.sidebarFrame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.placesList = QListWidget(self.sidebarFrame)
        
        icon = QIcon()
        icon.addFile(u":/icons/home", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem = QListWidgetItem(self.placesList)
        __qlistwidgetitem.setIcon(icon);
        icon1 = QIcon()
        icon1.addFile(u":/icons/desktop", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.placesList)
        __qlistwidgetitem1.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/icons/documents", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.placesList)
        __qlistwidgetitem2.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/icons/downloads", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.placesList)
        __qlistwidgetitem3.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u":/icons/music", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.placesList)
        __qlistwidgetitem4.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u":/icons/pictures", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem5 = QListWidgetItem(self.placesList)
        __qlistwidgetitem5.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u":/icons/videos", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem6 = QListWidgetItem(self.placesList)
        __qlistwidgetitem6.setIcon(icon6);
        icon7 = QIcon()
        icon7.addFile(u":/icons/trash", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem7 = QListWidgetItem(self.placesList)
        __qlistwidgetitem7.setIcon(icon7);
        self.placesList.setObjectName(u"placesList")
        self.placesList.setFrameShape(QFrame.NoFrame)
        self.placesList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.placesList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  
        self.placesList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.placesList.setFixedHeight(250)
        self.placesList.setResizeMode(QListWidget.Adjust)
        self.verticalLayout_2.addWidget(self.placesList, 0, Qt.AlignLeft)

        

        self.label_2 = QLabel(self.sidebarFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        

        self.devicesList = QListWidget(self.sidebarFrame)
        icon8 = QIcon()
        icon8.addFile(u":/icons/filesystem", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem8 = QListWidgetItem(self.devicesList)
        __qlistwidgetitem8.setIcon(icon8);
        icon9 = QIcon()
        icon9.addFile(u":/icons/usb", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qlistwidgetitem9 = QListWidgetItem(self.devicesList)
        __qlistwidgetitem9.setIcon(icon9);
        self.devicesList.setObjectName(u"devicesList")
        self.devicesList.setFrameShape(QFrame.NoFrame)
        self.devicesList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.devicesList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable scrolling
        self.devicesList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.devicesList.setFixedHeight(50) 

        self.verticalLayout_2.addWidget(self.devicesList)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pathFrame = QFrame(self.centralwidget)
        self.pathFrame.setObjectName(u"pathFrame")
        self.pathFrame.setFrameShape(QFrame.StyledPanel)
        self.pathFrame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.pathFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.currentPathLabel = QLabel(self.pathFrame)
        self.currentPathLabel.setObjectName(u"currentPathLabel")

        self.horizontalLayout_2.addWidget(self.currentPathLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.selectedCountLabel = QLabel(self.pathFrame)
        self.selectedCountLabel.setObjectName(u"selectedCountLabel")
        self.horizontalLayout_2.addWidget(self.selectedCountLabel)

        self.horizontalLayout_2.addSpacing(10)

        self.itemCountLabel = QLabel(self.pathFrame)
        self.itemCountLabel.setObjectName(u"itemCountLabel")

        self.horizontalLayout_2.addWidget(self.itemCountLabel)

        self.selectedCountLabel = QLabel(self.pathFrame)
        self.selectedCountLabel.setObjectName(u"selectedCountLabel")
        self.horizontalLayout_2.addWidget(self.selectedCountLabel)


        self.verticalLayout_3.addWidget(self.pathFrame)

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
        if (self.file_list.rowCount() < 2):
            self.file_list.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.file_list.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.file_list.setVerticalHeaderItem(1, __qtablewidgetitem5)
        self.file_list.setObjectName(u"file_list")
        self.file_list.setAlternatingRowColors(True)
        self.file_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.file_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_list.setShowGrid(False)
        self.file_list.setSortingEnabled(True)
        self.file_list.setCornerButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.file_list)

        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"File Manager", None))
#if QT_CONFIG(tooltip)
        self.backButton.setToolTip(QCoreApplication.translate("MainWindow", u"Back", None))
#endif // QT_CONFIG(tooltip)
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"←", None))
#if QT_CONFIG(tooltip)
        self.forwardButton.setToolTip(QCoreApplication.translate("MainWindow", u"Forward", None))
#endif // QT_CONFIG(tooltip)
        self.forwardButton.setText(QCoreApplication.translate("MainWindow", u"→", None))
#if QT_CONFIG(tooltip)
        self.upButton.setToolTip(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(tooltip)
        self.upButton.setText(QCoreApplication.translate("MainWindow", u"↑", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"🏠", None))
        self.address_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search files and folders...", None))
#if QT_CONFIG(tooltip)
        self.search_button.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"🔍", None))
#if QT_CONFIG(tooltip)
        self.new_folder_button.setToolTip(QCoreApplication.translate("MainWindow", u"New Folder", None))
#endif // QT_CONFIG(tooltip)
        self.new_folder_button.setText(QCoreApplication.translate("MainWindow", u"📁", None))
#if QT_CONFIG(tooltip)
        self.refresh_button.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"🔄", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Places", None))

        __sortingEnabled = self.placesList.isSortingEnabled()
        self.placesList.setSortingEnabled(False)
        ___qlistwidgetitem = self.placesList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"🏠 Home", None));
        ___qlistwidgetitem1 = self.placesList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"🖥️ Desktop", None));
        ___qlistwidgetitem2 = self.placesList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"📄 Documents", None));
        ___qlistwidgetitem3 = self.placesList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"📥 Downloads", None));
        ___qlistwidgetitem4 = self.placesList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"🎵 Music", None));
        ___qlistwidgetitem5 = self.placesList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"🖼️ Pictures", None));
        ___qlistwidgetitem6 = self.placesList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"🎬 Videos", None));
        ___qlistwidgetitem7 = self.placesList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"🗑️ Trash", None));
        self.placesList.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Devices", None))

        __sortingEnabled1 = self.devicesList.isSortingEnabled()
        self.devicesList.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.devicesList.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"🗂️ File System", None));
        ___qlistwidgetitem9 = self.devicesList.item(1)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"💽 Removable Media", None));
        self.devicesList.setSortingEnabled(__sortingEnabled1)

        #self.currentPathLabel.setText(QCoreApplication.translate("MainWindow", u"Path: /home/user", None))
        self.itemCountLabel.setText(QCoreApplication.translate("MainWindow", u"Items: 42", None))
        self.selectedCountLabel.setText(QCoreApplication.translate("MainWindow", u"Selected: 0", None))
        
        ___qtablewidgetitem = self.file_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.file_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.file_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem3 = self.file_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Modified", None));
        ___qtablewidgetitem4 = self.file_list.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.file_list.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));

        self.actionList_View.setText(QCoreApplication.translate("MainWindow", u"List View", None))
        self.actionIcon_View.setText(QCoreApplication.translate("MainWindow", u"Icon View", None))
        self.actionSmall_Icons.setText(QCoreApplication.translate("MainWindow", u"Small Icons", None))
        self.actionMedium_Icons.setText(QCoreApplication.translate("MainWindow", u"Medium Icons", None))
    # retranslateUi