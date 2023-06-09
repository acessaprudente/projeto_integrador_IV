# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appclima.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#imports
import sys
import statistics
import numpy as np
import pandas as pd
from tkinter import Tk
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from statsmodels.tsa.ar_model import AutoReg
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import date
from tkinter.filedialog import askopenfilename

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 862)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_tipoPredicao = QtWidgets.QLabel(self.centralwidget)
        self.lb_tipoPredicao.setMinimumSize(QtCore.QSize(150, 30))
        self.lb_tipoPredicao.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.lb_tipoPredicao.setFont(font)
        self.lb_tipoPredicao.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 87 10pt \"Arial Black\";")
        self.lb_tipoPredicao.setObjectName("lb_tipoPredicao")
        self.gridLayout.addWidget(self.lb_tipoPredicao, 6, 5, 1, 1)
        self.sb_colunas = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_colunas.setMinimumSize(QtCore.QSize(50, 30))
        self.sb_colunas.setMaximumSize(QtCore.QSize(50, 30))
        self.sb_colunas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.sb_colunas.setObjectName("sb_colunas")
        self.gridLayout.addWidget(self.sb_colunas, 5, 4, 1, 1)
        self.bt_predizer = QtWidgets.QPushButton(self.centralwidget)
        self.bt_predizer.setMinimumSize(QtCore.QSize(100, 50))
        self.bt_predizer.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.bt_predizer.setObjectName("bt_predizer")
        self.gridLayout.addWidget(self.bt_predizer, 9, 6, 1, 1)
        self.lb_climaemPresidentePrudente = QtWidgets.QLabel(self.centralwidget)
        self.lb_climaemPresidentePrudente.setMinimumSize(QtCore.QSize(250, 50))
        self.lb_climaemPresidentePrudente.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lb_climaemPresidentePrudente.setFont(font)
        self.lb_climaemPresidentePrudente.setObjectName("lb_climaemPresidentePrudente")
        self.gridLayout.addWidget(self.lb_climaemPresidentePrudente, 5, 0, 1, 1)
        self.bt_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.bt_arquivo.setMinimumSize(QtCore.QSize(100, 50))
        self.bt_arquivo.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.bt_arquivo.setFont(font)
        self.bt_arquivo.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.bt_arquivo.setObjectName("bt_arquivo")
        self.gridLayout.addWidget(self.bt_arquivo, 5, 5, 1, 1)
        self.lb_totalDias = QtWidgets.QLabel(self.centralwidget)
        self.lb_totalDias.setMinimumSize(QtCore.QSize(120, 30))
        self.lb_totalDias.setMaximumSize(QtCore.QSize(120, 30))
        self.lb_totalDias.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.lb_totalDias.setObjectName("lb_totalDias")
        self.gridLayout.addWidget(self.lb_totalDias, 5, 3, 1, 1)
        self.txt_totalDias = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_totalDias.setMinimumSize(QtCore.QSize(200, 30))
        self.txt_totalDias.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txt_totalDias.setFont(font)
        self.txt_totalDias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.txt_totalDias.setText("")
        self.txt_totalDias.setObjectName("txt_totalDias")
        self.gridLayout.addWidget(self.txt_totalDias, 5, 2, 1, 1)
        self.bt_grafico = QtWidgets.QPushButton(self.centralwidget)
        self.bt_grafico.setMinimumSize(QtCore.QSize(100, 50))
        self.bt_grafico.setMaximumSize(QtCore.QSize(100, 50))
        self.bt_grafico.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 87 12pt \"Arial Black\";")
        self.bt_grafico.setObjectName("bt_grafico")
        self.gridLayout.addWidget(self.bt_grafico, 5, 6, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rb_media_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_media_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rb_media_2.setChecked(True)
        self.rb_media_2.setObjectName("rb_media_2")
        self.verticalLayout_2.addWidget(self.rb_media_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.rb_devioPadrao_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_devioPadrao_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rb_devioPadrao_2.setObjectName("rb_devioPadrao_2")
        self.verticalLayout_2.addWidget(self.rb_devioPadrao_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.rb_mediaPonderada_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mediaPonderada_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rb_mediaPonderada_2.setObjectName("rb_mediaPonderada_2")
        self.verticalLayout_2.addWidget(self.rb_mediaPonderada_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.rb_segregacaoDados_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_segregacaoDados_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rb_segregacaoDados_2.setObjectName("rb_segregacaoDados_2")
        self.verticalLayout_2.addWidget(self.rb_segregacaoDados_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.rb_regressaoLinear_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_regressaoLinear_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rb_regressaoLinear_2.setObjectName("rb_regressaoLinear_2")
        self.verticalLayout_2.addWidget(self.rb_regressaoLinear_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.rb_seriesTemporais_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_seriesTemporais_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rb_seriesTemporais_2.setObjectName("rb_seriesTemporais_2")
        self.verticalLayout_2.addWidget(self.rb_seriesTemporais_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 8, 5, 1, 2)
        self.tb_Chuva = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tb_Chuva.setFont(font)
        self.tb_Chuva.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.tb_Chuva.setObjectName("tb_Chuva")
        self.tb_Chuva.setColumnCount(6)
        self.tb_Chuva.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Chuva.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Chuva.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Chuva.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Chuva.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Chuva.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Chuva.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tb_Chuva, 7, 0, 2, 5)
        self.txt_predicao = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_predicao.setMinimumSize(QtCore.QSize(500, 30))
        self.txt_predicao.setMaximumSize(QtCore.QSize(500, 30))
        self.txt_predicao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_predicao.setObjectName("txt_predicao")
        self.gridLayout.addWidget(self.txt_predicao, 9, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_tipoPredicao.setText(_translate("MainWindow", "Tipo de predição"))
        self.bt_predizer.setText(_translate("MainWindow", "Predizer"))
        self.lb_climaemPresidentePrudente.setText(_translate("MainWindow", "Clima em Presidente Prudente"))
        self.bt_arquivo.setText(_translate("MainWindow", "Arquivo"))
        self.lb_totalDias.setText(_translate("MainWindow", "Total Dias"))
        self.bt_grafico.setText(_translate("MainWindow", "Gráfico"))
        self.rb_media_2.setText(_translate("MainWindow", "Média"))
        self.rb_devioPadrao_2.setText(_translate("MainWindow", "Desvio padrão"))
        self.rb_mediaPonderada_2.setText(_translate("MainWindow", "Média ponderada"))
        self.rb_segregacaoDados_2.setText(_translate("MainWindow", "Segregação de dados"))
        self.rb_regressaoLinear_2.setText(_translate("MainWindow", "Regressão Linear"))
        self.rb_seriesTemporais_2.setText(_translate("MainWindow", "Séries temporais"))
        item = self.tb_Chuva.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tb_Chuva.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temp Med"))
        item = self.tb_Chuva.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temp Max"))
        item = self.tb_Chuva.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Temp Min"))
        item = self.tb_Chuva.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Chuva"))
        item = self.tb_Chuva.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "UR"))


        self.bt_predizer.setText(_translate("MainWindow", "Predizer"))
        self.lb_climaemPresidentePrudente.setText(_translate("MainWindow", "Clima em Presidente Prudente"))
        self.bt_arquivo.setText(_translate("MainWindow", "Arquivo"))
        self.lb_totalDias.setText(_translate("MainWindow", "Total Dias"))
        self.bt_grafico.setText(_translate("MainWindow", "Gráfico"))
        self.bt_arquivo.clicked.connect(self.openFile)
        self.bt_predizer.clicked.connect(self.predicao)
        self.bt_grafico.clicked.connect(self.plot)
        
        
    
       
    def openFile(self):
        Tk().withdraw()
        path = askopenfilename()
        self.all_data = pd.read_csv(path)             
        numColumn = self.sb_colunas.value()
        if numColumn == 0:
            numRows = len(self.all_data.index)
        else:
            numRows = numColumn
        self.tb_Chuva.setColumnCount(len(self.all_data.columns))
        self.tb_Chuva.setRowCount(numRows)
        self.tb_Chuva.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tb_Chuva.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i,j])))

        self.tb_Chuva.resizeColumnsToContents()
        self.tb_Chuva.resizeRowsToContents()
        

        # Chuva
        Data = str((self.all_data['Data']))
        self.txt_totalDias.setText(Data)

    def predicao(self):
        df = self.all_data
         ### Média ###
       
        if self.rb_media_2.isChecked() == True:
            df.replace(0, np.nan, inplace = True)
            df['Chuva'] = df['Chuva'].replace(to_replace = np.nan, value = df['Chuva'].mean())
            media = statistics.fmean(df['Chuva'])
            predicao = 'Predicao  de Chuvas para os proximos  dias ' + str('%0.02f' %media) + ' mm em media.'
            self.txt_predicao.setText(predicao)            
        ### Desvio Padrão ###
        elif self.rb_devioPadrao_2.isChecked() == True:
            df.replace(0, np.nan, inplace = True)
            media = statistics.mean(df['Chuva'])
            df['Chuva'] = df['Chuva'].replace(to_replace = np.nan, value = df['Chuva'].mean())
            desvpad = statistics.stdev(df['Chuva'].replace(to_replace = np.nan, value = df['Chuva'].mean()))
            coe_var = ((desvpad / media) * 100)
            predicao = 'Predição de  ' + str('%0.02f' %desvpad) + ' mm podendo variar em torno de ' + str('%0.02f' %coe_var) + '%'
            self.txt_predicao.setText(predicao)
        ### Media Ponderada ###
        elif self.rb_mediaPonderada_2.isChecked() == True:
            lista = np.transpose((np.array([df['Chuva'].tail(), np.arange(1,6)])))
            pesos = np.arange(1,6)
            df_ult = pd.DataFrame(lista, columns = ['Chuvas', 'Pesos'])
            df_ult['Ponderado'] = df_ult['Chuvas'] * df_ult['Pesos']
            med_pond = df_ult['Ponderado'].sum() / df_ult['Pesos'].sum()
            predicao = 'Predição ponderada de ' + str('%0.02f' %med_pond) + ' mm para os próximos meses.'
            self.txt_predicao.setText(predicao)
        ### Segregação dos Dados ###
        elif self.rb_segregacaoDados_2.isChecked() == True:
            df = df_janeiro
            df_janeiro = pd.to_datetime(date['Data'], format='%d/%m/%Y')
            df_janeiro.loc[df['Data'] == 1]
            med_seg = statistics.mean(df_janeiro['Chuva'])
            predicao = 'Predição segregada de ' + str('%0.02f' %med_seg) + ' para janeiro.'
            self.txt_predicao.setText(predicao)
                
        ### Regressão Linear ###
        elif self.rb_regressaoLinear_2.isChecked() == True:
            coefficients = np.polyfit(df.index, df['Chuva'], 1)
            a = coefficients[0]
            b = coefficients[1]
            jan_reta = a * 36 + b
            predicao = 'Predição por regressão de ' + str('%0.02f' %jan_reta) + ' mm para janeiro.'
            self.txt_predicao.setText(predicao)
        ### Series temporais ###
        elif self.rb_seriesTemporais_2.isChecked() == True:
            model = AutoReg(df['Chuva'], lags=1, old_names=True) #old_names só foi utilizado por conta de um aviso da próxima versão
            model_fit = model.fit()
            yhat = model_fit.predict(len(df['Chuva']), len(df['Chuva'])+2)
            pred = np.array(yhat)
            predicao = 'Predição por serie temporal de ' + str('%0.02f' %pred[0]) + ' mm para janeiro e  ' + str('%0.02f' %pred[1]) + ' mm para fevereiro.'
            self.txt_predicao.setText(predicao)
            
        # Gráfico1
        
    def plot (self):
        df = self.all_data
        df.replace(0, np.nan, inplace = True)
        df['Chuva'] = df['Chuva'].replace(to_replace = np.nan, value = df['Chuva'].mean())
        plt.style.use("seaborn")
        plt.figure(figsize=(12, 18))
        plt.subplot(2, 1, 1)      
        x = df["Data"]
        y= df["Chuva"]
        plt.title('Chuvas em Presidente Prudente')
        plt.xlabel('Data')
        plt.ylabel('Chuvas em mm')        
        plt.scatter(x,y,  color='blue' , )
        # Gráfico2        
        plt.subplot(2, 1, 2)     
        x = df["Data"]
        y = df["Chuva"]
        plt.title('Chuvas em Presidente Prudente')
        plt.xlabel('Data')
        plt.ylabel('Chuvas em mm')
        plt.plot(x,y, color='green')
        plt.show()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
