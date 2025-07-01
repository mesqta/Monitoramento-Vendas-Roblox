import pytesseract
from PIL import ImageGrab
import schedule
import time
import re
import requests
import pyautogui

# instale: https://codeload.github.com/VirageRoblox/Virage-Grow-A-Garden-Macro/zip/refs/tags/SummerFree
# Configuração do pytesseract (ajuste o caminho se necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# URL da webhook do Discord
WEBHOOK_URL = "link"

def extrair_valor_robusto(texto, palavras_chave):
    """
    Procura por linhas que contenham qualquer palavra-chave e extrai o número mais próximo.
    """
    for linha in texto.split('\n'):
        for chave in palavras_chave:
            if chave in linha.lower():
                # Extrai o primeiro número da linha
                match = re.search(r'([\d.,]+)', linha)
                if match:
                    return linha.strip(), match.group(1)
                return linha.strip(), "VALOR NÃO ENCONTRADO"
    return "NOME NÃO ENCONTRADO", "NÃO ENCONTRADO"

def monitorar():
    # Sempre recarrega o navegador antes de cada captura
    print("Clicando na posição do navegador para garantir o foco...")
    pyautogui.click(x=84, y=54)
    print("Reiniciando navegador com ALT+F5...")
    pyautogui.hotkey('alt', 'f5')
    print("Aguardando 3 minutos para garantir que o navegador carregue completamente...")
    time.sleep(180)  # Aguarda 3 minutos

    print("Capturando tela completa...")
    img = ImageGrab.grab()
    texto = pytesseract.image_to_string(img, lang='eng')

    # Para debug: veja o texto reconhecido
    print("Texto OCR reconhecido:\n", texto)

    # Procura por variações das palavras-chave (sem acento, minúsculo, etc)
    fundos_keys = ["fundos da comunidade", "fundos da comun", "fundos da", "fundos"]
    # Adicione variações para "robux pendentes" para melhorar o OCR
    pendentes_keys = [
        "robux pendentes", "robux penden", "robux pen", "pendentes", "pendente", "robux", "penden"
    ]

    nome_fundos, valor_fundos = extrair_valor_robusto(texto.lower(), fundos_keys)
    nome_pendentes, valor_pendentes = extrair_valor_robusto(texto.lower(), pendentes_keys)

    print(f"{nome_fundos}: {valor_fundos}")
    print(f"{nome_pendentes}: {valor_pendentes}")

    # Monta o embed para o Discord
    embed = {
        "title": "🔄 Monitoramento automático - TheVoid Studio",
        "color": 0x5865F2,
        "fields": [
            {
                "name": "💰 Fundos da comunidade",
                "value": f"{valor_fundos} Robux",
                "inline": False
            },
            {
                "name": "⏳ Robux pendentes",
                "value": f"{valor_pendentes} Robux",
                "inline": False
            }
        ],
        "footer": {
            "text": "Atualização automática via OCR"
        }
    }

    print("Enviando mensagem ao Discord via webhook (embed)...")
    data = {"embeds": [embed]}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204 or response.status_code == 200:
        print("Mensagem enviada com sucesso!\n")
    else:
        print(f"Falha ao enviar mensagem! Status: {response.status_code}\n")

# Agenda a função para rodar a cada 5 minutos, sempre recarregando o navegador antes de capturar
schedule.every(5).minutes.do(monitorar)

print("Monitoramento iniciado! O script enviará atualizações a cada 5 minutos.")
print("Você tem 5 segundos para abrir o navegador e o Discord na posição correta...")
time.sleep(5)

# Executa uma vez imediatamente ao iniciar, já recarregando o navegador
monitorar()

while True:
    schedule.run_pending()
    time.sleep(1)