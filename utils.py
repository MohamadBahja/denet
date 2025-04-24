from web3 import Web3
import json
import os
from datetime import datetime

# === Configuration ===
RPC_URL = "https://polygon-rpc.com"
TOKEN_ADDRESS = Web3.to_checksum_address("0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0")

# === Load ABI ===
ABI_PATH = os.path.join("abi", "erc20.json")
with open(ABI_PATH, "r") as f:
    ERC20_ABI = json.load(f)

# === Web3 Setup ===
web3 = Web3(Web3.HTTPProvider(RPC_URL))
token = web3.eth.contract(address=TOKEN_ADDRESS, abi=ERC20_ABI)

# === Level A ===
def get_balance(address):
    try:
        address = Web3.to_checksum_address(address)
        balance = token.functions.balanceOf(address).call()
        decimals = token.functions.decimals().call()
        return balance / (10 ** decimals)
    except Exception as e:
        return f"Error: {str(e)}"

# === Level B ===
def get_balance_batch(addresses):
    return [get_balance(addr) for addr in addresses]

# === Level C — Mocked Top Holders ===
def get_top_holders(n):
    return [
        ("0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d", 1000.0),
        ("0x4830AF4aB9cd9E381602aE50f71AE481a7727f7C", 850.0),
        ("0x1fF3Ef6FeA287bCf3591A07b46a5D1232Bc9F874", 750.0),
        ("0xEfB827E1E2E18C8D0D4dEaA2E3dE7Db8162CdE45", 620.0),
        ("0x8C3A6f53B7BAFFeFA57b8433C1F67EDB962b3A5C", 500.0)
    ][:n]

# === Level D — Mocked Top Holders with Transactions ===
def get_top_holders_with_transactions(n):
    now = datetime.utcnow().isoformat()
    return [(addr, bal, now) for (addr, bal) in get_top_holders(n)]

# === Level E — Token Info ===
def get_token_info():
    try:
        name = token.functions.name().call()
        symbol = token.functions.symbol().call()
        totalSupply = token.functions.totalSupply().call()
        decimals = token.functions.decimals().call()
        totalSupplyFormatted = totalSupply / (10 ** decimals)
        return {
            "name": name,
            "symbol": symbol,
            "totalSupply": totalSupplyFormatted
        }
    except Exception as e:
        return {"error": str(e)}
