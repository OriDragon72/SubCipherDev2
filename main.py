#Decryption of Substitution Cipher

def DOSC(EMessage):
  freqAna = {}
  for char in EMessage:
    if char.isalpha():
      if char in freqAna:
        freqAna[char] += 1
      else:
        freqAna[char] = 1

  # Sort the Frequency Analysis results
  SFA = dict(
    sorted(freqAna.items(), key=lambda item: item[1], reverse=True)
  )

  #Map is based on the table:
  #Ref -> https://pi.math.cornell.edu/%7Emec/2003-2004/cryptography/subs/frequencies.html
  
  subsMap = {
    'e': list(SFA.keys())[0],
    't': list(SFA.keys())[1],
    'a': list(SFA.keys())[2],
    'o': list(SFA.keys())[3],
    'i': list(SFA.keys())[4],
    'n': list(SFA.keys())[5],
    's': list(SFA.keys())[6],
    'r': list(SFA.keys())[7],
    'h': list(SFA.keys())[8],
    'd': list(SFA.keys())[9],
    'l': list(SFA.keys())[10],
    'u': list(SFA.keys())[11],
    'c': list(SFA.keys())[12],
    'm': list(SFA.keys())[13],
    'f': list(SFA.keys())[14],
    'y': list(SFA.keys())[15],
    'w': list(SFA.keys())[16],
    'g': list(SFA.keys())[17],
    'p': list(SFA.keys())[18],
    'b': list(SFA.keys())[19],
    'v': list(SFA.keys())[20],
    'k': list(SFA.keys())[21],
    'x': list(SFA.keys())[22],
    'q': list(SFA.keys())[23],
    'j': list(SFA.keys())[24],
    'z': list(SFA.keys())[25]
  }

  DMessage = ''.join([
      subsMap[char] if char.isalpha() else char
      for char in EMessage
  ])
  print("This is the key used:\n")
  print(list(subsMap.keys()))
  print("\n")
  return DMessage

print("Welcome to SubCipherDev2! \n")
print("*This project uses the theory of 'frequency analysis'*")

EM = input("Enter the Encrypted Message: ")
DM = DOSC(EM)

print("This is the Decrypted Message: ")
print(DM)

exit(1)