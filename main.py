import flet as ft
import requests

# Versão atual do aplicativo
CURRENT_VERSION = "v1.0.0"

# URL da API do GitHub para obter a última release
GITHUB_API_URL = "https://api.github.com/repos/antoniellonline/joga-facil-app/releases/latest"

def check_for_updates():
    try:
        response = requests.get(GITHUB_API_URL)
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get("tag_name", CURRENT_VERSION)
            if latest_version != CURRENT_VERSION:
                return f"Nova atualização disponível: {latest_version}. Atualize o aplicativo."
    except Exception as e:
        print("Erro ao verificar atualizações:", e)
    return None

def main(page: ft.Page):
    page.title = "Meu App Flet"
    
    # Checa atualizações ao iniciar
    update_msg = check_for_updates()
    if update_msg:
        page.add(ft.Text(update_msg, color="red", size=16))
    
    # Resto da interface
    page.add(ft.Text("Bem-vindo ao Meu App Flet!"))
    # Adicione outros componentes conforme necessário

ft.app(target=main)
