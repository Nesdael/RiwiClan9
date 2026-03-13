print("spa servicios")
print("masaje")
print("facial")
print("manicure")


servicio = input("Que servicio de spa desea?\n")

if servicio.strip() == "masaje":
    print("Si existe")
elif servicio.strip() == "facial":
    print("Si existe")
elif servicio.strip() == "manicure":
    print("Si existe")
else:
    print("no existe, disculpe las molestias")
    