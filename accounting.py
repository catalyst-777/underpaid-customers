melon_cost = 1.00


def customer_payment_discrepancy_report(file_name):
    """Determine if there are customer payment discrepancies"""

    # open file 
    payment_file = open(file_name)

    # iterate over each line in file
    for line in payment_file:
        # remove any white space at end of line and split into list
        line = line.rstrip()
        words = line.split('|')

        # get customer number, name, number of melons ordered, and payment amount
        cust_num = words[0]
        cust_name = words[1]
        num_melons = float(words[2])
        amount_paid = float(words[3])

        # calculate the expected payment
        expected = num_melons * melon_cost

        # if the expected payment amount is not equal to amount paid print a detailed report.
        if expected != amount_paid:
            print(f"{cust_name} with customer ID {cust_num} paid ${amount_paid:.2f},",
                f"expected ${expected:.2f}"
                )
            if expected > amount_paid:
                amount = expected - amount_paid
                print(f"Under by ${amount:.2f}")
            else:
                amount = amount_paid - expected
                print(f"Over by ${amount:.2f}")
    # close file
    payment_file.close()


customer_payment_discrepancy_report('customer-orders.txt')

