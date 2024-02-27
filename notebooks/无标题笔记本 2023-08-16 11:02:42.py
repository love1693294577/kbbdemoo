# Databricks notebook source
`test2.name`

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from test002pppp

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE test00444
# MAGIC   USING JDBC
# MAGIC OPTIONS (
# MAGIC   url "jdbc:hive2://testspark001.azurehdinsight.cn:443/default;transportMode=http;ssl=true;httpPath=/hive2?hive.resultset.use.unique.column.names=false",
# MAGIC   dbtable "test",
# MAGIC   user 'admin',
# MAGIC   password 'P@ssw0rd!...'
# MAGIC ) 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from test00444

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE test00333
# MAGIC USING JDBC
# MAGIC OPTIONS (
# MAGIC   url "jdbc:sqlserver://sqlservertest001.database.chinacloudapi.cn:1433;database=testsql2",
# MAGIC   dbtable "test001",
# MAGIC   user 'admin123',
# MAGIC   password 'P@ssw0rd!...'
# MAGIC )
# MAGIC
# MAGIC //hive.resultset.use.unique.column.names=false

# COMMAND ----------

# MAGIC %sql
# MAGIC select  * from  test00333

# COMMAND ----------

String url="jdbc:mysql://testmysql0629.mysql.database.chinacloudapi.cn:3306/{your_database}?useSSL=true";myDbConn=DriverManager.getConnection(url, "admin123", "{your_password}");

# COMMAND ----------

# MAGIC %sql
# MAGIC select test2.name from test00222

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from new_employees_table