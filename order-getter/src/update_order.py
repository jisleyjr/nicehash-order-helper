import nicehash
import os

# Production - https://www.nicehash.com
host = 'https://api2.nicehash.com'

# Pull out of environment variables
organisation_id = os.getenv('ORG_ID')
key = os.getenv('API_KEY')
secret = os.getenv('API_SECRET')

# Create public api object
public_api = nicehash.public_api(host, True)

# # Get all algorithms
algorithms = public_api.get_algorithms()

print("Updating order...")

# Create private api object
private_api = nicehash.private_api(host, organisation_id, key, secret, True)
#response = private_api.algo_settings_from_response("EQUIHASH", algorithms)
response = private_api.set_limit_hashpower_order("51640af6-9834-4001-b782-6f5474e6b990", "0.0060", "EQUIHASH", algorithms)
print(response)