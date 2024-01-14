import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

def send_command(command):
    ser.write(command.encode())

def send_ardunio(s):
    detected = "*D*" in s


    coord = None
    if detected:
        start_index = s.split("[")
        
        end = start_index[1].split("]")
        
        alo = list(end[0].split(", "))
        
        coord = [float(cord) for cord in alo]

        im_width = 640  
        im_height = 640

        x_pixel = int(coord[0] * im_width)
        y_pixel = int(coord[1] * im_height) # işimiz yok
        width_pixel = int(coord[2] * im_width)
        height_pixel = int(coord[3] * im_height) # işimiz yok

        left_edge = x_pixel - (width_pixel // 2)
        right_edge = x_pixel + (width_pixel // 2)

        threshold = 150

        left_border = (im_width/2) - threshold
        right_border = (im_width/2) + threshold

        if left_edge <= left_border:
            send_command(-1)
        elif right_edge >= right_border:
            send_command(1)
        else:
            send_command(0)
    else:
        send_command(404)


    # Print the results
    print("Detected:", detected)
    print("Bbox Coordinates:", coord)

