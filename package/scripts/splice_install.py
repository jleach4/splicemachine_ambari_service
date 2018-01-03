import sys
import grp
import os
import pwd
import sys

from resource_management.core.resources.accounts import User
from resource_management.core.resources.system import Directory, File, Execute

reload(sys)
sys.setdefaultencoding('utf8')

class SpliceInstall(Script):
  def install(self, env):
    import params
    env.set_params(params)
    Execute("echo Foo",
        timeout=30,
        logoutput=True)
    print 'Install the client';
  def configure(self, env):
    print 'Configure the client';
  def somethingcustom(self, env):
    print 'Something custom';

if __name__ == "__main__":
  SpliceInstall().execute()