from zope import component
from zope import schema
from zope import interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.app.layout.viewlets import common
from plone.memoize import view
from plone.registry.interfaces import IRegistry
from plone.registry.field import Tuple

from collective.metarobots import _


content_vocabulary = SimpleVocabulary([
  SimpleTerm('all', 'all', u"all"),
  SimpleTerm('noindex', 'noindex', u"noindex"),
  SimpleTerm('nofollow', 'nofollow', u"nofollow"),
  SimpleTerm('none', 'none', u"none"),
  SimpleTerm('noarchive', 'noarchive', u"noarchive"),
  SimpleTerm('nosnippet', 'nosnippet', u"nosnippet"),
  SimpleTerm('noodp', 'noodp', u"noodp"),
  SimpleTerm('notranslate', 'notranslate', u"notranslate"),
  SimpleTerm('noimageindex', 'noimageindex', u"noimageindex"),
  SimpleTerm('unavailable_after_end', 'unavailable_after_end', u"unavailable after end time"),
])


class TagSettings(interface.Interface):
    """This schema define the settings to use to build the tag"""

    content = schema.List(title=_(u"Content"),
                          description=_(u"settings_content_description"),
                          value_type=schema.Choice(title=_(u"Content value"),
                                               vocabulary=content_vocabulary),
                          required=True)


class Tag(common.ViewletBase):

    def update(self):
        super(Tag, self).update()
        registry = component.getUtility(IRegistry)
        self.contextual = False
        if registry:
            self.settings = registry.forInterface(TagSettings)
            content = self.settings.content
            if content and "unavailable_after_end" in content:
                self.contextual = True

    def render(self):
        self.update()
        if self.settings.content:
            return self.index()

        return u""

    def content(self):
        if not self.contextual:
            return self.content_cached()

        content = list(self.settings.content)
        if "unavailable_after_end" in content:
            dt = self.content.end()
            format = '%d %b %Y %H:%M:%S %Z'
            content.remove("unavailable_after_end")
            content.append("unavailable_after: %s" % end.strftime(format))

        return u", ".join(content)

    @view.memoize_contextless
    def content_cached(self):
        return u", ".join(self.settings.content)
