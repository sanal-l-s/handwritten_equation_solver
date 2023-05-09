from sympy import symbols, Eq, solve

import time
from firebase import Firebase

config = {
  "apiKey": "AIzaSyCKd0dpGbvyjbp-FBNrJbVn4D--xQwDspQ",
  "authDomain": "iot-project-da6bb.firebaseapp.com",
  "databaseURL": "https://iot-project-da6bb-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "iot-project-da6bb",
  "storageBucket": "iot-project-da6bb.appspot.com",
  "messagingSenderId": "265478967667",
  "appId": "1:265478967667:web:e400b96bd8412ce965b506",
  "measurementId": "G-T1KSP0NMDT"
}


firebase = Firebase(config)
db = firebase.database()
storage = firebase.storage()


import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


#.....................................................................
print('waiting for the problem')

while True:
    uploadFlag = db.child("EquationSolver").child("uploadFlag").get().val()
    #print(f'uploadFlag: {uploadFlag}')


    if(uploadFlag=='1'):
        try:
            time.sleep(2)
            uploadFlag = db.child("EquationSolver").child("uploadFlag").set('0')
            #print(f'uploadFlag: {uploadFlag}')
            path_on_cloud = "EquationSolver/img.jpg"
            storage.child(path_on_cloud).download("1.jpg")

            #frame = cv2.imread('e4.png')
            frame = cv2.imread('1.jpg')

            #print("Shape: ", frame.shape)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            kernl = np.ones((1,1),np.uint8)
            img_dlt = cv2.dilate(img,kernl,iterations=1)
            img_dlt_erd = cv2.erode(img,kernl,iterations=1)
            target = pytesseract.image_to_string(img_dlt_erd)

            ##data=pytesseract.image_to_boxes(img_dlt_erd)
            ##data = data.split('\n')
            ##print(data)

            print(target)
            target = target.replace("\n", ",")
            target = target.replace(" ", "")
            #talk(target)

    ##        cv2.imshow("Original",frame)
    ##        cv2.imshow("Gray",img)
    ##        cv2.imshow("Dilated",img_dlt)
    ##
    ##        cv2.imshow("Dilated-Eroded",img_dlt_erd)
    ##        #cv2.waitKey(0)


            problem = target
            #problem = 'x+y=1,x-y=1'
            #problem = 'x+2y=5,x-y=6'
            #problem = 'x+2y=15,x-y=6'
            #problem='V=I*R,I=10,R=3'

            expressions = problem.split(',')
            print(expressions)

            input_variable_list=[]
            input_variable_value_list =[]
            variable=0
            output_variable=[]
            equaltion_list=[]
            for i in expressions:
                if '=' in i:
                    expression_element=i.split('=')
                    print(expression_element)

                    try:
                        value= float(expression_element[1])
                        input_variable_value_list.append(value)
                        variable= expression_element[0]
                        input_variable_list.append(variable)
                        
                        
                    except:
                        output_variable.append(expression_element[0])
                        equaltion_list.append(expression_element[1])


            print(f'input_variable_list : {input_variable_list}')
            print(f'input_variable_value_list : {input_variable_value_list}')
            print(f'output_variable : {output_variable}')
            print(f'equaltion_list : {equaltion_list}')

            symbols_list=[]
            if len(output_variable)==0:
                for exp in input_variable_list:
                    for i in exp:
                        if(i.isalpha()):
                            if(i not in symbols_list):
                                symbols_list.append(i)
                            
                print(f'symbols_list: {symbols_list}')

                Symbol_str=symbols_list[0]
                for i in symbols_list[1:]:
                    Symbol_str=Symbol_str+','+i

                print(f'Symbol_str: {Symbol_str}')    
                symbols1 = symbols('x,y')
                #symbols1 = Symbol_str
                print(symbols1)

                equation_list=[]
                
                for exp in input_variable_list:
                    exp_equation_list=[]
                    for i in exp:
                        if(i.isalpha()):
                            exp_equation_list.append(symbols1[symbols_list.index(i)])
                        else:
                            exp_equation_list.append(i)
                            
                    equation_list.append(exp_equation_list)
                      

                print(f'equation_list : {equation_list}')

                eqn_list=[]
                for i in equation_list:
                    eqn=0
                    if '+' in i:
                        try:
                            if(i[i.index('+')+1].isalpha()):
                                eqn = i[i.index('+')-1]+ i[i.index('+')+2]
                            else:
                                eqn = i[i.index('+')-1]+ float(i[i.index('+')+1]) * i[i.index('+')+2]
                        except:
                            eqn = i[i.index('+')-1]+ i[i.index('+')+2]
                            

                    if '-' in i:
                        eqn = i[i.index('-')-1]- i[i.index('-')+1 ]

                    eqn_list.append(eqn)

                print(f'eqn_list: {eqn_list}')

                x, y = symbols(Symbol_str)

                #eq1 = Eq((x+y), 1)
                eq1 = Eq(eqn_list[0], input_variable_value_list[0])

                eq2 = Eq(eqn_list[1], input_variable_value_list[1])
                ans = problem + "\n"+ str(solve((eq1, eq2), (x, y)))
                print(ans)

                result = {"result":ans}
                db.child("EquationSolver").child("result").set(result)
                db.child("EquationSolver").child("resultFlag").set('1')
                print('waiting for the problem')


            else:
                eqn = equaltion_list[0]
                for i in input_variable_list:
                    if i in eqn:
                        value = input_variable_value_list[input_variable_list.index(i)]
                        eqn = eqn.replace(i,str(value))
                        print(f'i = {i} , value: {value} , {eqn}')

                print(eqn)
                print(f'{output_variable} = {eval(eqn)}')
                ans= problem + "\n"+output_variable[0] +"="+ str(eval(eqn))
                print(ans)
                #result = {"result":"a=1"}
                result = {"result":ans}
                db.child("EquationSolver").child("result").set(result)
                db.child("EquationSolver").child("resultFlag").set('1')
                print('waiting for the problem')
                
        except:
            ans = 'sorry, i can not process the data, try again with new image'
            result = {"result":ans}
            db.child("EquationSolver").child("result").set(result)
            db.child("EquationSolver").child("resultFlag").set('1')
            print('waiting for the problem')
            
