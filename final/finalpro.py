def read_customer_file(filename):
   
    customers = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            customers[data[3]] = {
                'name': data[0],
                'family_name': data[1],
                'phone': data[2]
            }
    return customers

def read_storage_file(filename):
    
    storage = []
    with open(filename, 'r') as file:
        
        next(file)
        for line in file:
            data = line.strip().split('|')
            storage.append({
                'goods_id': data[0],
                'input': int(data[1]),
                'output': int(data[2]),
                'price': float(data[3])
            })
    return storage

def read_goods_item_file(filename):
    
    goods_items = {}
    with open(filename, 'r') as file:
     
        next(file)
        for line in file:
            data = line.strip().split('|')
            goods_items[data[0]] = {
                'name': data[1],
                'price': float(data[2])
            }
    return goods_items


def assign_goods_to_customers():
    
    customer_goods_mapping = {
        '1': ['1', '2','5'],  
        '2': ['3', '4','1'],  
        '3': ['1', '4','2'],  
        '4': ['2', '5','4'],  
        '5': ['3', '5','2']   
    }
    return customer_goods_mapping

def generate_bill(customer_id, discount_percentage, customer_goods_mapping):
    customers = read_customer_file('G:\\python mojtamafani\\final\\customer.txt')
    storage = read_storage_file('G:\\python mojtamafani\\final\\storage.txt')
    goods_items = read_goods_item_file('G:\\python mojtamafani\\final\\list_item.txt')

    
    customer = customers.get(customer_id)

    if customer:
        try:
            
            discount = float(discount_percentage) / 100.0

            
            selected_goods_ids = customer_goods_mapping.get(customer_id, [])

            
            print("                                           Factor")
            print(f"name: {customer['name']:40}family name: {customer['family_name']:40}phone: {customer['phone']}")

            
            total_price = 0

           
            print(f"{'Name':<10}{'Price':<20}{'Amount':<20}{'Discount':<20}{'Final Price':<20}")

            
            for goods_id in selected_goods_ids:
                goods_item = goods_items.get(goods_id)
                if goods_item:
                    input_amount = 0
                    output_amount = 0

                   
                    for s in storage:
                        if s['goods_id'] == goods_id:
                            input_amount += s['input']
                            output_amount += s['output']

                    amount = input_amount - output_amount
                    price = goods_item['price']
                    total_price_item = (price * amount) - (price * amount * discount)

                    
                    price_formatted = f"${price:.2f}"
                    total_price_item_formatted = f"${total_price_item:.2f}"
                    discount_percentage_formatted = f"{discount * 100:.1f}%"

                    
                    print(f"{goods_item['name']:<10}{price_formatted:<20}{amount:<20}{discount_percentage_formatted:<20}{total_price_item_formatted:<20}")

                   
                    total_price += total_price_item

            
            total_price_formatted = f"${total_price:.2f}"
            
            
            print(f"\nTOTAL: {total_price_formatted:<66}")
        except ValueError:
            print("Invalid discount percentage. Please enter a numeric value.")
    else:
        print(f"Customer with ID '{customer_id}' not found.")


customer_id = input("Enter customer ID: ")
discount_percentage = input("Enter discount percentage (e.g., 15 for 15%): ")
customer_goods_mapping = assign_goods_to_customers()
generate_bill(customer_id, discount_percentage, customer_goods_mapping)

