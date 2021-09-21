# TEST

This small program plus a crontab is an easy solution and deployable (Docker) for this problem.

The only problem this solution will have is that as we need to download the flat file, to update it. Because S3 doesn't have an append option, we need to download, append and update the file. 

All you need to do, after cloning the repo. And making sure, you have all the requirements installed. Is importing the 'crontab.bak'

I did this based on what I understood on the Readme for the test. We would need to see, home much money we would like to expend, calculate our finale and the cost-efficient we are willing to get.

What could be a problem when we start having a huge amount of data on our file. As s3 has no append functionality. You need to read the file from s3, append the data in your code. One solution that would increase efficiency, would be to embed the whole process on AWS, creating this program as a lambda or firehouse. 

Either way would be better to use a table or a service  (HIVE/Pyspark) where we can append new data to it, without downloading our previous data, make queries to it... Another option could be, to create partitions of our data, and when our data reaches a point, create a new one, instead of appending it all in the same one on S3, but we would be downloading the data. 