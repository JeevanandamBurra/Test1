
# coding: utf-8

# In[1]:


import random


# In[92]:


class Cipher:
    #creating static variable to generate random key value to encrypt and decrypt
    Rd= random.randint(1,51)
    # Class constructor
    def __init__(self):
        self.strg=input('Please enter text to be encrypted:')
        self.e=self.Rd
    #Method to encrypt the text
    def enc(self):
        #using filter to exclued special charecters
        self.Etext=''.join(filter(str.isalnum, self.strg))
        self.value_altered = ''.join(chr(ord(letter)+self.e) for letter in self.Etext)
        print('The Key :',self.e)
        return self.value_altered
      #Method to decrypt the encrypted text  
    def dec(self,s):
        self.altered = ''.join(chr(ord(letter)-self.e) for letter in s)
        return self.altered
              


# In[93]:


a=Cipher()
b=a.enc()
print(b)
print(a.dec(b))

