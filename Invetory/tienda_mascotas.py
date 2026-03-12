print("Mascotas")
print("1. perrro")
print("2 .gato")
print("3. Conejo")

mascota = int(input("Elija la opcion de la mascota"))

if mascota == 1:
    print("Elegiste al perro, te dare una recomendacion del alimento")
    print("""
          Los perros necesitan una alimentación balanceada que incluya proteínas, carbohidratos, grasas saludables,\n vitaminas y minerales. Lo más recomendable es darles alimento concentrado de buena calidad según su edad y tamaño.
          """)
elif mascota == 2:
    print("Elegiste al gato, te dare una recomendacion del alimento")
    print("""
          con wiskas ya esta fino
          """)
elif mascota == 3:
    print("Elegiste al conejo, te dare una recomendacion del alimento")
    print("""
         vegetales y queda para el fin de año sabroso
          """)
else:
      print("coloque una opcion valida 1/2/3")