# config.py
import json
from web3 import Web3

# Polygon RPC endpoint
POLYGON_RPC = "https://polygon-rpc.com"

# ERC20 token address (TBY)
TOKEN_ADDRESS = Web3.to_checksum_address("0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0")

# Load ERC20 ABI
with open("abi/erc20.json") as f:
    ERC20_ABI = json.load(f)

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
