MiembrosDeLaFamia=[
    "tatarabuelo",
] #lista vacia
Abuelo=[]
MiembrosDeLaFamia.append("abuelo")
MiembrosDeLaFamia.insert(1,"abuela")
MiembrosDeLaFamia.append("papa")
MiembrosDeLaFamia.append("mama")
MiembrosDeLaFamia.append("yo")
#MiembrosDeLaFamia.remove("abuelo")
print("ANTES:",MiembrosDeLaFamia)
#del MiembrosDeLaFamia[2]
#MiembrosDeLaFamia.pop(2)
#print("cantidad de miembros:",le(MiembrosDeLaFamia))
#MiembrosDeLaFamia.sort()
print("DESPUES",MiembrosDeLaFamia)
for i in MiembrosDeLaFamia:
    print("#->",i.upper())
