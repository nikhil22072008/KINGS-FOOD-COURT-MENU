#1 OUR ITEM

class OurItem:
   
    def __init__(self, name, price):
       
        self.name = name
       
        self.price = price

#2 ORDER

class Order:
    
    
    def __init__(self):
      
        self.items = []
   
   
    def add_item(self, OurItem):
       
        self.items.append(OurItem)
       
        print(f"Added {OurItem.name} to your order.")
    
   
    def total(self):
       
        return sum(item.price for item in self.items)
    
   
    def show_order(self):
       
        if not self.items:
           
            print("No items in order.")
          
            return
        
        
        print("\nYour Order:")
     
        for i, item in enumerate(self.items, 1):
         
            print(f"{i}. {item.name} - ₹{item.price}")
      
        print(f"Total: ₹{self.total()}\n")
    
    
    def checkout(self):
        
        if not self.items:
           
            print("Your cart is empty.")
            
            return
        
        self.show_order()
     
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
       
        if confirm == "yes":
           
            print("Order confirmed! Thank you.")
            
            self.items.clear()
        
        else:
            
            print("Checkout cancelled.")

# MENU

def main():

    menu = [

        OurItem("Orange Juice", 19), 

        OurItem("Oreo Shake", 87),

        OurItem("Mango Juice", 43),

        OurItem("Cold Drink", 41),

        OurItem("Banana Shake", 93),

        OurItem("Veg Manchurian", 154),

        OurItem("Hakka Noodles", 169),

        OurItem("Veg Fried Rice", 179),

        OurItem("Cakes", 633),

        OurItem("Pastries", 112),

        OurItem("Choco Lava", 143),

        OurItem("Aloo Tikki", 35),

        OurItem("Samosa", 30),

        OurItem("Pani Puri(4pcs)", 20)
    ]

   #LOOP

    my_order = Order()
    
    while True:
        
        print("\n *****KINGS FOOD COURT MENU*****")

        for i, fooditem in enumerate(menu, 1):

            print(f"{i}. {fooditem.name} - ₹{fooditem.price}")
        
        print("15. View Order")
        
        print("16. Checkout")
        
        print("17. Exit")
        
        choice = input("Choose an option: ")
        
        #SELECTION

        if choice.isdigit():
            
            choice = int(choice)

            if 1 <= choice <= 14:
                my_order.add_item(menu[choice - 1])

            elif choice == 15:
                my_order.show_order()

            elif choice == 16:
                my_order.checkout()

            elif choice == 17:
                print("Thanks For Visiting Kings Food Court. Goodbye!")
                
                break
            
            else:
                
                print("Invalid choice. Try again.")
        
        
        else:
            
            print("Please enter a number.")

# MAIN

if __name__ == "__main__":
    
    main()