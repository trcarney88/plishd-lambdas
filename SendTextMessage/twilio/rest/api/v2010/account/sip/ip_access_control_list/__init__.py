# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address import IpAddressList


class IpAccessControlListList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the IpAccessControlListList

        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListList
        """
        super(IpAccessControlListList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams IpAccessControlListInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists IpAccessControlListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return IpAccessControlListPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return IpAccessControlListPage(self._version, response, self._solution)

    def create(self, friendly_name):
        """
        Create the IpAccessControlListInstance

        :param unicode friendly_name: A human readable description of this resource

        :returns: The created IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def get(self, sid):
        """
        Constructs a IpAccessControlListContext

        :param sid: A string that identifies the resource to fetch

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        return IpAccessControlListContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a IpAccessControlListContext

        :param sid: A string that identifies the resource to fetch

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        return IpAccessControlListContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAccessControlListList>'


class IpAccessControlListPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the IpAccessControlListPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        """
        super(IpAccessControlListPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpAccessControlListInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAccessControlListPage>'


class IpAccessControlListContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the IpAccessControlListContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account
        :param sid: A string that identifies the resource to fetch

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        super(IpAccessControlListContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json'.format(**self._solution)

        # Dependents
        self._ip_addresses = None

    def fetch(self):
        """
        Fetch the IpAccessControlListInstance

        :returns: The fetched IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name):
        """
        Update the IpAccessControlListInstance

        :param unicode friendly_name: A human readable description of this resource

        :returns: The updated IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the IpAccessControlListInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def ip_addresses(self):
        """
        Access the ip_addresses

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        """
        if self._ip_addresses is None:
            self._ip_addresses = IpAddressList(
                self._version,
                account_sid=self._solution['account_sid'],
                ip_access_control_list_sid=self._solution['sid'],
            )
        return self._ip_addresses

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAccessControlListContext {}>'.format(context)


class IpAccessControlListInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the IpAccessControlListInstance

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        super(IpAccessControlListInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'subresource_uris': payload.get('subresource_uris'),
            'uri': payload.get('uri'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: IpAccessControlListContext for this IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        if self._context is None:
            self._context = IpAccessControlListContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def subresource_uris(self):
        """
        :returns: The IP addresses associated with this resource.
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch the IpAccessControlListInstance

        :returns: The fetched IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name):
        """
        Update the IpAccessControlListInstance

        :param unicode friendly_name: A human readable description of this resource

        :returns: The updated IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        return self._proxy.update(friendly_name, )

    def delete(self):
        """
        Deletes the IpAccessControlListInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def ip_addresses(self):
        """
        Access the ip_addresses

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        """
        return self._proxy.ip_addresses

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAccessControlListInstance {}>'.format(context)
