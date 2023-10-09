cadena = "+34-913724710-56"

pos1 = cadena.find("-")
pos2 = cadena.find("-", pos1 + 1)
prefijo = cadena[:pos1 - 1]
numero = cadena[pos1:pos2]

extension = cadena[pos2:]

        