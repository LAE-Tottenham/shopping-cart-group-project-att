from shop_functions import start_shop
import pgeocode
import math
print('Welcome to my shop')
import postcodes_uk
print(postcodes_uk.validate("N17 0BX"))

def calculate_distance(postcode1, postcode2):
    nomi = pgeocode.Nominatim('GB')
    
    distance_km = pgeocode.GeoDistance('GB').query_postal_code(postcode1, postcode2)
    
    return distance_km

postcode1 = "N17 0BX"
postcode2 = "dsfsdf"
distance = calculate_distance(postcode1, postcode2)
print(distance)

