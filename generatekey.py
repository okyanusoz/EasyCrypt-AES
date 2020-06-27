from Crypto.Random import get_random_bytes
print("EasyCrypt AES-256 - Generate Key");
keyfile = input("Key file(existing will be overwritten): ");
open(keyfile, "wb").write(get_random_bytes(32));
print("Done!");