import time
import usb.core

class Launcher:
  
  DOWN = 0x01
  UP = 0x02
  LEFT = 0x04
  RIGHT = 0x08
  FIRE = 0x10
  STOP = 0x20

  def __init__(self):
    self.dev = usb.core.find(idVendor=0x0a81, idProduct=0x0701)
    self.dev.detach_kernel_driver(0)
    self.dev.set_configuration()

  def send_command(self, command):
    self.dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [command])

  def send_command_duration(self, command, delay):
    self.send_command(command)
    time.sleep(delay)
    self.stop()

  def stop(self):
    self.send_command(0x20)

  def fire(self, count):
    self.send_command_duration(Launcher.FIRE, 5.5 * count)
