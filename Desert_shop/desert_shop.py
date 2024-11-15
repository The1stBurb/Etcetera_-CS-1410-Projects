# Changes to Order Class
# add a new method, order_cost(), that calculates and returns the total cost for all items in the order
# add a new method, order_tax(), calculates and returns the total tax for all items in the order

from desert import candy,iceCream,cookie,sunday
from recipter import maker
items=[
    candy("Candy Corn", 1.5, .25),
    iceCream("Gummy Bears", .25, .35),
    candy("Chocolate Chips", 6, 3.99),
    sunday("Pistachio", 2, .79, "Hot Fudge", 1.29),
    iceCream("Vanilla", 3, .69),
    cookie("Oatmeal Raisin", 2, 3.45),
]
class desShop():
    def __init__(self):
        pass
    def user_prompt_cookie(self):
        nm=input("What kind of cookie do you want? ")
        am=0
        while True:
            am=input("How many dozens? ")
            if am.isdigit():
                am=float(am)
                break
        pr=0
        while True:
            pr=input("How is the price per dozen? ")
            if pr.isdigit():
                pr=float(pr)
                break
        return cookie(nm,am,pr)
    def user_prompt_candy(self):
        nm=input("What kind of CANDY do you want? ")
        am=0
        while True:
            am=input("How many pounds? ")
            if am.isdigit():
                am=float(am)
                break
        pr=0
        while True:
            pr=input("How is the price per pound? ")
            if pr.isdigit():
                pr=float(pr)
                break
        return candy(nm,am,pr)
    def user_prompt_icecream(self):
        nm=input("What kind of icecream do you want? ")
        am=0
        while True:
            am=input("How many scoops? ")
            if am.isdigit():
                am=int(am)
                break
        pr=0
        while True:
            pr=input("How is the price per scoop? ")
            if pr.isdigit():
                pr=float(pr)
                break
        return iceCream(nm,am,pr)
    def user_prompt_sundae(self):
        nm=input("What kind of icecream do you want? ")
        am=0
        while True:
            am=input("How many scoops? ")
            if am.isdigit():
                am=int(am)
                break
        pr=0
        while True:
            pr=input("How is the price per scoop? ")
            if pr.isdigit():
                pr=float(pr)
                break
        tp=input("What kind of topping do you want? ")
        tpr=0
        while True:
            tpr=input("How is the price for the topping? ")
            if tpr.isdigit():
                tpr=float(tpr)
                break
        return sunday(nm,am,pr,tp,tpr)
    
class order:
    def __init__(self):
        self.ord=[]
    def add(self,itm):
        # quan=input(f"How many {itm.nm}s would you like? ")
        # itm.quan=quan
        self.ord.append(itm)
    def __str__(self):
        return "\n".join([f"{i.nm}" for i in self.ord])+f"\nTotal number of items in the order: {len(self.ord)}"#{i.quan}x 
    def __len___(self):
        return len(self.ord)
    def ordtx(self):
        txs=0
        for i in self.ord:
            txs+=round((i.calctx())*100)/100
        return txs
    def ordcst(self):
        tp=0
        for i in self.ord:
            tp+=i.cost()
        return tp
def main2():
    ord=order()
    # print(ord)
    for i in items:
        ord.add(i)
    # ord.add(items[3])
    print(ord)
    ll=[]
    for i in ord.ord:
        ll.append([i.nm,i.cost(),round((i.calctx())*100)/100])
    ll.append(["Order Subtotals",ord.ordcst(),ord.ordtx()])
    ll.append(["Order Total",ord.ordcst()+ord.ordtx(),""])
    ll.append(["Total items in order","",len(ord.ord)])
    print(ll)
    maker(ll,"ord.pdf")
def main():
    shop = desShop()
    order = order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sunday',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.nm} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.nm} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.nm} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.nm} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()
    #
    #add your code below here to print the PDF receipt as the last thing in main()
    #

main()
# Name	Item Cost	Tax
# Candy Corn	$0.38	$0.03
# Gummy Bears	$0.09	$0.01
# Chocolate Chip	$2.00	$0.14
# Pistachio	$1.58	$0.11
# Vanilla	$3.36	$0.24
# Oatmeal Raisin	$0.57	$0.04
# --------------------------------------------------------
# Order Subtotals	$7.97	$0.58
# Order Total		$8.55
# Total items in the order		6