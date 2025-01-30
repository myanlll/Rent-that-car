# This Python file uses the following encoding: utf-8
import sys
import mysql.connector

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox

from PySide6.QtCore import QDate

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_musteriler import Ui_Musteri
from ui_araclar import Ui_Araclar
from ui_bul import Ui_Bul
from ui_ara_arac import Ui_araarac
from ui_kiralama import Ui_Kiralama
from ui_kiradakiler import Ui_kiradakiler

class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.sqlBaglan()
        self.dbCheck()
        self.tableCheck()
        
        self.ui.p_araclar.clicked.connect(self.open_araclar)
        self.ui.p_musteri.clicked.connect(self.open_musteriler)
        self.ui.p_kiralama.clicked.connect(self.open_kiralama)
        self.ui.p_kiradakiaraclar.clicked.connect(self.open_kiradakiler)
        
        
    def sqlBaglan(self):
        self.dbConn=mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        
    def dbCheck(self):
        if self.dbConn.is_connected():
            print("Baglanti Basarili")
            self.mycursor = self.dbConn.cursor()
        self.target_db = "yourdatabase"
        try:
            self.mycursor.execute(f"USE {self.target_db}")
        except:
            self.mycursor.execute(f"CREATE DATABASE {self.target_db}")

                   
    def tableCheck(self):
        self.mycursor.execute(f"USE {self.target_db}")
        self.mycursor.execute("SHOW TABLES")
        dbtable = [dbTbl[0] for dbTbl in self.mycursor.fetchall()]
        
        if dbtable==[]:
            self.mycursor.execute("""
                CREATE TABLE musteriler (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ad VARCHAR(50),
                    soyad VARCHAR(50),
                    tc VARCHAR(50),
                    dogum_tarihi VARCHAR(50),
                    adres VARCHAR(210),
                    telefon VARCHAR(16),
                    meslek VARCHAR(25),
                    ehliyet VARCHAR(8),
                    medenidurum VARCHAR(50),
                    egitim_durum VARCHAR(15),
                    e_posta VARCHAR(30)
                );
            """)
            
            self.mycursor.execute("""
                CREATE TABLE araclar (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    arac_turu VARCHAR(50),
                    marka VARCHAR(50),
                    model VARCHAR(50),
                    uretim_yili VARCHAR(50),
                    yakit_turu VARCHAR(50),
                    vites VARCHAR(50),
                    motor_gucu VARCHAR(50),
                    motor_hacmi VARCHAR(50),
                    cekis VARCHAR(50),
                    kapi VARCHAR(50),
                    renk VARCHAR(50),
                    motor_no VARCHAR(50),
                    plaka VARCHAR(50),
                    gunluk_kira_bedeli INT,
                    durum VARCHAR(50)    
                );
            """)
            
            self.mycursor.execute("""
               CREATE TABLE kiralama(
                    id INT auto_increment PRIMARY KEY,
                    arac_id INT,
                    musteri_Id INT,
                    gunluk_kira_bedeli INT,
                    guzergah nvarchar(100),
                    baslangic_tarihi date,
                    bitis_tarihi date,
                    
                    FOREIGN KEY (arac_id) References Araclar(id),
                    FOREIGN KEY (musteri_id) references Musteriler(id)
                )              
               
            """)
            self.dbConn.commit()

            
    
    def open_musteriler(self):
        self.m = musteriler(self)
        self.m.show()
                
    def open_araclar(self):
        self.a = araclar(self)
        self.a.show()

    def open_kiralama(self):
        self.k = kiralama(self)
        self.k.show()


    def open_kiradakiler(self):
        self.d = kiradakiler(self)
        self.d.show()


class kiradakiler(QWidget):
    
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_kiradakiler()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID","Marka&Model","Musteri","Bitiş Tarihi","Günlük Kira"])
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 220)
        self.ui.tableWidget.setColumnWidth(2, 220)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 200)
        self.data_cek()
        self.ui.push_bitir.clicked.connect(self.kirayi_bitir)
        self.ui.tableWidget.doubleClicked.connect(self.fill_cell_field) 
        self.ui.push_uzat.clicked.connect(self.kirayı_uzat)         
        
    def label_doldur(self):
        current_user_row = self.ui.tableWidget.currentRow()
        
        self.fill_cell_field(current_user_row)

        
    def data_cek(self):
        
        query = """
            SELECT k.id, CONCAT(a.marka, ' ', a.model) as markamodel, m.ad, k.bitis_tarihi, a.gunluk_kira_bedeli
            FROM `{}`.kiralama as k
            INNER JOIN `{}`.musteriler as m ON m.id = k.musteri_Id
            INNER JOIN `{}`.araclar as a ON k.arac_id = a.id    
        """

        formatted_query = query.format(self.mainWindow.target_db, self.mainWindow.target_db, self.mainWindow.target_db)
        
        self.mainWindow.mycursor.execute(formatted_query)

        self.kiralama_data = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.table_doldur()
        
    def get_cell_value(self,table, row, column):
        item = table.item(row, column)
        return item.text() if item is not None else ""
        
    def table_doldur(self):
        self.ui.tableWidget.setRowCount(len(self.kiralama_data))
        if self.kiralama_data != []:
            for x in range(len(self.kiralama_data)):
                item_id = QTableWidgetItem(str(self.kiralama_data[x][0]))
                item_marka = QTableWidgetItem(str(self.kiralama_data[x][1]))
                item_musteri = QTableWidgetItem(str(self.kiralama_data[x][2]))
                item_bitis = QTableWidgetItem(str(self.kiralama_data[x][3]))
                item_gunluk_kira = QTableWidgetItem(str(self.kiralama_data[x][4]))
                self.ui.tableWidget.setItem(x, 0, item_id)
                self.ui.tableWidget.setItem(x, 1, item_marka)
                self.ui.tableWidget.setItem(x, 2, item_musteri)
                self.ui.tableWidget.setItem(x, 3, item_bitis)
                self.ui.tableWidget.setItem(x, 4, item_gunluk_kira)

    def kirayı_uzat(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            return
        bitis_tarihi_str = self.get_cell_value(self.ui.tableWidget, current_row, 3)
        if not bitis_tarihi_str:
            return
        try:
            gun_sayisi = int(self.ui.line_uzat.text())
        except ValueError:
            return
        try:
            eski_tarih = QDate.fromString(bitis_tarihi_str, "yyyy-MM-dd")
            if not eski_tarih.isValid():
                return

            yeni_tarih = eski_tarih.addDays(gun_sayisi)
        except Exception as e:
            return
        id = self.get_cell_value(self.ui.tableWidget, current_row, 0)
        
        query = (f"UPDATE `{self.mainWindow.target_db}`.`kiralama` "
                f"SET bitis_tarihi = '{yeni_tarih.toString('yyyy-MM-dd')}' "
                f"WHERE id = '{id}'")

        self.mainWindow.mycursor.execute(query)
        self.mainWindow.dbConn.commit()

        QMessageBox.information(self, "Başarılı", f"Kiralama süresi {gun_sayisi} gün uzatıldı.")
        self.data_cek()
        self.table_doldur()



            
    
    def kirayı_oto_bitir(self):
        today = QDate.currentDate()
        query = f"SELECT id FROM {self.mainWindow.target_db}.kiralama WHERE bitis_tarihi = '{today}'"
        self.mainWindow.mycursor.execute(query)
        id = self.mainWindow.mycursor.fetchone()
        if id is not None:
            self.mainWindow.mycursor.execute(f"DELETE FROM `{self.mainWindow.target_db}`.`kiralama` WHERE (`id` = '{id[0]}');")
            self.mainWindow.dbConn.commit()
            self.data_cek()
            self.clear_cell_field()
            QMessageBox.information(None, "Bilgi", "Kiralama işlemi başarılı.")
        else:
            QMessageBox.critical(None, "Hata", "Bugün için kiralama bitirilecek araç bulunamadı.")

    
            
            
    def kirayi_bitir(self):
        id = self.ui.line_kira_id.text()
        self.mainWindow.mycursor.execute(f"DELETE FROM `{self.mainWindow.target_db}`.`kiralama` WHERE (`id` = '{id}');")
        self.mainWindow.dbConn.commit()
        self.data_cek()
        self.clear_cell_field()

    def fill_cell_field(self):
        current_row = self.ui.tableWidget.currentRow()
        self.ui.line_kira_id.setText(self.get_cell_value(self.ui.tableWidget, current_row, 0))
        self.ui.line_marka_2.setText(self.get_cell_value(self.ui.tableWidget, current_row, 1))
        self.ui.line_musteri.setText(self.get_cell_value(self.ui.tableWidget, current_row, 2))
        self.ui.line_bitis_tarihi.setText(self.get_cell_value(self.ui.tableWidget, current_row, 3))
        self.ui.line_gunluk_kira_2.setText(self.get_cell_value(self.ui.tableWidget, current_row, 4))
    
    def clear_cell_field(self):
        self.ui.line_kira_id.setText("")
        self.ui.line_marka_2.setText("")
        self.ui.line_musteri.setText("")
        self.ui.line_bitis_tarihi.setText("")
        self.ui.line_gunluk_kira_2.setText("")

class kiralama(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_Kiralama()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID","Ad","Soyad","tc","ehliyet"])
        self.ui.tableWidget.setColumnWidth(0, 40)
        self.ui.tableWidget.setColumnWidth(1, 160)
        self.ui.tableWidget.setColumnWidth(2, 105)
        self.ui.tableWidget.setColumnWidth(3, 90)
        self.ui.tableWidget.setColumnWidth(4, 70)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["ID", "Marka","Plaka","Motor No","Günlük Kira"])
        self.ui.tableWidget_2.setColumnWidth(0, 40)
        self.ui.tableWidget_2.setColumnWidth(1, 125)
        self.ui.tableWidget_2.setColumnWidth(2, 125)
        self.ui.tableWidget_2.setColumnWidth(3, 100)
        self.ui.tableWidget_2.setColumnWidth(4, 80)
        self.data_cek()
        self.ui.tableWidget.doubleClicked.connect(self.label_doldur)
        self.ui.tableWidget_2.doubleClicked.connect(self.label_doldur)
        self.ui.push_kirala.clicked.connect(self.rent)
        self.ui.date_baslangic.setDisplayFormat("yyyy-MM-dd")
        self.ui.date_bitis.setDisplayFormat("yyyy-MM-dd")
        
        today = QDate.currentDate()
        self.ui.date_baslangic.setDate(today)
        self.ui.date_bitis.setDate(today)
        
    def check_if_car_is_rented(self):
        self.ui.date_baslangic.text()
        self.ui.date_bitis.text()
        
        query = f"SELECT 1 FROM {self.mainWindow.target_db}.kiralama WHERE arac_id = %s AND (baslangic_tarihi BETWEEN %s AND %s OR bitis_tarihi BETWEEN %s AND %s)"
        
        self.mainWindow.mycursor.execute(query, (self.ui.line_arac_id.text(), self.ui.date_baslangic.text(), self.ui.date_bitis.text(), self.ui.date_baslangic.text(), self.ui.date_bitis.text()))
        
        if self.mainWindow.mycursor.fetchone() is not None:
            return True
        else:
            return False

    def data_cek(self):
        self.mainWindow.mycursor.execute(f"SELECT * FROM `{self.mainWindow.target_db}`.`musteriler`;")
        self.musteri_data = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.table_doldur()

        self.mainWindow.mycursor.execute(f"SELECT id,marka,plaka,motor_no,gunluk_kira_bedeli FROM `{self.mainWindow.target_db}`.`araclar`;")
        self.arac_data = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.table_doldur2()

        
    def table_doldur(self):
        self.ui.tableWidget.setRowCount(len(self.musteri_data))
        if self.musteri_data != []:
            for x in range(len(self.musteri_data)):
                item_id = QTableWidgetItem(str(self.musteri_data[x][0]))
                item_ad = QTableWidgetItem(str(self.musteri_data[x][1]))
                item_soyad = QTableWidgetItem(str(self.musteri_data[x][2]))
                item_TC = QTableWidgetItem(str(self.musteri_data[x][3]))
                item_ehliyet = QTableWidgetItem(str(self.musteri_data[x][8]))
                self.ui.tableWidget.setItem(x, 0, item_id)
                self.ui.tableWidget.setItem(x, 1, item_ad)
                self.ui.tableWidget.setItem(x, 2, item_soyad)
                self.ui.tableWidget.setItem(x, 3, item_TC)
                self.ui.tableWidget.setItem(x, 4, item_ehliyet)

    def table_doldur2(self):
        self.ui.tableWidget_2.setRowCount(len(self.arac_data))
        if self.arac_data != []:
            for x in range(len(self.arac_data)):
                item_id = QTableWidgetItem(str(self.arac_data[x][0]))
                item_marka = QTableWidgetItem(str(self.arac_data[x][1]))
                item_plaka = QTableWidgetItem(str(self.arac_data[x][2]))
                item_motor_no = QTableWidgetItem(str(self.arac_data[x][3]))
                item_gunluk_kira = QTableWidgetItem(str(self.arac_data[x][4]))
                self.ui.tableWidget_2.setItem(x, 0, item_id)
                self.ui.tableWidget_2.setItem(x, 1, item_marka)
                self.ui.tableWidget_2.setItem(x, 2, item_plaka)
                self.ui.tableWidget_2.setItem(x, 3, item_motor_no)
                self.ui.tableWidget_2.setItem(x, 4, item_gunluk_kira)

    def fill_user_fields(self,row):
        self.ui.line_kullanci_id.setText(self.get_cell_value(self.ui.tableWidget, row, 0))
        self.ui.line_ad.setText(self.get_cell_value(self.ui.tableWidget, row, 1))
        self.ui.line_soyad.setText(self.get_cell_value(self.ui.tableWidget, row, 2))
        self.ui.line_TC.setText(self.get_cell_value(self.ui.tableWidget, row, 3))
        self.ui.line_ehliyet.setText(self.get_cell_value(self.ui.tableWidget, row, 4))

    def fill_car_fields(self,row):
        
        self.ui.line_arac_id.setText(self.get_cell_value(self.ui.tableWidget_2, row, 0))
        self.ui.line_marka.setText(self.get_cell_value(self.ui.tableWidget_2, row, 1))
        self.ui.line_plaka.setText(self.get_cell_value(self.ui.tableWidget_2, row, 2))
        self.ui.line_motor_no.setText(self.get_cell_value(self.ui.tableWidget_2, row, 3))
        self.ui.line_gunluk_kira.setText(self.get_cell_value(self.ui.tableWidget_2, row, 4))

        
    def get_cell_value(self,table, row, column):
        item = table.item(row, column)
        return item.text() if item is not None else ""
    
    
    def label_doldur(self):
        current_user_row = self.ui.tableWidget.currentRow()
        current_car_row = self.ui.tableWidget_2.currentRow()
        
        self.fill_user_fields(current_user_row)
        self.fill_car_fields(current_car_row)
    
    def clear_user_fields(self):
        self.ui.line_kullanci_id.setText("")
        self.ui.line_ad.setText("")
        self.ui.line_soyad.setText("")
        self.ui.line_TC.setText("")
        self.ui.line_ehliyet.setText("")
    
    def clear_car_fields(self):
        self.ui.line_arac_id.setText("")
        self.ui.line_marka.setText("")
        self.ui.line_plaka.setText("")
        self.ui.line_motor_no.setText("")
        self.ui.line_gunluk_kira.setText("")
    
    def rent(self):
        
        sqlEklemeKomut = """
            INSERT INTO kiralama
            (arac_id, musteri_Id, gunluk_kira_bedeli, guzergah, baslangic_tarihi, bitis_tarihi)
            VALUES ( %s, %s, %s, %s, %s, %s)
        """
        
        self.veri = (
            self.ui.line_arac_id.text(),
            self.ui.line_kullanci_id.text(),
            self.ui.line_gunluk_kira.text(),
            self.ui.line_guzergah.text(),
            self.ui.date_baslangic.text(),
            self.ui.date_bitis.text()
        )
        
        if self.check_if_car_is_rented():
            QMessageBox.critical(None, "Hata", "Bu araç bu tarihler arasında kiralanmış.")
        else:
            self.mainWindow.mycursor.execute(sqlEklemeKomut,self.veri)
            self.mainWindow.dbConn.commit()
            QMessageBox.information(None, "Bilgi", "Kiralama işlemi başarılı.")
            self.data_cek()
            self.clear_user_fields()
            self.clear_car_fields()

class araclar(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_Araclar()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["Id","Araç Türü","Marka","Model","Üretim Yılı","Yakıt Türü","Vites","Motor Gücü","Motor Hacmi","Çekiş","Kapı","Renk","Motor No", "Plaka", "Günlük Kiralama Bedeli", "Durum"])
        self.ui.tableWidget.setColumnWidth(0, 70)
        self.ui.tableWidget.setColumnWidth(1, 80)
        self.ui.tableWidget.setColumnWidth(2, 105)
        self.ui.tableWidget.setColumnWidth(3, 105)
        self.ui.tableWidget.setColumnWidth(4, 70)
        self.ui.tableWidget.setColumnWidth(5, 75)
        self.ui.tableWidget.setColumnWidth(6, 50)
        self.ui.tableWidget.setColumnWidth(7, 80)
        self.ui.tableWidget.setColumnWidth(8, 85)
        self.ui.tableWidget.setColumnWidth(9, 85)
        self.ui.tableWidget.setColumnWidth(10, 50)
        self.ui.tableWidget.setColumnWidth(11, 85)
        self.ui.tableWidget.setColumnWidth(12, 85)
        self.ui.tableWidget.setColumnWidth(13, 85)
        self.ui.tableWidget.setColumnWidth(14, 140)
        self.ui.tableWidget.setColumnWidth(15, 85)
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)
        
        query = f"SELECT * FROM {self.mainWindow.target_db}.araclar WHERE 1"
        self.mainWindow.mycursor.execute(query)
        self.table_doldur()
    
        self.ui.push_ara.clicked.connect(self.open_ara_arac)
        self.ui.push_ara.clicked.connect(self.ara_fonk)
        self.ui.push_yeni.clicked.connect(self.yeni_fonk)
        self.ui.push_yeni.clicked.connect(self.ara_fonk)
        self.ui.push_sil.clicked.connect(self.sil_fonk)
        self.ui.push_sil.clicked.connect(self.ara_fonk)
        self.ui.push_guncelle.clicked.connect(self.guncelle_fonk)
        self.ui.push_guncelle.clicked.connect(self.ara_fonk)
        self.ui.push_kaydet.clicked.connect(self.kaydet_fonk)
        self.ui.push_kaydet.clicked.connect(self.ara_fonk)
        self.ui.tableWidget.doubleClicked.connect(self.get_info_fonk)
        self.ui.tableWidget.doubleClicked.connect(self.ara_fonk)
        
    
    def open_ara_arac(self):
        self.k = araarac(self)
        self.k.show()
    
    def yeni_fonk(self):
        self.ui.comboBox_tur.setCurrentIndex(0)
        self.ui.line_marka.setText("")
        self.ui.line_model.setText("")
        self.ui.line_uretimyil.setText("")
        self.ui.comboBox_yakit.setCurrentIndex(0)
        self.ui.comboBox_vites.setCurrentIndex(0)
        self.ui.line_motor_guc.setText("")
        self.ui.line_motor_hacim.setText("")
        self.ui.line_cekis.setText("")
        self.ui.line_kapi.setText("")
        self.ui.line_renk.setText("")
        self.ui.line_motor_no.setText("")
        self.ui.line_plaka.setText("")
        self.ui.line_gunluk_kira.setText("")
        self.ui.line_arac_id.setText("")
        self.ui.line_durum.setText("")
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)   
    
    def sil_fonk(self):
        result=self.mesaj("Silmek İstediğinize Emin Misiniz?")
        if result==QMessageBox.Yes:
            id=int (self.ui.line_arac_id.text())
            self.mainWindow.mycursor.execute(f"""
                                    DELETE FROM `{self.mainWindow.target_db}`.`araclar` 
                                    WHERE (`id` = '{id}');""")
            self.ui.push_sil.setEnabled(False)
            self.mainWindow.dbConn.commit()
            self.ara_fonk()
            
        else:
            pass
     
    def guncelle_fonk(self):
        id = int(self.ui.line_arac_id.text())
        arac_turu = self.ui.comboBox_tur.currentIndex()
        marka = self.ui.line_marka.text()
        model = self.ui.line_model.text()
        uretim_yili = self.ui.line_uretimyil.text()
        yakit_turu = self.ui.comboBox_yakit.currentIndex()
        vites = self.ui.comboBox_vites.currentIndex()
        motor_gucu = self.ui.line_motor_guc.text()
        motor_hacmi = self.ui.line_motor_hacim.text()
        cekis = self.ui.line_cekis.text()
        kapi = self.ui.line_kapi.text()
        renk = self.ui.line_renk.text()
        motor_no = self.ui.line_motor_no.text()
        plaka = self.ui.line_plaka.text()
        gunluk_kira_bedeli = self.ui.line_gunluk_kira.text()
        durum = self.ui.line_durum.text()


        sorgu = f"""
            UPDATE `{self.mainWindow.target_db}`.`araclar` SET
            `arac_turu` = %s,
            `marka` = %s,
            `model` = %s,
            `uretim_yili` = %s,
            `yakit_turu` = %s,
            `vites` = %s,
            `motor_gucu` = %s,
            `motor_hacmi` = %s,
            `cekis` = %s,
            `kapi` = %s,
            `renk` = %s,
            `motor_no` = %s,
            `plaka` = %s,
            `gunluk_kira_bedeli` = %s,
            `durum` = %s
            WHERE `id` = %s;
        """
        degerler = (arac_turu, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, motor_hacmi, cekis, kapi, renk, motor_no, plaka, gunluk_kira_bedeli, durum, id)
        self.mainWindow.mycursor.execute(sorgu, degerler)
        self.mainWindow.dbConn.commit()
        self.ara_fonk()

    def kaydet_fonk(self):
        if(self.ui.line_arac_id.text()!=""):
            result=self.mesaj("Bu kayıt zaten mevcut. Güncellemek ister misiniz?")
            if (result==QMessageBox.Yes):
                self.guncelle_fonk()
            else:
                pass
        else:
            sqlBaglan = """
            INSERT INTO araclar
            (id, arac_turu, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, motor_hacmi, cekis, kapi, renk, motor_no, plaka, gunluk_kira_bedeli, durum)
            VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)
            """
            self.veri = (
                self.ui.comboBox_tur.currentIndex(),
                self.ui.line_marka.text(),
                self.ui.line_model.text(),
                self.ui.line_uretimyil.text(),
                self.ui.comboBox_yakit.currentIndex(),
                self.ui.comboBox_vites.currentIndex(),
                self.ui.line_motor_guc.text(),
                self.ui.line_motor_hacim.text(),
                self.ui.line_cekis.text(),
                self.ui.line_kapi.text(),
                self.ui.line_renk.text(),
                self.ui.line_motor_no.text(),
                self.ui.line_plaka.text(),
                self.ui.line_gunluk_kira.text(),
                self.ui.line_durum.text()
            )

            self.mainWindow.mycursor.execute(sqlBaglan,self.veri)
            self.mainWindow.dbConn.commit()

    def get_info_fonk(self):
        self.ui.push_sil.setEnabled(True)
        self.ui.push_guncelle.setEnabled(True)
        self.cell_changed_fonk()
        
    def cell_changed_fonk(self):
        row_sec = self.ui.tableWidget.currentRow()
        if row_sec >= 0:
            self.ui.line_arac_id.setText(self.ui.tableWidget.item(row_sec, 0).text())
            
            # Araç Türü
            tur_metin = self.ui.tableWidget.item(row_sec, 1).text()
            tur_index = self.ui.comboBox_tur.findText(tur_metin)
            self.ui.comboBox_tur.setCurrentIndex(tur_index if tur_index != -1 else 0)
            
            self.ui.line_marka.setText(self.ui.tableWidget.item(row_sec, 2).text())
            self.ui.line_model.setText(self.ui.tableWidget.item(row_sec, 3).text())
            self.ui.line_uretimyil.setText(self.ui.tableWidget.item(row_sec, 4).text())
            
            # Yakıt Türü
            yakit_metin = self.ui.tableWidget.item(row_sec, 5).text()
            yakit_index = self.ui.comboBox_yakit.findText(yakit_metin)
            self.ui.comboBox_yakit.setCurrentIndex(yakit_index if yakit_index != -1 else 0)
            
            # Vites Türü
            vites_metin = self.ui.tableWidget.item(row_sec, 6).text()
            vites_index = self.ui.comboBox_vites.findText(vites_metin)
            self.ui.comboBox_vites.setCurrentIndex(vites_index if vites_index != -1 else 0)
            
            self.ui.line_motor_guc.setText(self.ui.tableWidget.item(row_sec, 7).text())
            self.ui.line_motor_hacim.setText(self.ui.tableWidget.item(row_sec, 8).text())
            self.ui.line_cekis.setText(self.ui.tableWidget.item(row_sec, 9).text())
            self.ui.line_kapi.setText(self.ui.tableWidget.item(row_sec, 10).text())
            self.ui.line_renk.setText(self.ui.tableWidget.item(row_sec, 11).text())
            self.ui.line_motor_no.setText(self.ui.tableWidget.item(row_sec, 12).text())
            self.ui.line_plaka.setText(self.ui.tableWidget.item(row_sec, 13).text())
            self.ui.line_gunluk_kira.setText(self.ui.tableWidget.item(row_sec, 14).text())
            self.ui.line_durum.setText(self.ui.tableWidget.item(row_sec, 15).text())
            
            self.ui.push_sil.setEnabled(True)
            self.ui.push_guncelle.setEnabled(True)
        
    def mesaj(self, metin):
        self.messagebox = QMessageBox()
        self.messagebox.setText(metin)
        self.messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.messagebox.setDefaultButton(QMessageBox.Cancel)
        return self.messagebox.exec()
    
    def ara_fonk(self):
        self.mainWindow.mycursor.execute(f"SELECT * FROM `{self.mainWindow.target_db}`.`araclar`;")
        
        self.table_doldur()
        
        
    def table_doldur(self):
        araTable = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.ui.tableWidget.setRowCount(len(araTable))
        if(araTable!=[]):
            for x in range(len(araTable)):
                item_id = QTableWidgetItem(str(araTable[x][0]))
                item_arac_tur = QTableWidgetItem(str(araTable[x][1]))
                item_marka = QTableWidgetItem(str(araTable[x][2]))
                item_model = QTableWidgetItem(str(araTable[x][3]))
                item_uretim_yil = QTableWidgetItem(str(araTable[x][4]))
                item_yakit= QTableWidgetItem(str(araTable[x][5]))
                item_vites = QTableWidgetItem(str(araTable[x][6]))
                item_motor_guc = QTableWidgetItem(str(araTable[x][7]))
                item_motor_hacim = QTableWidgetItem(str(araTable[x][8]))
                item_cekis = QTableWidgetItem(str(araTable[x][9]))
                item_kapi = QTableWidgetItem(str(araTable[x][10]))
                item_renk = QTableWidgetItem(str(araTable[x][11]))
                item_motor_no = QTableWidgetItem(str(araTable[x][12]))
                item_plaka = QTableWidgetItem(str(araTable[x][13]))
                item_gunluk_kira = QTableWidgetItem(str(araTable[x][14]))
                item_durum = QTableWidgetItem(str(araTable[x][15]))
                self.ui.tableWidget.setItem(x,0, item_id)
                self.ui.tableWidget.setItem(x,1, item_arac_tur)
                self.ui.tableWidget.setItem(x,2, item_marka)
                self.ui.tableWidget.setItem(x,3, item_model)
                self.ui.tableWidget.setItem(x,4, item_uretim_yil)
                self.ui.tableWidget.setItem(x,5, item_yakit)
                self.ui.tableWidget.setItem(x,6, item_vites)
                self.ui.tableWidget.setItem(x,7, item_motor_guc)
                self.ui.tableWidget.setItem(x,8, item_motor_hacim)
                self.ui.tableWidget.setItem(x,9, item_cekis)
                self.ui.tableWidget.setItem(x,10, item_kapi)
                self.ui.tableWidget.setItem(x,11, item_renk)
                self.ui.tableWidget.setItem(x,12, item_motor_no)
                self.ui.tableWidget.setItem(x,13, item_plaka)
                self.ui.tableWidget.setItem(x,14, item_gunluk_kira)
                self.ui.tableWidget.setItem(x,15, item_durum)

class araarac(QWidget):
    def __init__(self,araclar):
        super().__init__()
        self.ui = Ui_araarac()
        self.ui.setupUi(self)
        self.araclar = araclar
        self.ui.push_bul.clicked.connect(self.arama_fonk)
        


    def arama_fonk(self):
        self.marka=self.ui.line_marka.text()
        self.model=self.ui.line_model.text()
        self.yil=self.ui.line_yil.text()
        self.motor_no=self.ui.line_motor_no.text()
        self.plaka=self.ui.line_plaka.text()
        self.renk=self.ui.line_renk.text()
        
        
        query = f"SELECT * FROM {self.araclar.mainWindow.target_db}.araclar WHERE 1"
        
        if(self.marka!=""):
            query += f" AND marka LIKE '%{self.marka}%'"
        
        if(self.model!=""):
            query += f" AND model LIKE '%{self.model}%'"
        
        if(self.yil!=""):
            query += f" AND uretim_yili LIKE '%{self.yil}%'"
        
        if(self.motor_no!=""):
            query += f" AND motor_no LIKE '%{self.motor_no}%'"
            
        if(self.plaka!=""):
            query += f" AND plaka LIKE '%{self.plaka}%'"
            
        if(self.renk!=""):
            query += f" AND renk LIKE '%{self.renk}%'"
            
        self.araclar.mainWindow.mycursor.execute(query)
        
        self.araclar.table_doldur()

class musteriler(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_Musteri()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["Id","Ad","Soyad","TC","Doğum Tarihi","Adres","Telefon","Meslek","Ehliyet","Medeni Durum","Eğitim Durumu","E-Posta"])
        self.ui.tableWidget.setColumnWidth(0, 70)
        self.ui.tableWidget.setColumnWidth(1, 135)
        self.ui.tableWidget.setColumnWidth(2, 120)
        self.ui.tableWidget.setColumnWidth(3, 105)
        self.ui.tableWidget.setColumnWidth(4, 90)
        self.ui.tableWidget.setColumnWidth(5, 150)
        self.ui.tableWidget.setColumnWidth(6, 105)
        self.ui.tableWidget.setColumnWidth(7, 110)
        self.ui.tableWidget.setColumnWidth(8, 75)
        self.ui.tableWidget.setColumnWidth(9, 90)
        self.ui.tableWidget.setColumnWidth(10, 110)
        self.ui.tableWidget.setColumnWidth(11, 200)
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)
        self.ui.mycursor = self.mainWindow.mycursor
        
        query = f"SELECT * FROM {self.mainWindow.target_db}.musteriler WHERE 1"
        self.mainWindow.mycursor.execute(query)
        self.table_doldur()

        self.ui.push_ara.clicked.connect(self.open_bul)
        self.ui.push_ara.clicked.connect(self.ara_fonk)
        self.ui.push_yeni.clicked.connect(self.yeni_fonk)
        self.ui.push_yeni.clicked.connect(self.ara_fonk)
        self.ui.push_sil.clicked.connect(self.sil_fonk)
        self.ui.push_sil.clicked.connect(self.ara_fonk)
        self.ui.push_guncelle.clicked.connect(self.guncelle_fonk)
        self.ui.push_guncelle.clicked.connect(self.ara_fonk)
        self.ui.push_kaydet.clicked.connect(self.kaydet_fonk)
        self.ui.push_kaydet.clicked.connect(self.ara_fonk)
        self.ui.tableWidget.doubleClicked.connect(self.get_info_fonk)
        self.ui.tableWidget.doubleClicked.connect(self.ara_fonk)
            


    def open_bul(self):
        self.b = bul(self)
        self.b.show()
        
    def yeni_fonk(self):
        self.ui.line_ad.setText("")
        self.ui.line_soyad.setText("")
        self.ui.line_TC.setText("")
        self.ui.line_eposta.setText("")
        self.ui.line_dogum.setText("")
        self.ui.line_kullanici_id.setText("")
        self.ui.line_adres.setText("")
        self.ui.line_meslek.setText("")
        self.ui.comboBox_ehliyet.setCurrentIndex(0)
        self.ui.line_medeni_durum.setText("")
        self.ui.comboBox_egitim.setCurrentIndex(0)
        self.ui.line_telefon.setText("")
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)
        
    
    def sil_fonk(self):
        result=self.mesaj("Silmek İstediğinize Emin Misiniz?")
        if result==QMessageBox.Yes:
            id=int (self.ui.line_kullanici_id.text())
            self.mainWindow.mycursor.execute(f"""
                                    DELETE FROM `{self.mainWindow.target_db}`.`musteriler` 
                                    WHERE (`id` = '{id}');""")
            self.ui.push_sil.setEnabled(False)
            self.mainWindow.dbConn.commit()
            self.ara_fonk()
            
        else:
            pass
    
    
    def guncelle_fonk(self):
        id = int(self.ui.line_kullanici_id.text())
        ad = self.ui.line_ad.text()
        soyad = self.ui.line_soyad.text()
        tc = self.ui.line_TC.text()
        dogum_tarihi = self.ui.line_dogum.text()
        adres = self.ui.line_adres.text()
        telefon = self.ui.line_telefon.text()
        meslek = self.ui.line_meslek.text()
        ehliyet = self.ui.comboBox_ehliyet.currentIndex()
        medenidurum = self.ui.line_medeni_durum.text()
        egitim_durum = self.ui.comboBox_egitim.currentIndex()
        e_posta = self.ui.line_eposta.text()

        sorgu = f"""
            UPDATE `{self.mainWindow.target_db}`.`musteriler` SET
            `ad` = %s,
            `soyad` = %s,
            `tc` = %s,
            `dogum_tarihi` = %s,
            `adres` = %s,
            `telefon` = %s,
            `meslek` = %s,
            `ehliyet` = %s,
            `medenidurum` = %s,
            `egitim_durum` = %s,
            `e_posta` = %s
            WHERE `id` = %s;
        """
        degerler = (ad, soyad, tc, dogum_tarihi, adres, telefon, meslek, ehliyet, medenidurum, egitim_durum, e_posta, id)

        self.mainWindow.mycursor.execute(sorgu, degerler)
        self.mainWindow.dbConn.commit()
        self.ui.push_guncelle.setEnabled(False)
        self.ara_fonk()

    
    def kaydet_fonk(self):
        if(self.ui.line_kullanici_id.text()!=""):
            result=self.mesaj("Bu kayıt zaten mevcut. Güncellemek ister misiniz?")
            if (result==QMessageBox.Yes):
                self.guncelle_fonk()
            else:
                pass
        else:
            sqlBaglan = """
            INSERT INTO musteriler
            (id, ad, soyad, tc, dogum_tarihi, adres, telefon, meslek, ehliyet, medenidurum, egitim_durum, e_posta)
            VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.veri = (

                self.ui.line_ad.text(),
                self.ui.line_soyad.text(),
                self.ui.line_TC.text(),
                self.ui.line_dogum.text(),
                self.ui.line_adres.text(),
                self.ui.line_telefon.text(),
                self.ui.line_meslek.text(),
                self.ui.comboBox_ehliyet.currentIndex(),
                self.ui.line_medeni_durum.text(),
                self.ui.comboBox_egitim.currentIndex(),
                self.ui.line_eposta.text()
                )


            self.mainWindow.mycursor.execute(sqlBaglan,self.veri)
            self.mainWindow.dbConn.commit()

    
    def get_info_fonk(self):
        self.ui.push_sil.setEnabled(True)
        self.ui.push_guncelle.setEnabled(True)
        self.cell_changed_fonk()
                 
    
    def cell_changed_fonk(self):
        row_sec=int(self.ui.tableWidget.currentRow())
        if(row_sec>=0):
            self.ui.line_kullanici_id.setText(str(self.ui.tableWidget.item(row_sec,0).text()))
            self.ui.line_ad.setText(str(self.ui.tableWidget.item(row_sec,1).text()))
            self.ui.line_soyad.setText(str(self.ui.tableWidget.item(row_sec,2).text()))
            self.ui.line_TC.setText(str(self.ui.tableWidget.item(row_sec,3).text()))
            self.ui.line_dogum.setText(str(self.ui.tableWidget.item(row_sec,4).text()))
            self.ui.line_adres.setText(str(self.ui.tableWidget.item(row_sec,5).text()))
            self.ui.line_telefon.setText(str(self.ui.tableWidget.item(row_sec,6).text()))
            self.ui.line_meslek.setText(str(self.ui.tableWidget.item(row_sec,7).text()))
            self.ui.comboBox_ehliyet.setCurrentIndex(int(self.ui.tableWidget.item(row_sec,8).text()))
            self.ui.line_medeni_durum.setText(str(self.ui.tableWidget.item(row_sec,9).text()))
            self.ui.comboBox_egitim.setCurrentIndex(int(self.ui.tableWidget.item(row_sec,10).text()))
            self.ui.line_eposta.setText(str(self.ui.tableWidget.item(row_sec,11).text()))
            
    
    def mesaj(self, metin):
        self.messagebox = QMessageBox()
        self.messagebox.setText(metin)
        self.messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.messagebox.setDefaultButton(QMessageBox.Cancel)
        return self.messagebox.exec()
    
    def ara_fonk(self):
        self.mainWindow.mycursor.execute(f"SELECT * FROM `{self.mainWindow.target_db}`.`musteriler`;")
        self.table_doldur()
        
    def table_doldur(self):
        araTable = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.ui.tableWidget.setRowCount(len(araTable))
        if(araTable!=[]):
            for x in range(len(araTable)):
                item_id = QTableWidgetItem(str(araTable[x][0]))
                item_ad = QTableWidgetItem(str(araTable[x][1]))
                item_soyad = QTableWidgetItem(str(araTable[x][2]))
                item_TC = QTableWidgetItem(str(araTable[x][3]))
                item_eposta = QTableWidgetItem(str(araTable[x][4]))
                item_dogum = QTableWidgetItem(str(araTable[x][5]))
                item_adres = QTableWidgetItem(str(araTable[x][6]))
                item_telefon = QTableWidgetItem(str(araTable[x][7]))
                item_meslek = QTableWidgetItem(str(araTable[x][8]))
                item_ehliyet = QTableWidgetItem(str(araTable[x][9]))
                item_medeni_durum = QTableWidgetItem(str(araTable[x][10]))
                item_egitim = QTableWidgetItem(str(araTable[x][11]))
                self.ui.tableWidget.setItem(x,0, item_id)
                self.ui.tableWidget.setItem(x,1, item_ad)
                self.ui.tableWidget.setItem(x,2, item_soyad)
                self.ui.tableWidget.setItem(x,3, item_TC)
                self.ui.tableWidget.setItem(x,4, item_eposta)
                self.ui.tableWidget.setItem(x,5, item_dogum)
                self.ui.tableWidget.setItem(x,6, item_adres)
                self.ui.tableWidget.setItem(x,7, item_telefon)
                self.ui.tableWidget.setItem(x,8, item_meslek)
                self.ui.tableWidget.setItem(x,9, item_ehliyet)
                self.ui.tableWidget.setItem(x,10, item_medeni_durum)
                self.ui.tableWidget.setItem(x,11, item_egitim)
                
    
class bul(QWidget):
    def __init__(self, musteriler):
        super().__init__()
        self.ui = Ui_Bul()
        self.ui.setupUi(self)
        self.musteriler = musteriler
        self.ui.push_bul.clicked.connect(self.arama_fonk)
    

    def arama_fonk(self):
        self.ad=self.ui.line_ad.text()
        self.soyad=self.ui.line_soyad.text()
        self.tc=self.ui.line_TC.text()
        self.dogum=self.ui.line_dogum.text()
        self.telefon=self.ui.line_telefon.text()
        self.e_posta=self.ui.line_eposta.text()
        
        
        query = f"SELECT * FROM {self.musteriler.mainWindow.target_db}.musteriler WHERE 1"
        
        if(self.ad!=""):
            query += f" AND ad LIKE '%{self.ad}%'"
        
        if(self.soyad!=""):
            query += f" AND soyad LIKE '%{self.soyad}%'"
        
        if(self.tc!=""):
            query += f" AND tc LIKE '%{self.tc}%'"
        
        if(self.dogum!=""):
            query += f" AND dogum_tarihi LIKE '%{self.dogum}%'"
            
        if(self.telefon!=""):
            query += f" AND telefon LIKE '%{self.telefon}%'"
            
        if(self.e_posta!=""):
            query += f" AND e_posta LIKE '%{self.e_posta}%'"
            
        self.musteriler.mainWindow.mycursor.execute(query)
        
        self.musteriler.table_doldur()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec())
