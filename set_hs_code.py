from fulfil_client import Client

# Initializing Api
client = Client('indiraactive', '4b7b1a442e8a44e69e3c5d8ad8a64386')

# Initializing Fulfil's Product model
Product = client.model('product.product')

# Getting all the Product ids
products = Product.search([()])

# Making a write call on list of products to update "hs_code"
# Processing purchase orders in batches of 100
for i in range(0, len(products), 100):
    Product.write(products[i:i + 100], {'hs_code': '3926.20'})
