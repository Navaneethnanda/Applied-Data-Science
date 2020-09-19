
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# You need to install MariabDb in your machine.
# Set the password for 'root' user during installation.
#" Let's say the password is 'pass'

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Insert a New Record in the Table
# Select all the records from the table

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pass',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # USE the Database
        sql = "USE `popDB`"
        cursor.execute(sql)

        # Insert a reccord in the table
        sql = "INSERT INTO `pop_user` (`id`, `email`, `password`) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('19','shaikh@bmu.in','bmu@pass111'))
        connection.commit()

        # Select records from the table
        sql = "SELECT * FROM `pop_user"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()



