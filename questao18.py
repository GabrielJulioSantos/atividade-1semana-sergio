tamanho=float(input("fale o tamanho do arquivo para dowwode em mb"))
velocidade=float(input("falee a velocidade do kink de internt em mbps"))
v=8
f=tamanho/v
g=f/60
print("analisando o tamanho do arquivo{},e a velocidade{},em minutos fica {}".format(tamanho,velocidade,g))