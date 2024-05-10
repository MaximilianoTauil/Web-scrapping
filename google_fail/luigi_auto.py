import luigi
import subprocess

class EjecutarScript1(luigi.Task):
    def run(self):
        
        ruta_al_script = "web_scrap.py"

        # Ejecutar el script utilizando subprocess
        subprocess.run(["python", ruta_al_script])
        print("Ejecutando script 1")

class EjecutarScript2(luigi.Task):
    def requires(self):
        return EjecutarScript1()

    def run(self):
        # Código para ejecutar el segundo script
        print("Ejecutando script 2")

class PushGitHub(luigi.Task):
    def requires(self):
        return EjecutarScript2()

    def run(self):
        # Código para realizar el push a GitHub
        print("Realizando push a GitHub")
        subprocess.run(["git", "push"])
