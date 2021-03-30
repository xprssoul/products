#記帳程式
#清單包含物件與價格
#如何建立清單中的清單？二維清單

products = []

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price]) #小清單p裝進大清單products
print(products)

#拿出大清單中的物件
for p in products:
	print(p[0], '的價格是', p[1])