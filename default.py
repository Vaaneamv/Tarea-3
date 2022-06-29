SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789' # maneja aspectos de seguridad
PROPAGATE_EXCEPTIONS = True #manejar las excepciones
# Database configuracion
SQLALCHEMY_DATABASE_URI = 'sqlite:///films.sqlite' #base de datos
SQLALCHEMY_TRACK_MODIFICATIONS = False #desactiva como indica la docu
SHOW_SQLALCHEMY_LOG_MESSAGES = False  #deshabilita mensajes de log
ERROR_404_HELP = False #deshabilita las sugerencias de otros endpoints