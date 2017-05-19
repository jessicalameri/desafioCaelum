def calculaUltimo(vetorAtaque):
	ultimo = 10001
	for item in vetorAtaque:
		if int(item) < ultimo:
			ultimo = int(item)
	return ultimo

def calculaUltimoEPenultimo(vetorDefesa):
	ultimo = 10001
	penultimo = 10001
	for item in vetorDefesa:
		if int(item) < ultimo:
			ultimo = int(item)
		elif int(item) < penultimo:
			penultimo = int(item)
	return ultimo, penultimo


def calculaImpedimento (ultimoA, ultimoD, penultimoD):
	if ultimoA >= penultimoD:
		return "N"
	else:
		return "Y"


ataque, defesa = input("Insira o numero de atacante e defensores, respectivamente: ").split()
ataque = int(ataque)
defesa = int(defesa)
while ataque != 0 and defesa!=0:

	distAtaque = input("Distacia dos atacantes: ").split()
	
	distDefesa = input("Distacia dos defensores: ").split()
	
	ultimoAtaq = calculaUltimo(distAtaque)
	ultimoDef, penultimoDef  = calculaUltimoEPenultimo(distDefesa)

	print(calculaImpedimento(ultimoAtaq, ultimoDef, penultimoDef))

	ataque, defesa = input("Insira o numero de atacante e defensores, respectivamente: ").split()
	ataque = int(ataque)
	defesa = int(defesa)



