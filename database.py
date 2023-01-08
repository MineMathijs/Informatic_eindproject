import sqlite3
import numpy as np


def update_vakken(vakid: int, vaknaam: str, vakuur: int):

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS vakken (
                vakid INTEGER UNIQUE,
                vaknaam TEXT,
                vakuur INTEGER
            );
        """)
        try:
            c.execute("""
                REPLACE INTO vakken (vakid, vaknaam, vakuur) 
                VALUES (?,?,?)
            """, (vakid, vaknaam, vakuur))
            print("Sucsesfully updated database vakken")
        except:
            print("error with insering data into vakken")


def delete_vakken():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                DELETE from vakken
            """)
            print("alles in vakken is succesvol verwijderd")
        except:
            print("niet alles in vakken is verwijderd")


def get_vakken():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                SELECT *
                FROM vakken
            """)
            datalist = c.fetchall()
            data = np.array(datalist)
            print("vakken opgehaalt")
        except:
            print("kon vakken niet ophalen")
        else:
            return data


def check_vakken():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                SELECT COUNT(vakid)
                FROM vakken
            """)
            count = int(c.fetchall()[0][0])
            print("vakken geteld")
        except:
            print("kon vakken niet vinden")
        else:
            return count


def update_daguur(dagen: int, uuren_per_dag: int):

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS daguur (
                id INTEGER UNIQUE,
                dagen INTEGER,
                uuren_per_dag INTEGER
            );
        """)
        try:
            c.execute("""
                REPLACE INTO daguur (id, dagen, uuren_per_dag) 
                VALUES (1,?,?)
            """, (dagen, uuren_per_dag))
            print("Sucsesfully updated database daguur")
        except:
            print("error with insering data into daguur")


def update_leerlingen(leerlingnmr: int, voornaam: str, achternaam: int, vakken: list):

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS leerlingen (
                leerlingnmr INTEGER UNIQUE,
                voor_naam TEXT,
                achter_naam TEXT,
                vakken BLOB
            );
        """)
        try:
            c.execute("""
                REPLACE INTO leerlingen (leerlingnmr, voor_naam, achter_naam, vakken)
                VALUES (?,?,?,?)
            """, (leerlingnmr, voornaam, achternaam, vakken))
            print("Sucsesfully updated database leerlingen")
        except:
            print("error with insering data into leerlingen")


# def update_vakuur(u1, u2, u3, u4, u5, u6, u7, u8, u9, u10):

#     conn = sqlite3.connect("gegevens.db")

#     with conn:
#         c = conn.cursor()
#         c.execute("""
#             CREATE TABLE IF NOT EXISTS vakuur (
#                 ID INTEGER UNIQUE,
#                 u1 INTEGER,
#                 u2 INTEGER,
#                 u3 INTEGER,
#                 u4 INTEGER,
#                 u5 INTEGER,
#                 u6 INTEGER,
#                 u7 INTEGER,
#                 u8 INTEGER,
#                 u9 INTEGER,
#                 u10 INTEGER
#             );
#         """)
#         try:
#             c.execute("""
#                 REPLACE INTO vakuur (id,u1,u2,u3,u4,u5,u6,u7,u8,u9,u10)
#                 VALUES (1,?,?,?,?,?,?,?,?,?,?)
#             """, (u1, u2, u3, u4, u5, u6, u7, u8, u9, u10))
#             print("Sucsesfully updated database vakuur")
#         except:
#             print("error with insering data into vakuur")


def delete_tables():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                DROP TABLE IF EXISTS daguur
            """)
            print("daguur is succesvol verwijderd")
        except:
            print("daguur kon niet worden verwijderd")

        try:
            c.execute("""
                DROP TABLE IF EXISTS leerlingen
            """)
            print("leerlingen is succesvol verwijderd")
        except:
            print("leerlingen kon niet worden verwijderd")

        try:
            c.execute("""
                DROP TABLE IF EXISTS vakuur
            """)
            print("vakuur is succesvol verwijderd")
        except:
            print("vakuur kon niet worden verwijderd")


def check_tables():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                SELECT *
                FROM daguur
            """)
            print("daguur bestaat")
        except:
            print("daguur bestaat niet")
            return False

        # try:
        #     c.execute("""
        #         SELECT *
        #         FROM vakuur
        #     """)
        #     print("vakuur bestaat")
        # except:
        #     print("vakuur bestaat niet")
        #     return False

        try:
            c.execute("""
                SELECT *
                FROM leerlingen
            """)
            print("leerlingen bestaat")
        except:
            print("leerlingen bestaat niet")
            return False
        else:
            return True


def get_daguur():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                SELECT *
                FROM daguur
                LIMIT 1
            """)
            datalist = c.fetchall()
            data = np.array(datalist[0])
            print("daguur opgehaalt")
        except:
            print("kon daguur niet ophalen")
        else:
            return data


# def get_vakuur():

#     conn = sqlite3.connect("gegevens.db")

#     with conn:
#         c = conn.cursor()

#         try:
#             c.execute("""
#                 SELECT *
#                 FROM vakuur
#                 LIMIT 1
#             """)
#             datalist = c.fetchall()
#             data = np.array(datalist[0])
#             print("vakuur opgehaalt")
#         except:
#             print("kon vakuur niet ophalen")
#         else:
#             return data


def get_leerlingen():

    conn = sqlite3.connect("gegevens.db")

    with conn:
        c = conn.cursor()

        try:
            c.execute("""
                SELECT *
                FROM leerlingen
            """)
            datalist = c.fetchall()
            data = np.array(datalist)
            print("leerlingen opgehaalt")
        except:
            print("kon leerlingen niet ophalen")
        else:
            return data
