"""
@brief: Defanging an IP Address
Problem 1108: Given an valid IPv4 address. In address replace "." with "[.]"
"""

address = "1.1.1.1"
input_address_list = address.split(".")
defanged_ip_address = "[.]".join(d for d in input_address_list)
print (defanged_ip_address)
