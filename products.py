#記帳程式
#清單包含物件與價格
#如何建立清單中的清單？二維清單
#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續迴圈，跳到下一回，而break是直接跳出迴圈，會寫在比較高的位置
		name, price = line.strip().split(',') #去掉換行符號\n，然後遇到逗號切割，切割完後變清單
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price]) #小清單p裝進大清單products
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#把使用者輸入的資料寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: #這一行在打開檔案,用utf-8編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #這一行在寫入