while True:
    try:
      a, b = map(int ,input().split())
      resultado = a ^ b
      print(resultado)
    except EOFError:
      break