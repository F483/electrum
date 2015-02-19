from PyQt4.QtGui import *
from electrum.plugins import BasePlugin, hook
from electrum.i18n import _

from gui.qt.amountedit import MyLineEdit
from gui.qt.util import HelpButton

class Plugin(BasePlugin):

  def fullname(self):
    return _('Bitcoin Message')

  def description(self):
    donate_address = "1Lb7eqQY3eBMdiZXz3A8GUaK4aGow1Gv89"
    text = _(
        "Store and forward messaging system using the bitcoin blockchain.\n"
        "Donation address: "
    )
    return "%s%s" % (text, donate_address)

  @hook
  def create_send_tab(self, grid):
    # FIXME change create_send_tab to allow for clean implementation
    self._label = QLabel(_('Bitcoin message'))
    self._message = MyLineEdit() # TODO correct class?
    self._help = HelpButton(_(
      "Add encrypted message to the transaction,"
      " only readable by the recipient."
    ))
    row = 5 # XXX overwrite fee
    grid.addWidget(self._label, row, 0)
    grid.addWidget(self._message, row, 1, 1, 3)
    grid.addWidget(self._help, row, 4)


