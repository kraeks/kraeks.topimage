from zope.interface import Interface
from uvc.api import api
from plone.app.layout.viewlets.interfaces import IAboveContent

api.templatedir('templates')

class TopImage(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IAboveContent)

