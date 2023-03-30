from model import Customer

def customerservice_getAll():
    return Customer.query.all()

def customerservice_searchOnCity(city):
    res = [] 
    for cust in customerservice_getAll():
        if city in cust.City:
            res.append(cust)
    return res
