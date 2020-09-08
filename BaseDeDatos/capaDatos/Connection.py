from loggerBase import logger
import psycopg2
import sys

class Connection:
    __DATABASE = 'test_db'
    __USERNAME = 'edgar-dev'
    __PASSWORD = '2014131046'
    __DBPORT = '5432'
    __HOST = 'localhost'
    __CONNECTION = None
    __CURSOR = None
    @classmethod
    def connect(cls):
        if cls.__CONNECTION is None:
            try:
                cls.__CONNECTION = psycopg2.connect(
                    host=cls.__HOST, 
                    user=cls.__USERNAME, 
                    password=cls.__PASSWORD, 
                    port=cls.__DBPORT, 
                    database=cls.__DATABASE)
                logger.info(f'Database connected successfully: {cls.__CONNECTION}')
                return cls.__CONNECTION
            except Exception as ex:
                logger.error(f'There was an error trying to connect to the database: {ex}')
                sys.exit()
        else:
            return cls.__CONNECTION
    
    @classmethod 
    def getCursor(cls):
        if cls.__CURSOR is None:
            try:
                cls.__CURSOR = cls.connect().cursor()
                logger.info(f'Cursor obtained successfully: {cls.__CURSOR}')
                return cls.__CURSOR
            except Exception as ex:
                logger.error(f'There was an error trying to get a cursor: {ex}')
                sys.exit()
        else:
            return cls.__CURSOR
            
    @classmethod
    def disconnect(cls):
            if cls.__CURSOR is not None:
                try:
                    cls.__CURSOR.close()
                    logger.info('Cursor closed successfully')
                except Exception as ex:
                    logger.error(f'There was an error trying to close the cursor: {ex}')
            if cls.__CONNECTION is not None:
                try:
                    cls.__CONNECTION.close()
                    logger.info('Database connection closed successfully')
                except Exception as ex:
                    logger.error(f'There was an error trying to close the database connection: {ex}')
