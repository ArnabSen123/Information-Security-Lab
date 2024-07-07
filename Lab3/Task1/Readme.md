
1.cbc
encrypt: openssl enc -aes-128-cbc -e -in plain.txt -out cipher_cbc.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
decrypt: openssl enc -aes-128-cbc -d -in cipher_cbc.bin -out decipher_cbc.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708

2.cfb
encrypt: openssl enc -aes-128-cfb -e -in plain.txt -out cipher_cfb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
decrypt: openssl enc -aes-128-cfb -d -in cipher_cfb.bin -out dicipher_cfb.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708

3.ecb
encrypt: openssl enc -aes-128-ecb -e -in plain.txt -out cipher_ecb.bin -K 00112233445566778889aabbccddeeff
decrypt: openssl enc -aes-128-ecb -d -in cipher_ecb.bin -out decipher_ecb.txt -K 00112233445566778889aabbccddeeff
