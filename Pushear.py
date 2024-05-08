import os
from git import Repo

# Ruta al repositorio Git
repo_path = 'C:\Users\Admin\OneDrive\Escritorio\Web-scrapping>'

# Mensaje del commit
commit_message = 'Actualización automática de datos'

# Agregar cambios al área de staging
repo = Repo(repo_path)
repo.git.add('Web_scrapp.parquet')

# Realizar el commit
repo.index.commit(commit_message)

# Hacer push al repositorio remoto
origin = repo.remote(name='origin')
origin.push()
