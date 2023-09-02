dato_nombre=input("Escriba el nombre y apellido del paciente: ")
dato_fecha=input("Escriba la fecha de nacimiento del paciente (DD/MM/AAAA): ")
dato_medicamento=input("Escriba el nombre, dosis e instrucciones de uso del medicamento recetado: ")

print("nombre y apellido", dato_nombre)
print("Fecha de naciemiento", dato_fecha)
print('\033[1m' + 'Clinica san martín, Mendoza 1236, VILLA MARÍA' + '\033[0m',)
print("Receta medicamento", dato_medicamento)
print(dato_medicamento)