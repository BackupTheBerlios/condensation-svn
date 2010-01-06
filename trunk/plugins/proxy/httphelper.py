############################################################################
#    Copyright (C) 2009 by Thomas Hille                                    #
#    thomas.hille@nightsabers.org                                          #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

HTTP_METHODS = {
    'CONNECT': {
        'definition': 'RFC 2616, Section 9.9',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.9',
    },
    'COPY': {
        'definition': 'RFC 2518, Section 8.8',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.8',
    },
    'DELETE': {
        'definition': 'RFC 2616, Section 9.7',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.7',
    },
    'GET': {
        'definition': 'RFC 2616, Section 9.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.3',
    },
    'HEAD': {
        'definition': 'RFC 2616, Section 9.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.4',
    },
    'LOCK': {
        'definition': 'RFC 2518, Section 8.10',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.10',
    },
    'MKCOL': {
        'definition': 'RFC 2518, Section 8.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.3',
    },
    'MOVE': {
        'definition': 'RFC 2518, Section 8.9',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.9',
    },
    'OPTIONS': {
        'definition': 'RFC 2616, Section 9.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.2',
    },
    'POST': {
        'definition': 'RFC 2616, Section 9.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.5',
    },
    'PROPFIND': {
        'definition': 'RFC 2518, Section 8.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.1',
    },
    'PROPPATCH': {
        'definition': 'RFC 2518, Section 8.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.2',
    },
    'PUT': {
        'definition': 'RFC 2616, Section 9.6',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.6',
    },
    'TRACE': {
        'definition': 'RFC 2616, Section 9.8',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-9.8',
    },
    'UNLOCK': {
        'definition': 'RFC 2518, Section 8.11',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2518.html#section-8.11',
    },
}


HTTP_STATUS_DESCRIPTION = {
    # Informational 1xx
    100: {
        'name': 'Continue',
        'definition': 'RFC 2616, Section 10.1.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.1.1',
    },
    101: {
        'name': 'Switching Protocols',
        'definition': 'RFC 2616, Section 10.1.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.1.2',
    },
    102: {
        'name': 'Processing',
        'definition': 'RFC 2518, Section 10.1',
        'definition-url': 'http://www.webdav.org/specs/rfc2518#STATUS_102',
    },
    # Successful 2xx
    200: {
        'name': 'OK',
        'definition': 'RFC 2616, Section 10.2.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.1',
    },
    201: {
        'name': 'Created',
        'definition': 'RFC 2616, Section 10.2.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.2',
    },
    202: {
        'name': 'Accepted',
        'definition': 'RFC 2616, Section 10.2.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.3',
    },
    203: {
        'name': 'Non-Authoritative Information',
        'definition': 'RFC 2616, Section 10.2.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.4',
    },
    204: {
        'name': 'No Content',
        'definition': 'RFC 2616, Section 10.2.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.5',
    },
    205: {
        'name': 'Reset Content',
        'definition': 'RFC 2616, Section 10.2.6',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.6',
    },
    206: {
        'name': 'Partial Content',
        'definition': 'RFC 2616, Section 10.2.7',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.2.7',
    },
    207: {
        'name': 'Multi-Status',
        'definition': 'RFC 2518, Section 10.2',
        'definition-url': 'http://www.webdav.org/specs/rfc2518#STATUS_207',
    },
    226: {
        'name': 'IM Used',
        'definition': 'RFC 3229, Section 10.4.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc3229.html#section-10.4.1',
    },
    # Redirection 3xx
    300: {
        'name': 'Multiple Choices',
        'definition': 'RFC 2616, Section 10.3.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.1',
    },
    301: {
        'name': 'Moved Permanently',
        'definition': 'RFC 2616, Section 10.3.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.2',
    },
    302: {
        'name': 'Found',
        'definition': 'RFC 2616, Section 10.3.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.3',
    },
    303: {
        'name': 'See Other',
        'definition': 'RFC 2616, Section 10.3.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.4',
    },
    304: {
        'name': 'Not Modified',
        'definition': 'RFC 2616, Section 10.3.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.5',
    },
    305: {
        'name': 'Use Proxy',
        'definition': 'RFC 2616, Section 10.3.6',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.6',
    },
    306: {
        'name': '(Unused)',
        'definition': 'RFC 2616, Section 10.3.7',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.7',
    },
    307: {
        'name': 'Temporary Redirect',
        'definition': 'RFC 2616, Section 10.3.8',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.3.9',
    },
    # Client Error 4xx
    400: {
        'name': 'Bad Request',
        'definition': 'RFC 2616, Section 10.4.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.1',
    },
    401: {
        'name': 'Unauthorized',
        'definition': 'RFC 2616, Section 10.4.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.2',
    },
    402: {
        'name': 'Payment Required',
        'definition': 'RFC 2616, Section 10.4.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.3',
    },
    403: {
        'name': 'Forbidden',
        'definition': 'RFC 2616, Section 10.4.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.4',
    },
    404: {
        'name': 'Not Found',
        'definition': 'RFC 2616, Section 10.4.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.5',
    },
    405: {
        'name': 'Method Not Allowed',
        'definition': 'RFC 2616, Section 10.4.6',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.6',
    },
    406: {
        'name': 'Not Acceptable',
        'definition': 'RFC 2616, Section 10.4.7',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.7',
    },
    407: {
        'name': 'Proxy Authentication Required',
        'definition': 'RFC 2616, Section 10.4.8',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.8',
    },
    408: {
        'name': 'Request Timeout',
        'definition': 'RFC 2616, Section 10.4.9',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.9',
    },
    409: {
        'name': 'Conflict',
        'definition': 'RFC 2616, Section 10.4.10',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.10',
    },
    410: {
        'name': 'Gone',
        'definition': 'RFC 2616, Section 10.4.11',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.11',
    },
    411: {
        'name': 'Length Required',
        'definition': 'RFC 2616, Section 10.4.12',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.12',
    },
    412: {
        'name': 'Precondition Failed',
        'definition': 'RFC 2616, Section 10.4.13',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.13',
    },
    413: {
        'name': 'Request Entity Too Large',
        'definition': 'RFC 2616, Section 10.4.14',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.14',
    },
    414: {
        'name': 'Request-URI Too Long',
        'definition': 'RFC 2616, Section 10.4.15',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.15',
    },
    415: {
        'name': 'Unsupported Media Type',
        'definition': 'RFC 2616, Section 10.4.16',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.16',
    },
    416: {
        'name': 'Requested Range Not Satisfiable',
        'definition': 'RFC 2616, Section 10.4.17',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.17',
    },
    417: {
        'name': 'Expectation Failed',
        'definition': 'RFC 2616, Section 10.4.18',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.4.18',
    },
    418: {
        'name': 'I\'m a teapot',
        'definition': 'RFC 2324, Section 2.3.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2324.html#section-2.3.2',
    },
    422: {
        'name': 'Unprocessable Entity',
        'definition': 'RFC 4918, Section 11.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc4918.html#section-11.2',
    },
    423: {
        'name': 'Locked',
        'definition': 'RFC 4918, Section 11.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc4918.html#section-11.3',
    },
    424: {
        'name': 'Failed Dependency',
        'definition': 'RFC 4918, Section 11.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc4918.html#section-11.4',
    },
    425: {
        'name': 'Unordered Collection',
        'definition': 'WebDAV Advanced Collections Protocol (Draft), Section 7.2',
        'definition-url': 'http://tools.ietf.org/html/draft-ietf-webdav-collection-protocol-04#section-7.2',
    },
    426: {
        'name': 'Upgrade Required',
        'definition': 'RFC 2817, ',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2817.html#section-6',
    },
    449: {
        'name': 'Microsoft Crap',
        'definition': 'unknown',
        'definition-url': '',
    },
    450: {
        'name': 'Microsoft Crap',
        'definition': 'unknown',
        'definition-url': '',
    },
    # Server Error 5xx
    500: {
        'name': 'Internal Server Error',
        'definition': 'RFC 2616, Section 10.5.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.5.1',
    },
    501: {
        'name': 'Not Implemented',
        'definition': 'RFC 2616, Section 10.5.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.5.2',
    },
    502: {
        'name': 'Bad Gateway',
        'definition': 'RFC 2616, Section 10.5.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.5.3',
    },
    503: {
        'name': 'Service Unavailable',
        'definition': 'RFC 2616, Section 10.5.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.5.4',
    },
    504: {
        'name': 'Gateway Timeout',
        'definition': 'RFC 2616, Section 10.5.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.5.5',
    },
    505: {
        'name': 'HTTP Version Not Supported',
        'definition': 'RFC 2616, Section 10.5.6',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-10.5.6',
    },
    506: {
        'name': 'Loop Detected',
        'definition': 'WebDAV Advanced Collections Protocol (Draft), Section 7.1',
        'definition-url': 'http://tools.ietf.org/html/draft-ietf-webdav-collection-protocol-04#section-7.1',
    },
    507: {
        'name': 'Insufficient Storage',
        'definition': 'RFC 4918, Section 11.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc4918.html#section-11.5',
    },
    510: {
        'name': 'Not Extended',
        'definition': 'RFC 2774 (Experimental), Section 7',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2774.html#section-7',
    },

}


HTTP_GENERAL_HEADERS = {
    'Cache-Control': {
        'short-description': 'The Cache-Control general-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain.',
        'definition': 'RFC 2616, Section 14.9',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.9',
    },
    'Connection': {
        'short-description': 'The Connection general-header field allows the sender to specify options that are desired for that particular connection and MUST NOT be communicated by proxies over further connections.',
        'definition': 'RFC 2616, Section 14.10',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.10',
    },
    'Date': {
        'short-description': 'The Date general-header field represents the date and time at which the message was originated, having the same semantics as orig-date in RFC 822.',
        'definition': 'RFC 2616, Section 14.18',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.18',
    },
    'Pragma': {
        'short-description': 'The Pragma general-header field is used to include implementation-specific directives that might apply to any recipient along the request/response chain.',
        'definition': 'RFC 2616, Section 14.32',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.32',
    },
    'Trailer': {
        'short-description': 'The Trailer general field value indicates that the given set of header fields is present in the trailer of a message encoded with chunked transfer-coding.',
        'definition': 'RFC 2616, Section 14.40',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.40',
    },
    'Transfer-Encoding': {
        'short-description': 'The Transfer-Encoding general-header field indicates what (if any) type of transformation has been applied to the message body in order to safely transfer it between the sender and the recipient.',
        'definition': 'RFC 2616, Section 14.41',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.41',
    },
    'Upgrade': {
        'short-description': 'The Upgrade general-header allows the client to specify what additional communication protocols it supports and would like to use if the server finds it appropriate to switch protocols.',
        'definition': 'RFC 2616, Section 14.42',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.42',
    },
    'Via': {
        'short-description': 'The Via general-header field MUST be used by gateways and proxies to indicate the intermediate protocols and recipients between the user agent and the server on requests, and between the origin server and the client on responses.',
        'definition': 'RFC 2616, Section 14.45',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.45',
    },
    'Warning': {
        'short-description': 'The Warning general-header field is used to carry additional information about the status or transformation of a message which might not be reflected in the message.',
        'definition': 'RFC 2616, Section 14.46',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.46',
    },
}


HTTP_REQUEST_HEADERS = {
    'Accept': {
        'short-description': 'The Accept request-header field can be used to specify certain media types which are acceptable for the response.',
        'definition': 'RFC 2616, Section 14.1',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.1',
    },
    'Accept-Charset': {
        'short-description': 'The Accept-Charset request-header field can be used to indicate what character sets are acceptable for the response.',
        'definition': 'RFC 2616, Section 14.2',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.2',
    },
    'Accept-Encoding': {
        'short-description': 'The Accept-Encoding request-header field is similar to Accept, but restricts the content-codings that are acceptable in the response.',
        'definition': 'RFC 2616, Section 14.3',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.3',
    },
    'Accept-Language': {
        'short-description': 'The Accept-Language request-header field is similar to Accept, but restricts the set of natural languages that are preferred as a response to the request.',
        'definition': 'RFC 2616, Section 14.4',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.4',
    },
    'Authorization': {
        'short-description': 'A user agent that wishes to authenticate itself with a server--usually, but not necessarily, after receiving a 401 response--does so by including an Authorization request-header field with the request.',
        'definition': 'RFC 2616, Section 14.8',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.8',
    },
    'Expect': {
        'short-description': 'The Expect request-header field is used to indicate that particular server behaviors are required by the client.',
        'definition': 'RFC 2616, Section 14.20',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.20',
    },
    'From': {
        'short-description': 'The From request-header field, if given, SHOULD contain an Internet e-mail address for the human user who controls the requesting user agent.',
        'definition': 'RFC 2616, Section 14.22',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.22',
    },
    'Host': {
        'short-description': 'The Host request-header field specifies the Internet host and port number of the resource being requested, as obtained from the original URI given by the user or referring resource (generally an HTTP URL)',
        'definition': 'RFC 2616, Section 14.23',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.23',
    },
    'If-Match': {
        'short-description': 'The If-Match request-header field is used with a method to make it conditional.',
        'definition': 'RFC 2616, Section 14.24',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.24',
    },
    'If-Modified-Since': {
        'short-description': 'The If-Modified-Since request-header field is used with a method to make it conditional: if the requested variant has not been modified since the time specified in this field, an entity will not be returned from the server;',
        'definition': 'RFC 2616, Section 14.25',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.25',
    },
    'If-None-Match': {
        'short-description': 'The If-None-Match request-header field is used with a method to make it conditional.',
        'definition': 'RFC 2616, Section 14.26',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.26',
    },
    'If-Range': {
        'short-description': 'If a client has a partial copy of an entity in its cache, and wishes to have an up-to-date copy of the entire entity in its cache, it could use the Range request-header with a conditional GET',
        'definition': 'RFC 2616, Section 14.27',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.27',
    },
    'If-Unmodified-Since': {
        'short-description': 'The If-Unmodified-Since request-header field is used with a method to make it conditional.',
        'definition': 'RFC 2616, Section 14.28',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.28',
    },
    'Max-Forwards': {
        'short-description': 'The Max-Forwards request-header field provides a mechanism with the TRACE and OPTIONS methods to limit the number of proxies or gateways that can forward the request to the next inbound server.',
        'definition': 'RFC 2616, Section 14.31',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.31',
    },
    'Proxy-Authorization': {
        'short-description': 'The Proxy-Authorization request-header field allows the client to identify itself (or its user) to a proxy which requires authentication.',
        'definition': 'RFC 2616, Section 14.34',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.34',
    },
    'Range': {
        'short-description': 'HTTP retrieval requests using conditional or unconditional GET methods MAY request one or more sub-ranges of the entity, instead of the entire entity, using the Range request header.',
        'definition': 'RFC 2616, Section 14.35',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.35',
    },
    'Referer': {
        'short-description': 'The Referer[sic] request-header field allows the client to specify the address (URI) of the resource from which the Request-URI was obtained (the "referrer", although the header field is misspelled.)',
        'definition': 'RFC 2616, Section 14.36',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.36',
    },
    'TE': {
        'short-description': 'The TE request-header field indicates what extension transfer-codings it is willing to accept in the response and whether or not it is willing to accept trailer fields in a chunked transfer-coding.',
        'definition': 'RFC 2616, Section 14.39',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.39',
    },
    'User-Agent': {
        'short-description': 'The User-Agent request-header field contains information about the user agent originating the request.',
        'definition': 'RFC 2616, Section 14.43',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.43',
    },
}


HTTP_RESPONSE_HEADERS = {
    'Accept-Ranges': {
        'short-description': 'The Accept-Ranges response-header field allows the server to indicate its acceptance of range requests for a resource.',
        'definition': 'RFC 2616, Section 14.5',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.5',
    },
    'Age': {
        'short-description': 'The Age response-header field conveys the sender\'s estimate of the amount of time since the response (or its revalidation) was generated at the origin server.',
        'definition': 'RFC 2616, Section 14.6',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.6',
    },
    'ETag': {
        'short-description': 'The ETag response-header field provides the current value of the entity tag for the requested variant.',
        'definition': 'RFC 2616, Section 14.19',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.19',
    },
    'Location': {
        'short-description': 'The Location response-header field is used to redirect the recipient to a location other than the Request-URI for completion of the request or identification of a new resource.',
        'definition': 'RFC 2616, Section 14.30',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.30',
    },
    'Proxy-Authenticate': {
        'short-description': 'The Proxy-Authenticate response-header field MUST be included as part of a 407 (Proxy Authentication Required) response.',
        'definition': 'RFC 2616, Section 14.33',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.33',
    },
    'Retry-After': {
        'short-description': 'The Retry-After response-header field can be used with a 503 (Service Unavailable) response to indicate how long the service is expected to be unavailable to the requesting client.',
        'definition': 'RFC 2616, Section 14.37',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.37',
    },
    'Server': {
        'short-description': 'The Server response-header field contains information about the software used by the origin server to handle the request.',
        'definition': 'RFC 2616, Section 14.38',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.38',
    },
    'Vary': {
        'short-description': 'The Vary field value indicates the set of request-header fields that fully determines, while the response is fresh, whether a cache is permitted to use the response to reply to a subsequent request without revalidation.',
        'definition': 'RFC 2616, Section 14.44',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.44',
    },
    'WWW-Authenticate': {
        'short-description': 'The WWW-Authenticate response-header field MUST be included in 401 (Unauthorized) response messages.',
        'definition': 'RFC 2616, Section 14.47',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.47',
    },
}


HTTP_ENTITY_HEADERS = {
    'Allow': {
        'short-description': 'The Allow entity-header field lists the set of methods supported by the resource identified by the Request-URI.',
        'definition': 'RFC 2616, Section 14.7',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.7',
    },
    'Content-Encoding': {
        'short-description': 'The Content-Encoding entity-header field is used as a modifier to the media-type.',
        'definition': 'RFC 2616, Section 14.11',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.11',
    },
    'Content-Language': {
        'short-description': 'The Content-Language entity-header field describes the natural language(s) of the intended audience for the enclosed entity.',
        'definition': 'RFC 2616, Section 14.12',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.12',
    },
    'Content-Length': {
        'short-description': 'The Content-Length entity-header field indicates the size of the entity-body, in decimal number of OCTETs, sent to the recipient or, in the case of the HEAD method, the size of the entity-body that would have been sent had the request been a GET.',
        'definition': 'RFC 2616, Section 14.13',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.13',
    },
    'Content-Location': {
        'short-description': 'The Content-Location entity-header field MAY be used to supply the resource location for the entity enclosed in the message when that entity is accessible from a location separate from the requested resource\'s URI.',
        'definition': 'RFC 2616, Section 14.14',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.14',
    },
    'Content-MD5': {
        'short-description': 'The Content-MD5 entity-header field, as defined in RFC 1864 [23], is an MD5 digest of the entity-body for the purpose of providing an end-to-end message integrity check (MIC) of the entity-body.',
        'definition': 'RFC 2616, Section 14.15',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.15',
    },
    'Content-Range': {
        'short-description': 'The Content-Range entity-header is sent with a partial entity-body to specify where in the full entity-body the partial body should be applied.',
        'definition': 'RFC 2616, Section 14.16',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.16',
    },
    'Content-Type': {
        'short-description': 'The Content-Type entity-header field indicates the media type of the entity-body sent to the recipient or, in the case of the HEAD method, the media type that would have been sent had the request been a GET.',
        'definition': 'RFC 2616, Section 14.17',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.17',
    },
    'Expires': {
        'short-description': 'The Expires entity-header field gives the date/time after which the response is considered stale.',
        'definition': 'RFC 2616, Section 14.21',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.21',
    },
    'Last-Modified': {
        'short-description': 'The Last-Modified entity-header field indicates the date and time at which the origin server believes the variant was last modified.',
        'definition': 'RFC 2616, Section 14.29',
        'definition-url': 'http://www.condensation-hq.org/docs/rfcs/rfc2616.html#section-14.29',
    },
}


if __name__ == "__main__":

    def print_headers(title, header_definition):
        headers = header_definition.keys()
        headers.sort()
        print "<h3>%s</h3>" % title
        print '<table>'
        print '<thead><tr><th nowrap="nowrap" scope="col" style="text-align: left;">Name</th><th nowrap="nowrap" scope="col" style="text-align: left;">Definition</th><th scope="col" style="text-align: left;">Description</th></tr></thead>'
        print '<tbody>'
        for header in headers:
            info = header_definition[header]
            print ('<tr><td nowrap="nowrap">%s</td><td nowrap="nowrap"><a href=\"%s\">%s</a></td><td>%s</td></tr>' %
                (header, info['definition-url'], info['definition'], info['short-description']))
        print "</tbody></table>"
        print "<p>&nbsp;</p>"


    print "<html><head></head><body>"
    # methods
    methods = HTTP_METHODS.keys()
    methods.sort()
    print "<h2>Methods</h2>"
    print "<table><tbody>"
    for method in methods:
        info = HTTP_METHODS[method]
        print ("<tr><td>%s</td><td><a href=\"%s\">%s</a></td></tr>" %
            (method, info['definition-url'], info['definition']))
    print "</tbody></table>"
    print "<p>&nbsp;</p>"

    # status codes
    codes = HTTP_STATUS_DESCRIPTION.keys()
    codes.sort()
    print "<h2>Status Codes</h2>"
    print "<table><tbody>"
    for code in codes:
        info = HTTP_STATUS_DESCRIPTION[code]
        print ("<tr><td>%i</td><td>%s</td><td><a href=\"%s\">%s</a></td></tr>" %
            (code, info['name'], info['definition-url'], info['definition']))
    print "</tbody></table>"
    print "<p>&nbsp;</p>"

    print "<h2>Headers</h2>"
    print "<p>&nbsp;</p>"
    print_headers('General Headers', HTTP_GENERAL_HEADERS)
    print_headers('Request Headers', HTTP_REQUEST_HEADERS)
    print_headers('Response Headers', HTTP_RESPONSE_HEADERS)
    print_headers('Entity Headers', HTTP_ENTITY_HEADERS)

    # finish
    print "</body></html>"