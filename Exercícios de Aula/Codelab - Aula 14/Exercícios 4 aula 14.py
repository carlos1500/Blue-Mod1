def calculadosalário (horas, salario):
    salario_hora =  salario / 40
    s_receber = salario_hora * horas
    if horas > 40:
        s_receber = salario
        horasExtras = horas - 40
        valorHorasEtras = horasExtras * 1.5 * salario_hora
        s_receber += valorHorasEtras
    print(f"Seu salario será: R${s_receber:.2f}")

salario1 = float(input("Salario: "))
horas1 = float(input("Horas trabalhadas: "))
calculadosalário(horas1, salario1)

