# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(378, 212)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 130, 31, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(22, -8, 221, 61))
        self.p_musteri = QPushButton(self.centralwidget)
        self.p_musteri.setObjectName(u"p_musteri")
        self.p_musteri.setGeometry(QRect(3, 50, 91, 61))
        self.p_araclar = QPushButton(self.centralwidget)
        self.p_araclar.setObjectName(u"p_araclar")
        self.p_araclar.setGeometry(QRect(96, 50, 91, 61))
        self.p_kiralama = QPushButton(self.centralwidget)
        self.p_kiralama.setObjectName(u"p_kiralama")
        self.p_kiralama.setGeometry(QRect(189, 50, 91, 61))
        self.p_kiradakiaraclar = QPushButton(self.centralwidget)
        self.p_kiradakiaraclar.setObjectName(u"p_kiradakiaraclar")
        self.p_kiradakiaraclar.setGeometry(QRect(282, 50, 91, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 378, 21))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ara\u00e7 Kiralama Yaz\u0131l\u0131m\u0131 V1.6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"V 1.6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ara\u00e7 Kiralama Yaz\u0131l\u0131m\u0131", None))
        self.p_musteri.setText(QCoreApplication.translate("MainWindow", u"M\u00fc\u015fteriler", None))
        self.p_araclar.setText(QCoreApplication.translate("MainWindow", u"Ara\u00e7lar", None))
        self.p_kiralama.setText(QCoreApplication.translate("MainWindow", u"Kiralama", None))
        self.p_kiradakiaraclar.setText(QCoreApplication.translate("MainWindow", u"Kiradaki Ara\u00e7lar", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

