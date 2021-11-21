# convert tuple to dictionary


customer = (
    ('id','98698761'),
    ('name', 'marry'),
    ('surname', 'smith'),
    ('rented_books', 3 )
    )

cust_dict = dict(customer)

print(cust_dict)