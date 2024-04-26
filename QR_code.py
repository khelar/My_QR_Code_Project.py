import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=3)

features.add_data(input("Enter the data you want to convert into QR code: "))
features.make(fit=True)

image_generator = features.make_image(fill_color='black', back_color='white')
image_generator.save('image1.png')
print("QR code generated successfully")
print(features.data_list)
