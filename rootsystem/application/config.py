from os import environ


DB_HOST = "localhost"
DB_USER = "daniel"
DB_PASS = "mysqlroot"
DB_NAME = "mostplayed"
PRIVATE_DIR = ""

DEFAULT_RESOURCE = ""
SHOW_ERROR_404 = False
ROOT_DIR = environ.get("DOCUMENT_ROOT", "/home/daniel/Proyectos/MostPlayed/rootsystem")
STATIC_DIR = "{}/static".format(ROOT_DIR)
