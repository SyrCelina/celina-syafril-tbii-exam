# importing necessary libraries
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create GUI
root = tk.Tk()
#name GUI
root.title("Meme Capsule")
#GUI size
root.geometry("650x450")  # Set the window size


# Frame for the window - PAGE 1
f1 = tk.Frame(root, width=650, height=450)
f1.place(x=0, y=0)
#backround picture
img = Image.open('Images/welcome.jpg')
img = img.resize((650, 450), Image.LANCZOS)
pic = ImageTk.PhotoImage(img)
label = tk.Label(f1, image=pic)
label.image = pic
label.pack()

#user login
def handle_login():
 input_username = username_box.get()

# message for users after login
 if input_username in allowed_usernames:
  result_label.config(text=" Welcome inside :) " + input_username + "!", fg="green")
 else:
  result_label.config(text=" Please try again.", fg="red")

# Allowed usernames
allowed_usernames = {"celina", "sarah"}

# Box to store username
username_label = tk.Label(root, text='Please Enter Your Username:', font='arial 12 bold')
username_label.place(x=228, y=250)
username_box = tk.Entry(root, font='arial 14 bold')
username_box.place(x=228, y=275)


# Login Button
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.place(x=270, y=305)


# Result Label
result_label = tk.Label(root, text="", font='arial 12')
result_label.place(x=228, y=335)


# List of preloaded images
preloaded_images = [
  "Images/arthur.jpeg",
  "Images/pigeon.jpeg",
  "Images/crabs.jpeg",
  "Images/spongebob.jpeg",
  "Images/drake.jpeg",
  "Images/trollface.jpeg",
  "Images/stiffwhere.jpeg",
  "Images/saltbae.jpeg",
  "Images/lying.jpeg",
  "Images/sideeye.jpeg",
  "Images/crying.jpeg",
  "Images/evilkermit.jpeg"
]

# Store selected images
selected_images = []

# page to create the capsule
def createpage():
  create_button.destroy()
  f1.destroy()
  create_page()


  # Title
  Create = tk.Label(text="Create your Capsule:", font="roboto 26 bold", bg="Blue", fg="black")
  Create.place(x=80, y=40)


  # Button to save capsule
  save_capsule_button = tk.Button(root, text="Save Capsule", command=save_capsule)
  save_capsule_button.place(x=200, y=375)


  # Button to view capsule
  view_capsule_button = tk.Button(root, text="View Capsule", command=view_capsule)
  view_capsule_button.place(x=50, y=375)

  # Information box
  click_button = tk.Button(root, text="Click me for Information", command=show_info_message)
  click_button.place(x=375, y =45)

  #Button to lock capsule and leave
  exit_button = tk.Button(text="Lock your Capsule and Goodbye <3", command=root.destroy)
  exit_button.place(x=350, y=375)

# PAGE 2
def create_page():
  global f2
  global img_labels

# background for create page
  f2 = tk.Frame(root, width=650, height=450)
  f2.place(x=0, y=0)
  img_create = Image.open('Images/regbackround.jpg')
  img_create = img_create.resize((650, 450), Image.LANCZOS)
  pic_create = ImageTk.PhotoImage(img_create)
  label_create = tk.Label(f2, image=pic_create)
  label_create.image = pic_create
  label_create.place(x=0, y=0)


  img_labels = []

# aligning the preloaded pictures
  num_images_per_row = 4
  image_width = 100
  image_height = 70
  spacing = 20


  total_images = len(preloaded_images)
  num_rows = (total_images + num_images_per_row - 1) // num_images_per_row

#selecting pictures and binding click with selection
  for i, image_path in enumerate(preloaded_images):
      img = Image.open(image_path)
      img = img.resize((image_width, image_height), Image.LANCZOS)
      img = ImageTk.PhotoImage(img)


      row = i // num_images_per_row
      col = i % num_images_per_row
      x_pos = col * (image_width + spacing) + (650 - num_images_per_row * (image_width + spacing)) // 2
      y_pos = row * (image_height + spacing) + (450 - num_rows * (image_height + spacing)) // 2

      img_label = tk.Label(f2, image=img)
      img_label.image = img
      img_label.place(x=x_pos, y=y_pos)
      img_label.bind("<Button-1>", lambda event, idx=i: select_image(idx))
      img_labels.append(img_label)

#messagebox with information
def show_info_message():
    messagebox.showinfo("Information", "Hi! If you want to create a Meme Capsule this is how you do it: 1. Look at all the memes and think about which one you found to be the most amusing 2. Select the memes you want by clicking on them. Be warned once you put something in the capsule you wont be able to take it back! 3. Save your capsule by clicking on the save button. 4. View your capsule by clicking on the view button on the capsule page 5. Lock your Capsule and be notified about it again, in a few years once new memes have made their way on to the internet and our hearts. Again be warned you won't be able to look at the capsule for a very long time, so make sure to remember the moment and memes. Have fun! ")

#confirmation of selection in pycharm terminal
def select_image(idx):
  selected_images.append(preloaded_images[idx])
  print("Image selected:", preloaded_images[idx])

#message for successful capsule saving
def save_capsule():
   global saved_capsule
   saved_capsule = selected_images
   messagebox.showinfo("Successfull", "You successfully saved your Capsule!")

# Page to vie capsule after selection - PAGE 3
def view_capsule():
  # Confirmation message before viewing capsule
  confirmation = messagebox.askyesno("Confirmation", "You are timetraveling! Are you sure you want to view the capsule?")
  if confirmation:
      # New window for viewing the capsule page
      capsule_window = tk.Toplevel(root)
      capsule_window.title("Capsule Page")
      capsule_window.geometry("650x450")


      # Background for capsule viewing page
      img_view = Image.open('Images/regbackround.jpg')
      img_view = img_view.resize((650, 450), Image.LANCZOS)
      pic_view = ImageTk.PhotoImage(img_view)
      label_view = tk.Label(capsule_window, image=pic_view)
      label_view.image = pic_view
      label_view.place(x=0, y=0)


      # Display image selection in capsule page
  for i, img_path in enumerate(selected_images):
      img = Image.open(img_path)
      img = img.resize((100, 100), Image.LANCZOS)
      img = ImageTk.PhotoImage(img)

      img_label = tk.Label(capsule_window, image=img)
      img_label.image = img
      img_label.grid(row=i // 4, column=i % 4, padx=5, pady=5)


# Button to enter create page
create_button = tk.Button(root, text='Create new Meme Capsule', height=2, width=15, command=createpage)
create_button.place(x=230, y=370)

root.mainloop()






