from tkinter import *
import smtplib


app=Tk()

app.geometry("500x500")
app.title("Login page")

f=("Times new roman",30,"bold")
address_field = Label(text="recipent address :")


address_field.place(x=15,y=70)


address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address,width=30)


address_entry.place(x=15,y=100)


def sendmessage():
        sender_email ='satyambhosale8298@gmail.com'
        sender_password ='bcabvdjdzsipzfhq'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        address_info = address.get()


        email_body_info = 'Your attendance has been marked'
        server.sendmail(sender_email, address_info, email_body_info)
        msg="Login successful"
        ans.configure(text=msg)
        address_entry.delete(0, END)







btn = Button(app,text="login",bg="red",command=sendmessage,width=30)
btn.place(x=15,y=220)
ans=Label(app,font=f)
ans.pack(pady=10)
mainloop()