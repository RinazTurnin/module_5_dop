
def password(n):
  y = ""
  for i in range(1,21):
    for j in range(i+1, 21):
      pair_sum = i + j
      if n % pair_sum == 0:
        pair_str = str(i) + str(j)
        y += pair_str
  return y    
     
for n in range(3,21):
  print(f"Ключ:{n} - Пароль:{password(n)}")