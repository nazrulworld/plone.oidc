# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 19:20:50
# @Author  : Md Nazrul Islam (email2nazrul@gmail.com)
# @Link    : http://nazrul.me/
# @Version : $Id$
# All imports here
from oic.utils.webfinger import WebFinger as org_WebFinger
from six.moves.urllib.parse import urlparse
from zope.interface import Invalid

import six


__author__ = 'Md Nazrul Islam (email2nazrul@gmail.com)'


class WebFinger(org_WebFinger):
    """ """
    def __init__(self, default_rel=None, httpd=None, site_root=None):
        """
        :param: plone/zope specific site path aka root
        """
        super(WebFinger, self).__init__(default_rel=default_rel, httpd=httpd)
        self._site_root = self.transform_site_root(site_root)

    def transform_site_root(self, site_root):
        """ """
        if site_root is None:
            site_root = '/'

        elif isinstance(site_root, six.string_types):
            if not site_root.startswith('/'):
                site_root = '/{0}'.format(site_root)

        elif isinstance(site_root, (list, tuple)):

            site_root = '/{0}/'.format('/'.join(site_root))
        else:
            raise Invalid('{0} is not supported data type as site_root'.format(site_root))

        return site_root

    @property
    def site_root(self):
        """ """
        return self._site_root

    @site_root.setter
    def site_root(self, value):
        """ """
        self._site_root = \
            self.transform_site_root(value)

    def query(self, resource, rel=None):
        """ """
        url = super(WebFinger, self).query(resource, rel=rel)
        parse_result = urlparse(url)
        base_path = parse_result.path

        if not base_path.startswith(self.site_root):

            new_base_path = '{0}{1}'.format(self.site_root, base_path)

            url = url.replace(base_path, new_base_path)
        host = parse_result.netloc
        if parse_result.scheme == 'https' and \
                (host.startswith('nohost') or
                 host.startswith('localhost') or
                 host.startswith('127.0.0.1')):

            parts = url.split('://')
            url = 'http://{0}'.format('://'.join(parts[1:]))

        return url
