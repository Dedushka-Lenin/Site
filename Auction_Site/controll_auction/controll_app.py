import sys
import os
import shutil
import hashlib

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

# Добавить возможность группировать задачи
# Закрепление задач
# Уведомления, таймер
# Добавить возможнось создавать список мелких задач (Рядом с кажной мелкой задачей будет стоять галочка)

# Размер галочек


def hiding_widgets(h,r):
    for i in range(len(h)):
        h[i].setVisible(r)

def button_size(h,r):
    for i in range(len(h)):
        h[i].setIconSize(QSize(r, r))
        h[i].setFixedSize(r, r)

def button_text(h,r):
    font = QFont()
    font.setPointSize(r)
    for i in range(len(h)):
        h[i].setFont(font)

class widget(QWidget):
    def __init__(self):
        super().__init__() 

#########################################################################################

        self.PROFILE_defolt = "Guest"

        self.PROFILE_list = []
        self.PASSWORD_list = []

        self.PROFILE = self.PROFILE_defolt

        if not os.path.exists("task_process"):
            os.mkdir("task_process")
            os.mkdir(f"task_process/{self.PROFILE}")

        elif not os.path.exists(f"task_process/{self.PROFILE}"):
            os.mkdir(f"task_process/{self.PROFILE}")

        if os.path.exists(f"task_process/PROFILE_list.txt"):
            with open(f"task_process/PROFILE_list.txt", "r", encoding = "utf-8") as file:

                list_1 = file.readlines()
                list_1 = [line.rstrip() for line in list_1]

                for i in range(len(list_1)):  
                    list_2 = list_1[i].split("|")
                    self.PROFILE_list.append(list_2[0])
                    self.PASSWORD_list.append(list_2[1])
        else:
            with open(f"task_process/PROFILE_list.txt", "w", encoding = "utf-8") as file:
                pass

#########################################################################################

        self.button_menu = QPushButton(self) #Кнопка меню
        self.button_menu.setIcon(QIcon('img/button_menu.png'))
        self.button_menu.setStyleSheet("border-radius: 10px")
        self.button_menu.clicked.connect(self.button_menu_clicked)

        self.button_profile_menu = QPushButton(self) #Кнопка настройки профиля
        self.button_profile_menu.setIcon(QIcon('img/button_profile.png'))
        self.button_profile_menu.setStyleSheet("border-radius: 10px")
        self.button_profile_menu.clicked.connect(self.button_profile_menu_clicked)

        self.button_setting_menu = QPushButton(self) #Кнопка настройки
        self.button_setting_menu.setIcon(QIcon('img/button_ settings.png'))
        self.button_setting_menu.setStyleSheet("border-radius: 10px")
        self.button_setting_menu.clicked.connect(self.button_setting_menu_clicked)

        self.button_exit = QPushButton(self) #Кнопка выхода
        self.button_exit.setIcon(QIcon('img/button_exit.png'))
        self.button_exit.setStyleSheet("border-radius: 10px")
        self.button_exit.clicked.connect(self.close)

#########################################################################################

        self.list_task = []
        self.list_complexity = []
        self.list_priorities = []

        if os.path.exists(f"task_process/{self.PROFILE}/task_list.txt"):
            with open(f"task_process/{self.PROFILE}/task_list.txt", "r", encoding = "utf-8") as file:
                list_1 = file.readlines()
                list_1 = [line.rstrip() for line in list_1]

                for i in range(len(list_1)):  
                    list_2 = list_1[i].split("|")
                    self.list_task.append(list_2[0])
                    self.list_complexity.append(int(list_2[1]))
                    self.list_priorities.append(int(list_2[2]))
        else:
            with open(f"task_process/{self.PROFILE}/task_list.txt", "w", encoding = "utf-8") as file:
                pass
        
        self.list_task = [line.rstrip() for line in self.list_task]

        self.listwidget_task = QListWidget(self)  #Создание кнопок задач
        self.listwidget_task.addItems(self.list_task)
        self.listwidget_task.setVisible(False)
        self.listwidget_task.currentTextChanged.connect(self.listwidget_task_changed)

#########################################################################################

        self.sort_alphabetically = QPushButton("Сортировать по алфовиту", self)
        self.sort_alphabetically.clicked.connect(self.sort_alphabetically_clicked)
        self.sort_alphabetically.setVisible(False)

        self.sort_severity = QPushButton("Сортировать по соложность", self)
        self.sort_severity.clicked.connect(self.sort_severity_clicked)
        self.sort_severity.setVisible(False)

        self.sort_priority = QPushButton("Сортировать по приоритету", self)
        self.sort_priority.clicked.connect(self.sort_priority_clicked)
        self.sort_priority.setVisible(False)

#########################################################################################

        self.tasks_title = QLabel(self)
        self.tasks_title.setVisible(False)

        self.tasks_text = QPlainTextEdit(self)
        self.tasks_text.setVisible(False)

#########################################################################################

        self.button_task_create = QPushButton("Создать задачу", self) #Кнопка создания задичи
        self.button_task_create.clicked.connect(self.button_task_create_clicked)

        self.button_save = QPushButton("Сохранить", self) #Кнопка сохранения
        self.button_save.setVisible(False)
        self.button_save.clicked.connect(self.button_save_clicked)

        self.button_cancel = QPushButton("Отмена", self) #Кнопка отмены
        self.button_cancel.setVisible(False)
        self.button_cancel.clicked.connect(self.button_cancel_clicked)

        self.button_delete = QPushButton("Очистить", self) #Кнопка очищения
        self.button_delete.setVisible(False)
        self.button_delete.clicked.connect(self.button_delete_clicked)

        self.button_setting_task  = QPushButton("Настроить задачу", self)  #Кнопка настройки задачи
        self.button_setting_task.clicked.connect(self.button_task_setting_clicked)
        self.button_setting_task.setVisible(False)

        self.button_task_delete = QPushButton("Удалить задачу", self) #Кнопка удаления задичи
        self.button_task_delete.clicked.connect(self.button_task_delete_clicked)
        self.button_task_delete.setVisible(False)

#########################################################################################

        self.tasks_title_create = QLabel(self)
        self.tasks_title_create.setVisible(False)

        self.new_task = QLineEdit()
        self.new_task.setMaxLength(30) #максимум букв
        self.new_task.setPlaceholderText("Введите название задачи")
        self.new_task.setVisible(False)

#########################################################################################

        self.complexity_task = QSpinBox()   # Сложность задачи
        self.complexity_task.setRange(0,10)
        self.complexity_task.setVisible(False)

        self.label_complexity_task = QLabel("Сложность задачи", self)
        self.label_complexity_task.setVisible(False)

        self.checkbox_complexity_task = QCheckBox()
        self.checkbox_complexity_task.setVisible(False)


        self.priority_task = QSpinBox()     # Приоритет задачи
        self.priority_task.setRange(0,10)
        self.priority_task.setVisible(False)

        self.label_priority_task = QLabel("Приоритет задачи", self)
        self.label_priority_task.setVisible(False)

        self.checkbox_priority_task = QCheckBox()
        self.checkbox_priority_task.setVisible(False)


        self.label_create_copy = QLabel("Создать копию", self)  # Создать копию
        self.label_create_copy.setVisible(False)

        self.create_copy = QCheckBox()
        self.create_copy.setVisible(False)

#########################################################################################

        self.button_create = QPushButton("Создать", self) #Кнопка(2) создания задичи
        self.button_create.clicked.connect(self.button_create_clicked)
        self.button_create.setVisible(False)

        self.button_delete_task = QPushButton("Удалить", self) #Кнопка(2) удаления задичи
        self.button_delete_task.clicked.connect(self.button_task_delete_clicked)
        self.button_delete_task.setVisible(False)

        self.button_cancel_create = QPushButton("Отмена", self) #Кнопка(2) отмены
        self.button_cancel_create.clicked.connect(self.button_cancel_clicked)
        self.button_cancel_create.setVisible(False)

        self.message = QLabel(self)
        self.message.setVisible(False)

#########################################################################################

        self.profile_name = QLabel(self)
        self.profile_name.setVisible(False)

        self.button_create_profile = QPushButton("Создать новый профиль", self)
        self.button_create_profile.clicked.connect(self.button_create_profile_clicked)
        self.button_create_profile.setVisible(False)

        self.button_login_profile = QPushButton("Войти в другой профиль", self)
        self.button_login_profile.clicked.connect(self.button_login_profile_clicked)
        self.button_login_profile.setVisible(False)

        self.change_profile_name = QPushButton("Поменять имя профиля", self)
        self.change_profile_name.clicked.connect(self.change_profile_name_clicked)
        self.change_profile_name.setVisible(False)

        self.change_password = QPushButton("Поменять пароль", self)
        self.change_password.clicked.connect(self.change_password_clicked)
        self.change_password.setVisible(False)

        self.button_delete_profile = QPushButton("Удалить профиль", self)
        self.button_delete_profile.clicked.connect(self.button_delete_profile_clicked)
        self.button_delete_profile.setVisible(False)

        self.button_cancel_profile = QPushButton("Отмена", self)
        self.button_cancel_profile.clicked.connect(self.button_cancel_clicked)
        self.button_cancel_profile.setVisible(False)

#########################################################################################

        self.line_profile = QLineEdit()
        self.line_profile.setMaxLength(30) #максимум букв
        self.line_profile.setPlaceholderText("Введите имя профиля")
        self.line_profile.setVisible(False)

        self.line_password_1 = QLineEdit()
        self.line_password_1.setMaxLength(30) #максимум букв
        self.line_password_1.setPlaceholderText("Введите пароль")
        self.line_password_1.setVisible(False)

        self.line_password_2 = QLineEdit()
        self.line_password_2.setMaxLength(30) #максимум букв
        self.line_password_2.setPlaceholderText("Введите пароль ещё раз")
        self.line_password_2.setVisible(False)

        self.create_profile = QPushButton("Создать", self)
        self.create_profile.clicked.connect(self.create_profile_clicked)
        self.create_profile.setVisible(False)

        self.save_password = QPushButton("Сохранить", self)
        self.save_password.clicked.connect(self.save_password_clicked)
        self.save_password.setVisible(False)

        self.save_profile = QPushButton("Сохранить", self)
        self.save_profile.clicked.connect(self.save_profile_clicked)
        self.save_profile.setVisible(False)

        self.canceling_profile = QPushButton("Отмена", self)
        self.canceling_profile.clicked.connect(self.button_cancel_clicked)
        self.canceling_profile.setVisible(False)

        self.login_profile = QPushButton("Войти", self)
        self.login_profile.clicked.connect(self.login_profile_clicked)
        self.login_profile.setVisible(False)

        self.login_guest = QPushButton("Войти как гость", self)
        self.login_guest.clicked.connect(self.login_guest_clicked)
        self.login_guest.setVisible(False)

#########################################################################################
    
        self.button_size_p = 32
        self.text_size_p = 8

        if os.path.exists(f"task_process/setting.txt"):
            with open(f"task_process/setting.txt", "r", encoding = "utf-8") as file:
                list_setting = file.readlines()
                list_setting = [line.rstrip() for line in list_setting]

                self.button_size_p = int(list_setting[0])
                self.text_size_p = int(list_setting[1])
        else:
            with open(f"task_process/setting.txt", "w", encoding = "utf-8") as file:
                file.write(f'{self.button_size_p}\n{self.text_size_p}')
        
#########################################################################################

        self.button_size_s = {
            'Маленький': 16,
            'Средний': 32,
            'Большой': 64,
            'Гиганский': 128,}
        
        self.button_size_s_v = {
            16: 'Маленький',
            32: 'Средний',
            64: 'Большой',
            128: 'Гиганский',}

        self.text_size_s = {
            'Маленький': 4,
            'Средний': 8,
            'Большой': 16,
            'Гиганский': 24,}
        
        self.text_size_s_v = {
            4: 'Маленький',
            8: 'Средний',
            16: 'Большой',
            24: 'Гиганский',}
        
#########################################################################################

        self.size_m = ["Маленький","Средний","Большой","Гиганский"]

        self.button_size = QLabel("Размер кнопок:", self)  # Размер кнопок
        self.button_size.setVisible(False)

        self.combobox_button_size = QComboBox()
        self.combobox_button_size.addItems(self.size_m)
        self.combobox_button_size.setVisible(False)

        self.text_size = QLabel("Размер текста:", self)  # Размер текста
        self.text_size.setVisible(False)

        self.combobox_text_size = QComboBox()
        self.combobox_text_size.addItems(self.size_m)
        self.combobox_text_size.setVisible(False)

        self.save_setting = QPushButton("Сохранить", self)
        self.save_setting.clicked.connect(self.save_setting_clicked)
        self.save_setting.setVisible(False)

        self.default_setting = QPushButton("По умолчанию", self)
        self.default_setting.clicked.connect(self.default_setting_clicked)
        self.default_setting.setVisible(False)

        self.cancel_setting = QPushButton("Отмена", self)
        self.cancel_setting.clicked.connect(self.button_cancel_clicked)
        self.cancel_setting.setVisible(False)

#########################################################################################

        self.button_m = [
            self.button_menu,
            self.button_profile_menu,
            self.button_setting_menu,
            self.button_exit]

        self.text_m = [
            self.listwidget_task,
            self.sort_alphabetically,
            self.sort_severity,
            self.sort_priority,
            self.tasks_title,
            self.tasks_text,
            self.button_task_create,
            self.button_save,
            self.button_cancel,
            self.button_delete,
            self.button_setting_task,
            self.button_task_delete,
            self.tasks_title_create,
            self.new_task,
            self.label_complexity_task,
            self.label_priority_task,
            self.label_create_copy,
            self.button_create,
            self.button_delete_task,
            self.button_cancel_create,
            self.message,
            self.profile_name,
            self.button_create_profile,
            self.button_login_profile,
            self.change_profile_name,
            self.change_password,
            self.button_delete_profile,
            self.button_cancel_profile,
            self.line_profile,
            self.line_password_1,
            self.line_password_2,
            self.create_profile,
            self.save_password,
            self.save_profile,
            self.canceling_profile,
            self.login_profile,
            self.login_guest,
            self.button_size,
            self.combobox_button_size,
            self.text_size,
            self.combobox_text_size,
            self.save_setting,
            self.default_setting,
            self.cancel_setting,
            
            self.complexity_task,
            self.priority_task]

#########################################################################################

        button_size(self.button_m, self.button_size_p)
        button_text(self.text_m, self.text_size_p)

#########################################################################################

        self.menu_m = [
            self.button_menu,
            self.button_profile_menu,
            self.button_setting_menu,
            self.button_exit,
            self.button_task_create]

        self.login_profile_m = [
            self.line_profile,
            self.line_password_1,
            self.login_profile,
            self.login_guest]

#########################################################################################

        self.setting_menu_guest_m = [
            self.profile_name,
            self.button_create_profile,
            self.button_login_profile,
            self.button_cancel_profile]

        self.profile_menu_m = [
            self.profile_name,
            self.button_create_profile,
            self.button_login_profile,
            self.change_profile_name,
            self.change_password,
            self.button_delete_profile,
            self.button_cancel_profile]

        self.create_profile_m = [
            self.line_profile,
            self.line_password_1,
            self.line_password_2,
            self.create_profile,
            self.canceling_profile]

        self.change_profile_name_m = [
            self.line_profile,
            self.canceling_profile,
            self.save_profile]
        
        self.change_password_m = [
            self.line_profile,
            self.line_password_1,
            self.line_password_2,
            self.canceling_profile,
            self.save_password]

#########################################################################################

        self.setting_menu_m = [
            self.button_size,
            self.combobox_button_size,
            self.text_size,
            self.combobox_text_size,
            self.save_setting,
            self.default_setting,
            self.cancel_setting]

#########################################################################################

        self.list_task_m = [
            self.listwidget_task,
            self.sort_alphabetically,
            self.sort_severity,
            self.sort_priority]
                
        self.tasks_text_m = [
            self.tasks_title,
            self.tasks_text,
            self.button_save,
            self.button_delete,
            self.button_cancel,
            self.button_task_delete,
            self.button_setting_task]
                
        self.new_task_m = [
            self.new_task,
            self.complexity_task,
            self.label_complexity_task,
            self.checkbox_complexity_task,
            self.priority_task,
            self.label_priority_task,
            self.checkbox_priority_task,
            self.button_create,
            self.button_cancel_create,
            self.message]
                
        self.setting_m = [
            self.tasks_title_create,
            self.label_create_copy,
            self.create_copy,
            self.button_delete_task]
        
#########################################################################################

        column_1 = QVBoxLayout()
        column_1.addWidget(QLabel("", self))
        column_1.addWidget(self.button_menu, 0)
        column_1.addWidget(self.button_profile_menu, 0)
        column_1.addWidget(self.button_setting_menu, 0)
        column_1.addWidget(self.button_exit, 0)
        column_1.addStretch()


        line_1 = QHBoxLayout()
        line_1.addWidget(self.complexity_task, 1)
        line_1.addWidget(self.label_complexity_task, 1)
        line_1.addWidget(self.checkbox_complexity_task, 1)

        line_2 = QHBoxLayout()
        line_2.addWidget(self.priority_task, 1)
        line_2.addWidget(self.label_priority_task, 1)
        line_2.addWidget(self.checkbox_priority_task, 1)

        line_3 = QHBoxLayout()
        line_3.addWidget(self.label_create_copy, 1)
        line_3.addWidget(self.create_copy, 1)

        line_4 = QHBoxLayout()
        line_4.addWidget(self.button_create, 1)
        line_4.addWidget(self.button_delete_task, 1)
        line_4.addWidget(self.button_cancel_create, 1)

        line_5 = QHBoxLayout()
        line_5.addWidget(self.button_delete_profile, 1)
        line_5.addWidget(self.button_cancel_profile, 1)

        line_6 = QHBoxLayout()
        line_6.addWidget(self.create_profile, 1)
        line_6.addWidget(self.save_password, 1)
        line_6.addWidget(self.save_profile, 1)
        line_6.addWidget(self.canceling_profile, 1)

        line_7 = QHBoxLayout()
        line_7.addWidget(self.button_size, 1)
        line_7.addWidget(self.combobox_button_size, 1)

        line_8 = QHBoxLayout()
        line_8.addWidget(self.text_size, 1)
        line_8.addWidget(self.combobox_text_size, 1)

        line_9 = QHBoxLayout()
        line_9.addWidget(self.save_setting, 1)
        line_9.addWidget(self.default_setting, 1)
        line_9.addWidget(self.cancel_setting, 1)

        column_2 = QVBoxLayout()
        column_2.addWidget(QLabel("", self))
        column_2.addWidget(self.tasks_title_create)
        column_2.addWidget(self.new_task, 0)
        column_2.addLayout(line_1)
        column_2.addLayout(line_2)
        column_2.addLayout(line_3)
        column_2.addLayout(line_4)

        column_2.addWidget(self.profile_name, 0)
        column_2.addWidget(self.button_create_profile, 0)
        column_2.addWidget(self.button_login_profile, 0)
        column_2.addWidget(self.change_profile_name, 0)
        column_2.addWidget(self.change_password, 0)
        column_2.addLayout(line_5)

        column_2.addWidget(self.line_profile, 0)
        column_2.addWidget(self.line_password_1, 0)
        column_2.addWidget(self.line_password_2, 0)
        column_2.addLayout(line_6)
        column_2.addWidget(self.login_profile, 0)
        column_2.addWidget(self.login_guest, 0)
        column_2.addWidget(self.message, 0)

        column_2.addLayout(line_7)
        column_2.addLayout(line_8)
        column_2.addLayout(line_9)
        column_2.addStretch()


        column_3 = QVBoxLayout()
        column_3.addWidget(QLabel("", self))
        column_3.addWidget(self.listwidget_task, 4)
        column_3.addWidget(self.sort_alphabetically, 0)
        column_3.addWidget(self.sort_severity, 0)
        column_3.addWidget(self.sort_priority, 0)
        column_3.addStretch()


        line_auxiliary = QHBoxLayout()
        line_auxiliary.addStretch()

        column_4 = QVBoxLayout()
        column_4.addLayout(line_auxiliary)
        column_4.addWidget(self.tasks_title, 0)
        column_4.addWidget(self.tasks_text, 0)


        column_5 = QVBoxLayout()
        column_5.addWidget(QLabel("", self))
        column_5.addWidget(self.button_task_create, 0)
        column_5.addStretch()
        column_5.addWidget(self.button_save, 0)
        column_5.addWidget(self.button_cancel, 0)
        column_5.addWidget(QLabel("", self))
        column_5.addWidget(self.button_delete, 0)
        column_5.addWidget(self.button_setting_task)
        column_5.addWidget(self.button_task_delete, 0)


        line_main = QHBoxLayout()
        line_main.addLayout(column_1)
        line_main.addLayout(column_2)
        line_main.addLayout(column_3)
        line_main.addLayout(column_4)
        line_main.addLayout(column_5)

        Table = QWidget()
        Table.setLayout(line_main)
        self.Table = Table

#########################################################################################

        if not len(self.PROFILE_list) == 0:
            hiding_widgets(self.profile_menu_m, False)
            hiding_widgets(self.menu_m, False)
            hiding_widgets(self.login_profile_m, True)
            self.line_profile.setText('')
            self.line_password_1.setText('')
            
#########################################################################################

        k = self.size_m.index(self.text_size_s_v[self.text_size_p]) + 1
        t = self.size_m.index(self.button_size_s_v[self.button_size_p]) + 1

        if t > k: self.setMinimumSize (235 * k , 140 * t )
        else: self.setMinimumSize (235 * k , 140 * k )

        self.listwidget_task.setFixedWidth(100 * k )
        self.new_task.setMinimumWidth(110 * k )

        self.complexity_task.setFixedWidth(25 * k )
        self.label_complexity_task.setFixedWidth(90 * k + 8)
        self.priority_task.setFixedWidth(25 * k)
        self.label_priority_task.setFixedWidth(90 * k + 8)

        self.label_create_copy.setFixedWidth(112 * k )

#########################################################################################

    def button_menu_clicked(self):
        self.sort_severity.setEnabled(True)
        self.sort_priority.setEnabled(True)
        self.sort_alphabetically.setEnabled(False)
        self.listwidget_task.clear()
        self.listwidget_task.addItems(sorted(self.list_task))

        hiding_widgets(self.tasks_text_m, False)
        hiding_widgets(self.new_task_m, False)
        hiding_widgets(self.setting_m, False)
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.create_profile_m, False)
        hiding_widgets(self.change_profile_name_m, False)
        hiding_widgets(self.change_password_m, False)
        hiding_widgets(self.setting_menu_m, False)

        if len(self.list_task) != 0:
            hiding_widgets(self.list_task_m, True)
            self.message.setVisible(False)
        else:
            self.message.setText("У Вас нет запланированных задач")
            self.message.setVisible(True)

    def button_profile_menu_clicked(self):
        hiding_widgets(self.list_task_m, False)
        hiding_widgets(self.tasks_text_m, False)
        hiding_widgets(self.new_task_m, False)
        hiding_widgets(self.setting_m, False)
        hiding_widgets(self.create_profile_m, False)
        hiding_widgets(self.change_profile_name_m, False)
        hiding_widgets(self.change_password_m, False)
        hiding_widgets(self.setting_menu_m, False)

        if self.PROFILE == self.PROFILE_defolt:
            hiding_widgets(self.setting_menu_guest_m, True)
        else:
            hiding_widgets(self.profile_menu_m, True)

        self.profile_name.setText(self.PROFILE)

    def button_setting_menu_clicked(self):
        hiding_widgets(self.list_task_m, False)
        hiding_widgets(self.tasks_text_m, False)
        hiding_widgets(self.new_task_m, False)
        hiding_widgets(self.setting_m, False)
        hiding_widgets(self.create_profile_m, False)
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.change_profile_name_m, False)
        hiding_widgets(self.change_password_m, False)

        hiding_widgets(self.setting_menu_m, True)

        self.combobox_button_size.setCurrentIndex(self.size_m.index(self.button_size_s_v[self.button_size_p]))
        self.combobox_text_size.setCurrentIndex(self.size_m.index(self.text_size_s_v[self.text_size_p]))

    def button_cancel_clicked(self):
        hiding_widgets(self.tasks_text_m, False)
        hiding_widgets(self.new_task_m, False)
        hiding_widgets(self.setting_m, False)
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.list_task_m, False)
        hiding_widgets(self.create_profile_m, False)
        hiding_widgets(self.change_profile_name_m, False)
        hiding_widgets(self.change_password_m, False)
        hiding_widgets(self.setting_menu_m, False)

#########################################################################################

    def listwidget_task_changed(self, s):
        if not s == '':
            self.s = s
            self.tasks_title.setText(self.s)

            hiding_widgets(self.list_task_m, False)
            hiding_widgets(self.tasks_text_m, True)
            self.message.setVisible(False)

            if os.path.exists(f"task_process/{self.PROFILE}/{self.s}.txt"):
                with open(f"task_process/{self.PROFILE}/{self.s}.txt", "r", encoding = "utf-8") as file:
                    self.tasks_text.setPlainText(file.read())
            else:
                with open(f"task_process/{self.PROFILE}/{self.s}.txt", "w+", encoding = "utf-8") as file:
                    self.tasks_text.setPlainText('')

    def sort_alphabetically_clicked(self):
        self.listwidget_task.clear()
        self.listwidget_task.addItems(sorted(self.list_task))

        self.sort_severity.setEnabled(True)
        self.sort_priority.setEnabled(True)
        self.sort_alphabetically.setEnabled(False)

    def sort_severity_clicked(self):
        list_task_sort = self.list_task.copy()
        list_complexity_sort = self.list_complexity.copy()


        n = len(list_complexity_sort)
        for i in range(n):
            for j in range(0, n-i-1):
                if list_complexity_sort[j] > list_complexity_sort[j+1]:
                    list_complexity_sort[j], list_complexity_sort[j+1] = list_complexity_sort[j+1], list_complexity_sort[j]
                    list_task_sort[j], list_task_sort[j+1] = list_task_sort[j+1], list_task_sort[j]
        
        list_task_sort.reverse()
        self.listwidget_task.clear()
        self.listwidget_task.addItems(list_task_sort)

        self.sort_alphabetically.setEnabled(True)
        self.sort_priority.setEnabled(True)
        self.sort_severity.setEnabled(False)
    
    def sort_priority_clicked(self):
        list_task_sort = self.list_task.copy()
        list_priorities_sort = self.list_priorities.copy()


        n = len(list_priorities_sort)
        for i in range(n):
            for j in range(0, n-i-1):
                if list_priorities_sort[j] > list_priorities_sort[j+1]:
                    list_priorities_sort[j], list_priorities_sort[j+1] = list_priorities_sort[j+1], list_priorities_sort[j]
                    list_task_sort[j], list_task_sort[j+1] = list_task_sort[j+1], list_task_sort[j]

        list_task_sort.reverse()
        self.listwidget_task.clear()
        self.listwidget_task.addItems(list_task_sort)

        self.sort_severity.setEnabled(True)
        self.sort_alphabetically.setEnabled(True)
        self.sort_priority.setEnabled(False)

#########################################################################################

    def button_task_create_clicked(self):
        self.new_task.setText('')
        self.button_create.setText("Создать")
        self.new_task.setPlaceholderText("Введите название задачи")
        hiding_widgets(self.new_task_m, True)
        hiding_widgets(self.list_task_m, False)
        hiding_widgets(self.tasks_text_m, False)
        hiding_widgets(self.setting_m, False)
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.create_profile_m, False)
        hiding_widgets(self.change_profile_name_m, False)
        hiding_widgets(self.change_password_m, False)
        hiding_widgets(self.setting_menu_m, False)
        self.message.setVisible(False)

        self.complexity_task.setValue(0)
        self.priority_task.setValue(0)
        self.checkbox_complexity_task.setChecked(False)
        self.checkbox_priority_task.setChecked(False)

    def button_save_clicked(self):
        with open(f"task_process/{self.PROFILE}/{self.s}.txt", "w", encoding = "utf-8") as file:
            file.write(self.tasks_text.toPlainText())

    def button_task_setting_clicked(self):
        self.new_task.setText(self.s)
        self.message.setText('')
        self.tasks_title_create.setText(self.s)
        self.button_create.setText("Сохранить")
        self.new_task.setPlaceholderText("Введите новое название задачи")
        
        self.complexity_task.setValue(0)
        self.checkbox_complexity_task.setChecked(False)
        self.priority_task.setValue(0)
        self.checkbox_priority_task.setChecked(False)

        v = self.list_task.index(self.s)

        self.create_copy.setChecked(False)

        if self.list_complexity[v] != -1:
            self.complexity_task.setValue(self.list_complexity[v])
            self.checkbox_complexity_task.setChecked(True)

        if self.list_priorities[v] != -1:
            self.priority_task.setValue(self.list_priorities[v])
            self.checkbox_priority_task.setChecked(True)

        hiding_widgets(self.new_task_m, True)
        hiding_widgets(self.setting_m, True)
        hiding_widgets(self.list_task_m, False)
        hiding_widgets(self.tasks_text_m, False)

    def button_delete_clicked(self):
        with open(f"task_process/{self.PROFILE}/{self.s}.txt", "w", encoding = "utf-8") as file:
            file.write("")
        self.tasks_text.setPlainText("")

    def button_task_delete_clicked(self):
        if self.s != '':
            if self.s in self.list_task:
                t = self.list_task.index(self.s)

                self.list_task.remove(self.s)

                self.list_complexity.pop(t)
                self.list_priorities.pop(t)

                os. remove(f"task_process/{self.PROFILE}/{self.s}.txt")

                with open(f"task_process/{self.PROFILE}/task_list.txt", "w", encoding = "utf-8") as file:
                    file.write("")
                
                with open(f"task_process/{self.PROFILE}/task_list.txt", "a", encoding = "utf-8") as file:
                    for i in range(len(self.list_task)):
                        v = f"{self.list_task[i]}|{self.list_complexity[i]}|{self.list_priorities[i]}"
                        if i != len(self.list_task) - 1:
                            file.write(v + '\n')
                        else: file.write(v)

            hiding_widgets(self.tasks_text_m, False)
            hiding_widgets(self.new_task_m, False)
            hiding_widgets(self.setting_m, False)

#########################################################################################

    def button_create_clicked(self):
        self.message.setVisible(True)
        black_list = ['/', ':', '\\', '*', '?', '"', '<', '>', '|', '+',]
        good = True

        v = self.new_task.text().strip()

        for i in range(len(black_list)):
            if black_list[i] in v:
                good = False
                break

        if v == "":
            self.message.setText("Поле ввода не должно быть пустым")
        elif good == False:
            self.message.setText("Содержит недопустимые символы: " + ''.join(map(str, black_list)))
        elif v == "task_list":
            self.message.setText("Это имя может нарушить работу приложения")
        elif v in self.list_task and self.button_create.text() == "Создать":
            self.message.setText("Такое название здачи уже существует")
        elif v[-1] == ".":
            self.message.setText("Вконце названия задачи не должно быть точек")

        else:
            complexity_task = -1
            priority_task = -1

            if self.checkbox_complexity_task.isChecked() == True:
                complexity_task = self.complexity_task.value()
            if self.checkbox_priority_task.isChecked() == True:
                priority_task = self.priority_task.value()

            if self.button_create.text() == "Создать":
                with open(f"task_process/{self.PROFILE}/task_list.txt", "a", encoding = "utf-8") as file:
                    if len(self.list_task) == 0:
                        file.write(f"{v}|{complexity_task}|{priority_task}")
                    else:
                        file.write(f"\n{v}|{complexity_task}|{priority_task}")

                self.listwidget_task.addItems([v])
                self.list_task.append(v)

                self.list_complexity.append(int(complexity_task))
                self.list_priorities.append(int(priority_task))

                hiding_widgets(self.new_task_m, False)

            elif self.button_create.text() == "Сохранить":
                t = self.list_task.index(self.s)

                if v != self.s:
                    self.list_task[t] = v

                    with open(f"task_process/{self.PROFILE}/{self.s}.txt", "r", encoding = "utf-8") as file:
                        list = file.readlines()
                    with open(f"task_process/{self.PROFILE}/{v}.txt", "w", encoding = "utf-8") as file:
                        for i in range(len(list)):
                            file.write(list[i])

                    os.remove(f"task_process/{self.PROFILE}/{self.s}.txt")

                self.list_complexity[t] = int(complexity_task)
                self.list_priorities[t] = int(priority_task)

                if self.create_copy.isChecked() == True:
                    j = 1
                    
                    while f"{self.list_task[t]}({j})" in self.list_task:
                        j += 1

                    self.list_task.append(f"{self.list_task[t]}({j})")
                    self.list_complexity.append(int(complexity_task))
                    self.list_priorities.append(int(priority_task))

                    with open(f"task_process/{self.PROFILE}/{self.s}.txt", "r", encoding = "utf-8") as file:
                        list = file.readlines()
                    with open(f"task_process/{self.PROFILE}/{self.list_task[t]}({j}).txt", "w", encoding = "utf-8") as file:
                        for i in range(len(list)):
                            file.write(list[i])

                with open(f"task_process/{self.PROFILE}/task_list.txt", "w", encoding = "utf-8") as file:
                    file.write("")
                        
                with open(f"task_process/{self.PROFILE}/task_list.txt", "a", encoding = "utf-8") as file:
                    for i in range(len(self.list_task)):
                        v = f"{self.list_task[i]}|{self.list_complexity[i]}|{self.list_priorities[i]}"
                        if i != len(self.list_task) - 1:
                            file.write(v + '\n')
                        else: file.write(v)

                hiding_widgets(self.setting_m, False)
                hiding_widgets(self.new_task_m, False)
                hiding_widgets(self.tasks_text_m, True)

#########################################################################################
    
    def button_create_profile_clicked(self):
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.create_profile_m, True)
        self.line_profile.setPlaceholderText("Введите имя профиля")
        self.line_password_1.setPlaceholderText("Введите пароль")
        self.line_password_2.setPlaceholderText("Введите пароль ещё раз")
        self.line_profile.setText('')
        self.line_password_1.setText('')
        self.line_password_2.setText('')

    def create_profile_clicked(self):
        self.message.setVisible(True)
        black_list = ['/', ':', '\\', '*', '?', '"', '<', '>', '|', '+',]
        good = True

        v = self.line_profile.text().strip()

        for i in range(len(black_list)):
            if black_list[i] in v:
                good = False
                break

        if v == "":
            self.message.setText("Поле ввода не должно быть пустым")
        elif good == False:
            self.message.setText("Содержит недопустимые символы: " + ''.join(map(str, black_list)))
        elif not self.line_password_1.text() == self.line_password_2.text():
            self.message.setText("Пароли не совпадают")
        elif self.line_password_1.text().strip() == '':
            self.message.setText("Поле ввода пароля не должно быть пустым")
        elif len(self.line_password_1.text().strip()) < 8:
            self.message.setText("Пароль должен содержать больше 8 символов")
        elif v in self.PROFILE_list:
            self.message.setText("Такое имя профиля уже существует")
        else:
            with open(f"task_process/PROFILE_list.txt", "a", encoding = "utf-8") as file:
                b = f"{v}|{hashlib.md5(self.line_password_1.text().encode()).hexdigest()}"
                if len(self.PASSWORD_list) == 0:
                    file.write(b)
                else:
                    file.write('\n' + b)

            self.PROFILE = v
            self.PROFILE_list.append(v)
            self.PASSWORD_list.append(hashlib.md5(self.line_password_1.text().encode()).hexdigest())
            self.profile_name.setText(self.PROFILE)

            if not os.path.exists(f"task_process/{self.PROFILE}"):
                os.mkdir(f"task_process/{self.PROFILE}")
            if os.path.exists(f"task_process/{self.PROFILE}/task_list.txt"):
                with open(f"task_process/{self.PROFILE}/task_list.txt", "w", encoding = "utf-8") as file:
                    pass

            self.list_task = []
            self.list_complexity = []
            self.list_priorities = []

            self.listwidget_task.addItems(self.list_task)

            hiding_widgets(self.create_profile_m, False)
            self.message.setVisible(False)
            hiding_widgets(self.profile_menu_m, True)

#########################################################################################

    def button_login_profile_clicked(self):
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.menu_m, False)
        hiding_widgets(self.login_profile_m, True)
        self.line_profile.setPlaceholderText("Введите имя профиля")
        self.line_password_1.setPlaceholderText("Введите пароль")
        self.line_profile.setText('')
        self.line_password_1.setText('')

    def login_profile_clicked(self):
        self.message.setVisible(True)
        v = self.line_profile.text().strip()

        if v in self.PROFILE_list:
            t = self.PROFILE_list.index(v)
            if not self.PASSWORD_list[t] == hashlib.md5(self.line_password_1.text().encode()).hexdigest():
                self.message.setText("Неверный логин или пароль")
            else:
                self.PROFILE = v
                self.message.setVisible(False)
                hiding_widgets(self.login_profile_m, False)
                hiding_widgets(self.menu_m, True)

                if not os.path.exists(f"task_process/{self.PROFILE}"):
                    os.mkdir(f"task_process/{self.PROFILE}")

                self.list_task = []
                self.list_complexity = []
                self.list_priorities = []

                if os.path.exists(f"task_process/{self.PROFILE}/task_list.txt"):
                    with open(f"task_process/{self.PROFILE}/task_list.txt", "r", encoding = "utf-8") as file:
                        list_1 = file.readlines()
                        list_1 = [line.rstrip() for line in list_1]

                        for i in range(len(list_1)):  
                            list_2 = list_1[i].split("|")
                            self.list_task.append(list_2[0])
                            self.list_complexity.append(int(list_2[1]))
                            self.list_priorities.append(int(list_2[2]))
                else:
                    with open(f"task_process/{self.PROFILE}/task_list.txt", "w", encoding = "utf-8") as file:
                        pass

                self.listwidget_task.addItems(self.list_task)

        else: self.message.setText("Неверный логин или пароль")

    def login_guest_clicked(self):
        self.PROFILE = self.PROFILE_defolt
        self.message.setVisible(False)
        hiding_widgets(self.login_profile_m, False)
        hiding_widgets(self.menu_m, True)

        self.list_task = []
        self.list_complexity = []
        self.list_priorities = []

        if os.path.exists(f"task_process/{self.PROFILE}/task_list.txt"):
            with open(f"task_process/{self.PROFILE}/task_list.txt", "r", encoding = "utf-8") as file:
                list_1 = file.readlines()
                list_1 = [line.rstrip() for line in list_1]

            for i in range(len(list_1)):  
                list_2 = list_1[i].split("|")
                self.list_task.append(list_2[0])
                self.list_complexity.append(int(list_2[1]))
                self.list_priorities.append(int(list_2[2]))
        else:
            with open(f"task_process/{self.PROFILE}/task_list.txt", "w", encoding = "utf-8") as file:
                pass

        self.listwidget_task.addItems(self.list_task)

#########################################################################################

    def change_profile_name_clicked(self):
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.change_profile_name_m, True)
        self.line_profile.setPlaceholderText("Введите новое имя профиля")
        self.line_profile.setText('')

    def save_profile_clicked(self):
        self.message.setVisible(True)
        black_list = ['/', ':', '\\', '*', '?', '"', '<', '>', '|', '+',]
        good = True

        v = self.line_profile.text().strip()

        for i in range(len(black_list)):
            if black_list[i] in v:
                good = False
                break

        if v == "":
            self.message.setText("Поле ввода не должно быть пустым")
        elif good == False:
            self.message.setText("Содержит недопустимые символы: " + ''.join(map(str, black_list)))
        elif v in self.PROFILE_list:
            self.message.setText("Такое имя профиля уже существует")
        else:
            os.rename(f"task_process/{self.PROFILE}",f"task_process/{v}")

            t = self.PROFILE_list.index(self.PROFILE)
            self.PROFILE_list[t] = v
            self.PROFILE = self.PROFILE_list[t]

            with open(f"task_process/PROFILE_list.txt", "w", encoding = "utf-8") as file:
                file.write('')

            with open(f"task_process/PROFILE_list.txt", "a", encoding = "utf-8") as file:
                for i in range(len(self.PROFILE_list)):
                    v = f"{self.PROFILE_list[i]}|{self.PASSWORD_list[i]}"
                    if i == 0:
                        file.write(v)
                    else:
                        file.write('\n' + v)

            self.profile_name.setText(self.PROFILE)

            hiding_widgets(self.change_profile_name_m, False)
            self.message.setVisible(False)

            hiding_widgets(self.profile_menu_m, True)

#########################################################################################

    def change_password_clicked(self):
        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.change_password_m, True)

        self.line_profile.setPlaceholderText("Введите старый пароль")
        self.line_password_1.setPlaceholderText("Введите новый пароль")
        self.line_password_2.setPlaceholderText("Введите новый пароль ещё раз")

        self.line_profile.setText('')
        self.line_password_1.setText('')
        self.line_password_2.setText('')

    def save_password_clicked(self):
        self.message.setVisible(True)

        t = self.PROFILE_list.index(self.PROFILE)

        if  not hashlib.md5(self.line_profile.text().encode()).hexdigest() == self.PASSWORD_list[t]:
            self.message.setText("Пароль не верный")
        elif len(self.line_password_1.text().strip()) < 8:
            self.message.setText("Пароль должен содержать больше 8 символов")
        elif self.line_password_1.text().strip() == '':
            self.message.setText("Поле ввода пароля не должно быть пустым")
        elif not self.line_password_1.text() == self.line_password_2.text():
            self.message.setText("Пароли не совпадают")
        elif self.line_password_1.text() == self.line_profile.text():
            self.message.setText("Новый пароль не должен совпадать со стрым")
        else:
            self.PASSWORD_list[t] = hashlib.md5(self.line_password_1.text().encode()).hexdigest()

            with open(f"task_process/PROFILE_list.txt", "w", encoding = "utf-8") as file:
                file.write('')

            with open(f"task_process/PROFILE_list.txt", "a", encoding = "utf-8") as file:
                for i in range(len(self.PROFILE_list)):
                    b = f"{self.PROFILE_list[i]}|{self.PASSWORD_list[i]}"
                    if i == 0:
                        file.write(b)
                    else:
                        file.write('\n' + b)

            hiding_widgets(self.change_password_m, False)
            self.message.setVisible(False)

            hiding_widgets(self.profile_menu_m, True)

#########################################################################################

    def button_delete_profile_clicked(self):
        t = self.PROFILE_list.index(self.PROFILE)

        shutil.rmtree(f"task_process/{self.PROFILE}")

        self.PROFILE_list.pop(t)
        self.PASSWORD_list.pop(t)

        with open(f"task_process/PROFILE_list.txt", "w", encoding = "utf-8") as file:
            file.write('')

        with open(f"task_process/PROFILE_list.txt", "a", encoding = "utf-8") as file:
            for i in range(len(self.PROFILE_list)):
                b = f"{self.PROFILE_list[i]}|{self.PASSWORD_list[i]}"
                if i == 0:
                    file.write(b)
                else:
                    file.write('\n' + b)

        hiding_widgets(self.profile_menu_m, False)
        hiding_widgets(self.menu_m, False)
        hiding_widgets(self.login_profile_m, True)
        self.line_profile.setText('')
        self.line_password_1.setText('')

#########################################################################################

    def save_setting_clicked(self):
        self.button_size_p = self.button_size_s[self.combobox_button_size.currentText()]
        self.text_size_p = self.text_size_s[self.combobox_text_size.currentText()]

        button_size(self.button_m, self.button_size_p)
        button_text(self.text_m, self.text_size_p)
        
        k = self.size_m.index(self.text_size_s_v[self.text_size_p]) + 1
        t = self.size_m.index(self.button_size_s_v[self.button_size_p]) + 1

        if t > k: self.setMinimumSize (235 * k , 140 * t )
        else: self.setMinimumSize (235 * k , 140 * k )

        self.listwidget_task.setFixedWidth(100 * k )
        self.new_task.setMinimumWidth(110 * k )

        self.complexity_task.setFixedWidth(25 * k )
        self.label_complexity_task.setFixedWidth(90 * k + 8)
        self.priority_task.setFixedWidth(25 * k)
        self.label_priority_task.setFixedWidth(90 * k + 8)

        self.label_create_copy.setFixedWidth(112 * k )


        with open(f"task_process/setting.txt", "w", encoding = "utf-8") as file:
            file.write(f'{self.button_size_p}\n{self.text_size_p}')
        hiding_widgets(self.setting_menu_m, False)

    def default_setting_clicked(self):
        self.button_size_p = 40
        self.text_size_p = 8

        button_size(self.button_m, self.button_size_p)
        button_text(self.text_m, self.text_size_p)

        self.setMinimumSize (470, 240)

        self.listwidget_task.setFixedWidth(200)
        self.new_task.setMinimumWidth(250)

        self.complexity_task.setFixedWidth(50)
        self.label_complexity_task.setFixedWidth(180)
        self.priority_task.setFixedWidth(50)
        self.label_priority_task.setFixedWidth(180)

        self.label_create_copy.setFixedWidth(236)

        with open(f"task_process/setting.txt", "w", encoding = "utf-8") as file:
            file.write(f'{self.button_size_p}\n{self.text_size_p}')
        hiding_widgets(self.setting_menu_m, False)

#########################################################################################

class MainWindow(QMainWindow, widget):
    def __init__(self):
        super(MainWindow, self).__init__()  
        self.show()                                     #Создание окна
        self.setWindowTitle("Efficiency Hub")
        self.setWindowIcon(QIcon("img/application-logo.ico"))
        self.setCentralWidget(self.Table)

#########################################################################################

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()