import sys
from resource_management import *

class SpliceInstall(Script):
  def install(self, env):
    print 'Install the client';
  def configure(self, env):
    print 'Configure the client';
  def somethingcustom(self, env):
    print 'Something custom';

if __name__ == "__main__":
  SpliceInstall().execute()