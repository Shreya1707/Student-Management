import MySQLdb
import csv
import random
import matplotlib.pyplot as pp
from os import remove, rename
from tkinter import *

def createdb():
    sq = 'create database studentManagement'
    try:
        cursor.execute(sq)
        print('Database called studentManagement has been created.')
    except:
        print('Database already exists in the system.')

def newadm():
    def save_info():
        fin = open('student.txt', 'r')
        c = 0
        for data in fin:
            c += 1
        if c >= 1:
            admno = c + 1001
        elif c == 0:
            admno = 1001
        fout = open('student.txt', 'a')
        funame = fullname.get()
        na = funame.upper()
        rl = rollnum.get()
        cls = classs.get()
        s = sec.get()
        section = s.upper()
        cl = str(cls) + '-' + section
        ge = gender.get()
        gen = ge.upper()
        ddob = birthdate.get()
        mdob = birthmonth.get()
        ydob = birthyear.get()
        dob = str(ddob) + '/' + str(mdob) + '/' + str(ydob)
        fn = father.get()
        fname = fn.upper()
        mn = mother.get()
        mname = mn.upper()
        pno = phone.get()
        subc = subjcode.get()
        scode = subc.upper()
        arr = str(admno) + ',' + na + ',' + str(rl) + ',' + str(cl) + ',' + gen + ',' + dob + ',' + fname + ',' + mname + ',' + str(pno) + ',' + scode + '\n'
        fout.write(arr)
        fin.close()
        fout.close()
    project = Tk()
    frame = Frame(project)
    frame.pack()
    bottomframe = Frame(project)
    bottomframe.pack(side=BOTTOM)
    button1 = Button(frame, text="SHREYA", fg="red")
    button1.pack(side=LEFT)
    button2 = Button(frame, text="ANOUSHKA", fg="green")
    button2.pack(side=LEFT)
    button3= Button(frame, text="GARVIT", fg="blue")
    button3.pack(side=LEFT)
    button4 = Button(frame, text="MADHUMITHA", fg="orange")
    button4.pack(side=LEFT)
    project.title(string='')
    project.geometry("2500x2500")
    frame = LabelFrame(project,text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STUDENT MANAGEMENT SYSTEM WITH PERFORMANCE ANALYSIS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',bg='#66ffcc', font=(5))
    frame.pack(expand=True, fill=BOTH)
    fullname_text = Label(text="Full Name :")
    fullname_text.config(font=("Courier", 15))
    rollnum_text = Label(text="Roll Number :")
    rollnum_text.config(font=("Courier", 15))
    class_text = Label(text="Class [11/12] :")
    class_text.config(font=("Courier", 15))
    sec_text = Label(text="Section :")
    sec_text.config(font=("Courier", 15))
    gender_text = Label(text="Gender[F/M]:")
    gender_text.config(font=("Courier", 15))
    birthdate_text = Label(text="Birth Date [DD]:")
    birthdate_text.config(font=("Courier", 15))
    birthmonth_text = Label(text="Birth Month [MM] :")
    birthmonth_text.config(font=("Courier", 15))
    birthyear_text = Label(text="Birth Year [YYYY]:")
    birthyear_text.config(font=("Courier", 15))
    father_text = Label(text="Father's Name :")
    father_text.config(font=("Courier", 15))
    mother_text = Label(text="Mother's Name :")
    mother_text.config(font=("Courier", 15))
    phone_text = Label(text="Phone Number :")
    phone_text.config(font=("Courier", 15))
    subjcode_text = Label(text="Stream code[SE/SC/SB/CI/CM/HU] :")
    subjcode_text.config(font=("Courier", 15))

    fullname_text.place(x=15, y=70)
    rollnum_text.place(x=15, y=140)
    class_text.place(x=15, y=210)
    sec_text.place(x=400, y=210)
    gender_text.place(x=780, y=210)
    birthdate_text.place(x=15, y=280)
    birthmonth_text.place(x=400, y=280)
    birthyear_text.place(x=780, y=280)
    father_text.place(x=15, y=350)
    mother_text.place(x=400, y=350)
    phone_text.place(x=15, y=420)
    subjcode_text.place(x=400, y=420)

    fullname = StringVar()
    rollnum = IntVar()
    classs = IntVar()
    sec = StringVar()
    gender = StringVar()
    birthdate = IntVar()
    birthmonth = IntVar()
    birthyear = IntVar()
    father = StringVar()
    mother = StringVar()
    phone = IntVar()
    subjcode = StringVar()

    fullname_t = Entry(textvariable=fullname,width="120")
    fullname_t.config(font=("Courier", 15))
    rollnum_t = Entry(textvariable=rollnum, width="120")
    rollnum_t.config(font=("Courier", 15))
    class_t = Entry(textvariable=classs, width="40")
    class_t.config(font=("Courier", 15))
    sec_t = Entry(textvariable=sec, width="40")
    sec_t.config(font=("Courier", 15))
    gender_t = Entry(textvariable=gender, width="40")
    gender_t.config(font=("Courier", 15))
    birthdate_t = Entry(textvariable=birthdate, width='40')
    birthdate_t.config(font=("Courier", 15))
    birthmonth_t = Entry(textvariable=birthmonth, width="40")
    birthmonth_t.config(font=("Courier", 15))
    birthyear_t = Entry(textvariable=birthyear, width="40")
    birthyear_t.config(font=("Courier", 15))
    father_t = Entry(textvariable=father, width="60")
    father_t.config(font=("Courier", 15))
    mother_t = Entry(textvariable=mother, width="60")
    mother_t.config(font=("Courier", 15))
    phone_t = Entry(textvariable=phone, width="60")
    phone_t.config(font=("Courier", 15))
    sub_t = Entry(textvariable=subjcode, width="60")
    sub_t.config(font=("Courier", 15))

    fullname_t.place(x=15, y=100,height=30)
    rollnum_t.place(x=15, y=170,height=30)
    class_t.place(x=15, y=240,height=30)
    sec_t.place(x=400, y=240,height=30)
    gender_t.place(x=780, y=240,height=30)
    birthdate_t.place(x=15, y=310,height=30)
    birthmonth_t.place(x=400, y=310,height=30)
    birthyear_t.place(x=780, y=310,height=30)
    father_t.place(x=15, y=380,height=30)
    mother_t.place(x=400, y=380,height=30)
    phone_t.place(x=15, y=450,height=30)
    sub_t.place(x=400, y=450,height=30)
    button = Button(project, text="Submit Data", command=save_info, width="40", height="3", bg="yellow")
    button.place(x=600, y=600)
    project.mainloop()


def modif():
    fin = open('student.txt')
    ad = int(input('Adm No.=?'))
    record = fin.readlines()
    found = 0
    for x in range(len(record)):
        line = record[x].strip()
        arr = line.split(',')
        if ad == int(arr[0]):
            print()
            print("~~~~~~~~These are the options you can modify~~~~~~~")
            print()
            print('1.NAME')
            print('2.ROLL NUMBER')
            print('3.CLASS or SECTION')
            print('4.DATE OF BIRTH')
            print('5.NAME OF FATHER')
            print('6.NAME OF MOTHER')
            print('7.PHONE NUMBER')
            print('8.SUBJECT CODE')
            print('9.EXIT')
            print()
            choice = input('What you want to modify[1-9]=?')
            if choice in '123456789':
                if choice == '1':
                    arr[1] = input('New Name=?')
                elif choice == '2':
                    arr[2] = str(int(input('New roll no=?')))
                elif choice == '3':
                    cla = int(input('Please enter your class[11/12]=?'))
                    while not (cla > 10 and cla <= 12):
                        print('ERROR!This is a wrong input.Please input a valid class[11/12].')
                        cla = int(input('Please enter your class=?'))
                    sec = input('Please enter your section[A-Z/a-z]=?')
                    while not (sec >= 'A' and sec <= 'Z' or sec >= 'a' and sec <= 'z'):
                        print('ERROR!This is a wrong input.Please input a valid section[A-Z/a-z].')
                        sec = input('Please enter your section[A-Z]=?')
                    s = sec.upper()
                    cl = str(cla) + '-' + s
                    arr[3] = cl
                elif choice == '4':
                    ddob = int(input('Please enter your birth date[1-31]=?'))
                    mdob = int(input('Please enter your birth month[1-12]=?'))
                    ydob = int(input('Please enter year of date of birth=?'))
                    mdays = 0
                    if mdob == 1 or mdob == 3 or mdob == 5 or mdob == 7 or mdob == 8 or mdob == 10 or mdob == 12:
                        mdays = 31
                    elif mdob == 4 or mdob == 6 or mdob == 9 or mdob == 11:
                        mdays = 30
                    elif mdob == 2:
                        if ydob % 4 == 0 and ydob % 100 != 0 or ydob % 400 == 0:
                            mdays = 29
                        else:
                            mdays = 28
                    year = 2021
                    age = year - ydob
                    if not (
                            age == 19 or age == 18 or age == 17 or age == 16 or age == 15 or age == 14 and ddob >= 1 and ddob <= mdays):
                        print('Date is invalid')
                        ddob = int(input('Please enter your birth date[1-31]=?'))
                        mdob = int(input('Please enter the no. of your birth month[1-12]=?'))
                        ydob = int(input('Please enter year of date of birth=?'))
                    dob = str(ddob) + '/' + str(mdob) + '/' + str(ydob)
                    arr[5] = str(dob)
                elif choice == '5':
                    arr[6] = input('New Name of Father=?')
                elif choice == '6':
                    arr[7] = input('New Name of Mother=?')
                elif choice == '7':
                    arr[8] = str(int(input('New Mobile No=?')))
                elif choice == '8':
                    arr[9] = input('New Stream[SB/SE/CI/SC/CM/HU]=?')
            found = 1
            record[x] = ','.join(arr) + '\n'

    if found == 1:
        fout = open('student.txt', 'w')
        fout.writelines(record)
        fout.close()
    else:
        print('Admission number was not found!')

def delete():
    fin = open('student.txt', 'r')
    fout = open('temp.txt', 'w')
    ad = int(input('Enter the Admission no.=?'))
    found = 0
    for data in fin:
        line = data.strip()
        arr = line.split(',')
        if ad == int(arr[0]):
            found = 1
        else:
            fout.write(data)
    if found == 1:
        print('You have successfully deleted the details. Thank you!')
    else:
        print('Admission no. was not found!')
    fout.close()
    fin.close()
    remove('student.txt')
    rename('temp.txt', 'student.txt')

def displ():
    fin = open('student.txt', 'r')
    ad = int(input('Adm No.=?'))
    found = 0
    for data in fin:
        line = data.strip()
        arr = line.split(',')
        if int(arr[0]) == ad:
            print()
            print("THE DETAILS ARE AS FOLLOWS:")
            print()
            print('ADMISSION NUMBER: ',arr[0],end="\n")
            print('NAME: ', arr[1], end="\n")
            print('ROLL NUMBER: ', arr[2], end="\n")
            print('CLASS AND SEC: ', arr[3], end="\n")
            print('GENDER: ', arr[4], end="\n")
            print('BIRTHDAY: ', arr[5], end="\n")
            print("FATHER'S NAME: ", arr[6], end="\n")
            print("MOTHER'S NAME: ", arr[7], end="\n")
            print('PHONE NUMBER: ', arr[8], end="\n")
            print('STREAM CODE: ', arr[9], end="\n")
            print()
            found = 1
    if found == 0:
        print('Admission no. was not found!')
    fin.close()
def pag():
    fin = open('result.txt', 'r')
    flag = 0
    record = fin.readlines()
    ad = int(input('Please enter Admission No.='))
    for x in range(len(record)):
        line = record[x].strip()
        arr = line.split(',')
        if ad == int(arr[0]):
            flag=1
            name = arr[1]
            marks1 = float(arr[4])
            marks2 = float(arr[6])
            marks3 = float(arr[8])
            marks4 = float(arr[10])
            marks5 = float(arr[12])
            pp.bar(['sub1','sub2','sub3','sub4','sub5'],[marks1,marks2,marks3,marks4,marks5])
            pp.title(name)
            pp.xlabel("Subjects")
            pp.ylabel("Marks")
            pp.show()
    if flag==0:
        print("Admission form is not found...")

def graph():
    fin = open('student.txt', 'r')
    chu=cse=csb=csc=cci=ccm=0
    record = fin.readlines()
    for x in range(len(record)):
        line = record[x].strip()
        row = line.split(',')
        if row[9]=='SE':
            cse+=1
        elif row[9]=='SB':
            csb+=1
        elif row[9]=='SC':
            csc+=1
        elif row[9]=='HU':
            chu+=1
        elif row[9]=='CI':
            cci+=1
        elif row[9]=='CM':
            ccm+=1
    grpofclass=[cse,csb,csc,chu,cci,ccm]
    classes=['SE','SB','SC','HU','CI','CM']
    pp.pie(grpofclass,labels=classes,autopct='%1.0f%%')
    pp.grid(True)
    pp.title('PIE CHART:NUMBER OF STUDENTS ENROLLED IN A STREAM.',fontsize=15)
    pp.show()

def marks_grade_calculation():
    fin = open('student.txt', 'r')
    found = 0
    record = fin.readlines()
    ad = int(input('\nPlease enter Admission No. to enter the marks for='))
    for x in range(len(record)):
        line = record[x].strip()
        arr = line.split(',')
        if ad == int(arr[0]):
            found = 1
            print()
            print(*arr,sep=" ")
            print()
            if arr[9] == 'SB':
                m1 = float(input('MARKS OF ENGLISH=?'))
                m2 = float(input('MARKS OF MATHS=?'))
                m3 = float(input('MARKS OF PHYSICS=?'))
                m4 = float(input('MARKS OF CHEMISTRY=?'))
                m5 = float(input('MARKS OF BIOLOGY=?'))

            elif arr[9] == 'SE':
                m1 = float(input('MARKS OF ENGLISH=?'))
                m2 = float(input('MARKS OF MATHS=?'))
                m3 = float(input('MARKS OF PHYSICS=?'))
                m4 = float(input('MARKS OF CHEMISTRY=?'))
                m5 = float(input('MARKS OF ECONOMICS=?'))

            elif arr[9] == 'CI':
                m1 = float(input('MARKS OF ENGLISH=?'))
                m2 = float(input('MARKS OF ECONOMICS=?'))
                m3 = float(input('MARKS OF ACCOUNTANCY=?'))
                m4 = float(input('MARKS OF BUISNESS STUDIES=?'))
                m5 = float(input('MARKS OF INFORMATICS PRATICES=?'))

            elif arr[9] == 'SC':
                m1 = float(input('MARKS OF ENGLISH=?'))
                m2 = float(input('MARKS OF MATHS=?'))
                m3 = float(input('MARKS OF PHYSICS=?'))
                m4 = float(input('MARKS OF CHEMISTRY=?'))
                m5 = float(input('MARKS OF COMPUTER SCIENCE=?'))

            elif arr[9] == 'CM':
                m1 = float(input('MARKS OF ENGLISH=?'))
                m2 = float(input('MARKS OF MATHS=?'))
                m3 = float(input('MARKS OF ECONOMICS=?'))
                m4 = float(input('MARKS OF ACCOUNTANCY=?'))
                m5 = float(input('MARKS OF BUSINESS STUDIES=?'))

            elif arr[9] == 'HU':
                m1 = float(input('MARKS OF ENGLISH=?'))
                m2 = float(input('MARKS OF HISTORY=?'))
                m3 = float(input('MARKS OF GEOGRAPHY=?'))
                m4 = float(input('MARKS OF ECONOMICS=?'))
                m5 = float(input('MARKS OF POLITICAL STUDICAL STUDIES=?'))
            tot = m1 + m2 + m3 + m4 + m5
            avg = tot / 5
            subject='sub1'
            if subject == 'sub1':
                if m1 >= 90:
                    gr1 = 'A'
                    status1 = 'PASS'
                elif m1 >= 80 and m1 < 90:
                    gr1 = 'B'
                    status1 = 'PASS'
                elif m1 >= 70 and m1 < 80:
                    gr1 = 'C'
                    status1 = 'PASS'
                elif m1 >= 60 and m1 < 70:
                    gr1 = 'D'
                    status1 = 'PASS'
                elif m1 >= 50 and m1 < 60:
                    gr1 = 'E'
                    status1 = 'PASS'
                else:
                    gr1 = 'F'
                    status1 = 'FAIL'
                    print('You have failed in 1st subject!')
            subject = 'sub2'
            if subject == 'sub2':
                if m2 >= 90:
                    gr2 = 'A'
                    status2 = 'PASS'
                elif m2 >= 80 and m2 < 90:
                    gr2 = 'B'
                    status2 = 'PASS'
                elif m2 >= 70 and m2 < 80:
                    gr2 = 'C'
                    status2 = 'PASS'
                elif m2 >= 60 and m2 < 70:
                    gr2 = 'D'
                    status2 = 'PASS'
                elif m2 >= 50 and m2 < 60:
                    gr2 = 'E'
                    status2 = 'PASS'
                else:
                    gr2 = 'F'
                    status2 = 'FAIL'
                    print('You have failed in 2nd subject!')
            subject = 'sub3'
            if subject == 'sub3':
                if m3 >= 90:
                    gr3 = 'A'
                    status3 = 'PASS'
                elif m3 >= 80 and m3 < 90:
                    gr3 = 'B'
                    status3 = 'PASS'
                elif m3 >= 70 and m3 < 80:
                    gr3 = 'C'
                    status3 = 'PASS'
                elif m3 >= 60 and m3 < 70:
                    gr3 = 'D'
                    status3 = 'PASS'
                elif m3 >= 50 and m3 < 60:
                    gr3 = 'E'
                    status3 = 'PASS'
                else:
                    gr3 = 'F'
                    status3 = 'FAIL'
                    print('You have failed in 3rd subject!')
            subject = 'sub4'
            if subject == 'sub4':
                if m4 >= 90:
                    gr4 = 'A'
                    status4 = 'PASS'
                elif m4 >= 80 and m4 < 90:
                    gr4 = 'B'
                    status4 = 'PASS'
                elif m4 >= 70 and m4 < 80:
                    gr4 = 'C'
                    status4 = 'PASS'
                elif m4 >= 60 and m4 < 70:
                    gr4 = 'D'
                    status4 = 'PASS'
                elif m4 >= 50 and m4 < 60:
                    gr4 = 'E'
                    status4 = 'PASS'
                else:
                    gr4 = 'F'
                    status4 = 'FAIL'
                    print('You have failed in 4th subject!')
            subject = 'sub5'
            if subject=='sub5':
                if m5 >= 90:
                    gr5 = 'A'
                    status5 = 'PASS'
                elif m5 >= 80 and m5 < 90:
                    gr5 = 'B'
                    status5 = 'PASS'
                elif m5 >= 70 and m5 < 80:
                    gr5 = 'C'
                    status5 = 'PASS'
                elif m5 >= 60 and m5 < 70:
                    gr5 = 'D'
                    status5 = 'PASS'
                elif m5 >= 50 and m5 < 60:
                    gr5 = 'E'
                    status5 = 'PASS'
                else:
                    gr5 = 'F'
                    status5 = 'FAIL'
                    print('You have failed in 5th subject!')
            lis = str(arr[0]) + ',' + arr[1] + ',' + arr[9] + ',' + str(gr1) + ',' + str(m1) + ',' + str(gr2) + ',' + str(m2) + ',' + str(gr3) + ',' + str(m3) + ',' + str(gr4) + ',' + str(m4) + ',' + str(gr5) + ',' + str(m5) + ',' + str(tot) + ',' + str(avg) + ',' + str(status1) + ',' + str(status2) + ',' + str(status3) + ',' + str(status4) + ',' + str(status5) + ',' + arr[6] + ',' + arr[7] + ',' + arr[3] + '\n'
            print("\nMARKS HAVE BEEN SUCCESSFULLY ENTERED FOR THE STUDENT!")
            found = 1
    if found == 1:
        fout = open('result.txt', 'a')
        fout.write(lis)
        fout.close()
    else:
        print('Sorry...The Admission number was not found in the file.')


def display():
    fin = open('student.txt', 'r')
    found = 0
    record = fin.readlines()
    cursor.execute('use studentManagement')
    sq2 = 'create table stud(Admission numeric(6),Name char(25),Roll numeric(2),Class char(4),Father char(25),Mother char(25),Stream char(2))'
    try:
        cursor.execute(sq2)
    except:
        cursor.execute('drop table stud')
        cursor.execute(sq2)
    finally:
        for x in range(len(record)):
            line = record[x].strip()
            arr = line.split(',')
            adno = int(arr[0])
            name = arr[1]
            ro = int(arr[2])
            clas = arr[3]
            fname = arr[6]
            mname = arr[7]
            stream = arr[9]
            sq1 = 'insert into stud values({},"{}",{},"{}","{}","{}","{}")'.format(adno, name, ro, clas, fname, mname,stream)
            cursor.execute(sq1)
        cursor.execute('select * from stud ')
        data = cursor.fetchall()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("THE DETAILS OF ALL THE RECORDS ARE: ")
        print()
        for da in data:
            print(da[0],da[1],da[2],da[3],da[4],da[5],da[6],sep='\t\t\t')
            print()
        db.commit()


def swrl():
    fin = open('result.txt', 'r')
    found = 0
    record = fin.readlines()
    cursor.execute('use studentManagement')
    sq1 = 'create table result(Admission numeric(6),Name char(25),Stream char(2),GRADE_SUB1 char(1),MARKS_SUB1 float,GRADE_SUB2 char(1),MARKS_SUB2 float,GRADE_SUB3 char(1),MARKS_SUB3 float,GRADE_SUB4 char(1),MARKS_SUB4 float,GRADE_SUB5 char(1),MARKS_SUB5 float,TOTAL_MARKS float,AVG_MARKS float)'
    try:
        cursor.execute(sq1)
    except:
        cursor.execute('drop table result')
        cursor.execute(sq1)
    finally:
        for x in range(len(record)):
            line = record[x].strip()
            arr = line.split(',')
            adno = int(arr[0])
            name = arr[1]
            stream = arr[2]
            grade1 = arr[3]
            marks1 = float(arr[4])
            grade2 = arr[5]
            marks2 = float(arr[6])
            grade3 = arr[7]
            marks3 = float(arr[8])
            grade4 = arr[9]
            marks4 = float(arr[10])
            grade5 = arr[11]
            marks5 = float(arr[12])
            totalmark = float(arr[13])
            avgmark = float(arr[14])
            sq1 = 'insert into result values({},"{}","{}","{}",{},"{}",{},"{}",{},"{}",{},"{}",{},{},{})'.format(adno,name,stream,grade1,marks1,grade2,marks2,grade3,marks3,grade4,marks4,grade5,marks5,totalmark,avgmark)
            cursor.execute(sq1)
        cursor.execute('select * from result order by admission')
        data = cursor.fetchall()
        for da in data:
            for d in da:
                print(d, end='\t')
            print()
        db.commit()

def mos():
    admiss = int(input('Enter the admission number of student=?'))
    with open('student.txt', mode='r') as csvfile:
        record = csv.reader(csvfile,delimiter=',')
        for arr in record:
                if int(arr[0])==admiss:
                    global found
                    found=1
                    print(
                        '```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')

                    print(
                        '                                                            FIRST TERM REPORT CARD                                                                        ')
                    print(
                        '```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
                    print(
                        '                                            NAME OF SCHOOL : JAYSHREE PERIWAL INTERNATIONAL SCHOOL, JAIPUR                                                  ')
                    print()
                    print(
                        '                                                             ACADEMIC YEAR : 2021-2022                                                                     ')
                    print("FATHER'S NAME : ", arr[6],"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t","Attendance : ",random.uniform(50.00,99.99))
                    print("MOTHER'S NAME : ", arr[7])
                    print("STUDENT'S NAME :", arr[1])
                    print('ADMISSION NUMBER :', arr[0])
                    print('CLASS OF THE STUDENT :', arr[3])
                    print('ROLL NUMBER OF STUDENT :', int(arr[2]))
                    print('STREAM : ', arr[9])
                    print()
                    with open('result.txt', mode='r') as csvfile:
                        record = csv.reader(csvfile, delimiter=',')
                        while True:
                            for arr in record:
                                if len(arr):
                                    if int(arr[0]) == admiss:
                                        if (arr[2]=="SB"):
                                            print('SUBJECT\t\t\tMARKS OBTAINED\t\t\tGRADE')
                                            print('ENGLISH\t\t\t', arr[4],'\t\t\t', arr[3])
                                            print('MATHS\t\t\t',arr[6],'\t\t\t', arr[5])
                                            print('PHYSICS\t\t\t',arr[8],'\t\t\t', arr[7])
                                            print('CHEMISTRY\t\t\t',arr[10],'\t\t\t', arr[9])
                                            print('BIOLOGY\t\t\t',arr[12],'\t\t\t', arr[11])
                                        elif (arr[2]=="SE"):
                                            print('SUBJECT\t\t\tMARKS OBTAINED\t\t\tGRADE')
                                            print('ENGLISH \t\t\t',arr[4],'  \t\t\t', arr[3])
                                            print('MATHS   \t\t\t',arr[6],'  \t\t\t', arr[5])
                                            print('PHYSICS \t\t\t',arr[8],'  \t\t\t', arr[7])
                                            print('CHEMISTRY\t\t\t',arr[10],'\t\t\t\t',arr[9])
                                            print('ECONOMICS\t\t\t',arr[12],'\t\t\t\t', arr[11])
                                        elif (arr[2]=="CI"):
                                            print('SUBJECT\t\t\tMARKS OBTAINED\t\t\tGRADE')
                                            print('ENGLISH\t\t\t',arr[4],'\t\t\t', arr[3])
                                            print('ECONOMICS\t\t\t',arr[6],'\t\t\t', arr[5])
                                            print('ACCOUNTANCY\t\t\t',arr[8],'\t\t\t', arr[7])
                                            print('BUISNESS STUDIES\t\t\t',arr[10],'\t\t\t', arr[9])
                                            print('INFORMATICS PRACTICES\t   \t',arr[12],'\t\t\t', arr[11])
                                        elif (arr[2]=="SC"):
                                            print('SUBJECT\t\t\tMARKS OBTAINED\t\t\tGRADE')
                                            print('ENGLISH\t\t\t',arr[4],'\t\t\t', arr[3])
                                            print('MATHS\t\t\t',arr[6],'\t\t\t', arr[5])
                                            print('PHYSICS\t\t\t',arr[8],'\t\t\t', arr[7])
                                            print('CHEMISTRY\t\t\t',arr[10],'\t\t\t', arr[9])
                                            print('COMPUTER SCIENCE\t    \t', arr[12],'\t\t\t', arr[11])
                                        elif (arr[2]=="CM"):
                                            print('SUBJECT\t\t\tMARKS OBTAINED\t\t\tGRADE')
                                            print('ENGLISH\t\t\t',arr[4],'\t\t\t', arr[3])
                                            print('MATHS\t\t\t', arr[6],'\t\t\t', arr[5])
                                            print('ECONOMICS\t\t\t',arr[8],'\t\t\t', arr[7])
                                            print('ACCOUNTANCY\t\t\t',arr[10],'\t\t\t', arr[9])
                                            print('BUISNESS STUDIES   \t\t',arr[12],'\t\t\t', arr[11])
                                        elif (arr[2]=="HU"):
                                            print('SUBJECT\t\t\tMARKS OBTAINED\t\t\tGRADE')
                                            print('ENGLISH\t\t\t', arr[4],'\t\t\t', arr[3])
                                            print('HISTORY\t\t\t', arr[6],'\t\t\t', arr[5])
                                            print('GEOGRAPHY\t\t\t', arr[8],'\t\t\t', arr[7])
                                            print('ECONOMICS\t\t\t', arr[10],'\t\t\t', arr[9])
                                            print('POLITICAL SCIENCE    \t\t',arr[12],'\t\t\t', arr[11])
                                        print()
                                        print('TOTAL MARKS OBTAINED : ', float(arr[13]),'\tAVERAGE OF THE STUDENT : ', float(arr[14]))
                            return found

db = MySQLdb.connect('localhost', 'root', 'shreya')
cursor = db.cursor()
ch = 1
while ch:
    print()
    print("~~~~~~~~MAIN MENU~~~~~~~")
    print()
    print('0.CREATE A NEW DATABASE')
    print('1.NEW ADMISSION')
    print('2.MODIFICATION')
    print('3.DELETION')
    print('4.DISPLAY A PARTICULAR RECORD')
    print('5.DISPLAY THE ENTIRE TABLE')
    print('6.DISPLAY GRAPHICALLY')
    print('7.MARKS ENTRY AND GRADE DISPLAY ')
    print('8.REPORT CARD')
    print('9.EXIT FROM MENU')
    print()
    cho = input('Please input your choice[0-9]=?')
    if cho == '0':
        createdb()
    elif cho == '1':
        newadm()
    elif cho == '2':
        modif()
    elif cho == '3':
        delete()
    elif cho == '4':
        displ()
    elif cho == '5':
        display()
    elif cho == '6':
        graph()
    elif cho == '7':
        marks_grade_calculation()
    elif cho == '8':
        while True:
            print()
            print('~~~~~~~~PERFORMANCE GENERATION~~~~~~~')
            print()
            print('Please select from below options:')
            print('1.RESULT OF ALL THE STUDENTS')
            print('2.MARKSHEET OF A PARTICULAR STUDENT')
            print('3.PERFORMANCE ANALYSIS GRAPH')
            print('4.EXIT FROM MENU')
            print()
            choice = input('PLEASE ENTER A CHOICE[1-3]=?')
            if choice == '1':
                swrl()
            elif choice=='2':
                found = 0
                mos()
                if found==0:
                    print("The admission number was not found!")
                break
            elif choice=='3':
                pag()
            elif choice == '4':
                print('You have exited from menu')
                break
    elif cho == '9':
        print('You have exited from menu')
        break
