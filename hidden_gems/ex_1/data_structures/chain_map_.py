from collections import ChainMap
import os

# print(issubclass(ChainMap, dict))

# d = ChainMap()
# print(type(d))

# print(ChainMap.__mro__)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4, 'd': 5}

chain_map = ChainMap(dict1, dict2)
# dict1['a'] = 20

# chain_map.maps.reverse()
# print(chain_map.maps[-1]['b'])
# print(chain_map.maps)
#
# for key, value in chain_map.items():
#     print(key, value)

default_config = {
    'theme': 'Default',
    'language': "English",
    'show_ads': True
}

# env_config = os.environ
env_config = {}
app_config = ChainMap(env_config, default_config)
print('Theme',app_config['theme'])

user_config = {
    'theme': 'Light Mode',
    'show_ads': False
}
app_config = app_config.new_child(user_config)

print(app_config)
print(app_config['theme'])
print(app_config['show_ads'])
print(app_config['language'])