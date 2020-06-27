import classes
import traceback
import os

print("EasyCrypt AES-256 Edition - Folder encryption\nWARNING: Please keep your key safe. If the key gets deleted, there's really nothing you can do with the encrypted files. I am not responsible for any damage. All subdirectories will also be encrypted.");
print("----KEYFILE SELECTION----");
keyfilename = input("Please enter the keyfile's name: ");
key = open(keyfilename, "rb").read();
print("");
foldername = input("Folder name: ");
if(not os.path.isdir(foldername)):
    print("Invalid folder");
    exit();
while True:
    q = input("Delete original files?(yes/no): ");
    if(not q.lower() in ["yes", "no"]):
        print("Invalid choice");
        continue;
    if(q.lower() == "yes"):
        deleteoriginal = True;
    elif(q.lower() == "no"):
        deleteoriginal = False;
    break;
while True:
    q = input("Start encryption process? Before you say yes, make sure your key is safe.(yes/no):");
    if(not q.lower() in ["yes", "no"]):
        print("Invalid choice");
        continue;
    if(q.lower() == "no"):
        exit();
    break;
print("Encrypting files....\nThis may take some time depending on the folder size.");
def encryptdir(_dir):
    for i in os.listdir(_dir):
        path = os.path.join(_dir, i);
        if(os.path.isdir(path)):
            encryptdir(os.path.join(_dir, i));
            continue;
        out = path + ".easycrypt";
        try:
            classes.encryptfile(out, path, key);
        except:
            print("Unexpected error, skipping file " + i + "\nError: \n" + traceback.format_exc());
            continue;
        if(deleteoriginal):
            os.remove(path);
encryptdir(foldername);
print("Done!");