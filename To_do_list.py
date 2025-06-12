import tkinter
from tkinter import messagebox

# Tạo cửa sổ chính
root = tkinter.Tk()

# Thay đổi màu sắc nền 
root.configure(bg = "white")

# Đổi tiêu đề 
root.title("Danh sách công việc cần làm")

# Kích cỡ 
root.geometry("400x200")

# Tạo mảng task
tasks = []

# Hàm thêm công việc vào danh sách
def add_task(event=None):
    task = txt_input.get()
    if task:
        lbl_display.config(text=f"Task added: {task}")
        txt_input.delete(0, tkinter.END)
        tasks.append(task)
        update_listbox() 
    else:
        lbl_display.config(text="Please enter a task.")

# Hàm xoá một công việc được chọn
def del_one():
    lbl_display.config(text="Task deleted.")
    task = lb_task.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()

# Hàm xoá tất cả công việc được chọn
def del_all():
    lbl_display.config(text="All task deleted.")
    confirmed = messagebox.askyesno("Please confirm", "Do you want delete all task")
    if confirmed == True:
        global tasks
        tasks = []
        update_listbox()

# Hàm thêm công việc vào bảng 
def update_listbox():
    clear_listbox()

    for task in tasks :
        lb_task.insert("end",task)

# Hàm sắp xếp theo thứ tự
def sort_task():
    tasks.sort()
    update_listbox()

# Xóa tất cả các mục khỏi hộp danh sách 
def clear_listbox():
    lb_task.delete(0,"end")

# Giao diện tiêu đề
lbl_title = tkinter.Label(root,text="TO-DO-LIST",bg ="White")
lbl_title.grid(row= 0,column=0)

# Nhãn hiển thị thông báo
lbl_display = tkinter.Label(root, text = "", bg = "White")
lbl_display.grid(row = 0, column= 1)

# Ô nhập công việc
txt_input = tkinter.Entry(root, width= 50)
txt_input.grid(row= 1, column= 1)
txt_input.bind("<Return>", add_task)

# Nút thêm công việc
btn_add_task = tkinter.Button(root, text="Add task", fg = "black", bg = "White", command=add_task )
btn_add_task.grid(row = 1, column= 0)

# Nút xoá 1 công việc
btn_delete_task = tkinter.Button(root, text="Delete task", fg = "black", bg = "White", command=del_one )
btn_delete_task.grid(row= 2, column= 0)

# Nút xoá tất cả công việc
btn_delete_all_task = tkinter.Button(root, text="Delete all task", fg = "black", bg = "White", command=del_all )
btn_delete_all_task.grid(row=3, column= 0)

# Sắp xếp lại theo thứ tự
btn_sort = tkinter.Button(root, text="Sort task", fg = "black", bg = "White", command=sort_task )
btn_sort.grid(row=4, column= 0)

# Nút thoát chương trình
btn_exit = tkinter.Button(root, text="Exit", fg = "black", bg = "White", command=exit )
btn_exit.grid(row = 5, column= 0)

# Listbox để hiển thị danh sách công việc
lb_task = tkinter.Listbox(root, width= 50,height=7)
lb_task.grid(row=2,column=1,rowspan=4)

# Listbox để hiển thị danh sách công việc
root.mainloop()