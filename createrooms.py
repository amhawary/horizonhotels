#Create rooms

import dbfunc

conn = dbfunc.get_connection()
if conn != None:
    dbcursor = conn.cursor()
    dbcursor.execute('SELECT HID, Capacity FROM HOTELS;')
    hotels = dbcursor.fetchall()
    for hotel in hotels:
        count = 1
        max = hotel[1]
        standard = int(0.3 * max)
        double = int(0.5 * max)
        fam = int(0.2 * max)
        for i in range(0,standard):
            add_rooms = ("INSERT INTO rooms "
                "(RoomNum, Hotel, RoomType, available)"
                "VALUES (%s, %s, 'Standard', 1)")
            data_rooms = (count, hotel[0])
            dbcursor.execute(add_rooms,data_rooms)
            count = count + 1
        for i in range(0,double):
            add_rooms = ("INSERT INTO rooms "
                "(RoomNum, Hotel, RoomType, available)"
                "VALUES (%s, %s, 'Double', 1)")
            data_rooms = (count, hotel[0])
            dbcursor.execute(add_rooms,data_rooms)
            count = count + 1
        for i in range(0,fam):
            add_rooms = ("INSERT INTO rooms "
                "(RoomNum, Hotel, RoomType, available)"
                "VALUES (%s, %s, 'Family', 1)")
            data_rooms = (count, hotel[0])
            dbcursor.execute(add_rooms,data_rooms)
            count = count + 1
        conn.commit()