## Running on your computer

Run the following command in your terminal to install sqlite3

    $ pip install sqlite

Now, create an empty database:
		
		$ sqlite3 database.sqlite

Now, run the following commands to run the sql files:

    $ .read create.sql

This command will create all the tables in the empty database.

		$ .read insert_data.sql

This command will insert the sample data that I created.

Finally, to get the specific information about the data run the following commmand:

		$ .read query_data.sql

These sample queries contain interesting information about our data, but feel free to run any query on your terminal to retrieve more information about the data that I created for you.
