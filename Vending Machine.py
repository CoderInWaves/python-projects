import time

class Vending_Machine:
    @staticmethod
    def process():
        item = {
            70:"Chips",
            90: "Coldrink",
            150: "Venila icecream",
            200 : "Chocopy monoco",
            120: "Biscuit", 
            80: "Dairy Milk",
            190 : "Dry coffee",
            105 : "Premium Tea",
            125: "Cream bread"
        }
        print(item)
        print("Select items above with their name")

        money = int(input("Enter your money: "))
        while True:
            ite = str(input("Select an item from above list: "))
            if ite == "exit":
                print("THANK YOU FOR USING US :)")
                print(f"Your amount {money} refuneded successfully!")
                break
            else:

                item_found = False
                if money >= min(item.keys()):
                    for key , value in item.items():
                            if ite == value:
                                if money >= key:
                                    money -= key
                                    print(f"Your item {ite} get dispatched, available balance {money}")
                                    item_found = True
                                    break
                    if not item_found:
                        print(f"{ite} not in stock")
                            
                else:
                    print("Enter sufficient amount to buy")
                    money = int(input("Enter your money: "))
                            


if __name__=="__main__":
    Vending_Machine.process()