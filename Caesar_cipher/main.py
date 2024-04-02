import sys,art
print(art.ascii_art)
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
msg=[]
new_msg_list=[]
symbols=["@","_","!","#","$","%","^","&","*","(",")","<",">","?","/","|","}","{","~",":","]","[","-","+","=",".",";","'"," "]
#convert to the data to decoded form
def encrypt(msg,shift):     
  encrypt_msg=[]
  for i in range(0,len(msg)):
    count=0    
    for j in range(0,len(alphabet)):    
      
      if msg[i]==alphabet[j]:
        new_msg_index=j+shift
        
        if new_msg_index<=25:          
          encrypt_msg.append(alphabet[new_msg_index])  
          
        elif new_msg_index>25:
          while new_msg_index>=25:
            new_msg_index-=25
            count=count+1
          new_msg_index=new_msg_index-count
          encrypt_msg.append(alphabet[new_msg_index]) 
          
    if msg[i] in symbols:
      encrypt_msg.append(msg[i])    
  encrypt_msg_string=''.join(encrypt_msg)  
  print("Here is the encoded result:",encrypt_msg_string)
  
def decrypt(msg,shift):
  decrypt_msg=[] 
  for i in range(0,len(msg)):
    count=0
    for j in range(0,len(alphabet)):
      if msg[i] in alphabet[j]:
        msg_index=(len(alphabet)-1)-j        
        index_with_shift=msg_index+shift
        
        if index_with_shift<=25:
          new_shift_index=(len(alphabet)-1)-index_with_shift          
          decrypt_msg.append(alphabet[new_shift_index])
          
        elif index_with_shift>25:
          while index_with_shift>=25:
            index_with_shift-=25
            count=count+1
          index_with_shift=index_with_shift-count         
          new_shift_index=(len(alphabet)-1)-index_with_shift
          decrypt_msg.append(alphabet[new_shift_index])
          
    if msg[i] in symbols:
      decrypt_msg.append(msg[i])    
  decrypt_msg_string=''.join(decrypt_msg)  
  print("Here is the decoded result:",decrypt_msg_string,"\n")  
    
def main_code():
  print("Type 'encode' to encrypt,type 'decode' to decrypt" )
  entry=input().lower()
  message=input("Type your message:\n").lower()
  #print(new_msg_list)
  shift_number=int(input("Type your shift number:\n"))
  #convert string to list
  msg_list=list(message)
  if entry=="encode":     
    encrypt(msg_list,shift_number)
  elif entry=="decode":
    decrypt(msg_list,shift_number) 
  else:
    print("\nOops wrong entry..")
    sys.exit()  
    
  user_choice=input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  if user_choice=="yes":
    main_code()
  else:
    print("Goodbye.")
    sys.exit()
main_code()    

  
