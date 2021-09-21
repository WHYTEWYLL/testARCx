# TEST

This small program plus a crontab is an easy solution and deployable (Docker) for this problem.

The only problem this solution will have is that as we need to download the flat file, to update it. Because S3 doesn't have an append option, we need to download, append and update the file. 

All you need to do, after cloning the repo. And making sure, you have all the requirements installed. Is importing the 'crontab.bak'

What could be a problem when we start having a huge amount of data on our file. One solution would be to embed the whole process on AWS, creating this program as a lambda or firehouse. 

Either way, would be better to use a table,  or a service  (HIVE/Pyspark)where we can append new data to it, wituout to downloading our previus data. Other opction could be, to create partions of our data, and when our data reaches a point, create a new one, instead of append it all in the same one. 