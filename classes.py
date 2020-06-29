# EasyCrypt Encryption and Decryption Functions
from Crypto.Cipher import AES

def decryptfile(input_file, key, newfile):
    # Read the data from the file
    file_in = open(input_file, 'rb') # Open the file to read bytes
    iv = file_in.read(16) # Read the iv out - this is 16 bytes long
    ciphered_data = file_in.read() # Read the rest of the data
    file_in.close()

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)  # Setup cipher
    original_data = cipher.decrypt(ciphered_data);
    open(newfile, "wb").write(original_data);
def encryptfile(output_file, originalfile, key):
    data = open(originalfile, "rb").read() # Must be a bytes object
    # Create cipher object and encrypt the data
    cipher = AES.new(key, AES.MODE_CFB) # Create a AES cipher object with the key using the mode CFB
    ciphered_data = cipher.encrypt(data)

    file_out = open(output_file, "wb") # Open file to write bytes
    file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
    file_out.write(ciphered_data) # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.close()