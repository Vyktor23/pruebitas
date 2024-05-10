
print ("Hola Mundo")

print ("Hola","mundo","python",3)
print ("Hola","mundo","python",3, sep="*")
print ("Hola","mundo","python",3, sep="*", end="%")
print ("Hola","mundo","python",3)

x = 15
print ("Tipo de dato de x:" , type(x))
y = 2
print ("Tipo de dato de y:" , type(y))
z = x/y
print (z)
print ("Tipo de dato de z:" , type(z))
x = "hola"
print (x)
print (type(x))

print (5/2)
print (5%2)
print (5**2)
print (15//4)


# 0o Octal.
# 0x Hexadecimal.

print (12)
print (0o12)
print (0x12)

# Operadores Lógicos AND & , OR | , XOR ^

print (2 & 3) # 10 & 11 = 10 = 2
print (2 | 3) # 10 | 11 = 11 = 3
print (2 ^ 3) # 10 ^ 11 = 01 = 1


print (3>5)
print (3<=5)
print (3!=5)
print (type(3) is type(5))
print (type(3) is type(5.0))
print (3 in [4,5,6])
print (3 in [4,3,5])

print (2**3)
print (2E3)
print (2.5E2)
print (.5E4)


cad = "python"

print (cad)
print (cad[0])
print (cad[3])


# Cadena Multilíneas.

cad = """Escucha hermano
        la cancion de
        la alegría"""

print (cad)


cad2 = "\nEl canto alegre\ndel que espera\nun nuevo\ndía"
print (cad2)

x = "hola"

print (x.capitalize())


# Concatenación.

print("1) Hola"+"Mundo"+"Python")
print("2) Hola","Mundo","Python")

lenguaje,version = "python",3 # Asignacion múltiple.
print(lenguaje)
print(version)


lenguaje,version = "python",3  # Asignación Múltiple.

print ("3) hola mundo %s %s"%(lenguaje,version))

print ("4) hola mundo {} {}".format(lenguaje,version))

print (f"5) hola mundo {lenguaje} {version}")


cadena = "si,"

print (cadena*10,"este amor es tan profundo")


print ("+" + 10 * "-" + "+")
print (("|" + " " * 10 + "|\n") * 5, end="")
print ("+" + 10 * "-" + "+")


cadena = "Lenguaje de programacion python"
print(cadena[0:8])
print(cadena[9:11])
print(cadena[12:24])
print(cadena[25:31])


cadena = "Lenguaje de programacion python"
print(cadena[0:3])
print(cadena[16:])
print(cadena[-6:])
print(cadena[-4:])


# Conversiones entre Tipos.

# int(variable)
# float(variable)
# str(variable)

a,b = "3","5"
print (a+b)
print (int(a)+int(b)) # Pasando strings a enteros.


a,b = 5,5
print (a+b)
print (str(a)+str(b)) # Pasando enteros a strings.


print ("python",3)
print ("python " + str(3))



# Métodos de Cadenas.

cadena_base = "mi pobre angelito"

cad1 = cadena_base.upper() # Convierte en mayúsculas.
print (cad1)


numero_de_o = cadena_base.count("o") # Devuelve el numero de veces que se encuentre la letra "o".
print (numero_de_o)

print (f"la letra 'o' está {numero_de_o} veces en la palabra / frase '{cadena_base}' ")

cad2 = cadena_base.replace("pobre", "dulce") # Reemplaza una subcadena por otra.
print(cad2)


# Lectura de Datos.

marca = input ("Igrese la marca del auto:")
print ("La marca ingresada por el usuario es:", marca)


precio = int (input ("Ingrese el precio:"))

print (f"el auto marca {marca} tiene un precio de ${precio} y con el descuento del 10% le queda en {precio*.9}")

print ("El auto marca {} tiene un precio de ${:,} y con el descuento del 10% le queda en ${:,}".format(marca,precio,precio*0.9))






# Ejercicios

# 1) Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.
# Índice de cosecha = (cantidad de frutos recolectados / cantidad de frutos producidos) * 100%

frutos_recolectados = int(input("Ingrese la cantidad de frutos recolectados: "))
frutos_producidos = int(input("Ingrese la cantidad de frutos producidos en total: "))

indice_cosecha = (frutos_recolectados / frutos_producidos) * 100
print("El índice de cosecha es: {:.2f}%".format(indice_cosecha))


# 2) Dibujar la P de Python que abarque 7 filas y 5 columnas.

print ("+" + 5 * "-" + "+")
print (("|" + " " * 5 + "|\n") * 3, end="")
print ("+" + 5 * "-" + "+")
print (("|" + " " * 1 + "|\n") * 2, end="")
print ("+" + 1 * "-" + "+")

# 3) Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase.

frase = input("Ingrese una frase: ")

palabras = frase.split()
numero_palabras = len(palabras)

print("El número de palabras en la frase es:", numero_palabras)

# 4) Un alumno desea saber cuál será su calificación final en la materia de Matemáticas.
# Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 
# 30% de la calificación del examen final. 15% de la calificación de un trabajo final.


calificacion_parcial1 = float(input("Ingrese la calificación del primer parcial: "))
calificacion_parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
calificacion_parcial3 = float(input("Ingrese la calificación del tercer parcial: "))


calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))
calificacion_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))


promedio_parciales = (calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)


print("La calificación final en la materia de Matemáticas es:", calificacion_final)


# 5) Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido

frase = input("Ingrese una frase: ")

frase_mayuscula = frase.upper()
frase_invertida = frase_mayuscula[::-1]

print("La frase transformada a mayúscula e invertida es:", frase_invertida)



# Estructuras de Control

edad = int(input("Ingrese su edad"))
if edad >=18:
    print("Puede votar")


# Condiciones Doble Sintáxis

edad = int(input("Ingrese su edad"))
if edad >=18:
    print("Puede votar")
else:
    print("No puede votar")

print("Viva la democracia")


# Condicionales Múltiples

edad = int(input("Ingrese su edad"))
if edad >=18:
    print("Puede votar")
elif edad>=17:
    print("En un año o menos podrás votar")
else:
    print("No puede votar")



# Condiciones anidadas.

edad = int(input("Ingrese su edad"))
if edad>=18:
    print("Puede votar")
else:
    if edad>=17:
        print("En un año o menos podrás votar")
    else:
        print("No puedes votar")



# Operadores Lógicos

estado_civil = input("Ingrese estado civil (s,c)")
edad=int(input("Ingrese su edad:"))
buena_persona = input("Es buena persona (s,n)")
linda= input("es linda? (s,n)")
if estado_civil=="c":
    print("No me caso! ni me comprometo")
elif edad<30 and linda=="s" or buena_persona=="s":
    print("Si me caso!")
else:
    print("Solo me comprometo.")




# En un sistema de automatización industrial, un motor puede estar
# encendido o apagado. Si la temperatura de la máquina supera los 80 grados,
# el motor debe apagarse automáticamente. Escribir un programa que controle
# el estado del motor y lo apague si la temperatura supera los 80 grados.


temperatura = int(input("Ingrese la temperatura actual de la máquina en grados Celsius: "))

if temperatura > 80:
    print("La temperatura ha superado los 80 grados. ¡Apague el motor!")
    estado_motor = "Apagado -_-"
else:
    print("La temperatura está estable. El motor sigue encendido.")
    estado_motor = "Encendido :D"

print("Estado del motor:", estado_motor)





# Un programa de descarga de archivos multimedia tiene diferentes velocidades
# de descarga según la calidad de la conexión a internet del usuario.
# Si la conexión es mayor a 20 Mbps, la velocidad de descarga será de 10 Mbps,
# si la conexión es menor a 20 Mbps pero mayor a 5 Mbps,
# la velocidad será de 5 Mbps y si la conexión es menor a 5 Mbps,
# la velocidad de descarga será de 1 Mbps.Escribir un programa que calcule
# el tiempo de descarga de un archivo y el ancho de banda utilizado,
# según la velocidad de descarga.




velocidadConexion = float(input("Ingrese la velocidad de conexión del internet (Mbps): "))

if velocidadConexion > 20:
    velocidadDescarga = 10
elif velocidadConexion > 5:
    velocidadDescarga = 5
else:
    velocidadDescarga = 1


print("La velocidad de descarga es: ",(velocidadDescarga))



# Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad.
# Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la matrícula.
# Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. Si el estrato es 2
# y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o mas,
# el descuento será del 5%.



estrato = int(input("Ingrese el estrato del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))
valor_matricula = float(input("Ingrese el valor de la matrícula: "))


if estrato == 1:
    if edad < 18:
        descuento = 0.20
    else:
        descuento = 0.15
elif estrato == 2:
    if edad < 18:
        descuento = 0.10
    else:
        descuento = 0.05
else:
    descuento = 0.0


precio_con_descuento = valor_matricula * (1 - descuento)


print("Descuento aplicado: {:.0%}".format(descuento))
print("Precio final de la matrícula: ${:.2f}".format(precio_con_descuento))





#   Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
#   un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina
#   en la sangre, de su edad y de su sexo.

#   Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde,
#   se determina su resultado como positivo y en caso contrario como negativo.
# La tabla en la que el medico se basa para obtener el
# resultado es la siguiente:


    # Edad:
    #     0-1 mes nivel de hemoglobina 13 - 26 g%
    #     > 1 y <=6 meses 10 - 18 g%
    #     > 6 y <= 12 meses 11 - 15 g%
    #     > 1 y <=5 años 11.5 - 15 g%
    #     > 5 y <=10 años 12.6 - 15.5 g%
    #     > 10 y <=15 años 13 - 15.5 g%
    #     mujeres > 15 años 12 - 16 g%
    #     hombres > 15 años 14 - 18 g%


tipoEdad = input("¿La edad es en meses o años? (m, a): ")
edadM = None
edadA = None
sexo = None

if tipoEdad == "m":
    edadM = input("Ingrese la edad en meses: ")
elif tipoEdad == "a":
    edadA = input("Ingrese la edad en años: ")
    if edadA > 15:
        sexo = input("¿Eres hombre o mujer? (h, m): ")
else: 
    print("¡Error!")

nivelHemoglobina = float(input("Ingrese el nivel de hemoglobina en g: "))

if edadM != None:
    if edadM >= 0 and edadM <= 1:
        if nivelHemoglobina >= 13 and nivelHemoglobina <= 26:
            print("Positivo")
        else:
            print("Negativo")
    elif edadM > 1 and edadM <= 6:
        if nivelHemoglobina >= 10 and nivelHemoglobina <= 18:
            print("Positivo")
        else:
            print("Negativo")
    elif edadM > 6 and edadM <= 12:
        if nivelHemoglobina >= 11 and nivelHemoglobina <= 15:
            print("Positivo")
        else:
            print("Negativo")
    else:
        print("Error! niveles demasiado inestables, 2 horas de vida")
elif edadA != None:
    if edadA >= 1 and edadA <= 5:
        if nivelHemoglobina >= 11.5 and nivelHemoglobina <= 15:
            print("Positivo")
        else:
            print("Negativo")
    elif edadA > 5 and edadA <= 10:
        if nivelHemoglobina >= 12.6 and nivelHemoglobina <= 15.5:
            print("Positivo")
        else:
            print("Negativo")
    elif edadA > 10 and edadA <= 15:
        if nivelHemoglobina >= 13 and nivelHemoglobina <= 15.5:
            print("Positivo")
        else:
            print("Negativo")
    elif edadA > 10 and edadA <= 15:
        if nivelHemoglobina >= 13 and nivelHemoglobina <= 15.5:
            print("Positivo")
        else:
            print("Negativo")
    elif edadA > 15:
        if sexo == "h":
            if nivelHemoglobina >= 14 and nivelHemoglobina <= 18:
                print("Positivo")
            else:
                print("Negativo")
        elif sexo == "m":
            if nivelHemoglobina >= 12 and nivelHemoglobina <= 16:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Hola?")
    else:
        print("Error!")




# En un sistema de control de calidad, se deben inspeccionar las piezas de un producto
# para determinar si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe
# marcar como rechazada y enviar una alerta al operador. Si la pieza cumple con los estándares de
# calidad, se debe marcar como aprobada y continuar con la producción.  Realice un programa que lea
# una entrada binaria en la que los 1s significan estándares de calidad cumplidos y los 0s significan
# estándares de calidad No cumplidos.  El programa debe rechazar la pieza ante cualquier estándar
# no cumplido.



entrada_binaria = input("Ingrese la entrada binaria (1 para estándar cumplido, 0 para estándar no cumplido): ")


if '0' in entrada_binaria:
    print("La pieza es defectuosa. Fue rechazada y se ha enviado una alerta al operador.")
else:
    print("La pieza cumple con los estándares de calidad. Fue aprobada y se continúa con la producción.")