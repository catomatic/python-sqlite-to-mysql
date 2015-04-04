# SQLite To MySQL With Python

A pair of small scripts to transfer table data from SQLite to MySQL.

The MySQL database and table should already exist with the appropriate field names and data types.

These scripts could be merged into one even omitting the conversion to .csv, but I prefer to check the data coming from SQLite first before importing to MySQL.

### Source file: export-csv.py

This file should be run first, to convert a SQLite table to a .csv file. Replace "databasename" with the file name of your SQLite database, "allfieldnames" with a comma-separated list of your field names, and "tablename" with the name of your SQLite table. Once the .csv file is created, check it in a spreadsheet application to make sure everything looks ok.

### Source file: csv-mysql.py

Run this after you've checked the .csv file and everything looks ok there. Replace "hostname" with the name of the MySQL host (usually localhost), "username" with the MySQL username you want to use with your table, "password" with that user's password, "databasename" with the name of the database containing the table you're importing into, "tablename" with the name of the table to populate, and "allfieldnames" with a comma-separated list of field names. Add as many "%s" separated by commas as you have field names.