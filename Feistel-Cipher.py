import random
def Input(): #Gets input to encrypt
    var1=input(print("Enter Plaintext"))
    if len(var1)%2==1: #Length must be even so if not even add a space at the end to make even
        var1=var1+" "
    FeistelEncrypt(var1) #Call encrypt

def XOR(Var1,Var2): #Standard XOR modified to take Array
    Array=[]
    for i in range(len(Var1)):
        NewVar=""
        for j in range(len(Var1[i])):
            if (int(Var1[i][j])==int(Var2[i][j])):
                NewVar=NewVar+"0"
            else:
                NewVar=NewVar+"1"
        Array.append(NewVar)
    return Array 

def RandomKey(HalfLen): #Generates random binary key
    RandomKey=[]
    for i in range(HalfLen):
        Temp=""
        for i in range(8):
            Temp=Temp+str(random.randint(0,1))
        RandomKey.append(Temp)
    return RandomKey

def FeistelEncrypt(plaintext):
    Binary=[]
    for i in range(len(plaintext)): #Conv to Binary
        Binary.append(bin(ord(plaintext[i]))[2:].zfill(8))
    HalfLen=int(len(Binary)/2) #Half length of plaintext
    L1=[]
    for i in range(HalfLen): #Split message in half
        L1.append(Binary[i])
    R1=[]
    for i in range(HalfLen): #Split message in half
        R1.append(Binary[HalfLen+i])
    K1=RandomKey(HalfLen) #Generate random binary keys
    K2=RandomKey(HalfLen)
    f1=XOR(R1,K1) #XOR to encrypt
    R2=XOR(f1,L1)
    L2=R1
    f2=XOR(R2,K2)
    R3=XOR(f2,L2)
    L3=R2
    Encrypted=[]
    for i in range(len(L3)): #Combining halves back together
        Encrypted.append(L3[i])
    for i in range(len(R3)):
        Encrypted.append(R3[i])
    EncryptedPlaintext=""
    for i in range(len(Encrypted)): #Convert back to ASCII
        temp =int(Encrypted[i],2)
        EncryptedPlaintext= EncryptedPlaintext+(chr(temp))
    print("Encrypted Plaintext ",EncryptedPlaintext) #Output Encrypted text
    FeistelDecrypt(EncryptedPlaintext,K1,K2)
    
def FeistelDecrypt(EncryptedPlaintext,K1,K2):
    Binary=[]
    for i in range(len(EncryptedPlaintext)): #Conv to Binary
        Binary.append(bin(ord(EncryptedPlaintext[i]))[2:].zfill(8)) 
    HalfLen=int(len(Binary)/2)
    L3=[]
    for i in range(HalfLen): #Split in half
        L3.append(Binary[i])
    R3=[]
    for i in range(HalfLen):
        R3.append(Binary[HalfLen+i])
    f2=XOR(L3,K2) #XOR to reverse encryption
    L2=XOR(R3,f2)
    R2=L3
    f1=XOR(L2,K1)
    L1=XOR(R2,f1)
    R1=L2
    Decrypted=[]
    for i in range(len(L1)): #Put halves back together
        Decrypted.append(L1[i])
    for i in range(len(R1)):
        Decrypted.append(R1[i])
    DecryptedPlaintext=""
    for i in range(len(Decrypted)):
        temp =int(Decrypted[i],2)
        DecryptedPlaintext= DecryptedPlaintext+(chr(temp))
    print("Decrypted Plaintext ",DecryptedPlaintext) #Output decrypted user input back to them

Input()