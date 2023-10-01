import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='yuckyt0r1!',
    autocommit=True
)


def GetAirportByICAO(icao):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident = '" + icao + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"The following airport: {row[1]} , resides in {row[2]}")
    return



def GetAirportByArea(area):
    sql = "SELECT type, COUNT(type) FROM airport"
    sql += " WHERE iso_country = '" + area + "' "
    sql += " GROUP BY type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        print("Here are the airport types in the entered area code :")
        for row in result:
            print(f"There are {row[1]} of {row[0]} type airports")
    return


icao = input("Enter an airport ICAO code : ")
GetAirportByICAO(icao)

area = input("Enter an area code to fetch amount of airports by country: ")
GetAirportByArea(area)