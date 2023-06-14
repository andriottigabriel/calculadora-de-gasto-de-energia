from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # rota raiz da url ex ip
def index(): # função index quando digitar no navegardor
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    preco_conta = float(request.form['preco_conta'])
    valor_kw = float(request.form['valor_kw'])

    
    # Solicita o preço do KW/hora da conta de energia elétrica

   # preco_conta = float(input("Insira o preço final de sua ultima conta de energia elétrica: "))
   # valor_kw = float(input("Insira o total de kw consumido em sua ultima conta de Energia Elétrica: "))

    preco_kw = round(valor_kw / preco_conta , 2)

    print("O preço médio do KW/hora + impostos é de: ",preco_kw," REAIS")

    # Inicialização das variáveis
    custo_chuveiro = 0
    custo_geladeira = 0
    custo_microondas = 0
    custo_lavaroupa = 0
    custo_lampadas = 0
    custo_ar = 0
    custo_tv = 0

    # Solicita o consumo diário de cada equipamento
    qtd_chuveiro= int(request.form['qtd_chuveiro'])
    #if qtd_chuveiro > 0 :
    potencia_chuveiro = float(request.form['potencia_chuveiro'])
    tempo_chuveiro = float(request.form['tempo_chuveiro'])

    custo_chuveiro = (((qtd_chuveiro * potencia_chuveiro * tempo_chuveiro)/1000) * preco_kw)  * 30
        #print(custo_chuveiro)


    qtd_geladeira= int(request.form['qtd_geladeira'])

   # if qtd_geladeira > 0 :
    potencia_geladeira = float(request.form['potencia_geladeira'])
    tempo_geladeira = float(request.form['tempo_geladeira'])

    custo_geladeira = (((qtd_geladeira * potencia_geladeira * tempo_geladeira)/1000) * preco_kw)*30
    #print(custo_geladeira)


    qtd_microondas= int(request.form['qtd_microondas'])
    #if qtd_microondas > 0 :
    potencia_microondas = float(request.form['potencia_microondas'])
    tempo_microondas = float(request.form['tempo_microondas'])

    custo_microondas = (((qtd_microondas * potencia_microondas * tempo_microondas)/1000) * preco_kw)*30
    # print(custo_microondas)


    qtd_lavaroupa= int(request.form['qtd_lavaroupa'])
   # if qtd_lavaroupa > 0 :
    potencia_lavaroupa = float(request.form['potencia_lavaroupa'])
    tempo_lavaroupa = float(request.form['tempo_lavaroupa'])

    custo_lavaroupa = (((qtd_lavaroupa * potencia_lavaroupa * tempo_lavaroupa)/1000) * preco_kw)*30
        #print(custo_lavaroupa)


    qtd_lampadas= int(request.form['qtd_lampadas'])
   # if qtd_lampadas > 0 :
    potencia_lampadas = float(request.form['potencia_lampadas'])
    tempo_lampadas = float(request.form['tempo_lampadas'])

    custo_lampadas = (((qtd_lampadas * potencia_lampadas * tempo_lampadas)/1000) * preco_kw)*30
        #print(custo_lampadas)


    qtd_ar= int(request.form['qtd_ar'])
    #if qtd_ar > 0 :
    potencia_ar = float(request.form['potencia_ar'])
    tempo_ar = float(request.form['tempo_ar'])

    custo_ar = (((qtd_ar * potencia_ar * tempo_ar)/1000) * preco_kw)*30
    # print(custo_ar)

    qtd_tv= int(request.form['qtd_tv'])
   # if qtd_tv > 0 :
    potencia_tv = float(request.form['potencia_tv'])
    tempo_tv = float(request.form['tempo_tv'])

    custo_tv = (((qtd_tv* potencia_tv * tempo_tv)/1000) * preco_kw)*30
        #print(custo_tv)




    # Apresenta o relatório final com o consumo mensal em KW/hora e em reais de cada equipamento
    print("\n Relatório de consumo mensal de energia elétrica por equipamento, O primeiro equipamento é o que gasta mais e o ultimo menos ")


    variaveis = {
        'GASTO CHUVEIRO' : round(custo_chuveiro,2),
        'GASTO GELADEIRA' : round(custo_geladeira,2),
        'GASTO MICROONDAS' : round(custo_microondas,2),
        'GASTO LAVA ROUPA' : round(custo_lavaroupa,2),
        'GASTO LÂMPADAS' : round(custo_lampadas,2),
        'GASTO AR CONDICIONADO' : round(custo_ar,2),
        'GASTO TELEVISÃO' : round(custo_tv,2)
    }

    # Ordenando o dicionário em ordem decrescente pelos valores
    variaveis_ordenadas = sorted(variaveis.items(), key=lambda x: x[1], reverse=True)

    # Exibindo os valores e as variáveis um abaixo do outro
   # for i, (variavel, valor) in enumerate (variaveis_ordenadas, 1) :
    #    print(f'{i+1}.{variavel}: {valor:.2f} REAIS')

    for i, (variavel, valor) in enumerate(variaveis_ordenadas[::-1], 1):
        print(f'{len(variaveis) - i + 1}. {variavel}: {valor:.2f} REAIS')

    return render_template('result.html', variaveis=variaveis_ordenadas)

if __name__ == '__main__':
    app.run()
