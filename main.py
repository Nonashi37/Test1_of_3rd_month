import flet as ft 
import datetime 
import os 

def main(page: ft.Page):
    page.title = 'Мое первое приложение На Флет!'
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []


    if os.path.exists("history.txt"):
        file = open("history.txt", "r", encoding="utf-8")
        for line in file.readlines():
            greeting_history.append(line.strip())
        file.close()

    history_text = ft.Text(value="History of greetings: \n" + "\n".join(greeting_history))

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

        
            file = open("history.txt", "a", encoding="utf-8") # "a" means append
            file.write(new_message + "\n")
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
    

        history_text.value = "History of greeting:" 
        page.update() 

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
    delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_Button)

    main_objects = ft.Row([name_input, elevated_button, theme_button, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(text_hello, main_objects, history_text)

ft.app(main)