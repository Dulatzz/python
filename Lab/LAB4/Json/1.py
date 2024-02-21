import json

print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU ')
print('-------------------------------------------------- --------------------  ------  ------')

with open('sample-data.json', 'r') as file:
    data = json.load(file)
    for item in data['imdata']:
        dn = item['l1PhysIf']['attributes']['dn']
        speed = item['l1PhysIf']['attributes']['speed']
        mtu = item['l1PhysIf']['attributes']['mtu']
        print(f"{dn}                              {speed}   {mtu}")