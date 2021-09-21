import boto3

def s3_resource(AWS_KEY_ID,AWS_SECRET , region = 'us-east-1'):

     return boto3.resource('s3',
                region_name=region,
                aws_access_key_id=AWS_KEY_ID,
                aws_secret_access_key=AWS_SECRET)


def s3_client(AWS_KEY_ID,AWS_SECRET , region = 'us-east-1'):

    return boto3.client('s3',
                region_name=region,
                aws_access_key_id=AWS_KEY_ID,
                aws_secret_access_key=AWS_SECRET)  

def EthHist( AWS_KEY_ID,AWS_SECRET, vertical, path ):
    
    s3 = s3_resource(AWS_KEY_ID,AWS_SECRET)
    BUCKET = "ether-price-gid-requests-" + vertical

    s3.Bucket(BUCKET).download_file(path, 'ether.csv')

def uploadEthe(AWS_KEY_ID,AWS_SECRET, vertical, path):
    
    s3 = s3_resource( AWS_KEY_ID,AWS_SECRET)

    BUCKET = "ether-price-gid-requests-" + vertical

    s3.Bucket(BUCKET).upload_file(path, "ether.csv")             