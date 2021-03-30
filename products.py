#記帳程式
#清單包含物件與價格
#如何建立清單中的清單？二維清單

products = []

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price]) #小清單p裝進大清單products
print(products)

#拿出大清單中的物件
for p in products:
	print(p[0], '的價格是', p[1])

#把使用者輸入的資料寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: #這一行在打開檔案,用utf-8編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #這一行在寫入