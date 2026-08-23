from time import sleep
cores={"amarelo": "\033[33m",
       "vermelho": "\033[31m",
       "branco": "\033[1;97m",
       "azul": "\033[34m",
       "ciano": "\033[36m",
       "roxo": "\033[35m",
       "cinza": "\033[37m",
       "verde": "\033[32m",
       "limpa": "\033[m"
}
alunos=[]
temp={}
quant=int(input("Quantos alunos quer cadastar?: "))
aluno=0
for _ in range(quant):
       aluno+=1
       print(f'{cores["amarelo"]}-={cores["limpa"]}'*15)
       print(f'{cores["branco"]}Aluno{aluno}:{cores["limpa"]}', end='')
       print("|")
       temp["nome"]=input("Nome do aluno: ")
       temp["media"]=float(input("Média desse aluno: "))
       alunos.append(temp.copy())
print(f"{cores["branco"]}_{cores["limpa"]}"*20)
for a in alunos:
       if a["media"]>=7:
          print(f"{a["nome"]} foi {cores["verde"]}APROVADO{cores["limpa"]}")
sleep(1)
       else:
          print(f"{a["nome"]} foi {cores["vermelho"]}REPROVADO{cores["limpa"]}")
sleep(1)