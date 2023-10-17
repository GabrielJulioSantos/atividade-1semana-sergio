t=float(input("fala quanto vc ganha por horas"))
h=float(input("quantas horas vc trabalha no mes"))
salariototal=h*t
renda=salariototal * 0.11
inss=salariototal * 0.08
sindicato=salariototal  * 0.05
salariofinal=salariototal-(renda+inss+sindicato)
print("de acordo com seu salario total{}, com os descontos fica{}".format(salariototal,salariofinal))

