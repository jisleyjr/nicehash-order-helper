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

orders = private_api.get_hashpower_orderbook("EQUIHASH")
eu_stats = orders['stats']["EU"]
usa_stats = orders['stats']["USA"]

# Iterate through EU orders and print out the columns of interest
for order in eu_stats['orders']:
    print(f"Order ID: {order['id']}")
    print(f"  Type: {order['type']}")
    print(f"  Price: {order['price']}")
    print(f"  Limit: {order['limit']}")
    print(f"  Rigs Count: {order['rigsCount']}")
    print(f"  Accepted Speed: {order['acceptedSpeed']}")
    print(f"  Paying Speed: {order['payingSpeed']}")
    print(f"  Alive: {order['alive']}")
    print()

# Iterate through USA orders and print out the columns of interest
for order in usa_stats['orders']:
    print(f"Order ID: {order['id']}")
    print(f"  Type: {order['type']}")
    print(f"  Price: {order['price']}")
    print(f"  Limit: {order['limit']}")
    print(f"  Rigs Count: {order['rigsCount']}")
    print(f"  Accepted Speed: {order['acceptedSpeed']}")
    print(f"  Paying Speed: {order['payingSpeed']}")
    print(f"  Alive: {order['alive']}")
    print()