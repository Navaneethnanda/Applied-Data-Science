
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# You need to install MariabDb in your machine.
# Set the password for 'root' user during installation.
#" Let's say the password is 'pass'

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Create a New Database
# Create a New Table in this Database
# Insert a New Record in the Table
# Select a record from the table

import pymysql.cursors

# Connect to  MariaDb
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pass',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new Database
        sql = "CREATE DATABASE `popDB000`"
        cursor.execute(sql)
        
        # USE the Database
        sql = "USE `popDB000`"
        cursor.execute(sql)

        # Create a table
        sql = "CREATE TABLE `pop_user` (`id` int(11) NOT NULL AUTO_INCREMENT,\
                                       `email` varchar(255) COLLATE utf8_bin NOT NULL,\
                                       `password` varchar(255) COLLATE utf8_bin NOT NULL,\
                                       PRIMARY KEY (`id`))\
        ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1;"

        cursor.execute(sql)

        # Insert a reccord in the table
        sql = "INSERT INTO `pop_user` (`id`, `email`, `password`) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('1000','hossain@bmu.in','bmu@@pass'))
        connection.commit()

        # Select records from the table
        sql = "SELECT * FROM `pop_user"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()



