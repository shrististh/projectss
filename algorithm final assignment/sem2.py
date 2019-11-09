
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mc


try:
    connector = mc.connect(user='root', passwd='9813193803', host='localhost', database='my_db')
    db_cursor = connector.cursor()
    db_cursor.execute('create table if not exists my_table(id int(50) not null, name varchar(50) not null,'
                      'address varchar(50) not null, number int(10) not null, degree varchar(50) not null)')

except mc.DatabaseError as err:
    print(err)


root = Tk()
root.title("Student Management System")

root.geometry('700x640+300+50')
root.resizable(width=False, height=False)

root.configure(bg="dark blue")

class main_window:

    def __init__(self, root):
        self.root=root
        # ------------- Frames -------------

        self.top_frame = Frame(self.root, bg = "yellow")
        self.top_frame.place(x = 80, y =30, width=500, height=170)

        self.bottom_frame = Frame(self.root, bg = "white")
        self.bottom_frame.place(x = 80, y = 200, width=500, height=50)

        self.show_frame = Frame(self.root, height=100, relief=RIDGE, bd=4)
        self.show_frame.configure(bg="white")
        self.show_frame.place(x = 0, y = 390, width=700)

        self.lbl_student_info = Label(self.root, text = "STUDENT INFORMATION", font = 'TimesNewRoman 11 bold',
                                      fg='white', bg='dark blue')
        self.lbl_student_info.place(x=80, y=0)

        self.lbl_search_by = Label (self.root, text = "INFORMATION ENTRY", font = 'TimesNewRoman 11 bold',
                                    bg='dark blue', fg='white')
        self.lbl_search_by.place(x=80, y=255)

        self.lbl_search_by = Label(self.root, text="Search By", font='TimesNewRoman 11', bg='light blue')
        self.lbl_search_by.place(x=80, y=280)

        self.lbl_sort_by = Label(self.root, text='Sort By', font='TimesNewRoman 11', bg='light blue')
        self.lbl_sort_by.place(x=80,y=322)

        self.combo_search = ttk.Combobox(self.root, font='arial 12')
        self.combo_search['values'] = ('Id', 'Name', 'Address', 'Number', 'Degree')
        self.combo_search.current(0)
        self.combo_search.place(x=160, y=280, width=100)

        self.combo_sort = ttk.Combobox(self.root, font='arial 12')
        self.combo_sort['values'] = ('Id', 'Name', 'Address', 'Number', 'Degree')
        self.combo_sort.current(0)
        self.combo_sort.place(x=160, y=322, width=100)

        # Adding widgets in the form
        self.lbl_search = Label(self.root, text="Search", font='TimesNewRoman 11', bg='light blue')
        self.lbl_id = Label(self.top_frame, text="ID", font='TimesNewRoman 11', bg='yellow')
        self.lbl_name = Label(self.top_frame, text="Name", font='TimesNewRoman 11', bg='yellow')
        self.lbl_address = Label(self.top_frame, text="Address", font='TimesNewRoman 11', bg='yellow')
        self.lbl_number = Label(self.top_frame, text="Number", font='TimesNewRoman 11', bg='yellow')
        self.lbl_degree = Label(self.top_frame, text="Degree", font='TimesNewRoman 11', bg='yellow')

        self.lbl_search.place(x=280, y=280)

        self.entry_search = Entry(self.root, width=22, font='arial 11')
        self.entry_search.place(x=360, y=280)
        self.btn_search = Button(self.root, width=10, height=1, text='Search',
                                 font='TimesNewRoman 11', command=self.search_all)
        self.btn_search.place(x=560, y=280)

        self.lbl_id.place(x=10, y=10)
        self.lbl_name.place(x=10, y=40)
        self.lbl_address.place(x=10, y=70)
        self.lbl_number.place(x=10, y=100)
        self.lbl_degree.place(x=10, y=130)

        # ---------------- Entry of the form ----------------

        self.entry_id = Entry(self.top_frame, width=28, font='arial 11')
        self.entry_name = Entry(self.top_frame, width=28, font='arial 11')
        self.entry_address = Entry(self.top_frame, width=28, font='arial 11')
        self.entry_number = Entry(self.top_frame, width=28, font='arial 11')
        # self.entry_degree = Entry(self.top_frame, width=28, font='arial 11')

        self.entry_search.bind('<Return>', lambda e: self.search_all())

        self.entry_id.place(x=150, y=10)
        self.entry_name.place(x=150, y=40)
        self.entry_address.place(x=150, y=70)
        self.entry_number.place(x=150, y=100)
        # self.entry_degree.place(x=150, y=130)

        self.combo_degree = ttk.Combobox(self.root, font='TimesNewRoman 11', width=25)
        self.combo_degree['values'] = ('Bsc. (Hons) Computing', 'Bsc. (Hons) Ethical Hacking')
        self.combo_degree.current(0)
        self.combo_degree.place(x=231, y=160)

        # ---------------- Button Add -------------------
        self.btn_add = Button(self.bottom_frame, width=8, text='Add', font='TimesNewRoman 11',
                              command=self.add_info)
        self.btn_show = Button(root, width=8, text='Show', font='TimesNewRoman 11', command=self.show)
        self.btn_delete = Button(self.bottom_frame, width=8, text='Delete', font='TimesNewRoman 11',
                                 command=self.delete)
        self.btn_update = Button(self.bottom_frame, width=8, text='Update', font='TimesNewRoman 11',
                                 command=self.update)
        self.btn_clear = Button(self.bottom_frame, width=8, text='Clear', font='TimesNewRoman 11',
                                command=self.clear)
        self.btn_sort = Button(root, width=8, text='Sort', font='TimesNewRoman 11', command=self.sort_list)

        self.btn_add.grid(row = 0, column =1,padx=15,pady=15)
        self.btn_show.place(x=445, y=340)
        self.btn_sort.place(x=280, y=315)
        self.btn_delete.grid(row=0, column=3,padx=15,pady=15)
        self.btn_update.grid(row=0, column=4,padx=15,pady=15)
        self.btn_clear.grid(row=0, column=5,padx=15,pady=15)

        # ------------ Tree view ------------------
        self.scroll_x = Scrollbar(self.show_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.show_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(self.show_frame, column=('id', 'name', 'address', 'number', 'degree'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.student_table.pack(fill=BOTH)

        self.student_table.column('id', width=120)
        self.student_table.column('name', width=120)
        self.student_table.column('address', width=120)
        self.student_table.column('number', width=120)
        self.student_table.column('degree', width=120)
        self.student_table['show'] = 'headings'

        self.student_table.heading('id', text='ID')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('address', text='Address')
        self.student_table.heading('number', text='Number')
        self.student_table.heading('degree', text='Degree')

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.bind('<ButtonRelease-1>', lambda e: self.pointer())

        self.orderby = StringVar()
        self.ascending = Radiobutton(self.root, command=self.sort_list, text="Ascending", variable=self.orderby,
                                     value='Ascending', font='TimesNewRoman 11', bg='blue')
        self.ascending.place(x=100, y=350)

        self.descending = Radiobutton(self.root, command=self.sort_list, text="Descending", variable=self.orderby,
                                      value='Descending', font='TimesNewRoman 11', bg='blue')
        self.descending.place(x=200, y=350)

        self.ascending.invoke()

    def add_info(self):
        try:
            std_id = self.entry_id.get()
            name = self.entry_name.get()
            address = self.entry_address.get()
            number = self.entry_number.get()
            degree = self.combo_degree.get()

            if len(std_id) > 10:
                messagebox.showinfo('ID', "ID should be less than 10 digits.")
                return

            if len(name) > 40:
                messagebox.showinfo('Name', "Name should be less than 40 letters.")
                return

            if len(address) > 50:
                messagebox.showinfo('Address', "Address should be less than 50 letters.")
                return

            if len(number) > 13:
                messagebox.showinfo('Number', "Number should be less than 13 letters.")
                return

            if len(degree) > 60:
                messagebox.showinfo('Degree', "Degree should be less than 60 letters.")

            if not std_id.isdigit():
                messagebox.showinfo('ID', "Id should contain number only.")
                return
            else:
                std_id = int(std_id)

            if not number.isdigit():
                messagebox.showinfo("Number", 'Phone number should contain number only.')
                return

            query = 'insert into my_table(id, name, address, number, degree) values(%s, %s, %s, %s, %s)'
            values = (std_id, name, address, number, degree)
            db_cursor.execute(query, values)
            # mb.showinfo("Data inserted successfully.")
            connector.commit()
            self.clear()
            self.show()

        except ValueError as err:
            print(err)

        except mc.IntegrityError as err:
            print(err)

    def clear(self):
        self.entry_search.delete(0, END)
        self.entry_id.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_number.delete(0, END)
        self.combo_degree.delete(0, END)

    def show(self):
        self.student_table.delete(*self.student_table.get_children())

        query = 'select * from my_table'
        db_cursor.execute(query)
        results = db_cursor.fetchall()

        for row in results:
            self.student_table.insert('', 'end', values=row)

    def update(self):
        try:
            id = self.entry_id.get()
            name = self.entry_name.get()
            address = self.entry_address.get()
            number = self.entry_number.get()
            degree = self.combo_degree.get()

            if len(id) > 10:
                messagebox.showinfo('ID', "ID should be less than 10 digits.")
                return

            if len(name) > 40:
                messagebox.showinfo('Name', "Name should be less than 40 letters.")
                return

            if len(address) > 50:
                messagebox.showinfo('Address', "Address should be less than 50 letters.")
                return

            if len(number) > 13:
                messagebox.showinfo('Number', "Number should be less than 13 letters.")
                return

            if len(degree) > 60:
                messagebox.showinfo('Degree', "Degree should be less than 60 letters.")
                return

            if not id.isdigit():
                messagebox.showinfo('ID', "Id should contain number only.")
                return
            else:
                id = int(id)

            if not number.isdigit():
                messagebox.showinfo("Number", 'Phone number should contain number only.')
                return

            query = 'update my_table set name=%s, address=%s, number=%s, degree=%s where id=%s'
            values = (name, address, number, degree, id)
            db_cursor.execute(query, values)
            connector.commit()
            self.clear()
            self.show()

        except ValueError as err:
            print(err)

    def delete(self):
        query = 'delete from my_table where id=%s'
        values = (self.pointer(),)
        db_cursor.execute(query, values)
        connector.commit()
        self.show()
        self.clear()

    def pointer(self):
        try:
            self.clear()
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            self.entry_id.insert(0, row[0])
            self.entry_name.insert(0, row[1])
            self.entry_address.insert(0, row[2])
            self.entry_number.insert(0, row[3])
            self.combo_degree.insert(0, row[4])

            return row[0]

        except IndexError:
            pass

    def search_all(self, mylist=None):
        if not mylist:
            query = 'select * from my_table'
            db_cursor.execute(query)
            results = db_cursor.fetchall()
        else:
            results = mylist

        self.student_table.delete(*self.student_table.get_children())

        search_by = self.combo_search.get()
        target = self.entry_search.get()

        if search_by == 'Id':
            column = 0
            if target.isdigit():
                target = int(target)
            else:
                messagebox.showinfo('Id', "Id must be number.")
                return
        elif search_by == 'Name':
            column = 1
        elif search_by == 'Address':
            column = 2
        elif search_by == 'Number':
            column = 3
        elif search_by == 'Degree':
            column = 4
        else:
            return

        found = []
        for value in results:
            if value[column] == target:
                found.append(value)

        self.student_table.delete(*self.student_table.get_children())

        for row in found:
            self.student_table.insert('', 'end', values=row)

        if not found:
            messagebox.showinfo('Not found', "Student not found.")

        return found

    def partition(self, arr, low, high):
        sort_by = self.combo_sort.get()

        if sort_by == 'Id':
            column = 0
        elif sort_by == 'Name':
            column = 1
        elif sort_by == 'Address':
            column = 2
        elif sort_by == 'Number':
            column = 3
        elif sort_by == 'Degree':
            column = 4
        else:
            return

        if self.orderby.get() == 'Ascending':
            i = (low - 1)  # index of smaller element
            pivot = arr[high][column]  # pivot

            for j in range(low, high):
                # If current element is smaller than or
                # equal to pivot
                if arr[j][column] <= pivot:
                    # increment index of smaller element
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)

        else:
            i = (low - 1)  # index of smaller element
            pivot = arr[high][column]  # pivot

            for j in range(low, high):
                # If current element is smaller than or
                # equal to pivot
                if arr[j][column] >= pivot:
                    # increment index of smaller element
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)

        # The main function that implements QuickSort

    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort
    def quickSort(self, arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def sort_list(self):
        query = 'select * from my_table'
        db_cursor.execute(query)

        results = db_cursor.fetchall()
        self.quickSort(results, 0, len(results) - 1)
        self.student_table.delete(*self.student_table.get_children())

        for row in results:
            self.student_table.insert('', 'end', values=row)


if __name__ == '__main__':
    a = main_window(root)
    root.mainloop()
