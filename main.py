import qrcode

num_qr = int(input('How many QR codes? '))
clr1 = input('Enter fill colour: ')
clr2 = input('Enter back colour: ')

for i in range(num_qr):
    print(f'\n--- QR Code {i + 1} ---')
    data = input('Enter the text or url: ').strip()
    
    # Auto-generate filename
    filename = f'qrcode_{i + 1}.png'
    
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color=clr1, back_color=clr2)
    image.save(filename)
    print(f'QR code saved as {filename}')

print(f'\n✅ All {num_qr} QR codes generated!')