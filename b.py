class Yin: pass 
class Yang:
    def __del__(self):
        print("Yang destruido")
 
yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)

print(yang is yin.yang)
#del (yin)
del (yang)
print("?")

#sin añadir del(yin), yang destruido se ejecuta despues d "?" ya que al igualar yin.yang a yang,yang se asocia con la instancia yin.
#añadiendo del(yin) tambien eliminas yin y por tanto yang destruido se ejecuta antes que "?"