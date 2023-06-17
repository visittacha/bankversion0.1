import customtkinter as ctk
import random
app=ctk.CTk()
app.title('เสร็จกูแน่')
app.geometry('900x900')

da=["มึงทำดีแล้ว","ไอชั่ว","หน้าเลว","ปัญญาอ่อน","อ้วน","มีบุญมาก","ไอขี้คุก",'นิสัยต่ำๆ','กลับดาวไป']

def button_event():
    user_input=entry.get()
    if user_input == str("แบงค์"):
        answer1=(user_input," ","ตามนั้นคือจบ")
    elif user_input == str("bank"):
        answer1=(user_input,' ',"Good")
    elif user_input == str("ข้าวปั้น"):
        answer1=(user_input,' ',"เก่งดี")
    elif user_input == str("kp"):
        answer1=(user_input,' ',"เก่งมาก")
    elif user_input == str("เตชินท์"):
        answer1=(user_input,' ',"สุภาพเรียบร้อย")
    else :
        answer1="ไอ",(user_input),random.choice(da)
    answer_text.set(answer1)
    print(answer1)


def we2_event():
    user_input=entry.get()
    if user_input == str("แบงค์"):
        answer2=(user_input," ","ตามนั้นคือจันทบุรี")
    elif user_input == str("bank"):
        answer2=(user_input,' ',"Good")
    elif user_input == str("ข้าวปั้น"):
        answer2=(user_input,' ',"เก่งดี")
    elif user_input == str("kp"):
        answer2=(user_input,' ',"เก่งมาก")
    elif user_input == str("เตชินท์"):
        answer2=(user_input,' ',"สุภาพเรียบร้อย")
    else :
        answer2="มึงไอ",(user_input),random.choice(da)
    answer_text.set(answer2)
    print(answer2)

label=ctk.CTkLabel(app, text='ใส่ชื่อของคุณ',fg_color="transparent",font=("Aria",30))
label.pack(pady=(20,0))


entry=ctk.CTkEntry(app,placeholder_text="ใส่เลข ของคุณตรงนี้",font=("Aria",20),width=250,justify="center")
entry.pack(pady=(15,0))

answer_text = ctk.StringVar()
answer_label=ctk.CTkLabel(app, textvariable=answer_text,font=("Aria",30))
answer_label.pack(pady=(50,0))

label=ctk.CTkLabel(app, text="เลือก1 - 2",font=("aria",20))
label.pack(pady=(5,0))



button1=ctk.CTkButton(app, text='1',fg_color="#000000",command=button_event , width=250)
button1.pack(pady=(50,0))

we2=ctk.CTkButton(app, text='2',fg_color="#000000",command=we2_event , width=250)
we2.pack(pady=(100,0))

app.mainloop()