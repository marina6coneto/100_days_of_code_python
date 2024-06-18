# tip calculator to split the bills 

print('Welcome to the tip calculator!')
conta = float(input('What was the total bill? $'))
gorjeta = int(input('How much tip would you like to give? 10, 12, or 15? '))
pessoas = int(input('How many people to split the bill? '))


gorjeta_porcentagem = gorjeta / 100
gorjeta_total = conta * gorjeta_porcentagem
conta_total = conta + gorjeta_total
dividir_conta = conta_total / pessoas
print(f'Each person will pay: ${dividir_conta:.2f}')
