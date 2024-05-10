import subprocess
import sys

def ejecutar_scripts():
    try:
        # Ejecutar el script de recopilación de datos
        print("Ejecutando el script de recopilación de datos...")
        subprocess.run(["python", "web_scrap.py"], check=True)
        print("Script de recopilación de datos finalizado exitosamente.")

        # Ejecutar el script de Streamlit
        print("Ejecutando el script de Streamlit...")
        subprocess.run(["python", "app.py"], check=True)
        print("Script de Streamlit finalizado exitosamente.")

        # Ejecutar el script de deploy
        print("Ejecutando el script de deploy en Streamlit...")
        subprocess.run(["python", "streamlit_deploy.py"], check=True)
        print("Script de deploy en Streamlit finalizado exitosamente.")

    except subprocess.CalledProcessError as e:
        print(f"Error durante la ejecución del script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_scripts()
