import json
import time
import traceback

from PyQt5 import QtWidgets, QtCore, Qt, QtGui
# from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QGroupBox, QFormLayout, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, QScrollArea, \
    QMenuBar, QMenu, QTableWidgetItem, QComboBox, QAbstractItemView, QDialog


class UserWindow(QDialog):

    def __init__(self, parent=None):
        super(UserWindow, self).__init__(parent)
        self.resize(700, 450)

        self.settingDataTime = [str(time.strftime("%d.%m.%Y", time.localtime())),
                                str(time.strftime("%H:%M", time.localtime()))]  # :%S

        self.settingInformationMovie = {"27.11.2021": {"Во всё тяжкое": {"8:00": "CinemaHall 1",
                                                                         "12:30": "CinemaHall 3"},
                                                       "Поколение вояджера": {"9:30": "CinemaHall 2",
                                                                              "15:30": "CinemaHall 5"}},
                                        "28.11.2021": {"Поколение вояджера": {"8:00": "CinemaHall 1",
                                                                              "12:30": "CinemaHall 3"},
                                                       "Легенда": {"9:30": "CinemaHall 2",
                                                                   "15:30": "CinemaHall 5"}},
                                        "01.12.2021": {"Человек паук навсегда 2022": {"8:00": "CinemaHall 1",
                                                                                      "12:30": "CinemaHall 3"},
                                                       "Пираты карибского моря": {"9:30": "CinemaHall 2",
                                                                                  "15:30": "CinemaHall 5"}},
                                        "02.12.2021": {"Человек паук навсегда 2022": {"9:30": "CinemaHall 2",
                                                                                      "15:30": "CinemaHall 5"},
                                                       "Пираты карибского моря": {"10:30": "CinemaHall 1",
                                                                                  "13:30": {"CinemaHall 5"}}},
                                        "03.12.2021": {"Человек паук навсегда 2022": {"8:30": "CinemaHall 2",
                                                                                      "11:30": "CinemaHall 4"},
                                                       "Пираты карибского моря": {"8:30": "CinemaHall 2",
                                                                                  "11:30": "CinemaHall 4"}},
                                        "04.12.2021": {"Вечные": {"8:30": "CinemaHall 2",
                                                                  "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}},
                                        "05.12.2021": {"Вечные": {"8:30": "CinemaHall 2",
                                                                  "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}},
                                        "06.12.2021": {"Оно 3": {"8:30": "CinemaHall 2",
                                                                 "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}},
                                        "07.12.2021": {"Оно 3": {"8:30": "CinemaHall 2",
                                                                 "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}},
                                        "08.12.2021": {"Аватар 2": {"8:30": "CinemaHall 2",
                                                                    "11:30": "CinemaHall 4"},
                                                       "Оно 3": {"8:30": "CinemaHall 2",
                                                                 "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}},
                                        "09.12.2021": {"Аватар 2": {"8:30": "CinemaHall 2",
                                                                    "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}},
                                        "10.12.2021": {"Аватар 2": {"8:30": "CinemaHall 2",
                                                                    "11:30": "CinemaHall 4"},
                                                       "Анна": {"8:30": "CinemaHall 2",
                                                                "11:30": "CinemaHall 4"}}}
        # with open('data.json', 'w', encoding='utf-8') as file:
        #     json.dump(self.settingInformationMovie, file, ensure_ascii=False)

        self.infoEvent = QtWidgets.QLabel("...")
        self.infoDateAndTime = QtWidgets.QLabel("...")
        self.infoVenue = QtWidgets.QLabel("...")
        self.infoTickets = QtWidgets.QLabel("...")
        self.infoCost = QtWidgets.QLabel("...")

        self.mainContainer_Window = QtWidgets.QVBoxLayout()
        self.SelectingMovieInformation()
        self.TicketSales()
        self.setLayout(self.mainContainer_Window)  # Adds container to the window

    def SelectingMovieInformation(self):
        self.selectingMovieInformation = QGroupBox()
        self.selectingMovieInformation.setFixedHeight(50)

        ''' Создает контейнер layout для selectingMovieInformation'''
        layout = QtWidgets.QHBoxLayout()

        # ### Создаются контейнеры (виджеты) для вводв пользователем данным ( Дата-Фильм-Время )
        self.dateCalendar_SelectingMovieInformation = QtWidgets.QDateEdit()
        self.films_SelectingMovieInformation = QtWidgets.QComboBox()
        self.time_SelectingMovieInformation = QtWidgets.QComboBox()
        # self.dateCalendar_SelectingMovieInformation.dateChanged.connect(self.changed_dateCalendar_SelectingMovieInformation)
        # self.films_SelectingMovieInformation.currentTextChanged.connect(self.changed_films_SelectingMovieInformation)
        # self.time_SelectingMovieInformation.currentTextChanged.connect(self.changed_time_SelectingMovieInformation)

        # ### Выбираешь дату фильма ( день.месяц.год )
        # Устанавливает всплывающее окно календаря
        # Устанавливается максимальная ширина виджета
        # Обработка сигнала при изменении даты
        # Автоматически задается сегодняшняя дата
        self.dateCalendar_SelectingMovieInformation.setCalendarPopup(True)
        self.dateCalendar_SelectingMovieInformation.setMaximumWidth(100)
        self.dateCalendar_SelectingMovieInformation.setDate(
            QtCore.QDate.fromString(self.settingDataTime[0], "dd.MM.yyyy"))
        self.dateCalendar_SelectingMovieInformation.dateChanged.connect(
            self.changed_dateCalendar_SelectingMovieInformation)  # Обработка сигнала
        # self.changed_dateCalendar_SelectingMovieInformation()

        # ### Выбираешь фильм из списка
        # Добавляет в список элемент "..." = "пусто" (фильм не выбран)
        # Устанавливается максимальная ширина виджета
        # self.films_SelectingMovieInformation.addItems(["..."])
        self.films_SelectingMovieInformation.setMaximumWidth(200)

        # ### Выбираешь время сеанса из списка
        # Добавляет в список элемент "..." = "пусто" (время не выбрано)
        # Устанавливается максимальная ширина виджета
        # self.time_SelectingMovieInformation.addItems(["..."])
        self.time_SelectingMovieInformation.setMaximumWidth(100)

        # ### Дата и время устанавливается автоматически (сегодняшнее)
        # Создает надпись Дата с сегодняшней датой
        # Выравнивает надпись Дата ( день.месяц.год )
        # Создает надпись Время с сегодняшним временем
        # Устанавливается максимальная ширина виджета
        # Выравнивает надпись Время ( час:минуты )
        dateToday_SelectingMovieInformation = QtWidgets.QLabel(self.settingDataTime[0])
        dateToday_SelectingMovieInformation.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignRight)
        timeToday_SelectingMovieInformation = QtWidgets.QLabel(self.settingDataTime[1])
        timeToday_SelectingMovieInformation.setMaximumWidth(40)
        timeToday_SelectingMovieInformation.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignRight)

        # ### Добавление всех параметров в контейнер layout и главное окно UserWindow
        layout.addWidget(self.dateCalendar_SelectingMovieInformation)
        layout.addWidget(self.films_SelectingMovieInformation)
        layout.addWidget(self.time_SelectingMovieInformation)
        layout.addWidget(dateToday_SelectingMovieInformation)
        layout.addWidget(timeToday_SelectingMovieInformation)
        self.selectingMovieInformation.setLayout(layout)
        self.mainContainer_Window.addWidget(self.selectingMovieInformation)

    def TicketSales(self):
        self.ticketSales = QGroupBox("Продажа билетов")
        # self.ticketSales.setStyleSheet("background-color: rgb(65, 105, 225)")

        ''' Создает контейнер layout для ticketSales'''
        layout = QtWidgets.QHBoxLayout()

        #
        # ### Создает контейнер для отладки и box для размещения информации о CinemaHall
        containerBoxPlaces = QWidget(self)
        self.boxPlaces_TicketSales = QtWidgets.QVBoxLayout(containerBoxPlaces)

        # ### Создаются контейнеры (виджеты) для отображения информации о CinemaHall
        # Номер CinemaHall
        # Места в CinemaHall
        # Цена для каждого места
        self.nameCinemaHall_BoxPlaces_TicketSales = QtWidgets.QLabel("...")
        self.places_BoxPlaces_TicketSales = QtWidgets.QTableWidget()
        self.priceForPlaces_BoxPlaces_TicketSales = QtWidgets.QLabel("...")
        # self.priceForPlaces_BoxPlaces_TicketSales.

        #
        # ### Создает контейнер для отладки и box для конечной информации
        containerBoxPlacesInformation = QWidget(self)
        containerBoxPlacesInformation.setMaximumWidth(200)
        boxPlacesInformation_TicketSales = QVBoxLayout(containerBoxPlacesInformation)


        # ### Создаются кнопки для завершения программы
        btnCancel_BoxPlacesInformation_TicketSales = QtWidgets.QPushButton("Отмена")
        # btnCancel_BoxPlacesInformation_TicketSales.clicked.connect(self.cancelAllActions)  # Обработка сигнала
        btnPay_BoxPlacesInformation_TicketSales = QtWidgets.QPushButton("К оплате")
        btnPay_BoxPlacesInformation_TicketSales.setStyleSheet("background-color: rgb(200, 45, 10)")
        btnPay_BoxPlacesInformation_TicketSales.clicked.connect(self.pay_ticket)

        """ ВАЖНЫЕ параметры будут использоваться когда зададут ( Дату-Фильм-Время ) """
        self.boxPlaces_TicketSales.addWidget(self.nameCinemaHall_BoxPlaces_TicketSales)
        self.boxPlaces_TicketSales.addWidget(self.places_BoxPlaces_TicketSales)
        self.boxPlaces_TicketSales.addWidget(self.priceForPlaces_BoxPlaces_TicketSales)
        boxPlacesInformation_TicketSales.addWidget(QtWidgets.QLabel("<u>Мероприяте:</u>"))
        boxPlacesInformation_TicketSales.addWidget(self.infoEvent)
        boxPlacesInformation_TicketSales.addWidget(QtWidgets.QLabel("<u>Дата и время:</u>"))
        boxPlacesInformation_TicketSales.addWidget(self.infoDateAndTime)
        boxPlacesInformation_TicketSales.addWidget(QtWidgets.QLabel("<u>Место проведения:</u>"))
        boxPlacesInformation_TicketSales.addWidget(self.infoVenue)
        boxPlacesInformation_TicketSales.addWidget(QtWidgets.QLabel("<u>Билеты:</u>"))
        boxPlacesInformation_TicketSales.addWidget(self.infoTickets)
        boxPlacesInformation_TicketSales.addWidget(QtWidgets.QLabel("<u>Стоимость:</u>"))
        boxPlacesInformation_TicketSales.addWidget(self.infoCost)
        boxPlacesInformation_TicketSales.addWidget(btnCancel_BoxPlacesInformation_TicketSales)
        boxPlacesInformation_TicketSales.addWidget(btnPay_BoxPlacesInformation_TicketSales)

        # ### Добавление всех параметров в контейнер layout и главное окно UserWindow
        layout.addWidget(containerBoxPlaces)
        layout.addWidget(containerBoxPlacesInformation)
        self.ticketSales.setLayout(layout)
        self.mainContainer_Window.addWidget(self.ticketSales)

    def changed_dateCalendar_SelectingMovieInformation(self):
        try:
            dataCalendar_text = self.dateCalendar_SelectingMovieInformation.text()
            self.infoDateAndTime.setText(dataCalendar_text)

            if self.dateCalendar_SelectingMovieInformation.text() in self.settingInformationMovie:
                self.films_SelectingMovieInformation.clear()
                self.films_SelectingMovieInformation.addItems(list(self.settingInformationMovie.get(dataCalendar_text).keys()))
                self.infoEvent.setText(str(self.films_SelectingMovieInformation.currentText()))
            else:
                self.films_SelectingMovieInformation.clear()
                self.time_SelectingMovieInformation.clear()
                # if self.places_BoxPlaces_TicketSales.is:
                #     self.places_BoxPlaces_TicketSales.clear()
                #     self.places_BoxPlaces_TicketSales.setColumnCount(0)
                #     self.places_BoxPlaces_TicketSales.setRowCount(0)
                # self.infoEvent.setText("...")  # оно и так убирается
                self.infoVenue.setText("...")
                self.infoTickets.setText("...")
                self.infoCost.setText("...")

            if self.dateCalendar_SelectingMovieInformation.text() in self.settingInformationMovie:
                self.films_SelectingMovieInformation.currentTextChanged.connect(
                    self.changed_films_SelectingMovieInformation)
        except Exception as e:
            traceback.print_exc()
            # print("Error changed_dateCalendar_SelectingMovieInformation")
            # print(str(e))

    def changed_films_SelectingMovieInformation(self, s):
        try:
            self.infoEvent.setText(s)
            if self.dateCalendar_SelectingMovieInformation.text() in self.settingInformationMovie:
                if s in self.settingInformationMovie.get(self.dateCalendar_SelectingMovieInformation.text()):
                    self.time_SelectingMovieInformation.clear()
                    self.time_SelectingMovieInformation.addItems(list(self.settingInformationMovie.get(self.dateCalendar_SelectingMovieInformation.text()).get(s).keys()))
                    self.time_SelectingMovieInformation.currentTextChanged.connect(self.changed_time_SelectingMovieInformation)
                else:
                    self.time_SelectingMovieInformation.clear()
                    self.places_BoxPlaces_TicketSales.clear()
                    self.places_BoxPlaces_TicketSales.setColumnCount(0)
                    self.places_BoxPlaces_TicketSales.setRowCount(0)
                    self.infoVenue.setText("...")
                    self.infoTickets.setText("...")
                    self.infoCost.setText("...")
        except Exception as e:
            traceback.print_exc()
            # print("Error changed_films_SelectingMovieInformation")
            # print(str(e))

    def changed_time_SelectingMovieInformation(self, s):
        try:
            self.infoDateAndTime.setText(self.dateCalendar_SelectingMovieInformation.text() + " " + s)
            if self.time_SelectingMovieInformation.currentText():
                if s in self.settingInformationMovie.get(self.dateCalendar_SelectingMovieInformation.text()).get(
                        self.infoEvent.text()):

                    self.infoVenue.setText(
                        self.settingInformationMovie.get(self.dateCalendar_SelectingMovieInformation.text()).get(
                            self.infoEvent.text()).get(s))
                    self.nameCinemaHall_BoxPlaces_TicketSales.setText(self.infoVenue.text())
                    self.places_BoxPlaces_TicketSales.setRowCount(0)
                    self.places_BoxPlaces_TicketSales.setColumnCount(0)
                    self.create_cinema_hall(self.infoVenue.text())
                else:
                    self.nameCinemaHall_BoxPlaces_TicketSales.setText("...")

        except Exception as e:
            traceback.print_exc()
            # print("Error changed_time_SelectingMovieInformation")
            # print(str(e))

    def create_cinema_hall(self, hall):  # hall - если понадобиться создавать разные залы, а не однотипные

        self.places_BoxPlaces_TicketSales.setColumnCount(12)
        self.places_BoxPlaces_TicketSales.setRowCount(10)

        self.hall_1 = {10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                  9:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                  8:  [1, 2, 4, 5, 6, 7, 8, 9, 11, 12],
                  7:  [1, 2, 4, 5, 6, 7, 8, 9, 11, 12],
                  6:  [4, 5, 6, 7, 8, 9],
                  5:  [4, 5, 6, 7, 8, 9],
                  4:  [3, 4, 5, 6, 7, 8, 9, 10],
                  3:  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                  2:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                  1:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}

        for i in range(10):
            self.places_BoxPlaces_TicketSales.setRowHeight(i, 10)
            for j in range(12):
                self.places_BoxPlaces_TicketSales.setColumnWidth(j, 10)
                if (j + 1) in self.hall_1.get(i + 1):
                    self.places_BoxPlaces_TicketSales.setItem(i, j, QtWidgets.QTableWidgetItem(str(j + 1)))
                else:
                    self.places_BoxPlaces_TicketSales.setItem(i, j, QtWidgets.QTableWidgetItem(" "))

        # делаем ресайз колонок по содержимому
        # self.places_BoxPlaces_TicketSales.resizeColumnsToContents()

        # Убирает бордюры вокруг ячейки
        # self.places_BoxPlaces_TicketSales.setShowGrid(False)
        # убирает горизантальную черту с названиями
        self.places_BoxPlaces_TicketSales.horizontalHeader().setVisible(False)
        # изменим поведение выбора строк на множественный выбор
        self.places_BoxPlaces_TicketSales.setSelectionMode(QAbstractItemView.MultiSelection)
        # нельзя изменять ячейки
        self.places_BoxPlaces_TicketSales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # ??? нельзя изменять размер ячеек
        self.places_BoxPlaces_TicketSales.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        # Задать название вертикальных названий
        self.places_BoxPlaces_TicketSales.setVerticalHeaderLabels(
            [str(x + 1) + " ряд" for x in range(self.places_BoxPlaces_TicketSales.rowCount())])
        # Убрать возможность выделять ячейки
        self.places_BoxPlaces_TicketSales.setSelectionMode(QAbstractItemView.NoSelection)

        # self.places_BoxPlaces_TicketSales.setItemDelegate

        self.places_BoxPlaces_TicketSales.cellPressed[int, int].connect(self.clickedRowColumn)
        self.list_on_places = []


    def clickedRowColumn(self, r, c):
        if (r, c) in self.list_on_places:
            self.places_BoxPlaces_TicketSales.item(r, c).setBackground(QtGui.QColor("white"))
            self.list_on_places.remove((r, c))
        else:
            print(r + 1, c + 1)
            print(self.hall_1.get(r + 1))
            if (c + 1) in self.hall_1.get(r + 1):
                self.places_BoxPlaces_TicketSales.item(r, c).setBackground(QtGui.QColor(0, 128, 255))
                self.list_on_places.append((r, c))
        print(self.list_on_places)


    def pay_ticket(self):
        for i in range(self.places_BoxPlaces_TicketSales.rowCount()):
            print(self.places_BoxPlaces_TicketSales.item(i, 0).text())
        dialog = PayTicket(self)
        dialog.exec_()

    def cancelAllActions(self):
        # self.accept()
        # self.quit()
        # self.close()

        pass

        self.infoEvent.setText("...")
        self.infoDateAndTime.setText("...")
        self.infoVenue.setText("...")
        self.infoTickets.setText("...")
        self.infoCost.setText("...")
        self.nameCinemaHall_BoxPlaces_TicketSales.setText("...")
        self.places_BoxPlaces_TicketSales.clear()
        self.places_BoxPlaces_TicketSales.setColumnCount(0)
        self.places_BoxPlaces_TicketSales.setRowCount(0)
        self.priceForPlaces_BoxPlaces_TicketSales.setText("...")
        self.dateCalendar_SelectingMovieInformation.setDate(
            QtCore.QDate.fromString(self.settingDataTime[0], "dd.MM.yyyy"))
        self.films_SelectingMovieInformation.clear()
        self.time_SelectingMovieInformation.clear()
        self.changed_dateCalendar_SelectingMovieInformation()

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Подтверждение закрытия окна",
                                                "Вы дейстивтельно хотите закрыть окно?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
            # self.close()
        else:
            e.ignore()



class PayTicket(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PayTicket, self).__init__(parent)



# def application():
#     app = QtWidgets.QApplication(sys.argv)
#     window = UserWindow()
#     window.setWindowTitle("PyQt5")
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     application()
