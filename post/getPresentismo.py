from .connectar import getConnect
from datetime import datetime
import pytz

def modificar_presentismo(estado, bloque, tiempo,legajo, fecha):
    e = "'" + estado + "'"
    b = "'" + bloque + "'"
    t = "'" + tiempo + "'"
    l = "'" + legajo + "'"
    f = "'" + fecha + "'"
   
    print(e, b, t, l, f)

    hd = 'select * from api_presencia, api_clase, api_cxmxpxa where api_presencia."IdClase" = api_clase."IdClase" and api_cxmxpxa."IdCMPA" = api_clase."IdCMPA" and "LegajoAlumno" = ' + \
        l + ' and api_cxmxpxa."BloqueDia" = ' + b + ' and api_clase."Fecha" =' + f

    XD = 'update api_presencia set "Estado" = ' + e + ' ,"Tiempo" = ' + t + \
        ' from api_clase, api_cxmxpxa where api_presencia."IdClase" = api_clase."IdClase" and api_cxmxpxa."IdCMPA" = api_clase."IdCMPA" and "LegajoAlumno" = ' + \
        l + ' and api_cxmxpxa."BloqueDia" = ' + b + ' and api_clase."Fecha" =' + f

    try:
        conection = getConnect()
        with conection.cursor() as cursor:
            '''
            existe = cursor.execute()
            print(existe)
            if(existe):
            '''
            cursor.execute(XD)
            print(cursor.rowcount, "Presentimso actualizado")

        # display the PostgreSQL database server version

        conection.commit()

    except Exception as ex:
        raise Exception(ex)

    finally:
        if conection is not None:
            conection.close()
            print('Database connection closed.')
