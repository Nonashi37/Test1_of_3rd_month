import flet as ft 
import datetime 
import os  # realizing task 1

def main(page: ft.Page):
    page.title = 'Мое первое приложение На Флет!'
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []
    favorites = []

    if os.path.exists("history.txt"):
        file = open("history.txt", "r", encoding="utf-8")
        for line in file.readlines():
            greeting_history.append(line.strip())
        file.close()

    history_text = ft.Text(value="History of greetings: \n" + "\n".join(greeting_history))
    favorites_text = ft.Text(value="Favorite names:\n")

    text_hello = ft.Text(value='Как дела')

    def on_click_func(_):
        name = name_input.value

        if name:
            now = datetime.datetime.now()
            time_string = now.strftime("%Y:%m:%d - %H:%M:%S")

            new_message = f"{time_string} - Hello, {name}!"
            
            text_hello.value = f'Приветствую {name}'
            text_hello.color = None

            greeting_history.append(new_message)

            # limit history to last 5 realizing Task 4.
            if len(greeting_history) > 5:
                greeting_history[:] = greeting_history[-5:]

            file = open("history.txt", "w", encoding="utf-8")
            for i in greeting_history:
                file.write(i + "\n")
            file.close()

            name_input.value = None
            history_text.value = "History of greetings: \n" + "\n".join(greeting_history)

        else: 
            text_hello.color = ft.Colors.YELLOW
            text_hello.value = 'Введите Имя, Пж'

        page.update()

    name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)

    def edit_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()
    
    def delete_Button(_):
        greeting_history.clear()
        
        file = open("history.txt", "w", encoding="utf-8")
        file.write("")
        file.close()

        history_text.value = "History of Greeting:" 
        page.update() 

    # morning greetings at realtime if morning add to morning if evening add to evening looking at real time 
    def show_morning(_):
        filtered = []

        for line in greeting_history:
            try:
                time_part = line.split("-")[1].strip()
                hour = int(time_part.split(":")[0])

                if hour < 12:
                    filtered.append(line)
            except:
                pass

        history_text.value = "Morning greetings:\n" + "\n".join(filtered)
        page.update()

    # evening greetings realizing Task 3
    def show_evening(_):
        filtered = []

        for line in greeting_history:
            try:
                time_part = line.split("-")[1].strip()
                hour = int(time_part.split(":")[0])

                if hour >= 12:
                    filtered.append(line)
            except:
                pass

        history_text.value = "Evening greetings:\n" + "\n".join(filtered)
        page.update()

    # add last greeting name to favorites realizing task 2
    def add_favorite(_):
        if len(greeting_history) > 0:
            last = greeting_history[-1]

            try:
                name = last.split("Hello,")[1]
                name = name.replace("!", "").strip()
                favorites.append(name)
            except:
                pass

            favorites_text.value = "Favorite names:\n" + "\n".join(favorites)

        page.update()

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
    delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_Button)

    morning_button = ft.ElevatedButton("Morning greetings", on_click=show_morning)
    evening_button = ft.ElevatedButton("Evening greetings", on_click=show_evening)

    favorite_button = ft.ElevatedButton("Add last to favorites", on_click=add_favorite)

    main_objects = ft.Row([name_input, elevated_button, theme_button, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    filter_row = ft.Row([morning_button, evening_button, favorite_button])

    page.add(text_hello, main_objects, filter_row, history_text, favorites_text)

ft.app(main)



















