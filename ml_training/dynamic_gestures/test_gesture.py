from tensorflow.python.ops.gen_math_ops import ragged_bincount

mock_gesture = [[38,18,134,67,180,-2.58,-1.77,4.54,0.37,-0.39,-0.04],
[28,10,116,36,180,-2.61,-1.86,4.65,0.38,-0.35,-0.06],
[59,20,128,72,180,-2.55,-1.92,4.82,0.37,-0.33,-0.06],
[54,27,118,54,180,-2.51,-1.95,4.96,0.35,-0.32,-0.05],
[50,19,111,18,180,-2.58,-1.99,5.00,0.35,-0.31,-0.05],
[64,15,127,72,180,-2.61,-2.09,5.04,0.38,-0.27,-0.06],
[40,17,111,0,180,-2.60,-2.16,5.15,0.37,-0.25,-0.06],
[50,18,103,87,180,-2.59,-2.20,5.26,0.34,-0.24,-0.04],
[40,25,118,0,180,-2.63,-2.21,5.35,0.31,-0.22,-0.03],
[44,12,130,0,180,-2.66,-2.25,5.42,0.30,-0.18,-0.03],
[42,10,126,31,180,-2.63,-2.26,5.49,0.27,-0.15,-0.01],
[70,26,110,64,180,-2.63,-2.23,5.51,0.23,-0.13,0.01],
[51,38,140,0,180,-2.70,-2.21,5.49,0.21,-0.12,0.02],
[46,21,119,57,180,-2.76,-2.23,5.47,0.21,-0.10,0.01],
[64,39,130,120,180,-2.76,-2.28,5.51,0.19,-0.08,0.02],
[58,11,130,9,180,-2.73,-2.28,5.57,0.15,-0.07,0.03],
[40,17,127,0,180,-2.71,-2.25,5.61,0.13,-0.06,0.04],
[41,32,136,0,180,-2.72,-2.24,5.60,0.12,-0.04,0.04],
[49,29,126,117,180,-2.77,-2.25,5.55,0.10,-0.04,0.05],
[59,29,133,24,180,-2.78,-2.24,5.54,0.08,-0.04,0.06],
[57,29,125,145,180,-2.77,-2.19,5.59,0.06,-0.03,0.06],
[36,30,115,103,180,-2.76,-2.17,5.62,0.06,-0.02,0.05],
[61,22,127,0,180,-2.79,-2.20,5.59,0.06,-0.02,0.04],
[64,15,126,100,180,-2.83,-2.21,5.54,0.04,-0.02,0.04],
[48,23,131,0,180,-2.83,-2.19,5.53,0.02,-0.02,0.05],
[67,33,122,0,180,-2.82,-2.16,5.55,0.01,-0.03,0.04],
[48,30,114,54,180,-2.83,-2.15,5.56,0.02,-0.03,0.04],
[49,22,111,0,180,-2.85,-2.17,5.56,0.03,-0.03,0.03],
[55,24,129,69,180,-2.82,-2.20,5.59,0.04,-0.03,0.02],
[42,26,142,24,180,-2.80,-2.22,5.61,0.03,-0.02,0.02],
[64,32,126,106,180,-2.80,-2.22,5.61,0.01,-0.03,0.03],
[70,22,120,40,180,-2.83,-2.22,5.58,0.01,-0.02,0.03],
[65,18,129,67,180,-2.83,-2.22,5.59,-0.00,-0.02,0.04],
[56,24,125,51,180,-2.80,-2.20,5.62,-0.00,-0.02,0.04],
[36,31,115,72,180,-2.80,-2.19,5.62,-0.00,-0.01,0.04],
[47,14,141,103,180,-2.80,-2.19,5.61,-0.00,-0.01,0.04],
[38,14,139,3,180,-2.83,-2.19,5.58,-0.01,-0.00,0.04],
[54,30,142,94,180,-2.84,-2.19,5.57,-0.02,-0.00,0.05],
[55,25,126,0,180,-2.84,-2.17,5.56,-0.04,-0.00,0.06],
[36,21,135,0,180,-2.83,-2.14,5.57,-0.04,-0.00,0.06],
[46,15,119,27,180,-2.85,-2.12,5.55,-0.04,-0.01,0.06],
[70,27,131,51,180,-2.87,-2.13,5.52,-0.02,-0.01,0.05],
[64,25,143,15,180,-2.86,-2.13,5.52,-0.02,-0.00,0.05],
[66,14,122,91,180,-2.86,-2.11,5.52,-0.02,-0.01,0.05],
[60,32,134,99,180,-2.87,-2.09,5.52,-0.01,-0.01,0.05],
[76,17,122,0,180,-2.89,-2.08,5.50,-0.00,-0.01,0.05],
[72,27,138,45,180,-2.89,-2.07,5.50,0.00,-0.01,0.05],
[61,29,138,51,180,-2.88,-2.05,5.51,-0.00,-0.01,0.05],
[70,16,140,72,180,-2.88,-2.03,5.52,0.00,-0.01,0.04],
[71,25,116,114,180,-2.90,-2.01,5.51,0.01,-0.01,0.04],
[54,39,135,0,180,-2.90,-2.02,5.51,0.02,-0.01,0.03],
[62,26,121,21,180,-2.89,-2.02,5.52,0.01,-0.01,0.03],
[59,24,131,1,180,-2.89,-2.00,5.53,0.01,-0.02,0.03],
[62,27,140,67,180,-2.90,-1.99,5.53,0.01,-0.01,0.03],
[77,25,131,0,180,-2.91,-2.00,5.52,0.02,-0.01,0.02],
[74,25,134,42,180,-2.91,-2.01,5.51,0.01,-0.01,0.02],
[59,35,136,91,180,-2.90,-2.01,5.52,0.01,-0.02,0.02],
[53,16,134,141,180,-2.89,-2.00,5.52,0.01,-0.02,0.02],
[56,28,135,19,180,-2.89,-2.00,5.51,0.02,-0.02,0.02],
[72,28,130,75,180,-2.91,-2.01,5.49,0.02,-0.02,0.02],
[69,29,130,61,180,-2.92,-2.02,5.49,0.01,-0.02,0.02],
[77,28,138,37,180,-2.91,-2.00,5.50,0.01,-0.02,0.02],
[72,43,119,121,180,-2.91,-2.00,5.49,0.02,-0.02,0.02],
[77,21,130,9,180,-2.90,-1.99,5.49,0.02,-0.02,0.02],
[64,33,115,0,180,-2.91,-2.00,5.48,0.02,-0.02,0.02],
[56,26,144,58,180,-2.90,-2.00,5.48,0.02,-0.02,0.02],
[70,25,127,33,180,-2.91,-2.00,5.49,0.02,-0.02,0.02],
[96,42,137,93,180,-2.92,-2.00,5.50,0.03,-0.02,0.02],
[76,31,129,55,180,-2.92,-2.00,5.50,0.03,-0.02,0.02],
[81,24,130,40,180,-2.92,-2.00,5.50,0.02,-0.02,0.02],
[60,38,119,180,180,-2.91,-1.99,5.51,0.02,-0.02,0.02],
[67,39,150,99,180,-2.90,-1.99,5.52,0.02,-0.02,0.02],
[68,14,142,97,180,-2.89,-1.98,5.54,0.02,-0.02,0.02],
[58,23,121,112,180,-2.92,-1.98,5.52,0.02,-0.02,0.02],
[74,28,122,120,180,-2.93,-1.98,5.51,0.03,-0.01,0.02],
[64,33,135,48,180,-2.91,-1.98,5.53,0.02,-0.01,0.02],
[57,30,149,81,180,-2.90,-1.97,5.54,0.02,-0.01,0.02],
[47,21,126,175,180,-2.90,-1.97,5.53,0.02,-0.01,0.01],
[62,19,121,156,180,-2.92,-1.98,5.51,0.02,-0.00,0.01],
[68,39,119,75,180,-2.92,-1.98,5.51,0.02,-0.00,0.01],
[78,26,128,64,180,-2.91,-1.97,5.52,0.02,-0.00,0.01],
[81,17,131,69,180,-2.91,-1.97,5.51,0.02,-0.00,0.01],
[61,29,120,49,180,-2.94,-1.98,5.49,0.02,-0.00,0.01],
[59,46,136,76,180,-2.93,-2.00,5.49,0.03,0.01,0.00],
[64,26,132,100,180,-2.90,-2.00,5.52,0.02,0.00,0.01],
[50,20,134,114,180,-2.90,-1.98,5.52,0.02,-0.00,0.01],
[60,28,132,120,180,-2.92,-1.98,5.49,0.02,-0.00,0.01],
[45,25,129,0,180,-2.93,-1.98,5.48,0.02,-0.00,0.01],
[64,18,131,126,180,-2.90,-1.97,5.50,0.02,-0.00,0.01],
[82,29,122,169,180,-2.89,-1.97,5.50,0.02,-0.00,0.01],
[55,32,120,120,180,-2.90,-1.98,5.49,0.02,-0.00,0.01],
[72,25,147,135,180,-2.92,-1.99,5.47,0.02,0.00,0.01],
[71,37,129,16,180,-2.91,-2.00,5.46,0.03,0.00,0.01],
[60,42,134,90,180,-2.89,-1.99,5.46,0.02,-0.00,0.01],
[81,30,134,157,180,-2.89,-1.99,5.45,0.02,-0.01,0.01],
[64,25,112,118,180,-2.91,-2.00,5.45,0.03,-0.01,0.01],
[64,22,112,162,180,-2.91,-2.00,5.45,0.03,-0.01,0.01],
[60,31,116,97,180,-2.91,-2.02,5.46,0.03,-0.01,0.01],
[82,28,130,76,180,-2.90,-2.02,5.47,0.03,-0.01,0.01],
[79,13,129,117,180,-2.91,-2.01,5.47,0.02,-0.01,0.02],]


mock_gesture2 = []
for i in range(0,100):
    mock_gesture2.append([0,0,0,0,0,-0.03,-0.04,-0.02])

mock_gesture = mock_gesture2