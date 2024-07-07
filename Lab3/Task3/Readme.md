
1.ecb
openssl enc -aes-128-ecb -e -in plain.txt -out cipher128ecb.bin -K 00112233445566778889aabbccddeeff
ghex cipher128ecb.bin
change the 5th value
openssl enc -aes-128-ecb -d -in cipher128ecb.bin -out decipher128ecb.txt -K 00112233445566778889aabbccddeeff

2.cbc
openssl enc -aes-128-cbc -e -in plain.txt -out cipher_cbc.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
ghex cipher_cbc.bin
change the 5th value
openssl enc -aes-128-cbc -d -in cipher_cbc.bin -out decipher_cbc.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708

3.cfb
openssl enc -aes-128-cfb -e -in plain.txt -out cipher_cfb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
ghex cipher_cfb
change the 5th value
openssl enc -aes-128-cfb -d -in cipher_cfb.bin -out dicipher_cfb.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
