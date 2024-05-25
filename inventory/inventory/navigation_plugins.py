from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _


class NavigationPlugin(CMSPluginBase):
    module = 'Custom'
    name = 'Navigation Plugin'
    render_template = 'navigation.html'

    def render(self, context, instance, placeholder):
        return context


plugin_pool.register_plugin(NavigationPlugin)
