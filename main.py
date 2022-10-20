alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '.', '~', '|', '<', '>', '=', '-', '_', '/', ':', ';', '?', '[', ']', '{', '}', '~', ' ', ',']
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))
  
  if shift > (len(alphabet)-1):
    shift = shift % (len(alphabet)-1)
  
  def cesar(direction, text, shift):
    encoded_string = ""
    decoded_string = ""
    
    if direction == "encode":
      for var in text:
        if (alphabet.index(var) + shift) > (len(alphabet)-1):
          encoded_string += alphabet[((alphabet.index(var) + shift) - (len(alphabet)-1)) - 1]
        else:
          encoded_string += alphabet[(alphabet.index(var) + shift)]
      print (encoded_string)
    else:
      for var in text:
        if (alphabet.index(var) - shift) < 0:
          decoded_string += alphabet[((len(alphabet)-1) + (alphabet.index(var) - shift)) +1]
        else:
          decoded_string += alphabet[(alphabet.index(var) - shift)]
      print (decoded_string)
  
  cesar(direction, text, shift)
 
  cont = input("Type 'no' to exit the program or anythin else to run again.")
  if(cont.lower() == "no"):
    break
