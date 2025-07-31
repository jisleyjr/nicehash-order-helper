from nicehash_config import get_private_api, get_algorithms

# Get API clients and algorithms
algorithms = get_algorithms()
private_api = get_private_api()

print("Getting orders... ")

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