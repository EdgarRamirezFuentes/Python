from Person import Person
from Connection import Connection
from loggerBase import logger

class PersonDAO:
    '''
    DAO (Data Acess Object)
    CRUD (Create-Read-Update-Delete)
    '''    
    __SELECT = "SELECT * FROM persona ORDER BY id_persona"
    __INSERT = "INSERT INTO persona (nombre_persona, email_persona) VALUES(%s,%s)"
    __UPDATE = "UPDATE persona set nombre_persona = %s, email_persona = %s WHERE id_persona = %s"
    __DELETE = "DELETE FROM persona WHERE id_persona = %s"
    
    @classmethod
    def selectAllRows(cls):
        cursor = Connection.getCursor()
        logger.debug(cursor.mogrify(cls.__SELECT))
        cursor.execute(cls.__SELECT)
        people = cursor.fetchall()
        peopleList = []
        for person in people:
            personObject = Person(person[0],person[1], person[2])
            peopleList.append(personObject)
        Connection.disconnect()
        return peopleList
    
    @classmethod
    def insertRow(cls, person):
        try:
            cursor = Connection.getCursor()
            logger.debug(cursor.mogrify(cls.__INSERT))
            cursor.execute(cls.__INSERT, (person.getName(), person.getEmail()))
            Connection.connect().commit()
            logger.debug(f'Inserted row: {person}')
            return cursor.rowcount
        except Exception as ex:
            Connection.connect().rollback()
            logger.error(f"There was an error trying to insert something into the dabase: {ex}")
        finally:
            Connection.disconnect()
            
    @classmethod
    def updateRow(cls, person):
        try:
            cursor = Connection.getCursor()
            logger.debug(cursor.mogrify(cls.__UPDATE))
            cursor.execute(cls.__UPDATE, (person.getName(), person.getEmail(), person.getID()))
            Connection.connect().commit()
            logger.debug(f'Updated row: {person}')
            return cursor.rowcount
        except Exception as ex:
            Connection.connect().rollback()
            logger.error(f"There was an error trying to update a row: {ex}")
        finally:
            Connection.disconnect()
    @classmethod
    def deleteRow(cls, person):
        try:
            cursor = Connection.getCursor()
            logger.debug(cursor.mogrify(cls.__DELETE))
            cursor.execute(cls.__DELETE, (str(person.getID())))
            Connection.connect().commit()
            logger.debug(f'Deleted row: {person}')
            return cursor.rowcount
        except Exception as ex:
            Connection.connect().rollback()
            logger.error(f"There was an error trying to delete a row: {ex}")
        finally:
            Connection.disconnect()
##people = PersonDAO.selectAll()
##for person in people:
##    print(person)
person = Person(8,'Bruce Wayne', "bruce@gmail.com")
##PersonDAO.updateRow(person)
PersonDAO.deleteRow(person)