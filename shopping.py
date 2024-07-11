# Shopping_Cart:---

class MyCart:
    def __init__(self):
        self.my_items = []

    def add_item(self,item,price):
        self.my_items.append({'item_name':item,'item_price':price})

    def show_items(self):
        if len(self.my_items)==0:
            print("Cart is empyty")
        else:
            print("All cart details are :")
            for i in (self.my_items):
                print(i['item_name'],'=',i['item_price'])   

    def total_price(self):
        total = 0
        for i in self.my_items:
            total += i["item_price"]
        print("Total Amount =",total)
    
    def remove_item(self, item_name):
        for item in self.my_items:
            if item["item_name"] == item_name:
                self.my_items.remove(item)
                break

    def clear_cart(self):
        self.my_items=[]
        print("Now your cart is empity...")
        
    
obj = MyCart()
obj.add_item('Laptop',25000)
obj.add_item('Table_Lamp',5000)
obj.add_item('Decor',2000)
obj.show_items()
obj.total_price()
obj.remove_item('Laptop')
obj.show_items()
obj.total_price()
obj.clear_cart()
obj.show_items()
