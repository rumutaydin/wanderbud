import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) # serial connection between raspberry and ardunio, the port and baudrate might differ

def send_command(command): # function for sending the command with serial, see send_ardunio(s)
    ser.write(command.encode()) 

def send_ardunio(s):
    detected = "*D*" in s # check the string if it contains the characters that is manually put if detection occurs, see detect.py line 201


    coord = None
    if detected:
        start_index = s.split("[")
        
        end = start_index[1].split("]")
        
        alo = list(end[0].split(", "))
        
        coord = [float(cord) for cord in alo] # extract the coordinates from the string that is coming from the manipulated string in detect.py 

        im_width = 640  
        im_height = 640
        # taken coordinates are normalized so multiply with the default image wh
        x_pixel = int(coord[0] * im_width)
        y_pixel = int(coord[1] * im_height) 
        width_pixel = int(coord[2] * im_width)
        height_pixel = int(coord[3] * im_height) 
        # x_pixel and y_pixel are the coordinates of center of the bounding box, to determine the x axis coordinate of image's right and left edges add and substract the width//2 to/from it.
        left_edge = x_pixel - (width_pixel // 2)
        right_edge = x_pixel + (width_pixel // 2)
        '''threshold is for determining the bounding box's position on the frame, if the edges touch or pass the threshold border, send_command is invoked with pre-determined integers to 
        later manipulate in .ino code'''
        threshold = 150

        left_border = (im_width/2) - threshold
        right_border = (im_width/2) + threshold

        if left_edge <= left_border:
            send_command(-1) # turn left
        elif right_edge >= right_border:
            send_command(1) # turn right
        else:
            send_command(0) # go straight
    else:
        send_command(404) # no detection, stop


    # Print the results
    print("Detected:", detected)
    print("Bbox Coordinates:", coord)

