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
def main():
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