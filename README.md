# Rent-that-car
This is a prototype car rental software developed using QtPy. Nothing so fancy, just a simple demo.

# (Turkish)
# Araç Kiralama Yönetim Sistemi

Bu proje, araç kiralama işlemlerini dijitalleştirmek ve yönetmek için tasarlanmış bir masaüstü uygulamasıdır. Müşteri kayıtları, araç envanteri ve kiralama süreçlerini kolaylaştırır.


## Özellikler 
- **Müşteri Yönetimi**: TCKN, iletişim bilgileri ve ehliyet durumuyla müşteri kaydı.
- **Araç Envanteri**: Marka, model, plaka ve kira bedeli gibi detaylarla araç ekleme.
- **Kiralama İşlemleri**: Tarih bazlı kiralama, süre uzatma ve iade takibi.
- **Raporlama**: Aktif kiralamalar ve geçmiş işlemler için anlık görüntüleme.

## Teknolojiler 
- **Python 3.9+**: Temel programlama dili.
- **PySide6**: Kullanıcı arayüzü geliştirme.
- **MySQL**: Veritabanı yönetimi.
- **SQL Sorguları**: Veri depolama ve işleme.

## Kurulum 
1. **Gereksinimler**:
   - Python 3.9+ ve pip.
   - MySQL sunucusu (XAMPP/MAMP veya standalone).

   ### *Bağımlılıkları yükle
   pip install PySide6 mysql-connector-python

   ### *Veritabanını ayarla
   #### 1. mainwindow.py dosyasında MySQL bağlantı bilgilerini düzenleyin:
   ####    host="localhost", user="root", password=""
   #### 2. Uygulamayı çalıştırdığınızda, belirttiğiniz isimdeki veritabanı otomatik olarak oluşturulacaktır.
   ####    Veritabanı adını mainwindow.py dosyasındaki `target_db` değişkeninde belirtebilirsiniz.


   # (English)
   # Vehicle Rental Management System

This project is a desktop application designed to digitize and manage vehicle rental processes. It simplifies customer records, vehicle inventory, and rental operations.

## Features
- **Customer Management**: Track customers with ID, contact info, and driver's license status.
- **Vehicle Inventory**: Add vehicles with details like brand, model, plate, and daily rent.
- **Rental Operations**: Date-based rentals, extension, and return tracking.
- **Reporting**: Real-time overview of active rentals and history.

## Technologies 
- **Python 3.9+**: Core programming language.
- **PySide6**: GUI development.
- **MySQL**: Database management.
- **SQL Queries**: Data storage and processing.

## Installation 
1. **Prerequisites**:
   - Python 3.9+ and pip.
   - MySQL server (XAMPP/MAMP or standalone).

   ### *Install Dependencies
   pip install PySide6 mysql-connector-python

   ### *Set Up the Database
   #### 1. Update MySQL connection details in mainwindow.py:
   ####    host="localhost", user="root", password=""
   #### 2. When you run the application, the database with the specified name will be created automatically.
   ####    You can specify the database name in the `target_db` variable in mainwindow.py.
