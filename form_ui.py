# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(437, 234)
        self.actionThere_are_no_options = QAction(MainWindow)
        self.actionThere_are_no_options.setObjectName(u"actionThere_are_no_options")
        self.actionNo_options = QAction(MainWindow)
        self.actionNo_options.setObjectName(u"actionNo_options")
        self.actionNo_options_2 = QAction(MainWindow)
        self.actionNo_options_2.setObjectName(u"actionNo_options_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 411, 161))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.p_musteri = QPushButton(self.horizontalLayoutWidget)
        self.p_musteri.setObjectName(u"p_musteri")

        self.horizontalLayout.addWidget(self.p_musteri)

        self.p_araclar = QPushButton(self.horizontalLayoutWidget)
        self.p_araclar.setObjectName(u"p_araclar")

        self.horizontalLayout.addWidget(self.p_araclar)

        self.p_kiralama = QPushButton(self.horizontalLayoutWidget)
        self.p_kiralama.setObjectName(u"p_kiralama")

        self.horizontalLayout.addWidget(self.p_kiralama)

        self.p_kiradakiaraclar = QPushButton(self.horizontalLayoutWidget)
        self.p_kiradakiaraclar.setObjectName(u"p_kiradakiaraclar")

        self.horizontalLayout.addWidget(self.p_kiradakiaraclar)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 150, 31, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 221, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 437, 21))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.actionThere_are_no_options)
        self.menuOptions.addAction(self.actionNo_options)
        self.menuOptions.addAction(self.actionNo_options_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionThere_are_no_options.setText(QCoreApplication.translate("MainWindow", u"There are no options", None))
        self.actionNo_options.setText(QCoreApplication.translate("MainWindow", u"No options", None))
        self.actionNo_options_2.setText(QCoreApplication.translate("MainWindow", u"No options", None))
        self.p_musteri.setText(QCoreApplication.translate("MainWindow", u"M\u00fc\u015fteriler", None))
        self.p_araclar.setText(QCoreApplication.translate("MainWindow", u"Ara\u00e7lar", None))
        self.p_kiralama.setText(QCoreApplication.translate("MainWindow", u"Kiralama", None))
        self.p_kiradakiaraclar.setText(QCoreApplication.translate("MainWindow", u"Kiradaki Ara\u00e7lar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"V 1.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rent A Car by Mert ", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

