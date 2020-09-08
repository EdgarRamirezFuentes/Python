import logging
''' 
    Se clasifica en 5 níveles:
    - Debug
    - Info
    - Warning (Default)
    - Error
    - Critical
'''
## * El nivel debug solo se recomienda en el desarrollo de la aplicación
logger = logging
logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] -> %(message)s',
                   datefmt='%m/%d/%Y %I:%M:%S%p',
                    handlers=[ ## * Envía los mensajes al archivo seleccionado
                        logging.FileHandler('./BaseDeDatos/capaDatos/capaDatos.log'),
                        logging.StreamHandler()
                   ])

## ! Sólo se muestran los mensajes de warnining para abajo
if __name__ == '__main__': ## * Evita que se ejecuten estos mensajes desde cualquier archivo
    logging.warning('Ocurrió un error en el programa')
    logging.info('Mensaje de información')
    logging.error('Ocurrió un error en la base de datos')
    logging.debug('Se conectó correctamente a la base de datos')