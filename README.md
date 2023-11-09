# Scaling Database Systems - Artifacts
Artifacts for the course *Scaling Database Systems* at the University of Passau.

This information refers to the Udacity course *Intro to Hadoop and MapReduce* and how to execute it in the [Docker miniHive Container](https://github.com/sdbs-uni-p/minihive-docker).

## Example
These steps are necessary to run the example on Hadoop (in the miniHive Docker container):

```
# Clone repository in the miniHive Docker container
git clone https://github.com/sdbs-uni-p/sds-artifacts
cd sds-artifacts

# Unzip data
tar xzf purchases.tgz

# Hadoop preparation
hdfs dfs -mkdir -p /user/minihive
hdfs dfs -put purchases.txt

# Execute
cd 01-sales-per-store
mapred streaming -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input purchases.txt -output sales-per-store

```
Please note: 
- For Hadoop, mapper.py and reducer.py must be executable files (e.g. `chmod +x mapper.py`)
- You have to complete the code of mapper.py and reducer.py

