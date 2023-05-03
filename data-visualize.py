import psycopg2
import matplotlib.pyplot as plt
import numpy as np

# Connect to the database
conn = psycopg2.connect('host=localhost dbname=winnersdb user=postgres password=1234')

# Create a cursor object
cur = conn.cursor()

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

# Create a line plot using Matplotlib
# plt.plot(x, y1, label="Offense")
# plt.plot(x, y2, label="Defense")
# plt.xlabel("Year")
# plt.ylabel("Offense")
# plt.title("Rank Over the Years")

# bar_width = 0.35

# plt.bar(x, y1, width=bar_width, label='Offense')
# plt.bar(x, y2, width=bar_width, label='Defense')
# plt.xlabel("Year")
# plt.ylabel("Offensive Rank")
# plt.title("Histogram of Data")
# plt.legend()
# plt.show()

barWidth = 0.35
r1 = np.arange(len(y1))
r2 = [x + barWidth for x in r1]

# Create the bar graph
plt.bar(r1, y1, color='red', width=barWidth, edgecolor='white', label='Offense')
plt.bar(r2, y2, color='blue', width=barWidth, edgecolor='white', label='Defense')

# Add xticks on the middle of the group bars
plt.xlabel('Year')
plt.xticks([r + barWidth for r in range(len(y1))], x)

# Add y-axis label
plt.ylabel('Rank')

# Add legend
plt.legend()

# Show the graph
plt.show()




# Close the cursor and connection
cur.close()
conn.close()
