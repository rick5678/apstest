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

produto1 = Produto('Açucar', '10')
produto2 = Produto('alcool', '15')
produto3 = Produto('energia', '20')


empresa1 = infoEmpresa('CENTRAL AÇUCAREIRA SANTO ANTONIO S.A.', 'São Luís do Quitunde, ZONA RURAL, AL', '750 mil', '380', 'Exportação', 'Não informado', 'Não informado')

empresa2 = infoEmpresa('Amaggi Agro', 'São Miguel do Iguaçu (PR)', '1 milhão de toneladas de grãos', '7821', 'Mercado Interno', '876', 'Não informado')

empresa3 = infoEmpresa('alex stewart agriculture supervisão e analises ltda', 'Paranaguá, Rua Aristides de Oliveira, PR ', '1500 kg de soja e 4000 kg de milho', 'média 100 funcionários', 'Mercado interno e Externo ', '30', 'Manufaturada')

fiscal1 = infoFiscal(empresa1.produtora ,'1500 kg', 'R$ 86.540,94', 'R$ 120.010,21', 'R$ 83.202,03')

fiscal2 = infoFiscal(empresa2.produtora,'R$ 9 milhões e 721 mil', 'R$ 3 milhões e 214 mil', 'R$ 4 Milhões e 508 mil', 'R$ 2 Milhões e 201 mil')

fiscal3 = infoFiscal(empresa3.produtora, 'R$ 8 milhões', 'R$ 4 milhões e 300 mil', 'R$ 1 milhão e 600 mil', 'R$ 2 milhões e 340 mil')