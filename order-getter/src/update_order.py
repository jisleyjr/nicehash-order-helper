from nicehash_config import get_private_api, get_algorithms

# Get API clients and algorithms
private_api = get_private_api()
algorithms = get_algorithms()

print("Updating order...")

#response = private_api.algo_settings_from_response("EQUIHASH", algorithms)
#response = private_api.set_limit_hashpower_order("51640af6-9834-4001-b782-6f5474e6b990", "0.0060", "EQUIHASH", algorithms)
try:
    response = private_api.set_price_hashpower_order("51640af6-9834-4001-b782-6f5474e6b990", "0.0491", "EQUIHASH", algorithms)
    print(response)
except Exception as e:
    print(f"Error updating order: {e}")