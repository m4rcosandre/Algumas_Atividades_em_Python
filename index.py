from tkinter import *
import os

pasta =os.path.dirname(__file__) #pega o diretório onde está salvo o arquivo .py atual.
nomeArquivo = pasta + "\\nomes.txt" #cria o caminho completo para o arquivo nomes.txt, que será usado para salvar os dados.

#Criando função
def gravar_dados():
  arquivo = open(nomeArquivo, "a")
  arquivo.write('Nome: %s'% nome1.get())
  arquivo.write('\nSobrenome: %s'% sobrenome1.get())
  arquivo.write('\nE-mail: %s'% email1.get())
  arquivo.write('\nContato: %s'% telefone1.get())
  arquivo.write('\nOBS: %s'% obs1.get('1.0',END))#Por ser um Text, e não um Label
  arquivo.write('\n________________________________________________________________________________')
  arquivo.write('\n\n')
#Criando janela
app = Tk()
app.title('!!Testando!!') #Título da janela 
app.geometry('500x700') #Ajusta medidas da janela
app.configure(background='#FFE4B5') #Colocando a cor com RGB

  
"""
x = lado esquerdo
y = Alto
width = Largura
height = Altura 
"""
boas_vindas = Label(app, text="!!BOA NOITE!!", foreground="#000",background="#FFE4B5")
boas_vindas.place(x=200,y=10,width=100,height=15)

nome = Label(app, text="Nome:",background="#FFE4B5",anchor='w')
nome.place(x=10,y=50,width=100,height=20)

nome1 = Entry(app,)
nome1.place(x=10,y=70,width=200,height=20)


sobrenome = Label(app, text="Sobrenome:",background="#FFE4B5",anchor='w')
sobrenome.place(x=10,y=90,width=100,height=20)

sobrenome1 = Entry(app)
sobrenome1.place(x=10,y=110,width=200,height=20)


email = Label(app, text="E-mail:",background="#FFE4B5",anchor='w')
email.place(x=10,y=130,width=100,height=20)

email1 = Entry(app)
email1.place(x=10,y=150,width=200,height=20)


telefone = Label(app,text='Contato:', background='#FFE4B5',anchor='w')
telefone.place(x=10,y=170, width=100,height=20)

telefone1 = Entry(app)
telefone1.place(x=10,y=190, width=200, height=20)

obs = Label(app, text='OBS:',background='#FFE4B5', anchor='w')
obs.place(x=10,y=210,width=100,height=100)

obs1 = Text(app)
obs1.place(x=10,y=270,width=300,height=150)


botão = Button(app, text='Enviar', command=gravar_dados)
botão.place(x=10,y=450,width=100,height=20)






app.mainloop() #Mantem a caixa em loop para mantela aberta