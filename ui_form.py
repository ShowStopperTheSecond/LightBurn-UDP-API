# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(593, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(100, 100))
        Widget.setMaximumSize(QSize(593, 130))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.ip_txt = QLineEdit(Widget)
        self.ip_txt.setObjectName(u"ip_txt")

        self.horizontalLayout_2.addWidget(self.ip_txt)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.out_port_txt = QLineEdit(Widget)
        self.out_port_txt.setObjectName(u"out_port_txt")

        self.horizontalLayout_3.addWidget(self.out_port_txt)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.in_port_txt = QLineEdit(Widget)
        self.in_port_txt.setObjectName(u"in_port_txt")

        self.horizontalLayout_4.addWidget(self.in_port_txt)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.bind_btn = QPushButton(Widget)
        self.bind_btn.setObjectName(u"bind_btn")

        self.horizontalLayout_5.addWidget(self.bind_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.browse_file_btn = QPushButton(Widget)
        self.browse_file_btn.setObjectName(u"browse_file_btn")

        self.horizontalLayout.addWidget(self.browse_file_btn)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.load_file_btn = QPushButton(Widget)
        self.load_file_btn.setObjectName(u"load_file_btn")

        self.horizontalLayout_6.addWidget(self.load_file_btn)

        self.force_load_file_btn = QPushButton(Widget)
        self.force_load_file_btn.setObjectName(u"force_load_file_btn")

        self.horizontalLayout_6.addWidget(self.force_load_file_btn)

        self.close_btn = QPushButton(Widget)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout_6.addWidget(self.close_btn)

        self.force_close_btn = QPushButton(Widget)
        self.force_close_btn.setObjectName(u"force_close_btn")

        self.horizontalLayout_6.addWidget(self.force_close_btn)

        self.start_btn = QPushButton(Widget)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout_6.addWidget(self.start_btn)

        self.status_btn = QPushButton(Widget)
        self.status_btn.setObjectName(u"status_btn")

        self.horizontalLayout_6.addWidget(self.status_btn)

        self.ping_btn = QPushButton(Widget)
        self.ping_btn.setObjectName(u"ping_btn")

        self.horizontalLayout_6.addWidget(self.ping_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.status_lbl = QLabel(Widget)
        self.status_lbl.setObjectName(u"status_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_lbl.sizePolicy().hasHeightForWidth())
        self.status_lbl.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.status_lbl)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"IP:", None))
        self.ip_txt.setText(QCoreApplication.translate("Widget", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"UPD output port: ", None))
        self.out_port_txt.setText(QCoreApplication.translate("Widget", u"19840", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"UDP input port: ", None))
        self.in_port_txt.setText(QCoreApplication.translate("Widget", u"19841", None))
        self.bind_btn.setText(QCoreApplication.translate("Widget", u"Bind", None))
        self.browse_file_btn.setText(QCoreApplication.translate("Widget", u"Browse File", None))
        self.load_file_btn.setText(QCoreApplication.translate("Widget", u"Load File", None))
        self.force_load_file_btn.setText(QCoreApplication.translate("Widget", u"Force Load File", None))
        self.close_btn.setText(QCoreApplication.translate("Widget", u"Close", None))
        self.force_close_btn.setText(QCoreApplication.translate("Widget", u"Force Close", None))
        self.start_btn.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.status_btn.setText(QCoreApplication.translate("Widget", u"Status", None))
        self.ping_btn.setText(QCoreApplication.translate("Widget", u"Ping", None))
        self.status_lbl.setText(QCoreApplication.translate("Widget", u"Status: ", None))
    # retranslateUi

