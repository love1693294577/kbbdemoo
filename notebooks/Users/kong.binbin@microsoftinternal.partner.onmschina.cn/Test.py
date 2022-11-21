# Databricks notebook source
# MAGIC %fs ls file:/dbfs/

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE rrty (
# MAGIC   id int,
# MAGIC   name STRING,
# MAGIC   age  INT)using delta
# MAGIC location"/hive_metastore/gen2db/" 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from rrty;

# COMMAND ----------

# MAGIC %sql
# MAGIC update rrty set name='y' where id=1;

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history dbfs:/mnt/studtent01.csv

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE database stuwe 
# MAGIC location"/mnt/alexgen2/kbb/stuwe" 

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into rrty values (1,'a',4);
# MAGIC insert into rrty values (2,'b',3);
# MAGIC insert into rrty values (3,'c',5);
# MAGIC insert into rrty values (4,'d',6);
# MAGIC select * from rrty;

# COMMAND ----------

# MAGIC %sh
# MAGIC nc -vz sqlserver1203.database.chinacloudapi.cn 1433

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dbo.ceshi;

# COMMAND ----------

jdbcHostname = "sqlserver1203.database.chinacloudapi.cn"
jdbcPort="1433"
jdbcDatabase = "db"
    
jdbcUrl = "jdbc:sqlserver://${jdbcHostname}:${jdbcPort};database=${jdbcDatabase}"

jdbcUsername = "dbuser"
jdbcPassword = "P@ssw0rd!..."

import java.util.Properties
connectionProperties = new Properties()
connectionProperties.put("user", s"${jdbcUsername}")
connectionProperties.put("password", s"${jdbcPassword}")
ceshi = spark.read.jdbc(jdbcUrl, "ceshi", connectionProperties)  

display(ceshi)

# COMMAND ----------

# MAGIC %sql
# MAGIC create table abdd(userid string,id string,category string,name string,description string) using delta;

# COMMAND ----------

# MAGIC %sql
# MAGIC show TBLPROPERTIES rrty ('transient_lastDdlTime'); 