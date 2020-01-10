
def underpaid(file):
    """open a file and parse it into a format"""

    doc = open(file)

    for line in doc:
      line = line.rstrip() # strip the line of whitespaces and new line breaks
      section = line.split('|')


      melon_cost = 1.00

      customer_count = section[0]
      customer_name = section[1]
      customer_melons = section[2]
      customer_paid = section[3]


      customer_expected = float(customer_melons) * float(melon_cost)
      if customer_expected != customer_paid:
        print("{} paid ${}, expected ${}".format(customer_name, customer_paid, customer_expected))
        #print(f"{customer_name} paid ${customer_paid:.2f},", f"expected ${customer_expected:.2f}")
    doc.close()

orders_file = "customer-orders.txt"

underpaid(orders_file)