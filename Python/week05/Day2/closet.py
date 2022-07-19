class closet:
    def __init__(self,length,breadth,hight,max_capacity,items):
        self.length=float(length)
        self.breadth=float(breadth)
        self.hight=float(hight)
        self.max_capacity=int(max_capacity)
        self.items=int(items)

    def store_item(self):
        toAdd=input("Add items to the list")
    def fetch_item(self):
        self.items.pop(0)


        
