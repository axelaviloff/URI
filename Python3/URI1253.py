qtd = int(input())
for i in range(qtd):
    text = input()
    n = int(input())
    new_text = ''
    for w in text:
        posicao = ord(w)-n
    
        if posicao < 65:
            new_text += chr(91-(65-posicao))
        else:
            new_text += chr(ord(w)-n)
    print(new_text)
