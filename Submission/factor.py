import numpy as np

def encrypt(text):
    G = np.array([[1],[2],[3],[4]])  ### THis is a group of Z%5 excluding 0 
    g=G[np.random.randint(0,4)]             ## For taking random elements for g and h
    h=G[np.random.randint(0,4)]
    while g==h:
        h=G[np.random.randint(0,4)]             ## To make sure both are not same
    
    ## Fixing Sender and reciever values
    x=1
    y=2
    x_=3
    y_=4
    cipher_text=[]      
    for char in text:                   ## Convert each character in message to cypher    
        theta_1 = np.linalg.matrix_power(g.reshape(1,-1),x+x_) @ np.linalg.matrix_power(h.reshape(1,-1),y+y_)
        theta_2 = (np.linalg.matrix_power(g.reshape(1,-1),x_) @ np.linalg.matrix_power(h.reshape(1,-1),y_))*ord(char)
        cipher_text.append([theta_1,theta_2])
    public_key = (G, g, h, np.linalg.matrix_power(g.reshape(1,-1),x) @ np.linalg.matrix_power(h.reshape(1,-1),y))   ## Save public key
    private_key = (np.linalg.matrix_power(g.reshape(1,-1),x) , np.linalg.matrix_power(h.reshape(1,-1),y))           ## Save Private key
    return cipher_text, public_key, private_key

def decrypt(cipher_text, private_key):
    g,h=private_key             ## Extracting info from private key
    str=""
    for theta1,theta2 in cipher_text:           ## Decrypting
        str+=(chr(int((h@np.linalg.matrix_power(theta1,-1)@g@theta2)[0][0])))
    return str

# Example usage
original_texts=["This is a demo text","I went and bought a shirt for 2$","My name is Devesh!!", "I am Siddharth Prabhu", "I am sourabh i left MDS!!!"]
def test():
    for i in range(1000):
        original_text=original_texts[np.random.randint(0,len(original_texts))]
        cipher_text, public_key, private_key = encrypt(original_text)
        decrypted_text = decrypt(cipher_text, private_key)
        assert decrypted_text == original_text
        cipher_text_as_char=""
        for theta1, theta2 in cipher_text:
            cipher_text_as_char+= chr(int(theta2[0][0]))

def man_input():
    return input("Enter your message :-")
    

def demo():
    return original_texts[np.random.randint(0,len(original_texts))]



original_text=man_input()
cipher_text, public_key, private_key = encrypt(original_text)
decrypted_text = decrypt(cipher_text, private_key)
print("Original text:", original_text)
cipher_text_as_char=""
for theta1, theta2 in cipher_text:
    cipher_text_as_char+= chr(int(theta2[0][0]))
print("encrypted text = {text}".format(text=cipher_text_as_char))    
print("Decrypted text:", decrypted_text)