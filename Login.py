import flet as ft

def main(page: ft.Page):
    page.title = "Examen Flet"

    #Ejercicio 6
    def comprobardatos(e):
        if tfnombre.value ==tfpassword.value:
            dlg = ft.AlertDialog(title=ft.Text("Usuario y contraseña introducidos correctamente"), on_dismiss=lambda e: print("Usuario y contraseña introducidos correctamente!"))
            page.dialog = dlg
            dlg.open = True
        page.update()
            
    #Fin --- Ejercicio 6


    #Ejercicio 2
    
    img= ft.Image(src=f"fotos/Logo.png", width=150, height=150)
    page.update()
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 500



    tfnombre = ft.TextField(label="Nombre", width=250)
    #Ejercicio 4
    tfpassword = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)

    #Fin --- Ejercicio 4


    #Ejercicio 5
    btnEntrar = ft.ElevatedButton(text="Registrarse", icon=ft.icons.AIRPLANE_TICKET, on_click=comprobardatos) 

    #Fin-- Ejercicio 5


    page.add(img, tfnombre, tfpassword, btnEntrar)


ft.app(target=main,assets_dir="fotos")