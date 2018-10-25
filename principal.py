from paquete.modelo import *
d=Docente("Docente B D","Loja")
d2=Docente("Docente Prog", "Quito")
listado=[d,d2]
e=Estudiante ("Luis",listado)
print (e.presentar_datos())