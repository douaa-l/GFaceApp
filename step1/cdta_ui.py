# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cdta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        MainWindow.setMaximumSize(QtCore.QSize(1400, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1400, 900))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.full_menu = QtWidgets.QFrame(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full_menu.sizePolicy().hasHeightForWidth())
        self.full_menu.setSizePolicy(sizePolicy)
        self.full_menu.setMinimumSize(QtCore.QSize(160, 0))
        self.full_menu.setMaximumSize(QtCore.QSize(200, 900))
        self.full_menu.setAutoFillBackground(False)
        self.full_menu.setStyleSheet("background-color: rgb(36, 40, 59);")
        self.full_menu.setObjectName("full_menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.full_menu)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon = QtWidgets.QLabel(self.full_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QtCore.QSize(200, 100))
        self.icon.setMaximumSize(QtCore.QSize(80, 80))
        self.icon.setStyleSheet("image: url(:/images/Logo.png);background-color:rgb(36, 40, 59);padding:5px;border:none;\n"
"")
        self.icon.setText("")
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout.addWidget(self.icon)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.degradation_btn = QtWidgets.QPushButton(self.full_menu)
        self.degradation_btn.setStyleSheet("QPushButton{color: rgb(255, 255, 255);font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ajouter (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.degradation_btn.setIcon(icon)
        self.degradation_btn.setCheckable(True)
        self.degradation_btn.setChecked(False)
        self.degradation_btn.setObjectName("degradation_btn")
        self.verticalLayout.addWidget(self.degradation_btn)
        self.restoration_btn = QtWidgets.QPushButton(self.full_menu)
        self.restoration_btn.setStyleSheet("QPushButton{color: rgb(255, 255, 255);font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/identifiant-du-visage 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoration_btn.setIcon(icon1)
        self.restoration_btn.setCheckable(True)
        self.restoration_btn.setChecked(True)
        self.restoration_btn.setObjectName("restoration_btn")
        self.verticalLayout.addWidget(self.restoration_btn)
        self.verticalWidget = QtWidgets.QWidget(self.full_menu)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pairs_rest_btn = QtWidgets.QPushButton(self.verticalWidget)
        self.pairs_rest_btn.setStyleSheet("QPushButton{color: \"grey\";font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}")
        self.pairs_rest_btn.setObjectName("pairs_rest_btn")
        self.verticalLayout_3.addWidget(self.pairs_rest_btn)
        self.folds_rest_btn = QtWidgets.QPushButton(self.verticalWidget)
        self.folds_rest_btn.setStyleSheet("QPushButton{color:\"grey\";font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}")
        self.folds_rest_btn.setObjectName("folds_rest_btn")
        self.verticalLayout_3.addWidget(self.folds_rest_btn)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.verification = QtWidgets.QPushButton(self.full_menu)
        self.verification.setStyleSheet("QPushButton{color: rgb(255, 255, 255);font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Correct.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verification.setIcon(icon2)
        self.verification.setCheckable(True)
        self.verification.setChecked(True)
        self.verification.setObjectName("verification")
        self.verticalLayout.addWidget(self.verification)
        self.verticalWidget_2 = QtWidgets.QWidget(self.full_menu)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pairs_verif_btn = QtWidgets.QPushButton(self.verticalWidget_2)
        self.pairs_verif_btn.setStyleSheet("QPushButton{color:\"grey\";font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}")
        self.pairs_verif_btn.setObjectName("pairs_verif_btn")
        self.verticalLayout_4.addWidget(self.pairs_verif_btn)
        self.folds_verif_btn = QtWidgets.QPushButton(self.verticalWidget_2)
        self.folds_verif_btn.setStyleSheet("QPushButton{color:\"grey\";font-size:8pt; font-weight:bold;font-family: Georama;border:none; height: 30px}\n"
"QPushButton:hover{background-color:rgb(28, 142, 178);}")
        self.folds_verif_btn.setObjectName("folds_verif_btn")
        self.verticalLayout_4.addWidget(self.folds_verif_btn)
        self.verticalLayout.addWidget(self.verticalWidget_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.full_menu)
        self.principalscreen = QtWidgets.QWidget(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.principalscreen.sizePolicy().hasHeightForWidth())
        self.principalscreen.setSizePolicy(sizePolicy)
        self.principalscreen.setMinimumSize(QtCore.QSize(0, 0))
        self.principalscreen.setMaximumSize(QtCore.QSize(1200, 900))
        self.principalscreen.setStyleSheet("background-color: rgb(35, 33, 40);")
        self.principalscreen.setObjectName("principalscreen")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.principalscreen)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.principalscreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(830, 600))
        self.frame.setMaximumSize(QtCore.QSize(1200, 900))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(830, 600))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1200, 900))
        self.stackedWidget.setStyleSheet("background-color: rgb(35, 33, 40);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.degradationpage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.degradationpage.sizePolicy().hasHeightForWidth())
        self.degradationpage.setSizePolicy(sizePolicy)
        self.degradationpage.setStyleSheet("background-color: rgb(35, 33, 40);")
        self.degradationpage.setObjectName("degradationpage")
        self.right_menu_deg = QtWidgets.QFrame(self.degradationpage)
        self.right_menu_deg.setGeometry(QtCore.QRect(1000, 0, 200, 900))
        self.right_menu_deg.setStyleSheet("background-color: rgb(36, 40, 59);")
        self.right_menu_deg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_menu_deg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_menu_deg.setObjectName("right_menu_deg")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.right_menu_deg)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.right_menu_deg)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/reglages.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.right_menu_deg)
        self.label_5.setStyleSheet("background-color: \"transparent\";\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";\n"
"padding-right:20px")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.noisecheckBox = QtWidgets.QCheckBox(self.right_menu_deg)
        self.noisecheckBox.setStyleSheet("background-color: \"transparent\";\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";\n"
"padding-top:20px")
        self.noisecheckBox.setObjectName("noisecheckBox")
        self.verticalLayout_5.addWidget(self.noisecheckBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.right_menu_deg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(60, 50))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.meannoise = QtWidgets.QLineEdit(self.right_menu_deg)
        self.meannoise.setEnabled(False)
        self.meannoise.setMinimumSize(QtCore.QSize(100, 30))
        self.meannoise.setMaximumSize(QtCore.QSize(100, 30))
        self.meannoise.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;\n"
"")
        self.meannoise.setMaxLength(6)
        self.meannoise.setObjectName("meannoise")
        self.horizontalLayout_4.addWidget(self.meannoise)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.right_menu_deg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(60, 30))
        self.label_3.setMaximumSize(QtCore.QSize(60, 50))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.stdnoise = QtWidgets.QLineEdit(self.right_menu_deg)
        self.stdnoise.setEnabled(False)
        self.stdnoise.setMaximumSize(QtCore.QSize(100, 30))
        self.stdnoise.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;\n"
"")
        self.stdnoise.setMaxLength(6)
        self.stdnoise.setObjectName("stdnoise")
        self.horizontalLayout_7.addWidget(self.stdnoise)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.blurcheckbox = QtWidgets.QCheckBox(self.right_menu_deg)
        self.blurcheckbox.setStyleSheet("background-color: \"transparent\";\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";\n"
"padding-top:20px")
        self.blurcheckbox.setObjectName("blurcheckbox")
        self.verticalLayout_5.addWidget(self.blurcheckbox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.right_menu_deg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(60, 50))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.blurvalue = QtWidgets.QLineEdit(self.right_menu_deg)
        self.blurvalue.setEnabled(False)
        self.blurvalue.setMinimumSize(QtCore.QSize(100, 30))
        self.blurvalue.setMaximumSize(QtCore.QSize(100, 30))
        self.blurvalue.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;\n"
"")
        self.blurvalue.setMaxLength(3)
        self.blurvalue.setObjectName("blurvalue")
        self.horizontalLayout_5.addWidget(self.blurvalue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.lrcheckbox = QtWidgets.QCheckBox(self.right_menu_deg)
        self.lrcheckbox.setStyleSheet("background-color: \"transparent\";\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";\n"
"padding-top:20px")
        self.lrcheckbox.setObjectName("lrcheckbox")
        self.verticalLayout_5.addWidget(self.lrcheckbox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.right_menu_deg)
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.lowresvalue = QtWidgets.QLineEdit(self.right_menu_deg)
        self.lowresvalue.setEnabled(False)
        self.lowresvalue.setMinimumSize(QtCore.QSize(100, 30))
        self.lowresvalue.setMaximumSize(QtCore.QSize(100, 30))
        self.lowresvalue.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;\n"
"")
        self.lowresvalue.setInputMask("")
        self.lowresvalue.setMaxLength(4)
        self.lowresvalue.setObjectName("lowresvalue")
        self.horizontalLayout_6.addWidget(self.lowresvalue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.compressioncheckbox = QtWidgets.QCheckBox(self.right_menu_deg)
        self.compressioncheckbox.setEnabled(False)
        self.compressioncheckbox.setStyleSheet("background-color: \"transparent\";\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";\n"
"padding-top:20px\n"
"")
        self.compressioncheckbox.setObjectName("compressioncheckbox")
        self.verticalLayout_5.addWidget(self.compressioncheckbox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.right_menu_deg)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.compressionvalue = QtWidgets.QLineEdit(self.right_menu_deg)
        self.compressionvalue.setEnabled(False)
        self.compressionvalue.setMaximumSize(QtCore.QSize(100, 30))
        self.compressionvalue.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:10px;")
        self.compressionvalue.setObjectName("compressionvalue")
        self.horizontalLayout_8.addWidget(self.compressionvalue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.degradationpage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 999, 851))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.controlspace_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlspace_2.sizePolicy().hasHeightForWidth())
        self.controlspace_2.setSizePolicy(sizePolicy)
        self.controlspace_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.controlspace_2.setObjectName("controlspace_2")
        self.controlspace = QtWidgets.QHBoxLayout(self.controlspace_2)
        self.controlspace.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.controlspace.setObjectName("controlspace")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.controlspace.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.controlspace_2)
        self.label.setMaximumSize(QtCore.QSize(70, 50))
        self.label.setStyleSheet("padding-left:20px")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/identifiant-du-visage 1.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.controlspace.addWidget(self.label)
        self.deglabel = QtWidgets.QLabel(self.controlspace_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deglabel.sizePolicy().hasHeightForWidth())
        self.deglabel.setSizePolicy(sizePolicy)
        self.deglabel.setMinimumSize(QtCore.QSize(0, 0))
        self.deglabel.setMaximumSize(QtCore.QSize(1200, 70))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.deglabel.setFont(font)
        self.deglabel.setStyleSheet("background-color: \"transparent\";\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.deglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deglabel.setObjectName("deglabel")
        self.controlspace.addWidget(self.deglabel)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.controlspace.addItem(spacerItem5)
        self.verticalLayout_9.addWidget(self.controlspace_2)
        self.buttonsspace = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.buttonsspace.setMaximumSize(QtCore.QSize(16777215, 150))
        self.buttonsspace.setObjectName("buttonsspace")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttonsspace)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_random_deg_btn = QtWidgets.QPushButton(self.buttonsspace)
        self.select_random_deg_btn.setMaximumSize(QtCore.QSize(200, 40))
        self.select_random_deg_btn.setStyleSheet("border-radius: 10px;color:rgb(255, 255, 255);\n"
"font: 75 10pt \"Georgia\";\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.628821 rgba(105, 85, 163, 255), stop:1 rgba(231, 235, 244, 255));")
        self.select_random_deg_btn.setObjectName("select_random_deg_btn")
        self.horizontalLayout_2.addWidget(self.select_random_deg_btn)
        self.apply_deg_btn = QtWidgets.QPushButton(self.buttonsspace)
        self.apply_deg_btn.setEnabled(False)
        self.apply_deg_btn.setMaximumSize(QtCore.QSize(200, 40))
        self.apply_deg_btn.setStyleSheet("background-color: rgb(170, 170, 170);border-radius: 10px;color:rgb(255, 255, 255);\n"
"font: 75 10pt \"Georgia\";")
        self.apply_deg_btn.setObjectName("apply_deg_btn")
        self.horizontalLayout_2.addWidget(self.apply_deg_btn)
        self.verticalLayout_9.addWidget(self.buttonsspace)
        self.imagesspace_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.imagesspace_2.setObjectName("imagesspace_2")
        self.imagesspace = QtWidgets.QHBoxLayout(self.imagesspace_2)
        self.imagesspace.setObjectName("imagesspace")
        self.verticalLayout_9.addWidget(self.imagesspace_2)
        self.stackedWidget.addWidget(self.degradationpage)
        self.pairrestorationpage = QtWidgets.QWidget()
        self.pairrestorationpage.setObjectName("pairrestorationpage")
        self.pairsrestlabel = QtWidgets.QLabel(self.pairrestorationpage)
        self.pairsrestlabel.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pairsrestlabel.sizePolicy().hasHeightForWidth())
        self.pairsrestlabel.setSizePolicy(sizePolicy)
        self.pairsrestlabel.setMaximumSize(QtCore.QSize(1200, 900))
        self.pairsrestlabel.setStyleSheet("background-color: rgb(35, 33, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Georgia\";")
        self.pairsrestlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pairsrestlabel.setObjectName("pairsrestlabel")
        self.stackedWidget.addWidget(self.pairrestorationpage)
        self.foldsrestorationpage = QtWidgets.QWidget()
        self.foldsrestorationpage.setObjectName("foldsrestorationpage")
        self.foldrestlabel = QtWidgets.QLabel(self.foldsrestorationpage)
        self.foldrestlabel.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foldrestlabel.sizePolicy().hasHeightForWidth())
        self.foldrestlabel.setSizePolicy(sizePolicy)
        self.foldrestlabel.setMaximumSize(QtCore.QSize(1200, 900))
        self.foldrestlabel.setStyleSheet("background-color: rgb(35, 33, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Georgia\";")
        self.foldrestlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.foldrestlabel.setObjectName("foldrestlabel")
        self.stackedWidget.addWidget(self.foldsrestorationpage)
        self.pairsverifpage = QtWidgets.QWidget()
        self.pairsverifpage.setObjectName("pairsverifpage")
        self.pairsveriflabel = QtWidgets.QLabel(self.pairsverifpage)
        self.pairsveriflabel.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pairsveriflabel.sizePolicy().hasHeightForWidth())
        self.pairsveriflabel.setSizePolicy(sizePolicy)
        self.pairsveriflabel.setMaximumSize(QtCore.QSize(1200, 900))
        self.pairsveriflabel.setStyleSheet("background-color: rgb(35, 33, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Georgia\";")
        self.pairsveriflabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pairsveriflabel.setObjectName("pairsveriflabel")
        self.stackedWidget.addWidget(self.pairsverifpage)
        self.foldsverifpage = QtWidgets.QWidget()
        self.foldsverifpage.setObjectName("foldsverifpage")
        self.foldsveriflabel = QtWidgets.QLabel(self.foldsverifpage)
        self.foldsveriflabel.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foldsveriflabel.sizePolicy().hasHeightForWidth())
        self.foldsveriflabel.setSizePolicy(sizePolicy)
        self.foldsveriflabel.setMaximumSize(QtCore.QSize(1200, 900))
        self.foldsveriflabel.setStyleSheet("background-color: rgb(35, 33, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Georgia\";")
        self.foldsveriflabel.setAlignment(QtCore.Qt.AlignCenter)
        self.foldsveriflabel.setObjectName("foldsveriflabel")
        self.stackedWidget.addWidget(self.foldsverifpage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_7.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.principalscreen)
        self.verticalLayout_8.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.restoration_btn.toggled['bool'].connect(self.verticalWidget.setVisible) # type: ignore
        self.verification.toggled['bool'].connect(self.verticalWidget_2.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.degradation_btn.setText(_translate("MainWindow", "Degradation"))
        self.restoration_btn.setText(_translate("MainWindow", "Restoration"))
        self.pairs_rest_btn.setText(_translate("MainWindow", "Pairs"))
        self.folds_rest_btn.setText(_translate("MainWindow", "Folds"))
        self.verification.setText(_translate("MainWindow", "Verification"))
        self.pairs_verif_btn.setText(_translate("MainWindow", "Pairs"))
        self.folds_verif_btn.setText(_translate("MainWindow", "Folds"))
        self.label_5.setText(_translate("MainWindow", "Settings"))
        self.noisecheckBox.setText(_translate("MainWindow", "Noise"))
        self.label_6.setText(_translate("MainWindow", "mean"))
        self.label_3.setText(_translate("MainWindow", "std"))
        self.blurcheckbox.setText(_translate("MainWindow", "Blur"))
        self.label_7.setText(_translate("MainWindow", "kernel size"))
        self.lrcheckbox.setText(_translate("MainWindow", "Low Resolution"))
        self.label_8.setText(_translate("MainWindow", "scale"))
        self.compressioncheckbox.setText(_translate("MainWindow", "Compression"))
        self.label_4.setText(_translate("MainWindow", "quality"))
        self.deglabel.setText(_translate("MainWindow", "Drop an image from your computer or click on select a random image"))
        self.select_random_deg_btn.setText(_translate("MainWindow", "select a random image"))
        self.apply_deg_btn.setText(_translate("MainWindow", "apply"))
        self.pairsrestlabel.setText(_translate("MainWindow", "Pairs Restoration Page"))
        self.foldrestlabel.setText(_translate("MainWindow", "Folds Restoration Page"))
        self.pairsveriflabel.setText(_translate("MainWindow", "Pairs verification Page"))
        self.foldsveriflabel.setText(_translate("MainWindow", "Folds verification Page"))
import ressources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
