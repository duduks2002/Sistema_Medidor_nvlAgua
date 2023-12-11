import time
import datetime
import serial
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animação(i, datalist, ser):
    ser.write(b'g')
    arduinoData_String = ser.readline().decode('ascii')
    try:
        arduinoData = int(arduinoData_String)
        datalist.append(arduinoData)
    except:
        pass
    datalist = datalist[-5:]  # esse comando faz com que leia 5 numeros no grafico

    ax.clear()
    ax.plot(datalist, '-o')
    ax.set_ylim([0,1])
    ax.set_title("Saida Serial")
    ax.set_ylabel('MÍNIMO ------------------------ LIMITE')

def salvar_em_csv(lista):
    # Obter a data atual
    data_arquivo = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    data_formatada = datetime.datetime.now().strftime("%d/%m/%Y")
    # Nome do arquivo CSV com a data atual
    nome_arquivo =  f'log\dados_{data_arquivo}.csv'

    # Escrever os dados da lista no arquivo CSV
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['Dado', 'Data'])  # Cabeçalho do CSV

        for dado in lista:
            escritor_csv.writerow([dado, data_formatada])
datalist = []

fig = plt.figure("MEDIDOR DE NIVEL D'AGUA")
ax = fig.add_subplot(111)
ser = serial.Serial("COM3", 9600)
time.sleep(2)

ani = animation.FuncAnimation(fig, animação, frames=100, fargs=(datalist, ser), interval= 800)
#linha de cima é responsavel por chamar a função diversas vezes

plt.show()
ser.close()
salvar_em_csv(datalist)