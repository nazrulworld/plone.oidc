# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 19:18:56
# @Author  : Md Nazrul Islam (email2nazrul@gmail.com)
# @Link    : http://nazrul.me/
# @Version : $Id$
# All imports here
from .webfinger import WebFinger
from oic.oic import Client as org_Client
from oic.utils.webfinger import OIC_ISSUER


__author__ = 'Md Nazrul Islam (email2nazrul@gmail.com)'

"""Some overrien/patched version of component from original https://pypi.org/project/oic """


class Client(org_Client):
    """overriden class oic.oic.Client"""
    def __init__(self, client_id=None,
                 client_prefs=None, client_authn_method=None, keyjar=None,
                 verify_ssl=True, config=None, client_cert=None,
                 requests_dir='requests',
                 site_root=None):

        super(Client, self).__init__(
            client_id=client_id,
            client_prefs=client_prefs,
            client_authn_method=client_authn_method,
            keyjar=keyjar,
            verify_ssl=verify_ssl,
            config=config,
            client_cert=client_cert,
            requests_dir=requests_dir)

        # set site root
        self.wf = WebFinger(OIC_ISSUER, site_root=site_root)
        self.wf.httpd = self
