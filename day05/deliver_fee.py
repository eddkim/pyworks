#배송비 계싼

def get_price(each_price,quantity):
    delivery_fee = 2500
    price = each_price*quantity #(주문 상품가격 = 해당 제품*수량)
    if price < 20000 :
        price+delivery_fee
        return price+delivery_fee
    else: return price




price1 = get_price(15000,2)
price2 = get_price(5000,3)
print("상품 1 가격은 "+str(price1)+"원 입니다.")
print("상품 2 가격은 "+format(price2,",d")+"원 입니다.") #디폴트는 천단위