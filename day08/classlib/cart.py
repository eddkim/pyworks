class Cart :
    li = []

    def __init__(self,goods):
        Cart.li.append(goods)

    def __str__(self):
        return Cart.li

cart1 = Cart("κ³λ")
print(cart1.li)

cart2 = Cart("λλΆ")
print(cart2.li)