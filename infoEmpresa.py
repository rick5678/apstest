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
    def __init__(self, fclRcb, ImptMPago, ImptEPago, ImptRPago):
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

empresa2 = infoEmpresa('CENTRAL AÇUCAREIRA SANTO ANTONIO S.A.', 'São Luís do Quitunde, ZONA RURAL, AL', '750 mil', '380', 'Exportação', 'Não informado', 'Não informado')

fiscal1 = infoFiscal('1500 kg', '86.540,94', '120.010,21', '83.202,03')

fiscal2 = infoFiscal('1500 kg', '86.540,94', '120.010,21', '83.202,03')