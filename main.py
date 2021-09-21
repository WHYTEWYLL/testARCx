def main():
    import pandas as pd
    import os
    from dotenv import load_dotenv
    from src.S3 import s3_resource, s3_client ,  EthHist,uploadEthe
    from src.etherApi import getEth

    
    load_dotenv()

    AWS_KEY_ID = os.getenv('AWS_KEY_ID')
    AWS_SECRET = os.getenv('AWS_SECRET')
    apikey = os.getenv('apikey') # Etherscan APIkey
    vertical = os.getenv('vertical') # Vertical could be { dev / prod / test}
    path = './output/ether.csv'

    s3 = s3_client(AWS_KEY_ID,AWS_SECRET )

    if "ether-price-gid-requests-"+ vertical not in [_["Name"] for _ in s3.list_buckets()["Buckets"]] :
        
        bucket = s3.create_bucket(Bucket = 'ether-price-gid-requests-' + vertical)
        ether_gas_info = getEth(apikey)
        
        df_new_data = pd.DataFrame(data=ether_gas_info)
        df_new_data.to_csv('./output/ether.csv',index=False)
        uploadEthe(AWS_KEY_ID,AWS_SECRET, vertical, path)
        

    else:

        EthHist( AWS_KEY_ID, AWS_SECRET , vertical, path)
        df = pd.read_csv('./output/ether.csv')
        ether_gas_info = getEth(apikey)
        
        
        df_new_data = pd.DataFrame(data=ether_gas_info)
        new = df.append(df_new_data,ignore_index=True)
        new.to_csv('./output/ether.csv',index=False)
        
        
        uploadEthe(AWS_KEY_ID,AWS_SECRET, vertical, path)
    

if __name__ == "__main__":
    main()