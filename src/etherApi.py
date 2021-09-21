import requests
from datetime import datetime

def getEth(apikey, module = 'gastracker',action= 'gasoracle'):
    
    response = requests.get(f'https://api.etherscan.io/api?module={module}&action={action}&apikey={apikey} ').json()

    return  [{"suggestBaseFee":response['result']["suggestBaseFee"],"UTC-date":datetime.utcnow()}]
    

