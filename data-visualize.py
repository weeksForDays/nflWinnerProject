import psycopg2
import matplotlib.pyplot as plt
import numpy as np

# Connect to the database
conn = psycopg2.connect('host=localhost dbname=winnersdb user=postgres password=1234')

# Create a cursor object
cur = conn.cursor()

## LEAGUE RANK POINTS SCORED AND ALLOWED BAR GRAPH
# Fetch the data from the database
cur.execute('''
SELECT tyto.year, winTeam.name, tyto.pf AS points_scored_or_allowed_total
FROM TotalYdsTO AS tyto
INNER JOIN Player ON Player.id = tyto.pid
INNER JOIN (
    SELECT team.name, winner.year 
    FROM winner 
    INNER JOIN team ON team.id = winner.tid
) AS winTeam ON winTeam.year = tyto.year
WHERE tyto.pid IN (2);
''')
dataOffense = cur.fetchall()

cur.execute('''
SELECT tyto.year, winTeam.name, tyto.pf AS points_scored_or_allowed_total
FROM TotalYdsTO AS tyto
INNER JOIN Player ON Player.id = tyto.pid
INNER JOIN (
    SELECT team.name, winner.year 
    FROM winner 
    INNER JOIN team ON team.id = winner.tid
) AS winTeam ON winTeam.year = tyto.year
WHERE tyto.pid IN (3);
''')
dataDefense = cur.fetchall()

# Separate the x and y data
x = [row[0] for row in dataOffense]
y1 = [row[2] for row in dataOffense]
y2 = [row[2] for row in dataDefense]

barWidth = 0.35
r1 = np.arange(len(y1))
r2 = [x + barWidth for x in r1]

# Create the bar graph
plt.bar(r1, y1, color='red', width=barWidth, edgecolor='white', label='Offense')
plt.bar(r2, y2, color='blue', width=barWidth, edgecolor='white', label='Defense')

# Add xticks on the middle of the group bars
plt.xlabel('Year')
plt.xticks([r + barWidth for r in range(len(y1))], x)
plt.ylabel('League Rank')
plt.xticks(rotation=45)
plt.title('Offensive Points Scored and Defensive Points Allowed Rank for Super Bowl Winning Teams From 1971-2022')

plt.legend()

plt.show()

## TURNOVER LEAGUE RANK BAR GRAPH

cur.execute('''
SELECT tyto.year, tyto.turnOver
FROM TotalYdsTO AS tyto
WHERE tyto.pid = 2;
''')
dataOffense = cur.fetchall()

cur.execute('''
SELECT tyto.year, tyto.turnOver
FROM TotalYdsTO AS tyto
WHERE tyto.pid = 3;
''')
dataDefense = cur.fetchall()

barWidth = 0.35

x = [row[0] for row in dataOffense]
y1 = [row[1] for row in dataOffense]
y2 = [row[1] for row in dataDefense]

barWidth = 0.35
r1 = np.arange(len(y1))
r2 = [x + barWidth for x in r1]

# Create the bar graph
plt.bar(r1, y1, color='red', width=barWidth, edgecolor='white', label='Offense')
plt.bar(r2, y2, color='blue', width=barWidth, edgecolor='white', label='Defense')

# Add xticks on the middle of the group bars
plt.xlabel('Year')
plt.xticks([r + barWidth for r in range(len(y1))], x)
plt.ylabel('League Rank')
plt.xticks(rotation=45)
plt.title('Offensive and Defensive Turnovers League Rank From Super Bowl Winning Teams From 1971-2022')

plt.legend()
plt.show()

## OFFENSIVE AND DEFENSIVE EFFICIENCY LEAGUE RANK

cur.execute('''
SELECT p.year, p.nya
FROM Passing AS p
WHERE p.pid = 2;
''')
dataPassing = cur.fetchall()

cur.execute('''
SELECT r.year, r.ya
FROM Rushing AS r
WHERE r.pid = 3;
''')
dataRushing = cur.fetchall()

barWidth = 0.35

x = [row[0] for row in dataPassing]
y1 = [row[1] for row in dataPassing]
y2 = [row[1] for row in dataRushing]

barWidth = 0.35
r1 = np.arange(len(y1))
r2 = [x + barWidth for x in r1]

# Create the bar graph
plt.bar(r1, y1, color='orange', width=barWidth, edgecolor='white', label='Passing')
plt.bar(r2, y2, color='green', width=barWidth, edgecolor='white', label='Rushing')

# Add xticks on the middle of the group bars
plt.xlabel('Year')
plt.xticks([r + barWidth for r in range(len(y1))], x)
plt.ylabel('Offensive League Rank')
plt.xticks(rotation=45)
plt.title('Passing and Rushing Yards Per Attempt League Rank From Super Bowl Winning Offenses From 1971-2022')

plt.legend()
plt.show()

cur.execute('''
SELECT p.year, p.nya
FROM Passing AS p
WHERE p.pid = 3;
''')
dataPassing = cur.fetchall()

cur.execute('''
SELECT r.year, r.ya
FROM Rushing AS r
WHERE r.pid = 2;
''')
dataRushing = cur.fetchall()

barWidth = 0.35

x = [row[0] for row in dataPassing]
y1 = [row[1] for row in dataPassing]
y2 = [row[1] for row in dataRushing]

barWidth = 0.35
r1 = np.arange(len(y1))
r2 = [x + barWidth for x in r1]

# Create the bar graph
plt.bar(r1, y1, color='orange', width=barWidth, edgecolor='white', label='Passing')
plt.bar(r2, y2, color='green', width=barWidth, edgecolor='white', label='Rushing')

# Add xticks on the middle of the group bars
plt.xlabel('Year')
plt.xticks([r + barWidth for r in range(len(y1))], x)
plt.ylabel('Defensive League Rank')
plt.xticks(rotation=45)
plt.title('Passing and Rushing Yards Per Attempt Allowed League Rank From Super Bowl Winning Defense From 1971-2022')

plt.legend()
plt.show()

## PASSING AND RUSHING SPLIT PIE CHART

cur.execute('''
SELECT (SELECT AVG(r.yds)
FROM Rushing AS r
WHERE r.pid = 0),
(SELECT AVG(p.yds)
FROM Passing AS p
WHERE p.pid = 0);
''')
data = cur.fetchall()

values = []

for column in data:
    values = list(column)

labels = ['Rushing', 'Passing']

plt.pie(values, labels = labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Average Passing and Rushing Split for Super Bowl Winning Teams from 1971-2022')
plt.show()


# Close the cursor and connection
cur.close()
conn.close()
