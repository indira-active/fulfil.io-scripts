import csv
from fulfil_client import Client

client = Client('indiraactive', '4b7b1a442e8a44e69e3c5d8ad8a64386')
Product = client.model('product.product')
Country = client.model('country.country')
with open('supplier_country.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        products = Product.search([
            ('product_suppliers.party.name', 'ilike', row['supplier']),
            ('product_suppliers.party.is_supplier', '=', True)
        ])
        print "Setting country of origin for supplier %s to %s" % (
            row['supplier'], row['country_of_origin']
        )
        country, = Country.search([('code', 'ilike', row['country_of_origin'])])
        Product.write(products, {
            'country_of_origin': country
        })
