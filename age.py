driving = input('請問你有沒有開過車? ')
age = input('請問你的年齡? ')
age = int(age)

if driving !='有' and driving !='沒有' :
	print('第一個問題只能回答 有/沒有')
	raise SystemExit

if driving == '有':
	if age >=18:
		print('你通過驗證')
	else:
		print('奇怪 你怎麼開過車')
elif driving == '沒有':
	if age >=18:
		print('你可以去考駕照')
	elif age < 18:
		print('很好 再過幾年可以考駕照')