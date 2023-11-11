import flet
def main(pagina):
    texto = ft.text("hashzap")

    popup = ft.AlertDialog()

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

    ft.app(target=main, view=ft.WEB_BROWSER)

