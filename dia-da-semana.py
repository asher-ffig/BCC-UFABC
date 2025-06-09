d = int(input("Digite o dia:"))
m = int(input("Digite o mês:"))
a = int(input("Digite o ano:"))

def dia_da_semana(d, m, a) -> str:
  ax = a - (14 - m)//12
  x = ax + (ax//4) - (ax//100) + (ax//400)
  mx = m + 12 * ((14 - m)//12) - 2
  dx = (d + x + (31 * mx) // 12) % 7
  return ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"][dx]

dia_da_semana(d, m, a)
