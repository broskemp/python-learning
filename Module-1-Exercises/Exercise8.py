import mysql.connector
from geopy import distance

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


def GetAirportDistance(icao):
    sql = " select country.name, ident, airport.name, latitude_deg, longitude_deg from airport, country "
    sql += " where airport.iso_country = country.iso_country and ident = '" + icao + "'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def airport_distance(first, second):
    start = GetAirportDistance(first)
    ending = GetAirportDistance(second)
    start_coordinates = (start[0]['latitude_deg'], start[0]['longitude_deg'])
    end_coordinates = (ending[0]['latitude_deg'], ending[0]['longitude_deg'])

    return int(distance.distance(start_coordinates, end_coordinates).km)


icao = input("Enter an airport ICAO code : ")
GetAirportByICAO(icao)

area = input("Enter an area code to fetch amount of airports by country: ")
GetAirportByArea(area)

airport_1 = input("Enter an ICAO code for the first airport : ")
airport_2 = input("Enter an ICAO code for the second airport : ")
print(f"THe distance between the airports inputted is {airport_distance(airport_1, airport_2)} km.")

