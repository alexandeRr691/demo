# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orders.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_OrdersDialog(object):
    def setupUi(self, OrdersDialog):
        if not OrdersDialog.objectName():
            OrdersDialog.setObjectName(u"OrdersDialog")
        OrdersDialog.resize(800, 600)
        OrdersDialog.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.png", QSize(), QIcon.Normal, QIcon.Off)
        OrdersDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(OrdersDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(OrdersDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u"images/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.titleLabel = QLabel(OrdersDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"QLabel#titleLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"color: #70B2AF;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.titleLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.detailsLabel = QLabel(OrdersDialog)
        self.detailsLabel.setObjectName(u"detailsLabel")
        self.detailsLabel.setStyleSheet(u"QLabel#detailsLabel {\n"
"font-family: 'Calibri';\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"color: #70B2AF;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.detailsLabel)

        self.ordersTable = QTableWidget(OrdersDialog)
        self.ordersTable.setObjectName(u"ordersTable")
        self.ordersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ordersTable.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.ordersTable)

        self.orderDetailsTable = QTableWidget(OrdersDialog)
        self.orderDetailsTable.setObjectName(u"orderDetailsTable")

        self.verticalLayout.addWidget(self.orderDetailsTable)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backButton = QPushButton(OrdersDialog)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setStyleSheet(u"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.backButton)

        self.editOrderButton = QPushButton(OrdersDialog)
        self.editOrderButton.setObjectName(u"editOrderButton")
        self.editOrderButton.setStyleSheet(u"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}")

        self.horizontalLayout_2.addWidget(self.editOrderButton)

        self.deleteOrderButton = QPushButton(OrdersDialog)
        self.deleteOrderButton.setObjectName(u"deleteOrderButton")
        self.deleteOrderButton.setStyleSheet(u"QPushButton {\n"
"background-color: #70B2AF;\n"
"color: #FFFFFF;\n"
"border: none;\n"
"padding: 8px 16px;\n"
"font-family: 'Calibri';\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover  {\n"
"background-color: #5A9B98;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #4A8582;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.deleteOrderButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(OrdersDialog)

        QMetaObject.connectSlotsByName(OrdersDialog)
    # setupUi

    def retranslateUi(self, OrdersDialog):
        self.label.setText("")
        self.titleLabel.setText(QCoreApplication.translate("OrdersDialog", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438", None))
        self.detailsLabel.setText(QCoreApplication.translate("OrdersDialog", u"\u0421\u043e\u0441\u0442\u0430\u0432 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430:", None))
        self.backButton.setText(QCoreApplication.translate("OrdersDialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.editOrderButton.setText(QCoreApplication.translate("OrdersDialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.deleteOrderButton.setText(QCoreApplication.translate("OrdersDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        pass
    # retranslateUi

