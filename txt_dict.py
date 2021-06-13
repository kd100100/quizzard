# def get_ques(r):
#     with open('r'+str(r)+".txt", "r", encoding="utf8") as f:
#         data = f.readlines()
#     i=0;qno=0
#     questions = []

#     while len(data)>i:
#         # print(qno)
#         qno += 1
#         qa = {'qno' : qno}

#         if data[i][5] == '1':
#             qa['type'] = 1
#             qa['ques'] = data[i+1][:-1]
#             qa['opt1'] = data[i+2][:-1]
#             qa['opt2'] = data[i+3][:-1]
#             qa['opt3'] = data[i+4][:-1]
#             qa['opt4'] = data[i+5][:-1]
#             qa['crt'] = data[i+6][4:-1]
#             i+=8

#         elif data[i][5] == '2':
#             qa['type'] = 2
#             temp = data[i+1][4:-1].split(':')
#             qa['ques'] = temp[1]
#             qa['image'] = temp[0]
#             qa['opt1'] = data[i+2][:-1]
#             qa['opt2'] = data[i+3][:-1]
#             qa['opt3'] = data[i+4][:-1]
#             qa['opt4'] = data[i+5][:-1]
#             qa['crt'] = data[i+6][4:-1]
#             i+=8

#         elif data[i][5] == '3':
#             qa['type'] = 3
#             temp = data[i+1][4:-1].split(':')
#             qa['ques'] = temp[1]
#             qa['image'] = temp[0]
#             qa['opt1'] = data[i+2][4:-1]
#             qa['opt2'] = data[i+3][4:-1]
#             qa['opt3'] = data[i+4][4:-1]
#             qa['opt4'] = data[i+5][4:-1]
#             qa['crt'] = data[i+6][8:-1]
#             i+=8

#         elif data[i][5] == '4':
#             qa['type'] = 4
#             qa['ques'] = data[i+1][:-1]
#             qa['crt'] = data[i+2][4:-1]
#             i+=4
            
#         elif data[i][5] == '5':
#             qa['type'] = 5
#             temp = data[i+1][4:-1].split(':')
#             qa['ques'] = temp[1]
#             qa['image'] = temp[0]
#             qa['crt'] = data[i+2][4:-1]
#             i+=4
            
#         elif data[i][5] == '6':
#             qa['type'] = 6
#             temp = data[i+1][4:-1].split(':')
#             qa['ques'] = temp[2]
#             qa['image1'] = temp[0]
#             qa['image2'] = temp[1]
#             qa['crt'] = data[i+2][4:-1]
#             i+=4

#         questions.append(qa)
        
#     return questions

# # print(get_ques())
# print(get_ques(2))

# r1 =[
#     {'qno': 1, 'type': 1, 'ques': "Who first introduced the word 'robot'?", 'opt1': 'Isaac Asimov', 'opt2': 'Karel Capek', 'opt3': 'Isaac Newton', 'opt4':'Ben Skora', 'crt': 'Karel Capek'}, 
#     {'qno': 2, 'type': 2, 'ques': 'Guess the output for the following', 'image': 'carbon1.png', 'opt1': "['Q','I','A','Q','C']", 'opt2': "['QUIZZARD']", 'opt3': "['QUIZZARD','IS','A','QUIZ','COMPETITION']", 'opt4': 'Compilation Error', 'crt': "['Q','I','A','Q','C']"}, 
#     {'qno': 3, 'type': 1, 'ques': 'Which of the following terms IS NOT one of the five basic parts of a robot?', 'opt1': 'Peripheral tools', 'opt2': 'End effectors', 'opt3': 'Controller', 'opt4': 'Drive', 'crt': 'Peripheral tools'}, 
#     {'qno': 4, 'type': 1, 'ques': 'Which IC (Integrated Circuit) is present on NodeMCU?', 'opt1': 'ESP8266', 'opt2': 'Atmega326', 'opt3': 'Atmega328P', 'opt4': 'ESPN8266', 'crt': 'ESP8266'}, 
#     {'qno': 5, 'type': 1, 'ques': 'L293D is an', 'opt1': 'Micro Controller ', 'opt2': 'Bluetooth Module', 'opt3': 'Motor Driver IC ', 'opt4': 'IR Reciver/Transmitter', 'crt': 'Motor Driver IC'}, 
#     {'qno': 6, 'type': 1, 'ques': 'How many NOT Gates are contained in a 7404 NOT IC?', 'opt1': '1', 'opt2': '4', 'opt3': '6', 'opt4': '8', 'crt': '6'}, 
#     {'qno': 7, 'type': 1, 'ques': 'ANN stands for', 'opt1': 'Arithmetic Neural Network ', 'opt2': 'Artificial Neural Network ', 'opt3': 'Artificial Neural Node ','opt4': 'All of the above ', 'crt': 'Artificial Neural Network '}, 
#     {'qno': 8, 'type': 1, 'ques': 'Which of the following systems use a transducer?', 'opt1': 'The structural system', 'opt2': 'The propulsion system', 'opt3': 'The sensor and feedback system', 'opt4': 'The control system', 'crt': 'The sensor and feedback system'}, 
#     {'qno': 9, 'type': 1, 'ques': 'A humanoid robot developed by Hanson Robotics(human-like robot) is called ', 'opt1': 'Asimo', 'opt2': 'Sony Aibo', 'opt3': 'Sophia', 'opt4': 'Gort', 'crt': 'Sophia'}, 
#     {'qno': 10, 'type': 1, 'ques': 'The cut-in voltage for silicon diode is approximately', 'opt1': '0.2 V', 'opt2': '0.6 V', 'opt3': '1.1 V', 'opt4': '1.4 V', 'crt': '0.6 V'}, 
#     {'qno': 11, 'type': 1, 'ques': "Which organisation is developing 'Asimo'?", 'opt1': 'Google', 'opt2': 'Honda', 'opt3': 'Space X', 'opt4': 'Boston Dynamics', 'crt': 'Honda'}, 
#     {'qno': 12, 'type': 1, 'ques': 'The robotics subsystem that gives the robot the ability to detect various things in its environment. It is effectively “eyes and ears” of the robot.', 'opt1': 'Control Subsystem', 'opt2': 'Logic Subsystem', 'opt3': 'Sensor Subsystem', 'opt4': 'Structure Subsystem', 'crt': 'Sensor Subsystem'}, 
#     {'qno': 13, 'type': 1, 'ques': 'Which of the following is correct for proximity sensors', 'opt1': 'Ultrasonic Wave Type', 'opt2': 'Capacitive Type', 'opt3': 'Inductive Type', 'opt4': 'All of the above', 'crt': 'All of the above'}, 
#     {'qno': 14, 'type': 1, 'ques': 'LIDAR stands for', 'opt1': 'Light Detection and Radiation', 'opt2': 'Light Detection and Ranging', 'opt3': 'Lithium Detector and Radiator', 'opt4': 'Lithium Detection and Ranging', 'crt': 'Light Detection and Ranging'}, 
#     {'qno': 15, 'type': 1, 'ques': 'A program written with the IDE for Arduino is called', 'opt1': 'IDE source', 'opt2': 'Sketch', 'opt3': 'Cryptography', 'opt4': 'Source code', 'crt': 'Sketch'}, 
#     {'qno': 16, 'type': 1, 'ques': 'Which sensor is used in line following robots?', 'opt1': 'Infrared Sensor', 'opt2': 'Microwave Radar Sensor', 'opt3': 'Ultrasonic Sensor', 'opt4': 'Temperature Sensor', 'crt': 'Infrared Sensor'}, 
#     {'qno': 17, 'type': 1, 'ques': 'How do the rovers move about on the rocky surface of Mars?', 'opt1': 'On six wheels', 'opt2': 'Pneumatically propelled robotic legs', 'opt3': "On 'caterpillar' or tank wheels", 'opt4': "'Hopping' from spot to spot through rocket propulsion", 'crt': 'On six wheels'}, 
#     {'qno': 18, 'type': 1, 'ques': 'Which sensor can be used in robots for measuring distance?', 'opt1': 'mpu6050', 'opt2': 'Piezoelectric sensor', 'opt3': 'LDR module', 'opt4': 'Ultrasonic Sensor', 'crt': 'Ultrasonic Sensor'}, 
#     {'qno': 19, 'type': 1, 'ques': 'This actuator can only rotate between positions 0° to 120° degrees ', 'opt1':'Servo', 'opt2': 'Motor', 'opt3': 'Square Shaft', 'opt4': 'Delrin Bearing', 'crt': 'Servo'}, 
#     {'qno': 20, 'type': 1, 'ques': 'Drives are also known as','opt1': 'Controller', 'opt2': 'Sensors', 'opt3': 'Manipulator', 'opt4': 'Actuators', 'crt': 'Actuators'}, 
#     {'qno': 21, 'type': 1, 'ques': 'A Robot is a', 'opt1': 'Programmable', 'opt2': 'Zeroeth pass', 'opt3': 'Both (a) and (b)', 'opt4': 'None of the above', 'crt': 'Both (a) and (b)'}, 
#     {'qno': 22, 'type': 1, 'ques': 'Which of the following is a key objective of perseverance rover?', 'opt1': 'Search for signs of past microbial life', 'opt2': 'Characterize the Martian climate and geology', 'opt3': 'Demonstrate the viability of technologies which will ultimately pave the way for future human exploration beyond the Moon', 'opt4': 'All of the above', 'crt': 'All of the above'}, 
#     {'qno': 23, 'type': 2, 'ques': 'What is the current through the LED?', 'image': 'circuit.png', 'opt1': '0 mA', 'opt2': '23 mA', 'opt3': '18 mA', 'opt4': '13 mA', 'crt': '13 mA'}, 
#     {'qno': 24, 'type': 1, 'ques': 'The direction of rotation of D.C Series Motor can be changed by', 'opt1': 'Interchanging Supply Terminals', 'opt2': 'Interchanging Field Terminals', 'opt3': 'Interchanging Random Terminals', 'opt4': 'All of the above ', 'crt': 'Interchanging Field Terminals'}, 
#     {'qno': 25, 'type': 1, 'ques': 'SCARA robot is used in which of the following applications', 'opt1': 'Quality Control', 'opt2': 'Assembly', 'opt3': 'Defense', 'opt4': 'All of the above', 'crt': 'Assembly'}
#     ]

# r2 = [
#     {'qno': 1, 'type': 1, 'ques': 'Which is the software or a programming language used for controlling of Arduino?', 'opt1': 'Assembly Language', 'opt2': 'C Languages', 'opt3': 'JAVA', 'opt4': 'Any Language', 'crt': 'Any Language '}, 
#     {'qno': 2, 'type': 1, 'ques': 'Assertion (A): The servo robot is a closed loop system. Reason(R): It allows for a feedback', 'opt1': 'Both A and R are true and R is not correct explanation of A', 'opt2': 'Both A and R are true but R is not correct explanation of A', 'opt3': 'A is true but R is false', 'opt4': 'A is false but R is true', 'crt': ' Both A and R are true and R is not correct explanation of A'}, 
#     {'qno': 3, 'type': 1, 'ques': 'Which sensor should be used for calculating pressure?', 'opt1': 'DHT11', 'opt2': 'LM335Z/NOPB', 'opt3': 'HC-SR04', 'opt4': 'MPX10DP', 'crt': 'MPX10DP'}, 
#     {'qno': 4, 'type': 1, 'ques': 'which of the following is not a programing language for computer controlled robot', 'opt1': 'AMU', 'opt2': 'VAl', 'opt3': 'RAIL ', 'opt4': 'HELP', 'crt': 'AMU'}, 
#     {'qno': 5, 'type': 2, 'ques': 'What is the name of this part?', 'image': 'jpg1.jpg', 'opt1': 'Bushing Block', 'opt2': 'Bearing Flat', 'opt3': 'Guide Block', 'opt4': 'Spacer', 'crt': 'Bearing Flat'}, 
#     {'qno': 6, 'type': 1, 'ques': 'Which of the following robots are FULLY autonomous robots:', 'opt1': 'Ventana ROV (for Underwater jelly-tracking)', 'opt2': 'Minerva', 'opt3': 'MARs Rover Spirit', 'opt4': 'All of the above', 'crt': 'Minerva'}, 
#     {'qno': 7, 'type': 2, 'ques': 'Guess the output for the following', 'image': 'carbon.png', 'opt1': '[[[2, 3, 9]], [[2, 3, 9]], [[2, 3, 9]]]', 'opt2': '[[2, 3, 9], [2, 3, 9], [2, 3, 9]]', 'opt3': '[[[2, 3, 9]],[[2, 3, 9]]]', 'opt4': 'None of these', 'crt': '[[[2, 3, 9]], [[2, 3, 9]], [[2, 3, 9]]]'}, 
#     {'qno': 8, 'type': 1, 'ques': 'WiFi is not present in which of the following models?', 'opt1': 'Raspberry Pi 3', 'opt2': 'Raspberry Pi Zero WH', 'opt3': 'Raspberry Pi Zero W', 'opt4': 'Raspberry Pi Zero', 'crt': 'Raspberry Pi Zero'}, 
#     {'qno': 9, 'type': 1, 'ques': 'The study of mechanical systems that function like living organisms or parts of living organisms, is called?', 'opt1': 'Bionics', 'opt2': 'Biomechanics', 'opt3': 'Ergonomics', 'opt4': 'Ergometrics', 'crt': 'Biomechanics'}, 
#     {'qno': 10, 'type': 2, 'ques': 'Consider the circuit given below which uses two oppositely connected ideal diodes in parallel. The current flowing in the circuit is', 'image': 'circuit2.png', 'opt1': '0', 'opt2': '0.85A', 'opt3': '2A', 'opt4': '1A', 'crt': '2A'}, 
#     {'qno': 11, 'type': 1, 'ques': 'What is the name for space inside which a robot unit operates?', 'opt1': 'environment', 'opt2': 'spatial base', 'opt3': 'work envelope', 'opt4': 'exclusion zone', 'crt': 'work envelope'}, 
#     {'qno': 12, 'type': 1, 'ques': 'The work envelope of a Cartesian robot can best be described as', 'opt1': 'Hemisphere', 'opt2': 'Heart', 'opt3': 'Quadrilateral', 'opt4': 'Overlapping circles', 'crt': 'Quadrilateral'}, 
#     {'qno': 13, 'type': 1, 'ques': 'If a robot has 3 legs, then the number of possible events is _________', 'opt1': '24', 'opt2': '720', 'opt3': '120', 'opt4': '240', 'crt': '120'}, 
#     {'qno': 14, 'type': 1, 'ques': 'An autonomous robot is one that:', 'opt1': 'Has mechanisms to perform a variety of operations', 'opt2': 'Requires a human operator to carry out its tasks', 'opt3': 'Uses its own intelligence or program to handle situations', 'opt4': 'All of the above ', 'crt': 'Uses its own intelligence or program to handle situations'}, 
#     {'qno': 15, 'type': 1, 'ques': 'Which of the following does not need a power source to operate?', 'opt1': 'The propulsion system', 'opt2': 'The control system', 'opt3': 'The sensor and feedback system', 'opt4': 'The structural system', 'crt': 'The structural system'}
#     ]

def get_ques(r):
    r1 =[
        {'qno': 1, 'type': 1, 'ques': "Who first introduced the word 'robot'?", 'opt1': 'Isaac Asimov', 'opt2': 'Karel Capek', 'opt3': 'Isaac Newton', 'opt4':'Ben Skora', 'crt': 'Karel Capek'}, 
        {'qno': 2, 'type': 2, 'ques': 'Guess the output for the following', 'image': 'carbon1.png', 'opt1': "['Q','I','A','Q','C']", 'opt2': "['QUIZZARD']", 'opt3': "['QUIZZARD','IS','A','QUIZ','COMPETITION']", 'opt4': 'Compilation Error', 'crt': "['Q','I','A','Q','C']"}, 
        {'qno': 3, 'type': 1, 'ques': 'Which of the following terms IS NOT one of the five basic parts of a robot?', 'opt1': 'Peripheral tools', 'opt2': 'End effectors', 'opt3': 'Controller', 'opt4': 'Drive', 'crt': 'Peripheral tools'}, 
        {'qno': 4, 'type': 1, 'ques': 'Which Signal is used to control Servo motor?', 'opt1': 'PAM', 'opt2': 'PWM', 'opt3': 'AC', 'opt4': 'DC', 'crt': 'PWM'}, 
        {'qno': 5, 'type': 1, 'ques': 'L293D is an', 'opt1': 'Micro Controller ', 'opt2': 'Bluetooth Module', 'opt3': 'Motor Driver IC ', 'opt4': 'IR Reciver/Transmitter', 'crt': 'Motor Driver IC'}, 
        {'qno': 6, 'type': 1, 'ques': 'How many NOT Gates are contained in a 7404 NOT IC?', 'opt1': '1', 'opt2': '4', 'opt3': '6', 'opt4': '8', 'crt': '6'}, 
        {'qno': 7, 'type': 1, 'ques': 'ANN stands for', 'opt1': 'Arithmetic Neural Network ', 'opt2': 'Artificial Neural Network ', 'opt3': 'Artificial Neural Node ','opt4': 'All of the above ', 'crt': 'Artificial Neural Network '}, 
        {'qno': 8, 'type': 1, 'ques': 'Which of the following systems use a transducer?', 'opt1': 'The structural system', 'opt2': 'The propulsion system', 'opt3': 'The sensor and feedback system', 'opt4': 'The control system', 'crt': 'The sensor and feedback system'}, 
        {'qno': 9, 'type': 1, 'ques': 'A humanoid robot developed by Hanson Robotics(human-like robot) is called ', 'opt1': 'Asimo', 'opt2': 'Sony Aibo', 'opt3': 'Sophia', 'opt4': 'Gort', 'crt': 'Sophia'}, 
        {'qno': 10, 'type': 1, 'ques': 'The cut-in voltage for silicon diode is approximately', 'opt1': '0.2 V', 'opt2': '0.6 V', 'opt3': '1.1 V', 'opt4': '1.4 V', 'crt': '0.6 V'}, 
        {'qno': 11, 'type': 1, 'ques': "Which organisation is developing 'Asimo'?", 'opt1': 'Google', 'opt2': 'Honda', 'opt3': 'Space X', 'opt4': 'Boston Dynamics', 'crt': 'Honda'}, 
        {'qno': 12, 'type': 1, 'ques': 'The robotics subsystem that gives the robot the ability to detect various things in its environment. It is effectively “eyes and ears” of the robot.', 'opt1': 'Control Subsystem', 'opt2': 'Logic Subsystem', 'opt3': 'Sensor Subsystem', 'opt4': 'Structure Subsystem', 'crt': 'Sensor Subsystem'}, 
        {'qno': 13, 'type': 1, 'ques': 'Which of the following is correct for proximity sensors', 'opt1': 'Ultrasonic Wave Type', 'opt2': 'Capacitive Type', 'opt3': 'Inductive Type', 'opt4': 'All of the above', 'crt': 'All of the above'}, 
        {'qno': 14, 'type': 1, 'ques': 'LIDAR stands for', 'opt1': 'Light Detection and Radiation', 'opt2': 'Light Detection and Ranging', 'opt3': 'Lithium Detector and Radiator', 'opt4': 'Lithium Detection and Ranging', 'crt': 'Light Detection and Ranging'}, 
        {'qno': 15, 'type': 1, 'ques': 'A program written with the IDE for Arduino is called', 'opt1': 'IDE source', 'opt2': 'Sketch', 'opt3': 'Cryptography', 'opt4': 'Source code', 'crt': 'Sketch'}, 
        {'qno': 16, 'type': 1, 'ques': 'Which sensor is used in line following robots?', 'opt1': 'Infrared Sensor', 'opt2': 'Microwave Radar Sensor', 'opt3': 'Ultrasonic Sensor', 'opt4': 'Temperature Sensor', 'crt': 'Infrared Sensor'}, 
        {'qno': 17, 'type': 1, 'ques': 'How do the rovers move about on the rocky surface of Mars?', 'opt1': 'On six wheels', 'opt2': 'Pneumatically propelled robotic legs', 'opt3': "On 'caterpillar' or tank wheels", 'opt4': "'Hopping' from spot to spot through rocket propulsion", 'crt': 'On six wheels'}, 
        {'qno': 18, 'type': 1, 'ques': 'Which sensor can be used in robots for measuring distance?', 'opt1': 'mpu6050', 'opt2': 'Piezoelectric sensor', 'opt3': 'LDR module', 'opt4': 'Ultrasonic Sensor', 'crt': 'Ultrasonic Sensor'}, 
        {'qno': 19, 'type': 1, 'ques': 'Which parameter is changed when we bend a flex sensor?', 'opt1':'Capacitance', 'opt2': 'Inductance', 'opt3': 'Resistance', 'opt4': 'Reactance', 'crt': 'Resistance'}, 
        {'qno': 20, 'type': 1, 'ques': 'Drivers are also known as','opt1': 'Controller', 'opt2': 'Sensors', 'opt3': 'Manipulator', 'opt4': 'Actuators', 'crt': 'Actuators'}, 
        {'qno': 21, 'type': 1, 'ques': 'A Robot is a', 'opt1': 'Programmable', 'opt2': 'Zeroeth pass', 'opt3': 'Both (a) and (b)', 'opt4': 'None of the above', 'crt': 'Both (a) and (b)'}, 
        {'qno': 22, 'type': 1, 'ques': 'Which of the following is a key objective of perseverance rover?', 'opt1': 'Search for signs of past microbial life', 'opt2': 'Characterize the Martian climate and geology', 'opt3': 'Demonstrate the viability of technologies which will ultimately pave the way for future human exploration beyond the Moon', 'opt4': 'All of the above', 'crt': 'All of the above'}, 
        {'qno': 23, 'type': 2, 'ques': 'What is the current through the LED?', 'image': 'circuit.png', 'opt1': '0 mA', 'opt2': '23 mA', 'opt3': '18 mA', 'opt4': '13 mA', 'crt': '18 mA'}, 
        {'qno': 24, 'type': 1, 'ques': 'What type of processor Architecture used in raspberry pi boards?', 'opt1': 'ARM Cortex A series', 'opt2': 'ARM Cortex M series', 'opt3': 'Tensilica LX series', 'opt4': 'X86 series', 'crt': 'ARM Cortex A series'}, 
        {'qno': 25, 'type': 1, 'ques': 'SCARA robot is used in which of the following applications?', 'opt1': 'Quality Control', 'opt2': 'Assembly', 'opt3': 'Defense', 'opt4': 'All of the above', 'crt': 'Assembly'}
        ]

    r2 = [
        {'qno': 1, 'type': 1, 'ques': 'Which is the software or a programming language used for controlling of Arduino?', 'opt1': 'Assembly Language', 'opt2': 'C Languages', 'opt3': 'JAVA', 'opt4': 'Any Language', 'crt': 'Any Language '}, 
        {'qno': 2, 'type': 1, 'ques': 'Assertion (A): The servo robot is a closed loop system. Reason(R): It allows for a feedback', 'opt1': 'Both A and R are true but R is not correct explanation of A', 'opt2': 'Both A and R are true and R is correct explanation of A', 'opt3': 'A is true but R is false', 'opt4': 'A is false but R is true', 'crt': ' Both A and R are true but R is not correct explanation of A'}, 
        {'qno': 3, 'type': 1, 'ques': 'Which sensor should be used for calculating pressure?', 'opt1': 'DHT11', 'opt2': 'LM335Z/NOPB', 'opt3': 'HC-SR04', 'opt4': 'MPX10DP', 'crt': 'MPX10DP'}, 
        {'qno': 4, 'type': 1, 'ques': 'which of the following is not a programing language for computer controlled robot', 'opt1': 'AMU', 'opt2': 'VAL', 'opt3': 'RAIL ', 'opt4': 'HELP', 'crt': 'AMU'}, 
        {'qno': 5, 'type': 2, 'ques': 'What is the name of this part?', 'image': 'jpg1.jpg', 'opt1': 'Bushing Block', 'opt2': 'Bearing Flat', 'opt3': 'Guide Block', 'opt4': 'Spacer', 'crt': 'Bearing Flat'}, 
        {'qno': 6, 'type': 1, 'ques': 'Which of the following robots are FULLY autonomous robots:', 'opt1': 'Ventana ROV (for Underwater jelly-tracking)', 'opt2': 'Minerva', 'opt3': 'MARs Rover Spirit', 'opt4': 'All of the above', 'crt': 'Minerva'}, 
        {'qno': 7, 'type': 2, 'ques': 'Guess the output for the following', 'image': 'carbon.png', 'opt1': '[[[2, 3, 9]], [[2, 3, 9]], [[2, 3, 9]]]', 'opt2': '[[2, 3, 9], [2, 3, 9], [2, 3, 9]]', 'opt3': '[[[2, 3, 9]],[[2, 3, 9]]]', 'opt4': 'None of these', 'crt': '[[[2, 3, 9]], [[2, 3, 9]], [[2, 3, 9]]]'}, 
        {'qno': 8, 'type': 1, 'ques': 'WiFi is not present in which of the following models?', 'opt1': 'Raspberry Pi 3', 'opt2': 'Raspberry Pi Zero WH', 'opt3': 'Raspberry Pi Zero W', 'opt4': 'Raspberry Pi Zero', 'crt': 'Raspberry Pi Zero'}, 
        {'qno': 9, 'type': 1, 'ques': 'The study of mechanical systems that function like living organisms or parts of living organisms, is called?', 'opt1': 'Bionics', 'opt2': 'Biomechanics', 'opt3': 'Ergonomics', 'opt4': 'Ergometrics', 'crt': 'Biomechanics'}, 
        {'qno': 10, 'type': 2, 'ques': 'Consider the circuit given below which uses two oppositely connected ideal diodes in parallel. The current flowing in the circuit is', 'image': 'circuit2.png', 'opt1': '0', 'opt2': '0.85A', 'opt3': '2A', 'opt4': '1A', 'crt': '2A'}, 
        {'qno': 11, 'type': 1, 'ques': 'What is the name for space inside which a robot unit operates?', 'opt1': 'environment', 'opt2': 'spatial base', 'opt3': 'work envelope', 'opt4': 'exclusion zone', 'crt': 'work envelope'}, 
        {'qno': 12, 'type': 1, 'ques': "What does 'PUMA' stand for in context to robotics?", 'opt1': 'Programmable used machine to assemble', 'opt2': 'Programmed utility machine for assembly', 'opt3': 'Programmable universal machine for assembly', 'opt4': 'Programmed utility machine to assemble', 'crt': 'Programmable universal machine for assembly'}, 
        {'qno': 13, 'type': 1, 'ques': 'If a robot has 3 legs, then the number of possible events is _________', 'opt1': '24', 'opt2': '720', 'opt3': '120', 'opt4': '240', 'crt': '120'}, 
        {'qno': 14, 'type': 1, 'ques': 'An autonomous robot is one that:', 'opt1': 'Has mechanisms to perform a variety of operations', 'opt2': 'Requires a human operator to carry out its tasks', 'opt3': 'Uses its own intelligence or program to handle situations', 'opt4': 'All of the above ', 'crt': 'Uses its own intelligence or program to handle situations'}, 
        {'qno': 15, 'type': 1, 'ques': 'Motors used for electronic actuator drives:', 'opt1': 'AC servo motors', 'opt2': 'DC servo motors', 'opt3': 'Stepper motors', 'opt4': 'All of the above', 'crt': 'All of the above'}
        ]
    if r=='1':
        return r1
    elif r=='2':
        return r2
