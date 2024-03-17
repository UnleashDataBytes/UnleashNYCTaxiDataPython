## Explain Snowflake Connection Parameters

- **Account**: This is the unique identifier for your Snowflake account. It's typically provided to you when you sign up for Snowflake. 
You can also find it in the URL you use to access the Snowflake web interface. 
It usually looks like `https://<account>.snowflakecomputing.com`
- **User**:This is the username you use to log in to Snowflake.
- **Password**: This is the password associated with your Snowflake user account.
- **Warehouse**: In Snowflake, a warehouse is a computing resource that executes SQL queries. 
Create new warehouse `NYCTAXI` by navigating to the Admin -> Warehouses tab.
- **Database**: A database in Snowflake is a container for your data and database objects. 
Create new database `NYCTAXIDATABASE` by logging in to Snowflake and navigating to the Data -> Databases tab.
- **Schema**: A schema in Snowflake is a logical container for database objects, such as tables, views, and functions.
You can find the available schemas by logging in to Snowflake, selecting the desired database. `public` schema is the default schema in Snowflake.
