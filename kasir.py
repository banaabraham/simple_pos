# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kasir_2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import dbhandler
import send_mail
import sys

DATABASE = 'mayam.db'
TABLE = 'pelanggan'

class login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(213, 153)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 2, 3)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.password, 3, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setObjectName("login")
        self.verticalLayout_3.addWidget(self.login)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 1, 2, 2)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Dialog = Dialog
        self.login.clicked.connect(self.verify)

    def verify(self):
        if self.username.text()=="kasir" and self.password.text()=="password":
            self.Dialog.accept()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('username atau password salah')
            msg.setWindowTitle('Failed')
            msg.exec_()
            
                        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Kasir"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.login.setText(_translate("Dialog", "Login"))


class send_email(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(304, 115)
        self.formLayout_3 = QtWidgets.QFormLayout(Dialog)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.formLayout_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label)
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setObjectName("email")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.email)
        self.send = QtWidgets.QPushButton(Dialog)
        self.send.setObjectName("send")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.send)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.send.clicked.connect(self.sendDB)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kirim Database"))
        self.label.setText(_translate("Dialog", "Email:"))
        self.send.setText(_translate("Dialog", "Send"))

    def sendDB(self):
        db = dbhandler.dbhandler(DATABASE)
        revenue = db.show_daily_revenue(TABLE)
        db.close()
        emailfrom = "bana.abraham@gmail.com"
        emailto = str(self.email.text())
        fileToSend = "mayam.db"
        username = "bana.abraham"
        password = "julisabana"
        subject = "Laporan, Today Revenue: Rp %s,00" %(str(revenue))
        message = "Revenue: %s" %(str(revenue))
        try:
            send_mail.send_mail(emailfrom,emailto,fileToSend,username,password,subject,message)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('berhasil terkirim')
            msg.setWindowTitle('Success')
            msg.exec_()
        except :
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('gagal terkirim')
            msg.setWindowTitle('Failed')
            msg.exec_()
                

class warningDB(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 100)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning"))
        self.label.setText(_translate("Dialog", "\tApakah anda yakin?"))

               

class Ui_MainWindow(object):
    def __init__(self):
        self.jumlahHarga = []
        self.usedRow = 0
        self.pesanan = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setObjectName("total")
        self.total.setReadOnly(True)
        self.gridLayout_4.addWidget(self.total, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 2, 1, 1)
        self.kembalian = QtWidgets.QLineEdit(self.centralwidget)
        self.kembalian.setObjectName("kembalian")
        self.kembalian.setReadOnly(True)
        self.gridLayout_4.addWidget(self.kembalian, 5, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 5, 1, 1, 2)
        self.dibayar = QtWidgets.QLineEdit(self.centralwidget)
        self.dibayar.setObjectName("dibayar")
        self.gridLayout_4.addWidget(self.dibayar, 4, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 4, 1, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_4.addWidget(self.tableWidget, 1, 2, 1, 7)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 3, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 7, 1, 1)
        self.inputJumlah = QtWidgets.QLineEdit(self.centralwidget)
        self.inputJumlah.setObjectName("inputJumlah")
        self.gridLayout_4.addWidget(self.inputJumlah, 3, 8, 1, 1)
        
        """
        Only int validator 
        """
        self.onlyInt = QtGui.QIntValidator()
        self.inputJumlah.setValidator(self.onlyInt)
        
        self.tambah = QtWidgets.QPushButton(self.centralwidget)
        self.tambah.setObjectName("tambah")
        self.gridLayout_4.addWidget(self.tambah, 4, 5, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 2, 9)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 4, 1, 1)
        self.inputItem = QtWidgets.QLineEdit(self.centralwidget)
        self.inputItem.setObjectName("inputItem")
        self.gridLayout_4.addWidget(self.inputItem, 3, 6, 1, 1)
        self.hitung_total = QtWidgets.QPushButton(self.centralwidget)
        self.hitung_total.setObjectName("hitung_total")
        self.gridLayout_4.addWidget(self.hitung_total, 4, 6, 1, 1)
        self.checkOut = QtWidgets.QPushButton(self.centralwidget)
        self.checkOut.setObjectName("checkOut")
        self.gridLayout_4.addWidget(self.checkOut, 5, 5, 1, 1)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setObjectName("clear")
        self.gridLayout_4.addWidget(self.clear, 5, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClear_DB = QtWidgets.QAction(MainWindow)
        self.actionClear_DB.setObjectName("actionClear_DB")
        self.menuMenu.addAction(self.actionClear_DB)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.actionSend_DB = QtWidgets.QAction(MainWindow)
        self.actionSend_DB.setObjectName("actionSend_DB")
        self.menuMenu.addAction(self.actionSend_DB)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """
        inisialisasi
        """
        self.dibayar.setText("0")
        self.total.setText("0")
        
        self.kembalian.setText(str(int(self.dibayar.text())-int(self.total.text())))

        """
        pussButton handler
        """
        
        self.tambah.clicked.connect(self.addRow)
        self.hitung_total.clicked.connect(self.hitung)
        self.checkOut.clicked.connect(self.cetak)
        self.clear.clicked.connect(self.hapus)

        """
        action handler
        """
        self.actionClear_DB.triggered.connect(self.warningForm)
        self.actionSend_DB.triggered.connect(self.sendDB)

    def sendDB(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = send_email()
        dialog.ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()
    
    def warningForm(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = warningDB()
        dialog.ui.setupUi(dialog)
        dialog.show()        
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.hapusDB()
               
                      
        
    def hapusDB(self):
        db = dbhandler.dbhandler(DATABASE)
        db.delete_all(TABLE)
        
    def hitung_harga(self,item):
        f = open('harga.csv','r')
        
        price = dict()
        for i in f:
            temp = i.split(",")
            price[temp[0]] = temp[1]
    
        return price[item] 

    def addRow(self):
        try:
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
            item = self.inputItem.text()
            jumlah = self.inputJumlah.text()
            self.pesanan.append(str(item)+" "+str(jumlah))
            harga = self.hitung_harga(item)
            jumlah_harga = int(jumlah)*int(harga)           
            data = [str(item),str(jumlah),str(harga),str(jumlah_harga)]
            self.jumlahHarga.append(jumlah_harga)
            for i in range(4):
                item = QtWidgets.QTableWidgetItem()
                if data[i]==None:
                    item.setText("-")
                else:
                    item.setText(data[i])
                self.tableWidget.setItem(self.usedRow,i,item)
            self.usedRow +=1
            self.inputItem.clear()
            self.inputJumlah.clear()
        except:
            self.pesanan.pop()
            self.tableWidget.setRowCount(self.tableWidget.rowCount()-1)
            self.inputItem.clear()
            self.inputJumlah.clear()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Item tidak ditemukan!')
            msg.setWindowTitle('Failed')
            msg.exec_()

    def hitung(self):
        total = sum(self.jumlahHarga)
        self.total.setText(str(total))

    def cetak(self):
        total = int(self.total.text())
        dibayar = int(self.dibayar.text())
        self.kembalian.setText(str(dibayar-total))

    def write_db(self):
        db = dbhandler.dbhandler(DATABASE)
        db.insert_value(TABLE,self.pesanan,sum(self.jumlahHarga))
        self.pesanan = []
        self.jumlahHarga = []
        db.close()
        
    def hapus(self):
        self.write_db()
        self.total.clear()
        self.kembalian.clear()
        self.dibayar.clear()
        self.usedRow = 0
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)
            
           

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kasir"))
        self.label_3.setText(_translate("MainWindow", "TOTAL: "))
        self.label_5.setText(_translate("MainWindow", "KEMBALI:"))
        self.label_4.setText(_translate("MainWindow", "DIBAYAR:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Jumlah"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Harga"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Jumlah Harga"))
        self.label.setText(_translate("MainWindow", "        Item"))
        self.label_2.setText(_translate("MainWindow", "jumlah"))
        self.tambah.setText(_translate("MainWindow", "Tambah"))
        self.hitung_total.setText(_translate("MainWindow", "Hitung Total"))
        self.checkOut.setText(_translate("MainWindow", "Checkout"))
        self.clear.setText(_translate("MainWindow", "Submit + Clear"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionClear_DB.setText(_translate("MainWindow", "Clear DB"))
        self.actionSend_DB.setText(_translate("MainWindow","Send DB"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    dialog.ui = login()
    dialog.ui.setupUi(dialog)
    dialog.show()        
    if dialog.exec_() == QtWidgets.QDialog.Accepted:     
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


