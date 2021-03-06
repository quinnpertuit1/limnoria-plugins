###
# Copyright (c) 2019, cottongin
# All rights reserved.
#
#
###

from supybot import conf, registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('TVMaze')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x
    
from . import accountsdb


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('TVMaze', True)


TVMaze = conf.registerPlugin('TVMaze')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(TVMaze, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerGlobalValue(TVMaze, accountsdb.CONFIG_OPTION_NAME, accountsdb.CONFIG_OPTION)

conf.registerChannelValue(TVMaze, 'showEpisodeTitle',
    registry.Boolean(True, _("""Determines whether the episode title will be displayed in the schedule output.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
