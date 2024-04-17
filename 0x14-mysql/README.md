0x14-mysql

#Create a MySQL user named holberton_user on both web-01 and web-02 with the host name 
#set to localhost and the password projectcorrection280hbtn. This will allow us to access the replication 
#status on both servers.
#Make sure that holberton_user has permission to check the primary/replica status of your databases.

>> sudo su #to be in supersuer mode
>> mysql
>> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
>> GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
>> FLUSH PRIVILEGES;

#In order for you to set up replication, you’ll need to have a database with at least one table and one 
#row in your primary MySQL server (web-01) to replicate from.

#Create a database named tyrell_corp.
#Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
#Make sure that holberton_user has SELECT permissions on your table so that we 
#can check that the table exists and is not empty.

>> CREATE DATABASE tyrell_corp;
>> USE tyrell_corp;
>> CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

>> INSERT INTO nexus6 (name) VALUES ('Zika');
>> GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

#Before you get started with your primary-replica synchronization, you need one more thing in place. 
#On your primary MySQL server (web-01), create a new user for the replica server.

#The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
#replica_user must have the appropriate permissions to replicate your primary MySQL server.
#holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user 
#was created with the correct permissions.

>> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password_here';
>> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
>> GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
>> FLUSH PRIVILEGES;

