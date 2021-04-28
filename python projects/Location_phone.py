#para ver de donde es el numero y que comprañia es, codigo simple pero para algo servira 

import phonenumbers
from phonenumbers import geocoder

number = input("Enter person phone number: ")
ch_number = phonenumbers.parse(number,'CH')

print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier

s_num = phonenumbers.parse(number,'RO')
print(carrier.name_for_number(s_num,"en"))
