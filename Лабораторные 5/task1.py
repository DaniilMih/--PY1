from pprint import pprint

my_dict = [{"bin": bin(i)} | {"dec": i} | {"hex": hex(i)} | {"oct": oct(i)} for i in range(16)]


pprint(my_dict)
