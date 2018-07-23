# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 17:27:16
# @Author  : Md Nazrul Islam (email2nazrul@gmail.com)
# @Link    : http://nazrul.me/
# @Version : $Id$
# All imports here
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse
from zExceptions import BadRequest
from zExceptions import NotFound

__author__ = 'Md Nazrul Islam (email2nazrul@gmail.com)'


@implementer(IPublishTraverse)
class WebFingerView(BrowserView):
    """ """
    index = ViewPageTemplateFile('webfinger.pt')

    def __init__(self, context, request):
        """ """
        super(WebFingerView, self).__init__(context, request)

        self.params = []

    def publishTraverse(self, request, name):
        """sub paths aka params are added each one individually, those are provided
        after slash(/) of {portal url}/.well-known/"""
        self.params.append(name)
        return self

    @property
    def subpath(self):
        """ """
        if len(self.params) == 1:
            if self.params[0] == 'webfinger':
                return 'webfinger'
        return None

    def __call__(self):
        """ """
        # request validator
        if self.subpath is None:

            if api.env.debug_mode() or \
                    api.env.test_mode():
                raise BadRequest(
                    '`{0}` is not valid request URL. Request url must '
                    'contains single subpath `webfinger`. For example: '
                    '{1}/.well-known/webfinger'
                    .format(
                        self.request.getURL(),
                        self.context.portal_url())
                    )
            else:
                raise NotFound
        # request validation has been done

        return self.index()
