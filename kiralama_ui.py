# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kiralama.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1288, 375)
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
        self.tableWidget.setGeometry(QRect(10, 180, 491, 191))
        self.push_kirala = QPushButton(Form)
        self.push_kirala.setObjectName(u"push_kirala")
        self.push_kirala.setGeometry(QRect(1010, 110, 271, 261))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 491, 156))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.line_kullanci_id = QLineEdit(self.verticalLayoutWidget)
        self.line_kullanci_id.setObjectName(u"line_kullanci_id")
        self.line_kullanci_id.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.line_kullanci_id)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.line_ad = QLineEdit(self.verticalLayoutWidget)
        self.line_ad.setObjectName(u"line_ad")
        self.line_ad.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.line_ad)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_19.addWidget(self.label_19)

        self.line_soyad = QLineEdit(self.verticalLayoutWidget)
        self.line_soyad.setObjectName(u"line_soyad")
        self.line_soyad.setEnabled(False)

        self.horizontalLayout_19.addWidget(self.line_soyad)


        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.line_TC = QLineEdit(self.verticalLayoutWidget)
        self.line_TC.setObjectName(u"line_TC")
        self.line_TC.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.line_TC)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_21 = QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_21.addWidget(self.label_21)

        self.line_ehliyet = QLineEdit(self.verticalLayoutWidget)
        self.line_ehliyet.setObjectName(u"line_ehliyet")
        self.line_ehliyet.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.line_ehliyet)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(510, 10, 491, 156))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.line_arac_id = QLineEdit(self.verticalLayoutWidget_2)
        self.line_arac_id.setObjectName(u"line_arac_id")
        self.line_arac_id.setEnabled(False)

        self.horizontalLayout_16.addWidget(self.line_arac_id)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.line_marka = QLineEdit(self.verticalLayoutWidget_2)
        self.line_marka.setObjectName(u"line_marka")
        self.line_marka.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.line_marka)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_20 = QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_20.addWidget(self.label_20)

        self.line_plaka = QLineEdit(self.verticalLayoutWidget_2)
        self.line_plaka.setObjectName(u"line_plaka")
        self.line_plaka.setEnabled(False)

        self.horizontalLayout_20.addWidget(self.line_plaka)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.line_motor_no = QLineEdit(self.verticalLayoutWidget_2)
        self.line_motor_no.setObjectName(u"line_motor_no")
        self.line_motor_no.setEnabled(False)

        self.horizontalLayout_22.addWidget(self.line_motor_no)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_18.addWidget(self.label_18)

        self.line_gunluk_kira = QLineEdit(self.verticalLayoutWidget_2)
        self.line_gunluk_kira.setObjectName(u"line_gunluk_kira")
        self.line_gunluk_kira.setEnabled(False)

        self.horizontalLayout_18.addWidget(self.line_gunluk_kira)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(1010, 10, 271, 94))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_23 = QLabel(self.verticalLayoutWidget_3)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_23.addWidget(self.label_23)

        self.date_baslangic = QDateEdit(self.verticalLayoutWidget_3)
        self.date_baslangic.setObjectName(u"date_baslangic")

        self.horizontalLayout_23.addWidget(self.date_baslangic)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_24 = QLabel(self.verticalLayoutWidget_3)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.date_bitis = QDateEdit(self.verticalLayoutWidget_3)
        self.date_bitis.setObjectName(u"date_bitis")

        self.horizontalLayout_24.addWidget(self.date_bitis)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_25 = QLabel(self.verticalLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_25.addWidget(self.label_25)

        self.line_guzergah = QLineEdit(self.verticalLayoutWidget_3)
        self.line_guzergah.setObjectName(u"line_guzergah")
        self.line_guzergah.setEnabled(True)

        self.horizontalLayout_25.addWidget(self.line_guzergah)


        self.verticalLayout_3.addLayout(self.horizontalLayout_25)

        self.tableWidget_2 = QTableWidget(Form)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(510, 180, 491, 191))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
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
        self.push_kirala.setText(QCoreApplication.translate("Form", u"Kirala", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Kullan\u0131c\u0131 ID  ", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Ad                 ", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Soyad           ", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TC Kimlik     ", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Ehliyet          ", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Arac ID       ", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Marka         ", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Plaka           ", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Motor No   ", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"G\u00fcnl\u00fck Kira", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Ba\u015flang\u0131\u00e7 Tarihi               ", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Biti\u015f Tarihi", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Yolculuk G\u00fczergah\u0131          ", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"5", None));
    # retranslateUi

