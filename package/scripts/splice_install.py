import sys
import grp
import os
import pwd
import sys

from resource_management import *

reload(sys)
sys.setdefaultencoding('utf8')

class SpliceInstall(Script):
  def install(self, env):
    import params
    env.set_params(params)

    print 'Install the client';
  def configure(self, env):
    print 'Configure the client';
  def somethingcustom(self, env):
    print 'Something custom';

if __name__ == "__main__":
  SpliceInstall().execute()