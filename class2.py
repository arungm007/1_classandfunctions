class class2():
    def subfields():
        print("Sub-feields in AI are:")
        print("Machine Learning")
        print("Neural networks")
        print("Vision")
        print("Robotics")
        print("Speech processing")
        print("Natual Language Processing")
    def Oddeven():
            num=int(input("Enter the num:"))
            if(num%2==1):
                result=print(num,"is odd number")
            if(num%2==0):
                result=print(num,"is even number")
            return result
    def Elegible():
        gender=input("your gender:")
        age=int(input("your age:"))
        if(gender=="male"and age>=21):
            result=print("elegible")
        elif(gender=="female"and age>=18):
            result=print("elegible")
        else:
            result=print("not elegible")
            return result
    def percentage():
        sub1=int(input("subject1:"))
        sub2=int(input("subject2:"))
        sub3=int(input("subject3:"))
        sub4=int(input("subject4:"))
        sub5=int(input("subject5:"))
        Total=sub1+sub2+sub3+sub4+sub5
        result1=print("Total:",Total)
        percentage=Total/5
        result2=print("percentage:",percentage)
        return result1
        return result2
    def triangle():
        height=int(input("height:"))
        breadth=int(input("breadth:"))
        area=(height*breadth)/2
        result1=print("area:",area)
        height1=int(input("height1:"))
        height2=int(input("height2:"))
        breadth=int(input("breadth"))
        perimeter=height1+height2+breadth
        result2=print("perimeter",perimeter)
        return result1
        return result2
