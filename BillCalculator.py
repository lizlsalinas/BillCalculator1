
def Tip(bill_amount_parameter,tip_percentage_parameter):
	return bill_amount_parameter*tip_percentage_parameter*.01

def Total_Bill(bill_amount_parameter,tip_parameter):
	return bill_amount_parameter+tip_parameter

def Table_Split(Total_Bill_parameter, number_people_parameter):
	return Total_Bill_parameter/number_people_parameter

def main():
	choice=int(raw_input("Enter 1 to calculate tip, Enter 2 to split the bill"))
	if choice == 1 :
		bill_amount_input = float(raw_input("What is the bill amount?"))
		tip_percentage_input = float(raw_input("What is the tip percentage?"))
		calculated_tip_output = Tip (bill_amount_input, tip_percentage_input)
		calculated_total_bill_output = bill_amount_input + calculated_tip_output
		print "Tip = " + str(calculated_tip_output)
		print "Total Bill = " + str(calculated_total_bill_output)

		option = int(raw_input("Enter 2 if you would like to split the bill."))
		if option == 2:
			number_people_input = int(raw_input("How many people are there?"))
			print Table_Split(calculated_total_bill_output, number_people_input)

	elif choice == 2 :
		total_bill_amount_input = float(raw_input("What is the total bill amount?"))
		number_people_input = int(raw_input("How many people are there?"))
		print Table_Split(total_bill_amount_input, number_people_input)

if __name__ == '__main__': main()