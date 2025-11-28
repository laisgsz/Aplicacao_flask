import os
# Importa do __init__.py (que é onde o create_app e db costumam estar nessa estrutura)
from __init__ import create_app, db 
# Importa o arquivo models.py direto
from models import User, Role, Curso

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(debug=True)
