alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

code = input("Encode(e) or Decode(d) ? ").lower()
message = input("Type your message : ").lower()
shift = int(input("Enter the shift number : "))
shift %= 26

def caesar(text, shift_amt, cipher):
  cipher_text = ""
  if code == "d":
      shift_amt *= -1
  for i in text:
    if i in alphabets:
      pos = alphabets.index(i)
      new_pos = pos + shift_amt
      cipher_text += alphabets[new_pos]
    else:
      cipher_text += i

  print(f"The cipher text is {cipher_text}")

caesar(text = message, shift_amt = shift, cipher = code)


