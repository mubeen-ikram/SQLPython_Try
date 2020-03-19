import pymysql

password = '12345Qwerty'

# Connect to the database
connection = pymysql.connect(host='csmysql.cs.cf.ac.uk',
                             user='c1928902',
                             password=password,
                             db='MySQL',
                             charset='utf8mb4')

# Question 2.1
"""
Retrieve all purchases which happened in 2015. 
Provide the results in a 4-column table: order_date, client_name, total_bottles, and total_GBP_spent.
"""


def retrieve_purchases_2015():
    # your code here
    # return results
    mycursor = connection.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()


# Question 2.2
"""
Write a query to obtain the name of the salesperson in each region with the largest amount of total gbp sales.
"""


def most_successful_salesperson_per_year():
	pass

# your code here
# return results

if __name__ == '__main__':

    print('-- Question 1 --')
    res = retrieve_purchases_2015()
    for i in res:
        print(i)
    input('- Press Enter for Question 2 -')
    res = most_successful_salesperson_per_year()
    for i in res:
        print(i)
