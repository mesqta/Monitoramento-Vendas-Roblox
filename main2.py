import pyautogui
import time

print("Posicione o mouse no local desejado. Capturando em 3 segundos...")
time.sleep(3)
x, y = pyautogui.position()
print(f"Posição do cursor capturada: x={x}, y={y}")