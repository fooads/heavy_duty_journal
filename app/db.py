import mysql.connector

heavy_duty_database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "fuadsdb",
    database = "heavy_duty"
)
heavy_duty_database.autocommit = True

database_cursor = heavy_duty_database.cursor()