import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import segno
from segno import helpers
import io

def generate_qrcode():
    qrcode_type = qrcode_type_var.get()
    if qrcode_type == "URL":
        url = url_entry.get()
        qr = segno.make_qr(url)
    elif qrcode_type == "Email":
        to = email_to_entry.get()
        cc = email_cc_entry.get()
        bcc = email_bcc_entry.get()
        subject = email_subject_entry.get()
        body = email_body_entry.get()
        qr = helpers.make_email(to, cc, bcc, subject, body)
    elif qrcode_type == "GEO":
        latitude = geo_latitude_entry.get()
        longitude = geo_longitude_entry.get()
        qr = helpers.make_geo(latitude, longitude)
    elif qrcode_type == "Mecard":
        name = mecard_name_entry.get()
        phone = mecard_phone_entry.get()
        email = mecard_email_entry.get()
        qr = helpers.make_mecard(name=name, phone=phone, email=email)
    elif qrcode_type == "Wifi":
        ssid = wifi_ssid_entry.get()
        password = wifi_password_entry.get()
        security = wifi_security_var.get()
        qr = helpers.make_wifi(ssid=ssid, password=password, security=security)
    else:
        messagebox.showerror("Error", "Please select a QR code type")
        return

    out = io.BytesIO()
    qr.save(out, scale=10, kind='png')
    out.seek(0)
    qr_img = Image.open(out)
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    def save_qr():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr.save(file_path, scale=10)
            messagebox.showinfo("Saved", "QR Code saved successfully")

    download_button.config(command=save_qr)

def update_ui():
    for widget in input_frame.winfo_children():
        widget.grid_forget()
    
    qrcode_type = qrcode_type_var.get()
    if qrcode_type == "URL":
        url_label.grid(row=0, column=0, padx=5, pady=5)
        url_entry.grid(row=0, column=1, padx=5, pady=5)
    elif qrcode_type == "Email":
        email_to_label.grid(row=0, column=0, padx=5, pady=5)
        email_to_entry.grid(row=0, column=1, padx=5, pady=5)
        email_cc_label.grid(row=1, column=0, padx=5, pady=5)
        email_cc_entry.grid(row=1, column=1, padx=5, pady=5)
        email_bcc_label.grid(row=2, column=0, padx=5, pady=5)
        email_bcc_entry.grid(row=2, column=1, padx=5, pady=5)
        email_subject_label.grid(row=3, column=0, padx=5, pady=5)
        email_subject_entry.grid(row=3, column=1, padx=5, pady=5)
        email_body_label.grid(row=4, column=0, padx=5, pady=5)
        email_body_entry.grid(row=4, column=1, padx=5, pady=5)
    elif qrcode_type == "GEO":
        geo_latitude_label.grid(row=0, column=0, padx=5, pady=5)
        geo_latitude_entry.grid(row=0, column=1, padx=5, pady=5)
        geo_longitude_label.grid(row=1, column=0, padx=5, pady=5)
        geo_longitude_entry.grid(row=1, column=1, padx=5, pady=5)
    elif qrcode_type == "Mecard":
        mecard_name_label.grid(row=0, column=0, padx=5, pady=5)
        mecard_name_entry.grid(row=0, column=1, padx=5, pady=5)
        mecard_phone_label.grid(row=1, column=0, padx=5, pady=5)
        mecard_phone_entry.grid(row=1, column=1, padx=5, pady=5)
        mecard_email_label.grid(row=2, column=0, padx=5, pady=5)
        mecard_email_entry.grid(row=2, column=1, padx=5, pady=5)
    elif qrcode_type == "Wifi":
        wifi_ssid_label.grid(row=0, column=0, padx=5, pady=5)
        wifi_ssid_entry.grid(row=0, column=1, padx=5, pady=5)
        wifi_password_label.grid(row=1, column=0, padx=5, pady=5)
        wifi_password_entry.grid(row=1, column=1, padx=5, pady=5)
        wifi_security_label.grid(row=2, column=0, padx=5, pady=5)
        wifi_security_var.grid(row=2, column=1, padx=5, pady=5)

app = tk.Tk()
app.title("QR Code Maker")
app.geometry("400x600")

qrcode_type_var = tk.StringVar()

types_frame = tk.Frame(app)
types_frame.pack(pady=10)

tk.Radiobutton(types_frame, text="URL", variable=qrcode_type_var, value="URL", command=update_ui).pack(anchor='w')
tk.Radiobutton(types_frame, text="Email", variable=qrcode_type_var, value="Email", command=update_ui).pack(anchor='w')
tk.Radiobutton(types_frame, text="GEO", variable=qrcode_type_var, value="GEO", command=update_ui).pack(anchor='w')
tk.Radiobutton(types_frame, text="Mecard", variable=qrcode_type_var, value="Mecard", command=update_ui).pack(anchor='w')
tk.Radiobutton(types_frame, text="Wifi", variable=qrcode_type_var, value="Wifi", command=update_ui).pack(anchor='w')

input_frame = tk.Frame(app)
input_frame.pack(pady=10)

url_label = tk.Label(input_frame, text="URL:")
url_entry = tk.Entry(input_frame)

email_to_label = tk.Label(input_frame, text="To:")
email_to_entry = tk.Entry(input_frame)
email_cc_label = tk.Label(input_frame, text="CC:")
email_cc_entry = tk.Entry(input_frame)
email_bcc_label = tk.Label(input_frame, text="BCC:")
email_bcc_entry = tk.Entry(input_frame)
email_subject_label = tk.Label(input_frame, text="Subject:")
email_subject_entry = tk.Entry(input_frame)
email_body_label = tk.Label(input_frame, text="Body:")
email_body_entry = tk.Entry(input_frame)

geo_latitude_label = tk.Label(input_frame, text="Latitude:")
geo_latitude_entry = tk.Entry(input_frame)
geo_longitude_label = tk.Label(input_frame, text="Longitude:")
geo_longitude_entry = tk.Entry(input_frame)

mecard_name_label = tk.Label(input_frame, text="Name:")
mecard_name_entry = tk.Entry(input_frame)
mecard_phone_label = tk.Label(input_frame, text="Phone:")
mecard_phone_entry = tk.Entry(input_frame)
mecard_email_label = tk.Label(input_frame, text="Email:")
mecard_email_entry = tk.Entry(input_frame)

wifi_ssid_label = tk.Label(input_frame, text="SSID:")
wifi_ssid_entry = tk.Entry(input_frame)
wifi_password_label = tk.Label(input_frame, text="Password:")
wifi_password_entry = tk.Entry(input_frame)
wifi_security_label = tk.Label(input_frame, text="Security:")
wifi_security_var = ttk.Combobox(input_frame, values=["WPA", "WEP", "nopass"])
wifi_security_var.set("WPA")

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qrcode)
generate_button.pack(pady=10)

qr_label = tk.Label(app)
qr_label.pack(pady=10)

download_button = tk.Button(app, text="Download QR Code")
download_button.pack(pady=10)

app.mainloop()

