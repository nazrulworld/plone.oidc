# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.vdexvocabulary.vocabulary import VdexVocabulary
from plone import api
from plone.oidc.testing import PLONE_OIDC_INTEGRATION_TESTING
from zope.component import getAllUtilitiesRegisteredFor
from zope.schema.interfaces import IVocabularyFactory

import os
import pkg_resources
import unittest


class TestRegisteredVocabularies(unittest.TestCase):
    """Test all vocabularies are defined at `./vocabularies` directory
    are actually available."""

    layer = PLONE_OIDC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_available_vocabularies(self):
        """ """
        vocab_identifiers = [x.vocab_identifier for x in getAllUtilitiesRegisteredFor(IVocabularyFactory)
                             if isinstance(x, VdexVocabulary)]

        product_path = pkg_resources.get_distribution('plone.oidc').location
        vocab_dir = os.path.join(product_path, 'plone', 'oidc', 'vocabularies')

        for root, dirs, files in os.walk(vocab_dir):

            for file_name in files:
                if not file_name.endswith('vdex'):
                    continue

                if file_name.split('.')[0] not in vocab_identifiers:
                    raise AssertionError(
                        '{0} should be as registered vdex vocabulary'.
                        format(file_name.split('.')[0])
                        )


