from collective.grok import gs
from a5.phlocalities import MessageFactory as _

@gs.importstep(
    name=u'a5.phlocalities', 
    title=_('a5.phlocalities import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('a5.phlocalities.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
