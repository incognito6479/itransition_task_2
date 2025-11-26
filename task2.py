import glob 
import hashlib


my_email = 'bexruzmuminov@bk.ru'
keys_hashes = {}
keys_store = []
hash_concat = ''

def ordering_by_sortkey(hash_value):
    product = 1
    for hex_item in hash_value:
        product *= int(hex_item, 16) + 1
    return product

current_files = glob.glob("file_*")
for file_name in current_files:
    with open(file_name, 'rb') as bin_file:
        bin_file_hash = hashlib.sha3_256(bin_file.read()).hexdigest()
        keys_hashes[ordering_by_sortkey(bin_file_hash)] = bin_file_hash 

for key in keys_hashes.keys():
    keys_store.append(key)

keys_store = sorted(keys_store)

for key in keys_store:
    hash_concat += keys_hashes[key]

result = hash_concat + my_email
hashed_result = hashlib.sha3_256(result.encode()).hexdigest()
print(hashed_result) 