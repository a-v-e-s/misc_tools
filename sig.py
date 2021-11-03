import hmac
import secrets
import base64

def main(vin, alg='sha512'):
    
    key = base64.encodebytes(bytes(str(secrets.randbits(2048)), 'utf-8'))
    nft = hmac.new(key, bytes(vin, 'utf-8'), alg)

    return key, nft