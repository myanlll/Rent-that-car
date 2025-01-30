# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kiradakiler.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1180, 369)
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 991, 156))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_26 = QLabel(self.verticalLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.line_kira_id = QLineEdit(self.verticalLayoutWidget_2)
        self.line_kira_id.setObjectName(u"line_kira_id")
        self.line_kira_id.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.line_kira_id)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_27 = QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_27.addWidget(self.label_27)

        self.line_marka_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.line_marka_2.setObjectName(u"line_marka_2")
        self.line_marka_2.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.line_marka_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_28 = QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_28.addWidget(self.label_28)

        self.line_musteri = QLineEdit(self.verticalLayoutWidget_2)
        self.line_musteri.setObjectName(u"line_musteri")
        self.line_musteri.setEnabled(False)

        self.horizontalLayout_28.addWidget(self.line_musteri)


        self.verticalLayout_4.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_29 = QLabel(self.verticalLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_29.addWidget(self.label_29)

        self.line_bitis_tarihi = QLineEdit(self.verticalLayoutWidget_2)
        self.line_bitis_tarihi.setObjectName(u"line_bitis_tarihi")
        self.line_bitis_tarihi.setEnabled(False)

        self.horizontalLayout_29.addWidget(self.line_bitis_tarihi)


        self.verticalLayout_4.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_30 = QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_30.addWidget(self.label_30)

        self.line_gunluk_kira_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.line_gunluk_kira_2.setObjectName(u"line_gunluk_kira_2")
        self.line_gunluk_kira_2.setEnabled(False)

        self.horizontalLayout_30.addWidget(self.line_gunluk_kira_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_30)

        self.tableWidget = QTableWidget(Form)
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
        self.tableWidget.setGeometry(QRect(10, 170, 991, 191))
        self.push_bitir = QPushButton(Form)
        self.push_bitir.setObjectName(u"push_bitir")
        self.push_bitir.setGeometry(QRect(1010, 10, 161, 351))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Kira ID            ", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Marka              ", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"M\u00fc\u015fteri            ", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Kira Biti\u015f Tarihi", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"G\u00fcnl\u00fck Kira     ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"5", None));
        self.push_bitir.setText(QCoreApplication.translate("Form", u"Kiray\u0131 Bitir", None))
    # retranslateUi

