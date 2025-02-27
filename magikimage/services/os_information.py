import os

class OSInformation:
  
  def get_os(self):
    return os.uname().sysname
  
  def get_version(self):
    return os.uname().release
  
  def get_architecture(self):
    return os.uname().machine
  
  def get_hostname(self):
    return os.uname().nodename
  
  def get_kernel_version(self):
    return os.uname().version
  
  def get_home_directory(self):
    return os.environ['HOME']
  
  def get_user(self):
    return os.environ['USER']
  
  def get_shell(self):
    return os.environ['SHELL']
  
  
  