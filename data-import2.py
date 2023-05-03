import psycopg2
import csv

conn = psycopg2.connect('host=localhost dbname=winnersdb user=postgres password=2001')
cur = conn.cursor()

# cur.execute("""
#     DROP TABLE averagedrive;
#     DROP TABLE totalydsto;
#     DROP TABLE passing;
#     DROP TABLE rushing;
#     DROP TABLE penalties;
#     DROP TABLE misc;
#     DROP TABLE player;
#     DROP TABLE winner;
#     DROP TABLE team;
# """)
# conn.commit()

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

winners = [8, 16, 16, 24, 24, 22, 8, 24, 24, 22, 26, 31, 22, 26, 5, 20, 31, 26, 26, 20, 31, 8, 8, 26, 8, 11, 9, 9, 28, 2, 18, 29, 18, 18, 24, 13, 20, 24, 19, 11, 20, 2, 27, 18, 9, 18, 23, 18, 15, 29, 28, 15]

index = 0
for year in range (1971, 2023):
        cur.execute('INSERT INTO Winner VALUES (%s, %s)',
        (year, winners[index]))
        conn.commit()

        index += 1


players = ['Team Stats', 'Opp. Stats', 'Lg Rank Offense', 'Lg Rank Defense']

for i in range(0, 4):
    cur.execute('INSERT INTO Player VALUES (%s, %s)',
    (i, players[i]))
    conn.commit()


# Fill TotalYdsTO table
for i in range(1971, 2023):
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

# Fill Passing table
for i in range(1971, 2023):
    with open(str(i)+'.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        pid = 0
        next(reader)

        for row in reader:
            for x in range(0, len(row)):
                 if row[x] == '':
                      row[x] = -1
                      
            cur.execute('INSERT INTO Passing VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (i, pid, int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), float(row[13]), int(row[14]) ))
            conn.commit()

            pid +=1

# Fill Rushing table
for i in range(1971, 2023):
    with open(str(i)+'.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        pid = 0
        next(reader)

        for row in reader:
            for x in range(0, len(row)):
                 if row[x] == '':
                      row[x] = -1
                      
            cur.execute('INSERT INTO Rushing VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (i, pid, int(row[15]), int(row[16]), int(row[17]), float(row[18]), int(row[19])))
            conn.commit()

            pid +=1

# Fill Penalties table
for i in range(1971, 2023):
    with open(str(i)+'.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        pid = 0
        next(reader)

        for row in reader:
            for x in range(0, len(row)):
                 if row[x] == '':
                      row[x] = -1
                      
            cur.execute('INSERT INTO Penalties VALUES (%s, %s, %s, %s, %s)',
            (i, pid, int(row[20]), int(row[21]), int(row[22])))
            conn.commit()

            pid +=1

# Fill AverageDrive table
for i in range(2000, 2023):
    with open(str(i)+'.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        pid = 0
        next(reader)

        for row in reader:
            for x in range(0, len(row)):
                 if row[x] == '':
                      row[x] = -1
                      
            cur.execute('INSERT INTO AverageDrive VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (i, pid, row[26], row[27], float(row[28]), float(row[29]), float(row[30])))
            conn.commit()

            pid +=1

# Fill Misc table
for i in range(2000, 2023):
    with open(str(i)+'.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        pid = 0
        next(reader)

        for row in reader:
            for x in range(0, len(row)):
                 if row[x] == '':
                      row[x] = -1
                      
            cur.execute('INSERT INTO Misc VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (i, pid, float(row[6]), int(row[7]), int(row[23]), float(row[24]), float(row[25])))
            conn.commit()

            pid +=1

# Queries

# Finds the average points scored by super bowl winning teams
'''
SELECT AVG(tyto.pf)
FROM TotalYdsTO AS tyto
WHERE tyto.pid = 2;
SELECT player.name, tyto.year, tyto.pf
FROM TotalYdsTO AS tyto
INNER JOIN Player ON Player.id = tyto.pid
WHERE pid IN (2,3);
SELECT player.name, ad.year, winTeam.name, ad.plays
FROM AverageDrive as ad
INNER JOIN Player ON Player.id = ad.pid
INNER JOIN (
    SELECT team.name, winner.year 
    FROM winner 
    INNER JOIN team ON team.id = winner.tid
) AS winTeam ON winTeam.year = ad.year
WHERE pid IN (0,1);
SELECT Player.name, tyto.year, winTeam.name, tyto.pf AS points_scored_or_allowed_total
FROM TotalYdsTO AS tyto
INNER JOIN Player ON Player.id = tyto.pid
INNER JOIN (
    SELECT team.name, winner.year 
    FROM winner 
    INNER JOIN team ON team.id = winner.tid
) AS winTeam ON winTeam.year = tyto.year
WHERE tyto.pid IN (2,3);
SELECT misc.scorePercent
FROM misc
WHERE misc.pid = 0;
'''

# Ranking teams based on the number of superbowl rings they have since 2002
'''
SELECT Team.name, COUNT(Team.name) AS count
FROM Winner
INNER JOIN Team ON Team.id = Winner.tid
GROUP BY Team.name
ORDER BY COUNT(Team.name) desc;
'''

# Average rank of Team Defense in turnovers
'''
SELECT AVG(tyto.turnOver)
FROM TotalYdsTO AS tyto
WHERE tyto.pid = 3;
'''

# Average rank of Team Offense in turnovers
'''
SELECT AVG(tyto.turnOver)
FROM TotalYdsTO AS tyto
WHERE tyto.pid = 2;
'''

# Average number of plays per drive with every team's offense and the average league rank
'''
SELECT AVG(adTeam.plays) AS TeamStats, AVG(adLeague.plays) AS LgOffense
FROM AverageDrive AS adTeam, AverageDrive as adLeague
WHERE adTeam.pid = 0;
'''

'''
SELECT AVG(ad.pts)
FROM AverageDrive AS adOffense, AverageDrive AS adDefense
GROUP BY ;
'''