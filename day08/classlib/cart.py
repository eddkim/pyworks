class Cart :
    li = []

    def __init__(self,goods):
        Cart.li.append(goods)

    def __str__(self):
        return Cart.li

cart1 = Cart("계란")
print(cart1.li)

cart2 = Cart("두부")
print(cart2.li)