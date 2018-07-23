# -*- coding: utf-8 -*-
"""OpenID-Connect Issuer discoverying
http://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata"""
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from plone import api
from plone.app.testing import PLONE_SITE_ID
from plone.oidc.oic import Client
from plone.oidc.testing import PLONE_OIDC_REST_FUNCTIONAL_TESTING

import unittest


__author__ = 'Md Nazrul Islam<email2nazrul@gmail.com>'


class TestWorkflows(unittest.TestCase):
    """ """
    layer = PLONE_OIDC_REST_FUNCTIONAL_TESTING

    def setUp(self):
        """ """
        self.portal = self.layer['portal']

    def test_provider_metadata_discovery(self):
        """ """
        client = Client(client_authn_method=CLIENT_AUTHN_METHOD, site_root=PLONE_SITE_ID)
        client.discover(self.portal.portal_url())
