import psycopg2
import csv

conn = psycopg2.connect('host=localhost dbname=winnersdb user=postgres password=1234')
cur = conn.cursor()

cur.execute("""
    DROP TABLE averagedrive;
    DROP TABLE totalydsto;
    DROP TABLE passing;
    DROP TABLE rushing;
    DROP TABLE penalties;
    DROP TABLE misc;
    DROP TABLE player;
    DROP TABLE winner;
    DROP TABLE team;
""")
conn.commit()

# cur.execute("""
#     DELETE FROM averagedrive;
#     DELETE FROM totalydsto;
#     DELETE FROM passing;
#     DELETE FROM rushing;
#     DELETE FROM penalties;
#     DELETE FROM misc;
#     DELETE FROM player;
#     DELETE FROM winner;
#     DELETE FROM team;
# """)
# conn.commit()

cur.execute("""
    CREATE TABLE Team (
        id integer PRIMARY KEY,
        name text
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE Winner (
        year integer PRIMARY KEY,
        tid integer,
        CONSTRAINT fk_team
            FOREIGN KEY(tid)
                REFERENCES Team(id)
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE Player (
        id integer PRIMARY KEY,
        name text
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE TotalYdsTO (
        year integer,
        pid integer,
        PRIMARY KEY (year, pid),
        CONSTRAINT fk_Winner
            FOREIGN KEY(year)
                REFERENCES Winner(year),
        CONSTRAINT fk_Player
            FOREIGN KEY(pid)
                REFERENCES Player(id),
        pf integer,
        yds integer,
        ply integer,
        yp float,
        turnOver float
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE Passing (
        year integer,
        pid integer,
        PRIMARY KEY (year, pid),
        CONSTRAINT fk_Winner
            FOREIGN KEY(year)
                REFERENCES Winner(year),
        CONSTRAINT fk_Player
            FOREIGN KEY(pid)
                REFERENCES Player(id),
        cmp integer,
        att integer,
        yds integer,
        td integer,
        int integer,
        nya float,
        firstdown integer
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE Rushing (
        year integer,
        pid integer,
        PRIMARY KEY (year, pid),
        CONSTRAINT fk_Winner
            FOREIGN KEY(year)
                REFERENCES Winner(year),
        CONSTRAINT fk_Player
            FOREIGN KEY(pid)
                REFERENCES Player(id),
        att integer,
        yds integer,
        td integer,
        ya float,
        firstdown integer
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE Penalties (
        year integer,
        pid integer,
        PRIMARY KEY (year, pid),
        CONSTRAINT fk_Winner
            FOREIGN KEY(year)
                REFERENCES Winner(year),
        CONSTRAINT fk_Player
            FOREIGN KEY(pid)
                REFERENCES Player(id),
        pen integer,
        yds integer,
        firstdownpy integer
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE AverageDrive (
        year integer,
        pid integer,
        PRIMARY KEY (year, pid),
        CONSTRAINT fk_Winner
            FOREIGN KEY(year)
                REFERENCES Winner(year),
        CONSTRAINT fk_Player
            FOREIGN KEY(pid)
                REFERENCES Player(id),
        start text,
        time text,
        plays float,
        yds float,
        pts float
    )
""")

conn.commit()

cur.execute("""
    CREATE TABLE Misc (
        year integer,
        pid integer,
        PRIMARY KEY (year, pid),
        CONSTRAINT fk_Winner
            FOREIGN KEY(year)
                REFERENCES Winner(year),
        CONSTRAINT fk_Player
            FOREIGN KEY(pid)
                REFERENCES Player(id),
        fl float,
        firstdown integer,
        numOfDrives integer,
        scorePercent float,
        toPercent float
    )
""")

conn.commit()


with open('nfl_teams.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    tid = 0
    next(reader)
    for row in reader:
        cur.execute('INSERT INTO Team VALUES (%s, %s)',
        (tid, row[1]))
        conn.commit()

        tid += 1

winners = [29, 18, 18, 24, 13, 20, 24, 19, 11, 20, 2, 27, 18, 9, 18, 23, 18, 15, 29, 28, 15]

index = 0
for year in range (2002, 2023):
        cur.execute('INSERT INTO Winner VALUES (%s, %s)',
        (year, winners[index]))
        conn.commit()

        index += 1


players = ['Team Stats', 'Opp. Stats', 'Lg Rank Offense', 'Lg Rank Defense']

for i in range(0, 4):
    cur.execute('INSERT INTO Player VALUES (%s, %s)',
    (i, players[i]))
    conn.commit()



for i in range(2002, 2023):
    with open(str(i)+'.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        pid = 0
        next(reader)

        for row in reader:
            for x in range(0, len(row)):
                 if row[x] == '':
                      row[x] = -1
                      
            cur.execute('INSERT INTO TotalYdsTO VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (i, pid, int(row[1]), int(row[2]), int(row[3]), float(row[4]), int(row[5])))
            conn.commit()

            pid +=1
