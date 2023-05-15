#!/usr/bin/env python3
import base64

encoded_hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decoded_byte_string = bytes.fromhex(encoded_hex_string)
base64_encoded_string = base64.b64encode(decoded_byte_string)
flag = base64_encoded_string.decode("ascii")
print(flag)