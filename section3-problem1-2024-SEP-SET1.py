def item_amount(item):
  return item['price'] * item['quantity']

def total_bill_amount(grocery_list:list)->float:
  total_amount = 0
  for item in grocery_list:
      total_amount += item_amount(item)
  return total_amount

def max_quantity_item(grocery_list:list)->str:
  return max(grocery_list, key=lambda x: x['quantity'])['name']

def sort_by_total_amount(grocery_list:list)->list:
  sorted_items = sorted(
      grocery_list,
      key = lambda x: (-item_amount(x), x['name'])
  )
  return sorted_items


def process_grocery_list(grocery_list:list, request:str):
    """Process the grocery list as per the request.

    Args:
        grocery_list (list[dict]) - A list of dictionary with the keys
            "name", "quantity" and "price", where "price" is the amount of 
            one unit of the item.
        request: (str) - A string containing one of the following request.
            - 'total_bill_amount'
            - 'max_quantity_item'
            - 'sort_by_total_amount'

    Returns: 
        The output corresponding to the request.
    """
    
    
    if request == 'total_bill_amount':
       return total_bill_amount(grocery_list)
    elif request == 'max_quantity_item':
       return max_quantity_item(grocery_list)
    elif request == 'sort_by_total_amount':
       return sort_by_total_amount(grocery_list)
    else:
       return None

# #Another method



# def process_grocery_list(grocery_list:list, request:str):
#     max=0
#     sum=0
#     quantity='quantity'
#     price='price'
#     name='name'
    
#     if request=='total_bill_amount':
#         for i in grocery_list:
#             total=i[quantity]*i[price]
#             sum=sum+total
#         return sum
    
#     if request=='max_quantity_item':
#         for i in grocery_list:
#             if max<i[quantity]:
#                 max=i[quantity]
#                 winner=i[name]
#         return winner
        
#     if request=='sort_by_total_amount':
#         # d={}
#         # for i in grocery_list:
#         #     i['total']=i[quantity]*i[price]:
#         for i in range(len(grocery_list)):
#             for j in range(i+1,len(grocery_list)):
#                 if grocery_list[i][quantity]*grocery_list[i][price]<grocery_list[j][quantity]*grocery_list[j][price]:
#                     grocery_list[i],grocery_list[j]=grocery_list[j],grocery_list[i]
#                 if grocery_list[i][quantity]*grocery_list[i][price]==grocery_list[j][quantity]*grocery_list[j][price]:
#                     if grocery_list[i][name]>grocery_list[j][name]:
#                         grocery_list[i],grocery_list[j]=grocery_list[j],grocery_list[i]
                        
#         return grocery_list


# Shopping List
# Given a list of dictionaries with keys: name, quantity, and price for each item in a grocery list, write a function that does the following based on the request:

# total_bill_amount: Find the total bill amount by summing the price multiplied by the quantity for each item.
# max_quantity_item: Find the name of the item with the maximum quantity. If there are multiple items with the same quantity, return the first one.
# sort_by_total_amount: Sort the list by the highest total amount for an item (calculated as price * quantity). If two items have the same total amount, break the tie by sorting by name in ascending order.

# Example

# grocery_list = [
#     {'name': 'apple', 'quantity': 2, 'price': 3},
#     {'name': 'banana', 'quantity': 5, 'price': 2},
#     {'name': 'carrot', 'quantity': 4, 'price': 1}
# ]
# total_bill_amount -> 6+10+4 = 20
# max_quantity_item -> 'banana'
# sort_by_total_amount -> sorted list of dict in the order 'banana' , 'apple' and 'carrot'
    
