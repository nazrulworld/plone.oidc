# -*- coding: utf-8 -*-
# @Date    : 2017-10-12 19:34:26
# @Author  : Md Nazrul Islam (email2nazrul@gmail.com)
# @Link    : http://nazrul.me/
# @Version : $Id$
# All imports here
from plone import schema as ps
from plone.dexterity.content import Item
from plone.oidc import _
from plone.supermodel import model
from zope.interface import implementer
from zope.interface import Invalid
from zope.interface import invariant


__author__ = 'Md Nazrul Islam (email2nazrul@gmail.com)'


class ITokenCodeBase(model.Schema):
    """OID Map:
    :user_id = user
    :client_id = client"""
    user_id = ps.TextLine(
        title=_('User ID'),
        required=True
    )
    client_id = ps.TextLine(
        title=_('Client ID'),
        required=True
    )
    scope = ps.List(
        title=_('List of scopes'),
        required=False,
        value_type=ps.TextLine()
    )
    expire_at = ps.Datetime(
        title=_('Token Expire Date'),
        required=True
    )

    @invariant
    def validate_existance(self, data):
        """Validate if User and Application Is exists"""
        return Invalid('')


class IJWTBearerToken(ITokenCodeBase):
    """ """
    access_token = ps.TextLine(
        title=_('Access token')
        )
    refresh_token = ps.TextLine(
        title=_('Refresh token')
        )
    id_token = ps.JSONField(
        title=_('ID Token')
        )


@implementer(IJWTBearerToken)
class JWTBearerToken(Item):
    """ """
