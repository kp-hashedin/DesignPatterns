class Shoes:
    
    def __init__(self, info, price):
        self.info = info
        self.price = price
        
    def shoe_info(self):
        return self.info
        
    def shoe_name(self):
        res  = self.info.split(' ')
        return res[0]
        
    def shoe_price(self):
        return self.price
        
        
# Factory Function  
class Factory:
    def nike():
        name = "Nike Shoes Details"
        shoes_price = '38USD'
        return Shoes(name, shoes_price)
    
    def adidas():
        name = "Adidas Shoes Details"
        return Shoes(name, '78USD')
        
    def reebok():
        name =  "Reebok Shoes Details"
        return Shoes(name, '88USD')


# Calling Functions
print((Factory.nike().shoe_info()))     #Output -> Nike Shoes Details
print((Factory.reebok().shoe_info()))   #Output -> Reebok Shoes Details
print((Factory.adidas().shoe_info()))   #Output -> Adidas Shoes Details
print((Factory.adidas().shoe_name()))   #Output -> Adidas
print((Factory.adidas().shoe_price()))  #Output -> 78USD



        
