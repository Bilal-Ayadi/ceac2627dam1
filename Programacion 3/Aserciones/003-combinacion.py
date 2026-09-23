print("Principio del programa")
try: # este comando sirve para intentar algo y no interrumpe la operacion
	assert 4 < 3
except Exception as e: # es donde capturas el error
  print("No puedo continuar porque:",e)
print("Final del programa")