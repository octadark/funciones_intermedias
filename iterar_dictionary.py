estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for i in range(0,len(list)):
        output = ""
        for key,val in list[i].items():
            output += f"{key} - {val},"
        print(output)
iterateDictionary(estudiantes) 
print("----")
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
"""
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:
def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',estudiantes)
iterate_dictionary2('last_name',estudiantes)