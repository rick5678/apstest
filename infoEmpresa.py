class infoEmpresa:
    def __init__(self, produtora, endereco, prodAnual, numFunc, 
    destProd, qntMaq, nvlAuto):
        self.produtora = produtora
        self.endereco = endereco
        self.prodAnual = prodAnual
        self.numFunc = numFunc
        self.destProd = destProd
        self.qntMaq = qntMaq
        self.nvlAuto = nvlAuto

class infoFiscal:
    def __init__(self, nomeEmpresa,fclRcb, ImptMPago, ImptEPago, ImptRPago):
        self.nomeEmpresa = nomeEmpresa
        self.fclRcb = fclRcb
        self.ImptMPago = ImptMPago
        self.ImptEPago = ImptEPago
        self.ImptRPago = ImptRPago

class Produto:
    def __init__(self, nome, quantia):
        self.nome = nome
        self.quantia = quantia

produto1 = Produto('Açucar', '70 toneladas')
produto2 = Produto('Alcool', '154 toneladas')
produto3 = Produto('Energia', '20 toneladas')
produto4 = Produto('Milho', '13 toneladas')
produto5 = Produto('Café', '4 toneladas')
produto6 = Produto('Ração', '10 toneladas')
produto7 = Produto('Proteina Animal', '1.000.000 toneladas')
produto8 = Produto('Soja', '25 toneladas')


lista = [produto1, produto2, produto3]
lista2 = [produto4, produto5, produto6]
lista3 = [produto4, produto8]
lista4 = [produto5]
lista5 = [produto7]

empresa1 = infoEmpresa('CENTRAL AÇUCAREIRA SANTO ANTONIO S.A.', 'São Luís do Quitunde, ZONA RURAL, AL', '750 mil', '380', 'Exportação', 'Não informado', 'Não informado')

empresa2 = infoEmpresa('Amaggi Agro', 'São Miguel do Iguaçu (PR)', '1 milhão de toneladas de grãos', '7821', 'Mercado Interno', '876', 'Não informado')

empresa3 = infoEmpresa('alex stewart agriculture supervisão e analises ltda', 'Paranaguá, Rua Aristides de Oliveira, PR ', '1500 kg de soja e 4000 kg de milho', 'média 100 funcionários', 'Mercado interno e Externo ', '30', 'Manufaturada')

empresa4 = infoEmpresa('Areiao Agropesca', 'Guarulhos (SP)', '4 mil kg de café', '280', 'Mercado Interno', '123', 'Não informado')

empresa5 = infoEmpresa('JBS', 'Anápolis (GO)', '1 milhão de toneladas de proteina animal', '20000', 'Mercado Interno e externo', '15000', 'Não informado')

fiscal1 = infoFiscal(empresa1.produtora ,'1500 kg', 'R$ 86.540,94', 'R$ 120.010,21', 'R$ 83.202,03')

fiscal2 = infoFiscal(empresa2.produtora,'R$ 9 milhões e 721 mil', 'R$ 3 milhões e 214 mil', 'R$ 4 Milhões e 508 mil', 'R$ 2 Milhões e 201 mil')

fiscal3 = infoFiscal(empresa3.produtora, 'R$ 8 milhões', 'R$ 4 milhões e 300 mil', 'R$ 1 milhão e 600 mil', 'R$ 2 milhões e 340 mil')

fiscal4 = infoFiscal(empresa4.produtora, 'R$ 5 milhões', 'R$ 2 milhões e 300 mil', 'R$ 1 milhão', 'R$ 2 milhões')

fiscal5 = infoFiscal(empresa5.produtora, 'R$ 10 bilhões', 'R$ 16 bilhões', 'R$ 20 bilhões', 'R$ 18 bilhões')