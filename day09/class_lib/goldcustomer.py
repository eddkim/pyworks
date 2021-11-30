from day09.class_lib.customer import Customer

class GoldCustomer (Customer):
    def __init__(self,cid,name):
        super().__init__(cid,name) #부모 멤버 상속
        self.cgrade="GOLD"
        self.sale_ratio = 0.1
        self.bonus_ratio = 0.02

    def calc_price(self,price):
        price -= price - int(price*self.sale_ratio)
        self.bonus_point+=price*self.bonus_ratio
        #할인 된 가격 = 가격 - (가격 x 구매 할인율)
        return price