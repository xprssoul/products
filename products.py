"""
這是一個記帳程式。
"""
import os #operating system 作業系統
#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
    print('找到檔案了！')
    with open('products.csv', 'r', encoding = 'utf-8') as f: #讀取檔案跟寫入檔案都會有編碼上的問題
        for line in f:
            if '商品,價格' in line:
                continue #欄位文字不用讀取，跳過
            name, price = line.strip().split(',') #把尾巴的換行符號拿掉、且每一行遇到逗點就分隔
            products.append([name, price])
    print(products)
else:
    print('找不到檔案...')
#讓使用者輸入商品名稱
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    #二維清單詳細寫法：
        #p = []
        #p.append(name)
        #p.append(price)
        #products.append(p)
    #二維清單一行寫法：
    products.append([name, price])
print(products)
#印出所有商品價格
for p in products:
    print(p[0], '的價格為', p[1])
#寫入檔案：
with open('products.csv', 'w', encoding = 'utf-8') as f: #讀取檔案跟寫入檔案都會有編碼上的問題
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')