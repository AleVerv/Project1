slovo1 = input()
slovo2 = input()
predlojenie = (f'{slovo1} {slovo2}')
print(predlojenie)
predlojenie_perem_mesta = (f'{slovo2} {slovo1}')
new_pr = (f"!{slovo2} {slovo1}!")
print(new_pr)
print(new_pr, sep=' ! ') #или
print(f"'!', {slovo1} ! {slovo2}, '!'", sep=' ! ')
