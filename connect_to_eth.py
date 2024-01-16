from web3 import Web3
from web3.providers.rpc import HTTPProvider

def connect_to_eth():
    alchemy_token = "u0xCtlerNnrxyYQH0p5E-1Rtv80nIlJC"  # Replaced by my Alchemy API token
    url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"
    return w3

if __name__ == "__main__":
    connect_to_eth()
