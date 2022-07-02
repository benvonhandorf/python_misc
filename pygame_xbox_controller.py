def dumpStick(s):
  print("Joystick: {}".format(s.get_name()))
  for i in range(0,s.get_numaxes()):
    print("Axis {} - {}".format(i, s.get_axis(i)))
  for i in range(0,s.get_numbuttons()):
    print("Button {} - {}".format(i, s.get_button(i)))
