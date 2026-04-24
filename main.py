import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os

DATA_FILE = "data/weather_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_record():
    date = date_entry.get()
    try:
        temp = float(temp_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Температура должна быть числом")
        return
    description = desc_entry.get().strip()
    precipitation = "Да" if precip_var.get() else "Нет"

    if not date or not description:
        messagebox.showerror("Ошибка", "Дата и описание обязательны")
        return

    record = {
        "date": date,
        "temperature": temp,
        "description": description,
        "precipitation": precipitation
    }
    records.append(record)
    save_data(records)
    update_listbox()
    clear_inputs()

def update_listbox(filter_func=None):
    listbox.delete(0, tk.END)
    for rec in (filter_func(records) if filter_func else records):
        listbox.insert(tk.END, f"{rec['date']} | {rec['temperature']}°C | {rec['description']} | Осадки: {rec['precipitation']}")

def filter_by_date():
    target_date = date_filter_entry.get()
    update_listbox(lambda data: [r for r in data if r["date"] == target_date])

def filter_by_temp():
    try:
        threshold = float(temp_filter_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Порог температуры должен быть числом")
        return
    update_listbox(lambda data: [r for r in data if r["temperature"] > threshold])

def clear_inputs():
    date_entry.delete(0, tk.END)
    temp_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    precip_var.set(False)

# Загрузка данных
records = load_data()

# Основное окно
root = tk.Tk()
root.title("Weather Diary")
root.geometry("700x500")

# Вкладки
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Добавить запись")
tab_control.add(tab2, text="Фильтрация")
tab_control.pack(expand=1, fill="both")

# Вкладка 1: Добавление записи
tk.Label(tab1, text="Дата:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(tab1, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab1, text="Температура (°C):").grid(row=1, column=0, padx=5, pady=5)
temp_entry = tk.Entry(tab1)
temp_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(tab1, text="Описание:").grid(row=2, column=0, padx=5, pady=5)
desc_entry = tk.Entry(tab1)
desc_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(tab1, text="Осадки:").grid(row=3, column=0, padx=5, pady=5)
precip_var = tk.BooleanVar()
tk.Checkbutton(tab1, text="Да", variable=precip_var).grid(row=3, column=1, padx=5, pady=5)

tk.Button(tab1, text="Добавить запись", command=add_record).grid(row=4, columnspan=2, pady=10)

# Список записей
listbox = tk.Listbox(root, width=80, height=15)
listbox.pack(pady=10)
update_listbox()

# Вкладка 2: Фильтрация
tk.Label(tab2, text="Фильтр по дате (ГГГГ-ММ-ДД):").grid(row=0, column=0, padx=5, pady=5)
date_filter_entry = tk.Entry(tab2)
date_filter_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(tab2, text="Фильтровать по дате", command=filter_by_date).grid(row=0, column=2, padx=5, pady=5)

tk.Label(tab2, text="Фильтр по температуре (>°C):").grid(row=1, column=0, padx=5, pady=5)
temp_filter_entry = tk.Entry(tab2)
temp_filter_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(tab2, text="Фильтровать по температуре", command=filter_by_temp).grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
