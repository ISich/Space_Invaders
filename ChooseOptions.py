from GraphicalInterface import GraphicalInterface
from tkinter import *


class ChooseOptionsMenu:
    def __init__(self):
        self.window = None
        self.records = []
        self.parse_records()
        self.make_options_menu()

    def parse_records(self):
        with open("records.txt") as f:
            records = f.readlines()
            for i in range(len(records)):
                self.records.append(records[i][:-1])

    def make_options_menu(self):
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.grab_set()
        self.window.geometry("350x250")
        self.window.title("Space Invaders")
        self.draw_menu()

    def draw_menu(self):
        menu_label = Label(self.window, text="Space Invaders", font=("Roboto", 20))
        menu_label.pack(side=TOP, pady=10)
        choose_lvl_button = Button(self.window, text="Выбрать уровень", width=20, font=("Roboto", 14),
                                   command=lambda: self.choose_level())
        choose_lvl_button.pack(side=TOP, pady=10)
        records_button = Button(self.window, text="Таблица рекордов", width=20, font=("Roboto", 14),
                                command=lambda: self.open_record_table())
        records_button.pack(side=TOP, pady=10)

    def open_record_table(self):
        record_table = Toplevel(self.window)
        record_table.resizable(False, False)
        record_table.geometry("300x200")
        record_table.grab_set()

        main_label = Label(record_table, text="Таблица рекордов", font=("Roboto", 20, "bold"))
        first_lvl_label = Label(record_table, text="Уровень 1", font=("Roboto", 14))
        second_lvl_label = Label(record_table, text="Уровень 2", font=("Roboto", 14))
        third_lvl_label = Label(record_table, text="Уровень 3", font=("Roboto", 14))
        first_lvl_record = Label(record_table, text=f"{self.records[0]}", font=("Roboto", 14))
        second_lvl_record = Label(record_table, text=f"{self.records[1]}", font=("Roboto", 14))
        third_lvl_record = Label(record_table, text=f"{self.records[2]}", font=("Roboto", 14))

        main_label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)
        first_lvl_label.grid(row=1, column=0, padx=5, pady=5)
        second_lvl_label.grid(row=2, column=0, padx=5, pady=5)
        third_lvl_label.grid(row=3, column=0, padx=5, pady=5)
        first_lvl_record.grid(row=1, column=1, padx=5, pady=5)
        second_lvl_record.grid(row=2, column=1, padx=5, pady=5)
        third_lvl_record.grid(row=3, column=1, padx=5, pady=5)

    def choose_level(self):
        choose_level_window = Toplevel(self.window)
        choose_level_window.geometry("300x300")
        choose_level_window.resizable(False, False)
        choose_level_window.grab_set()

        lvl_label = Label(choose_level_window, text="Выберите уровень", font=("Roboto", 20, "bold"))
        first_button = Button(choose_level_window, text="Уровень 1", font=("Roboto", 14), width=40,
                              command=lambda: self.start_game(0, choose_level_window))
        second_button = Button(choose_level_window, text="Уровень 2", font=("Roboto", 14), width=40,
                               command=lambda: self.start_game(1, choose_level_window))
        third_button = Button(choose_level_window, text="Уровень 3", font=("Roboto", 14), width=40,
                              command=lambda: self.start_game(2, choose_level_window))
        cancel_button = Button(choose_level_window, text="Отмена", font=("Roboto", 10), width=5,
                               command=choose_level_window.destroy)

        lvl_label.pack(side=TOP, pady=10)
        first_button.pack(side=TOP, pady=10, padx=10)
        second_button.pack(side=TOP, pady=10, padx=10)
        third_button.pack(side=TOP, pady=10, padx=10)
        cancel_button.place(x=240, y=250)

    def start_game(self, picked_level, window):
        window.destroy()
        self.window.destroy()
        borders = [0, 2, 3]
        enemy_count = [15, 25, 30]
        game = GraphicalInterface(enemy_count[picked_level], borders[picked_level], picked_level,
                                  self)
        game.start()

    def check_new_record(self, level: int, new_time):
        if self.records[level] == "-" or float(self.records[level]) > new_time:
            self.records[level] = round(new_time, 3)
            self.save_record()

    def save_record(self):
        with open("records.txt", "w") as f:
            f.truncate()
            for i in range(len(self.records)):
                f.write(f"{self.records[i]}\n")

    def run(self):
        self.window.mainloop()
