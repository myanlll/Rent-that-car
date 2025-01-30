# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bul.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(560, 300)
        self.push_bul = QPushButton(Form)
        self.push_bul.setObjectName(u"push_bul")
        self.push_bul.setGeometry(QRect(170, 190, 231, 51))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 60, 541, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(60, 60, 211, 121))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_ad = QLineEdit(self.verticalLayoutWidget_3)
        self.line_ad.setObjectName(u"line_ad")

        self.verticalLayout_3.addWidget(self.line_ad)

        self.line_soyad = QLineEdit(self.verticalLayoutWidget_3)
        self.line_soyad.setObjectName(u"line_soyad")

        self.verticalLayout_3.addWidget(self.line_soyad)

        self.line_eposta = QLineEdit(self.verticalLayoutWidget_3)
        self.line_eposta.setObjectName(u"line_eposta")

        self.verticalLayout_3.addWidget(self.line_eposta)

        self.verticalLayoutWidget_4 = QWidget(Form)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(360, 60, 181, 121))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_dogum = QLineEdit(self.verticalLayoutWidget_4)
        self.line_dogum.setObjectName(u"line_dogum")

        self.verticalLayout_4.addWidget(self.line_dogum)

        self.line_telefon = QLineEdit(self.verticalLayoutWidget_4)
        self.line_telefon.setObjectName(u"line_telefon")

        self.verticalLayout_4.addWidget(self.line_telefon)

        self.line_TC = QLineEdit(self.verticalLayoutWidget_4)
        self.line_TC.setObjectName(u"line_TC")

        self.verticalLayout_4.addWidget(self.line_TC)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.push_bul.setText(QCoreApplication.translate("Form", u"Bul", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Ad", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Soyad", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"E-Mail", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Do\u011fum Tarihi", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Telefon", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TC Kimlik", None))
    # retranslateUi

