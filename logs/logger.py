import logging
import os
from logging.handlers import RotatingFileHandler

# Criar a pasta de logs caso não exista
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configuração do logger
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Criar um handler de rotação para evitar que o arquivo fique muito grande
handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3, encoding="utf-8")

# Formato do log: [Data e Hora] [Nível] [Nome do Módulo] Mensagem
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s")

handler.setFormatter(formatter)

# Criar logger principal
logger = logging.getLogger("RoboDoc")
logger.setLevel(logging.DEBUG)  # Pode mudar para INFO, WARNING, ERROR...
logger.addHandler(handler)

# Também exibir os logs no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Teste de logs
logger.info("Sistema de logs inicializado!")
