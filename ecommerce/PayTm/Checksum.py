# import base64
# import string
# import random
# import hashlib
# from Crypto.Cipher import AES

# # Constants
# IV = "@@@@&&&&####$$$$"
# BLOCK_SIZE = 16

# # Padding functions for AES encryption/decryption
# def __pad__(s):
#     pad_len = BLOCK_SIZE - len(s) % BLOCK_SIZE
#     return s + chr(pad_len) * pad_len

# def __unpad__(s):
#     return s[:-ord(s[-1])]

# # Key adjustment function to ensure it's the correct length for AES
# def adjust_key(key):
#     return key[:16].ljust(16, '0')

# # Checksum generation functions
# def generate_checksum(param_dict, merchant_key, salt=None):
#     params_string = __get_param_string__(param_dict)
#     salt = salt if salt else __id_generator__(4)
#     final_string = '%s|%s' % (params_string, salt)

#     # SHA-256 hashing
#     hasher = hashlib.sha256(final_string.encode())
#     hash_string = hasher.hexdigest()
#     hash_string += salt

#     return __encode__(hash_string, IV, merchant_key)

# def generate_refund_checksum(param_dict, merchant_key, salt=None):
#     for i in param_dict:
#         if "|" in param_dict[i]:
#             return None
#     return generate_checksum(param_dict, merchant_key, salt)

# def generate_checksum_by_str(param_str, merchant_key, salt=None):
#     salt = salt if salt else __id_generator__(4)
#     final_string = '%s|%s' % (param_str, salt)

#     hasher = hashlib.sha256(final_string.encode())
#     hash_string = hasher.hexdigest()
#     hash_string += salt

#     return __encode__(hash_string, IV, merchant_key)

# def verify_checksum(param_dict, merchant_key, checksum):
#     if 'CHECKSUMHASH' in param_dict:
#         param_dict.pop('CHECKSUMHASH')

#     paytm_hash = __decode__(checksum, IV, merchant_key)
#     salt = paytm_hash[-4:]
#     calculated_checksum = generate_checksum(param_dict, merchant_key, salt=salt)
#     return calculated_checksum == checksum

# # Helper functions
# def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
#     return ''.join(random.choice(chars) for _ in range(size))

# def __get_param_string__(params):
#     params_string = []
#     for key in sorted(params.keys()):
#         value = params[key]
#         params_string.append('' if value == 'null' else str(value))
#     return '|'.join(params_string)

# # AES encode/decode functions with CBC mode
# def __encode__(to_encode, iv, key):
#     key = adjust_key(key)  # Ensure key length is valid
#     to_encode = __pad__(to_encode)
#     cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
#     encrypted = cipher.encrypt(to_encode.encode('utf-8'))
#     return base64.b64encode(encrypted).decode("UTF-8")

# def __decode__(to_decode, iv, key):
#     key = adjust_key(key)  # Ensure key length is valid
#     to_decode = base64.b64decode(to_decode)
#     cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
#     decrypted = cipher.decrypt(to_decode)
#     return __unpad__(decrypted.decode("UTF-8"))

# # Example usage
# if __name__ == "__main__":
#     params = {
#         "MID": "mid",
#         "ORDER_ID": "order_id",
#         "CUST_ID": "cust_id",
#         "TXN_AMOUNT": "1",
#         "CHANNEL_ID": "WEB",
#         "INDUSTRY_TYPE_ID": "Retail",
#         "WEBSITE": "website_name"
#     }

#     merchant_key = 'xxxxxxxxxxxxxxxx'
#     checksum = generate_checksum(params, merchant_key)
#     print("Generated checksum:", checksum)

#     is_valid = verify_checksum(params, merchant_key, checksum)
#     print("Checksum valid:", is_valid)
