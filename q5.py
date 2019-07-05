	# Read the following json content and output the arn of the s3 bucket

#import json module
import json

#Open a textfile with the data and load the data as json
with open("data.txt", 'r') as f:
        datastore = json.load(f)

# printing the respective data 
print(datastore["Records"][0]["s3"]["bucket"]["arn"])
