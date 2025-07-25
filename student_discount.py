student_name = (input("enter student name: "))
student_grade = int(input("enter student grade level :"))
academic_toppers_status = (input("Academic Status: "))
base_tuition_fee = int(input("Base tuition fee: "))
discount_percentage = 0

if  student_grade >= 1 and student_grade<=12:
      print("student grades are valid")
else :
        print("student grades are invalid")
if  student_grade >= 1 and student_grade <=12:
       if academic_toppers_status == "yes" :
              discount_percentage = 20
       else:        
             discount_percentage = 10
elif  student_grade >= 6 and student_grade <=8 :
       discount_percentage = 5
else :
       discount_percentage = 0

if student_grade == 10:
    add_discount = 3
elif student_grade == 12:
       add_discount = 5
else:
       add_discount_percentage = 0
total_discount = discount_percentage + add_discount
discount_amount = base_tuition_fee * (total_discount / 100)
final_fee = base_tuition_fee - discount_amount
academic_toppers_status = "yes" if academic_toppers_status == "yes" else "no"
print(f"{total_discount}%")
print(f"{discount_amount}")
print(f"{final_fee}")


