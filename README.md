# Random Quote Generator — пошаговая инструкция по созданию приложения

## 1. Структура проекта

Создайте папку `quote_generator`, внутри которой расположите:
- файл `main.py` — основной код приложения;
- файл `quotes.json` — хранилище цитат и истории;
- файл `.gitignore` — исключение временных файлов;
- файл `README.md` — документация.

## 2. Основной код (`main.py`)

```python
import tkinter as tk
from tkinter import ttk, messagebox
import json
import random

QUOTES_FILE = 'quotes.json'

def load_quotes():
    try:
        with open(QUOTES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'quotes': [], 'history': []}

def save_quotes(data):
    with open(QUOTES_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def generate_quote():
    quotes = quote_data['quotes']
    filtered_quotes = quotes.copy()
    
    author_filter = entry_author.get()
    theme_filter = entry_theme.get()
    
    if author_filter:
        filtered_quotes = [q for q in filtered_quotes if q['author'].lower() == author_filter.lower()]
    if theme_filter:
        filtered_quotes = [q for q in filtered_quotes if q['theme'].lower() == theme_filter.lower()]
    
    if not filtered_quotes:
        messagebox.showinfo("Внимание", "Нет цитат по данному фильтру!")
        return
    
    selected_quote = random.choice(filtered_quotes)
    label_random_quote.config(text=f"{selected_quote['text']} ({selected_quote['author']})")
    quote_data['history'].append(selected_quote)
    save_quotes(quote_data)
    refresh_history()

def refresh_history():
    history_list.delete(0, tk.END)
    for idx, quote in enumerate(quote_data['history'][::-1]):
        history_list.insert(idx, f"{quote['text']} ({quote['author']})")

# Начальное состояние
quote_data = load_quotes()

# Интерфейс приложения
root = tk.Tk()
root.title("Random Quote Generator")

frame_input = ttk.Frame(root)
frame_input.pack(padx=10, pady=10)

ttk.Label(frame_input, text="Автор:").grid(row=0, column=0, sticky="W")
entry_author = ttk.Entry(frame_input)
entry_author.grid(row=0, column=1, pady=5)

ttk.Label(frame_input, text="Тема:").grid(row=1, column=0, sticky="W")
entry_theme = ttk.Entry(frame_input)
entry_theme.grid(row=1, column=1, pady=5)

btn_generate = ttk.Button(frame_input, text="Сгенерировать цитату", command=generate_quote)
btn_generate.grid(row=2, column=0, columnspan=2, pady=10)

label_random_quote = ttk.Label(frame_input, text="", font=("Arial", 14))
label_random_quote.grid(row=3, column=0, columnspan=2, pady=10)

# История цитат
frame_history = ttk.Frame(root)
frame_history.pack(padx=10, pady=10)

ttk.Label(frame_history, text="История цитат:", font=("Arial", 12)).pack()
history_list = tk.Listbox(frame_history, height=10, width=50)
history_list.pack()

refresh_history()

root.mainloop()
```

## 3. Список цитат (`quotes.json`)

Начните с примера списка цитат в файле `quotes.json`. Этот файл можно расширять новыми цитатами вручную.

```json
{
    "quotes": [
        {
            "text": "Жизнь похожа на книгу: важно не количество страниц, а качество сюжета.",
            "author": "Неизвестный",
            "theme": "Философия"
        },
        {
            "text": "Любовь сильнее смерти и страха смерти.",
            "author": "Лев Толстой",
            "theme": "Литература"
        },
        {
            "text": "Всегда будь собой, выражай себя, верь в себя.",
            "author": "Оскар Уайльд",
            "theme": "Искусство"
        }
    ],
    "history": []
}
```

## 4. Файл `.gitignore`

```bash
__pycache__
*.pyc
*.log
*.swp
*.bak
```

## 5. Файл `README.md`

```markdown
# Random Quote Generator

**Автор:** Александр Сергеев

## Описание программы

Программа генерирует случайные цитаты из предварительно подготовленного набора цитат. Она поддерживает фильтрацию по автору и теме, сохраняет историю сгенерированных цитат и выводит её в списке.

## Инструкция по запуску

1. Убедитесь, что у вас установлен Python 3.x.
2. Скопируйте файлы проекта в одну папку.
3. Запустите программу командой:

```shell
python main.py
```

## Особенности программы

- Возможность фильтровать цитаты по автору и теме.
- Генерация случайной цитаты из доступного набора.
- Хранение истории предыдущих цитат в формате JSON.

## Примеры использования

1. Генерация цитаты без фильтра:
- Нажмите кнопку "Сгенерировать цитату".

2. Выбор цитаты по автору:
- Введите имя автора в соответствующее поле и нажмите кнопку "Сгенерировать цитату".

---

Разработано Александром Сергеевым в учебных целях.
```

## 6. Работа с Git

Чтобы настроить репозиторий и выложить проект на GitHub:

```bash
git init
git add .
git commit -m "Первая версия генератора цитат"
git branch -M main
git remote add origin https://github.com/your_username/quote-generator.git
git push -u origin main
```

Теперь ваше приложение доступно на GitHub.
