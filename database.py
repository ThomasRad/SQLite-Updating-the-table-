# Import package.
import sqlite3

# Connect to the database. 
conn = sqlite3.connect('customer.db')

# Create a cursor.
c = conn.cursor()

#Update records. 
c.execute(""" UPDATE customers SET first_name = 'Tim'
			  WHERE rowid = 1


	""")
# Commit the command 
conn.commit()

#Quary 
c.execute("SELECT rowid, * FROM customers")
names = c.fetchall()

for name in names:
	print(name)

# Now we close the connection. 
conn.close()

