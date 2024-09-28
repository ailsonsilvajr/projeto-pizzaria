from colorama import Fore, init

init()

color = {
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'reset': Fore.RESET,
}

menu = [
    {'cod': 1, 'name': 'Calabresa', 'sizes': {'Pequena': 'R$19,70', 'Média': 'R$25,70', 'Grande': 'R$30,70'}},
    {'cod': 2, 'name': 'Mussarela', 'sizes': {'Pequena': 'R$22,70', 'Média': 'R$28,70', 'Grande': 'R$33,70'}},
    {'cod': 3, 'name': 'Frango', 'sizes': {'Pequena': 'R$21,70', 'Média': 'R$27,70', 'Grande': 'R$32,70'}},
    {'cod': 4, 'name': 'Portuguesa', 'sizes': {'Pequena': 'R$23,70', 'Média': 'R$29,70', 'Grande': 'R$34,70'}},
    {'cod': 5, 'name': 'Quatro Queijos', 'sizes': {'Pequena': 'R$24,70', 'Média': 'R$30,70', 'Grande': 'R$35,70'}},
    {'cod': 6, 'name': 'Marguerita', 'sizes': {'Pequena': 'R$20,70', 'Média': 'R$26,70', 'Grande': 'R$31,70'}},
    {'cod': 7, 'name': 'Pepperoni', 'sizes': {'Pequena': 'R$25,70', 'Média': 'R$31,70', 'Grande': 'R$36,70'}},
    {'cod': 8, 'name': 'Vegetariana', 'sizes': {'Pequena': 'R$22,70', 'Média': 'R$28,70', 'Grande': 'R$33,70'}},
    {'cod': 9, 'name': 'Napolitana', 'sizes': {'Pequena': 'R$21,70', 'Média': 'R$27,70', 'Grande': 'R$32,70'}},
    {'cod': 10, 'name': 'Bacon', 'sizes': {'Pequena': 'R$23,70', 'Média': 'R$29,70', 'Grande': 'R$34,70'}},
    {'cod': 11, 'name': 'Romana', 'sizes': {'Pequena': 'R$22,70', 'Média': 'R$28,70', 'Grande': 'R$33,70'}},
    {'cod': 12, 'name': 'Palmito', 'sizes': {'Pequena': 'R$24,70', 'Média': 'R$30,70', 'Grande': 'R$35,70'}},
    {'cod': 13, 'name': 'Frango com Catupiry', 'sizes': {'Pequena': 'R$23,70', 'Média': 'R$29,70', 'Grande': 'R$34,70'}},
    {'cod': 14, 'name': 'Camarão', 'sizes': {'Pequena': 'R$27,70', 'Média': 'R$33,70', 'Grande': 'R$38,70'}},
    {'cod': 15, 'name': 'Atum', 'sizes': {'Pequena': 'R$22,70', 'Média': 'R$28,70', 'Grande': 'R$33,70'}},
    {'cod': 16, 'name': 'Carne Seca com Catupiry', 'sizes': {'Pequena': 'R$24,70', 'Média': 'R$30,70', 'Grande': 'R$35,70'}},
    {'cod': 17, 'name': 'Abobrinha com Gorgonzola', 'sizes': {'Pequena': 'R$25,70', 'Média': 'R$31,70', 'Grande': 'R$36,70'}},
    {'cod': 18, 'name': 'Brócolis com Bacon', 'sizes': {'Pequena': 'R$23,70', 'Média': 'R$29,70', 'Grande': 'R$34,70'}},
    {'cod': 19, 'name': 'Alho e Óleo', 'sizes': {'Pequena': 'R$20,70', 'Média': 'R$26,70', 'Grande': 'R$31,70'}},
    {'cod': 20, 'name': 'Califórnia (Doce)', 'sizes': {'Pequena': 'R$24,70', 'Média': 'R$30,70', 'Grande': 'R$35,70'}},
]

delivery_fee = 5.00  

def convert_price(price_str):
    return float(price_str.replace('R$', '').replace(',', '.'))

while True:
    print(f"{color['blue']}PIZZARIA DEV{color['reset']}")
    print(f'\n[CARDÁPIO]')
    for item in menu:
        print(f'{item["cod"]}. {item["name"]}')
        for size, price in item['sizes'].items():
            print(f'    {size}: {color["yellow"]}{price}{color["reset"]}')
    
    choose1 = int(input(f"\n{color['magenta']}Escolha o primeiro sabor: {color['reset']}"))
    meio_a_meio = input(f"\n{color['magenta']}Deseja pizza meio a meio? (s/n): {color['reset']}").lower()
    
    if meio_a_meio == 's':
        choose2 = int(input(f"{color['magenta']}Escolha o segundo sabor: {color['reset']}"))
    else:
        choose2 = None
    
    size = input(f"{color['magenta']}Escolha o tamanho (Pequena/Média/Grande): {color['reset']}").capitalize()

    if meio_a_meio == 's' and choose2:
        price1 = convert_price(menu[choose1-1]['sizes'][size])
        price2 = convert_price(menu[choose2-1]['sizes'][size])
        pizza_price = (price1 + price2) / 2
    else:
        pizza_price = convert_price(menu[choose1-1]['sizes'][size])

    delivery = input(f"\n{color['magenta']}Deseja entrega? (s/n): {color['reset']}").lower()
    
    if delivery == 's':
        endereco = input(f"{color['magenta']}Digite seu endereço: {color['reset']}")
        total_price = pizza_price + delivery_fee
        print(f"{color['blue']}Sua pizza será entregue em: {endereco}{color['reset']}")
        print(f"{color['blue']}Taxa de entrega: {color['yellow']}R${delivery_fee:.2f}{color['reset']}")
    else:
        total_price = pizza_price
        print(f"{color['blue']}Você escolheu retirar a pizza na pizzaria.{color['reset']}")
    
    print(f"\n{color['blue']}Valor total do pedido: {color['yellow']}R${total_price:.2f}{color['reset']}")

    payment_method = input(f"\n{color['magenta']}Forma de pagamento (cartão ou dinheiro): {color['reset']}").lower()
    
    if payment_method == 'cartão':
        card_type = input(f"{color['magenta']}Cartão de crédito ou débito? (crédito/débito): {color['reset']}")
        print(f"{color['blue']}Você pagará com cartão de {card_type}.{color['reset']}")
    else:
        # Pagar em dinheiro
        dinheiro_pago = float(input(f"{color['magenta']}Quanto você pagou? R${color['reset']}").replace(',', '.'))
        troco = dinheiro_pago - total_price
        if troco >= 0:
            print(f"{color['blue']}Você pagará em dinheiro.{color['reset']}")
            if troco > 0:
                print(f"{color['blue']}Seu troco é: {color['yellow']}R${troco:.2f}{color['reset']}")
        else:
            print(f"{color['red']}O valor pago é menor do que o total do pedido. Por favor, pague a quantia correta.{color['reset']}")

    outro_pedido = input(f"\n{color['magenta']}Deseja fazer outro pedido? (s/n): {color['reset']}").lower()
    
    if outro_pedido == 'n':
        print(f"{color['blue']}Obrigado por escolher a PIZZARIA DEV!{color['reset']}")
        break
