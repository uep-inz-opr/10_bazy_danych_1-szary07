
import csv, sqlite3

if __name__ == "__main__":
    sqlite_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = sqlite_con.cursor()
    cursor.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                    to_subscriber data_type INTEGER, 
                    datetime data_type timestamp, 
                    duration data_type INTEGER , 
                    celltower data_type INTEGER);''')
 

    with open('polaczenia_duze.csv', 'r') as fin:
        reader = csv.reader(fin, delimiter = ";")
        headers = next(reader)

        rows = [x for x in reader]
        #print(rows)
        cursor.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", rows)
        
cursor = sqlite_con.cursor()
cursor.execute("SELECT sum(duration) from polaczenia")
moj_wynik = cursor.fetchone()[0]

print(int(moj_wynik))