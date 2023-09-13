def main():
    cost_per_item = 19.99
    quantity = 5 

    subtotal_cost: float = (cost_per_item)*(5) #cost per item multiplied by how many items there are
    tax: float = (subtotal_cost)*(0.13) #tax is 13% of subtotal cost
    total_cost: float = (subtotal_cost + tax) #adding subtotal cost and tax gived total cost
    
    #pytest --capture=sys

    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = 5')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}') 
    print(f'total_cost = ${total_cost:0.2f}')
    
if __name__ == "__main__":
    main()