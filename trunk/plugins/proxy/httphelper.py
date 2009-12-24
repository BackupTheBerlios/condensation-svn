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


HTTP_STATUS_DESCRIPTION = {
    # Informational 1xx
    100: {
        'name': 'Continue',
        'definition': 'RFC 2616, Section 10.1.1',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.1.1',
    },
    101: {
        'name': 'Switching Protocols',
        'definition': 'RFC 2616, Section 10.1.2',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.1.2',
    },
    102: {
        'name': 'Processing',
        'definition': 'RFC 2518, Section 10.1',
        'definition-url': 'http://www.webdav.org/specs/rfc2518.html#STATUS_102',
    },
    # Successful 2xx
    200: {
        'name': 'OK',
        'definition': 'RFC 2616, Section 10.2.1',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1',
    },
    201: {
        'name': 'Created',
        'definition': 'RFC 2616, Section 10.2.2',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2',
    },
    202: {
        'name': 'Accepted',
        'definition': 'RFC 2616, Section 10.2.3',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3',
    },
    203: {
        'name': 'Non-Authoritative Information',
        'definition': 'RFC 2616, Section 10.2.4',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.4',
    },
    204: {
        'name': 'No Content',
        'definition': 'RFC 2616, Section 10.2.5',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5',
    },
    205: {
        'name': 'Reset Content',
        'definition': 'RFC 2616, Section 10.2.6',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.6',
    },
    206: {
        'name': 'Partial Content',
        'definition': 'RFC 2616, Section 10.2.7',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.7',
    },
    207: {
        'name': 'Multi-Status',
        'definition': 'RFC 2518, Section 10.2',
        'definition-url': 'http://www.webdav.org/specs/rfc2518.html#STATUS_207',
    },
    226: {
        'name': 'IM Used',
        'definition': 'RFC 3229, Section 10.4.1',
        'definition-url': 'http://tools.ietf.org/html/rfc3229.html#section-10.4.1',
    },
    # Redirection 3xx
    300: {
        'name': 'Multiple Choices',
        'definition': 'RFC 2616, Section 10.3.1',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.1',
    },
    301: {
        'name': 'Moved Permanently',
        'definition': 'RFC 2616, Section 10.3.2',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.2',
    },
    302: {
        'name': 'Found',
        'definition': 'RFC 2616, Section 10.3.3',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.3',
    },
    303: {
        'name': 'See Other',
        'definition': 'RFC 2616, Section 10.3.4',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.4',
    },
    304: {
        'name': 'Not Modified',
        'definition': 'RFC 2616, Section 10.3.5',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.5',
    },
    305: {
        'name': 'Use Proxy',
        'definition': 'RFC 2616, Section 10.3.6',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.6',
    },
    306: {
        'name': '(Unused)',
        'definition': 'RFC 2616, Section 10.3.7',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.7',
    },
    307: {
        'name': 'Temporary Redirect',
        'definition': 'RFC 2616, Section 10.3.8',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.9',
    },
    # Client Error 4xx
    400: {
        'name': 'Bad Request',
        'definition': 'RFC 2616, Section 10.4.1',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1',
    },
    401: {
        'name': 'Unauthorized',
        'definition': 'RFC 2616, Section 10.4.2',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2',
    },
    402: {
        'name': 'Payment Required',
        'definition': 'RFC 2616, Section 10.4.3',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.3',
    },
    403: {
        'name': 'Forbidden',
        'definition': 'RFC 2616, Section 10.4.4',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4',
    },
    404: {
        'name': 'Not Found',
        'definition': 'RFC 2616, Section 10.4.5',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5',
    },
    405: {
        'name': 'Method Not Allowed',
        'definition': 'RFC 2616, Section 10.4.6',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.6',
    },
    406: {
        'name': 'Not Acceptable',
        'definition': 'RFC 2616, Section 10.4.7',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7',
    },
    407: {
        'name': 'Proxy Authentication Required',
        'definition': 'RFC 2616, Section 10.4.8',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.8',
    },
    408: {
        'name': 'Request Timeout',
        'definition': 'RFC 2616, Section 10.4.9',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.9',
    },
    409: {
        'name': 'Conflict',
        'definition': 'RFC 2616, Section 10.4.10',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10',
    },
    410: {
        'name': 'Gone',
        'definition': 'RFC 2616, Section 10.4.11',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.11',
    },
    411: {
        'name': 'Length Required',
        'definition': 'RFC 2616, Section 10.4.12',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.12',
    },
    412: {
        'name': 'Precondition Failed',
        'definition': 'RFC 2616, Section 10.4.13',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.13',
    },
    413: {
        'name': 'Request Entity Too Large',
        'definition': 'RFC 2616, Section 10.4.14',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.14',
    },
    414: {
        'name': 'Request-URI Too Long',
        'definition': 'RFC 2616, Section 10.4.15',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.15',
    },
    415: {
        'name': 'Unsupported Media Type',
        'definition': 'RFC 2616, Section 10.4.16',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.16',
    },
    416: {
        'name': 'Requested Range Not Satisfiable',
        'definition': 'RFC 2616, Section 10.4.17',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.17',
    },
    417: {
        'name': 'Expectation Failed',
        'definition': 'RFC 2616, Section 10.4.18',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.18',
    },
    418: {
        'name': 'I\'m a teapot',
        'definition': 'RFC 2324, Section 2.3.2',
        'definition-url': 'http://tools.ietf.org/html/rfc2324#section-2.3.2',
    },
    422: {
        'name': 'Unprocessable Entity',
        'definition': 'RFC 4918, Section 11.2',
        'definition-url': 'http://tools.ietf.org/html/rfc4918#section-11.2',
    },
    423: {
        'name': 'Locked',
        'definition': 'RFC 4918, Section 11.3',
        'definition-url': 'http://tools.ietf.org/html/rfc4918#section-11.3',
    },
    424: {
        'name': 'Failed Dependency',
        'definition': 'RFC 4918, Section 11.4',
        'definition-url': 'http://tools.ietf.org/html/rfc4918#section-11.4',
    },
    425: {
        'name': 'Unordered Collection',
        'definition': 'WebDAV Advanced Collections Protocol (Draft), Section 7.2',
        'definition-url': 'http://tools.ietf.org/html/draft-ietf-webdav-collection-protocol-04#section-7.2',
    },
    426: {
        'name': 'Upgrade Required',
        'definition': 'RFC 2817, ',
        'definition-url': 'http://tools.ietf.org/html/rfc2817#section-6',
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
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1',
    },
    501: {
        'name': 'Not Implemented',
        'definition': 'RFC 2616, Section 10.5.2',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.2',
    },
    502: {
        'name': 'Bad Gateway',
        'definition': 'RFC 2616, Section 10.5.3',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.3',
    },
    503: {
        'name': 'Service Unavailable',
        'definition': 'RFC 2616, Section 10.5.4',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.4',
    },
    504: {
        'name': 'Gateway Timeout',
        'definition': 'RFC 2616, Section 10.5.5',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.5',
    },
    505: {
        'name': 'HTTP Version Not Supported',
        'definition': 'RFC 2616, Section 10.5.6',
        'definition-url': 'http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.6',
    },
    506: {
        'name': 'Loop Detected',
        'definition': 'WebDAV Advanced Collections Protocol (Draft), Section 7.1',
        'definition-url': 'http://tools.ietf.org/html/draft-ietf-webdav-collection-protocol-04#section-7.1',
    },
    507: {
        'name': 'Insufficient Storage',
        'definition': 'RFC 4918, Section 11.5',
        'definition-url': 'http://tools.ietf.org/html/rfc4918#section-11.5',
    },
    510: {
        'name': 'Not Extended',
        'definition': 'RFC 2774 (Experimental), Section 7',
        'definition-url': 'http://tools.ietf.org/html/rfc2774#section-7',
    },

}


HTTP_GENERAL_HEADERS = {
    'Cache-Control': {
        'definition': 'RFC 2616, Section 14.9',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.9',
    },
    'Connection': {
        'definition': 'RFC 2616, Section 14.10',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.10',
    },
    'Date': {
        'definition': 'RFC 2616, Section 14.18',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.18',
    },
    'Pragma': {
        'definition': 'RFC 2616, Section 14.32',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.32',
    },
    'Trailer': {
        'definition': 'RFC 2616, Section 14.40',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.40',
    },
    'Transfer-Encoding': {
        'definition': 'RFC 2616, Section 14.41',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.41',
    },
    'Upgrade': {
        'definition': 'RFC 2616, Section 14.42',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.42',
    },
    'Via': {
        'definition': 'RFC 2616, Section 14.45',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.45',
    },
    'Warning': {
        'definition': 'RFC 2616, Section 14.46',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.46',
    },
}


HTTP_REQUEST_HEADERS = {
    'Accept': {
        'definition': 'RFC 2616, Section 14.1',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.1',
    },
    'Accept-Charset': {
        'definition': 'RFC 2616, Section 14.2',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.2',
    },
    'Accept-Encoding': {
        'definition': 'RFC 2616, Section 14.3',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.3',
    },
    'Accept-Language': {
        'definition': 'RFC 2616, Section 14.4',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.4',
    },
    'Authorization': {
        'definition': 'RFC 2616, Section 14.8',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.8',
    },
    'Expect': {
        'definition': 'RFC 2616, Section 14.20',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.20',
    },
    'From': {
        'definition': 'RFC 2616, Section 14.22',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.22',
    },
    'Host': {
        'definition': 'RFC 2616, Section 14.23',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.23',
    },
    'If-Match': {
        'definition': 'RFC 2616, Section 14.24',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.24',
    },
    'If-Modified-Since': {
        'definition': 'RFC 2616, Section 14.25',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.25',
    },
    'If-None-Match': {
        'definition': 'RFC 2616, Section 14.26',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.26',
    },
    'If-Range': {
        'definition': 'RFC 2616, Section 14.27',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.27',
    },
    'If-Unmodified-Since': {
        'definition': 'RFC 2616, Section 14.28',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.28',
    },
    'Max-Forwards': {
        'definition': 'RFC 2616, Section 14.31',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.31',
    },
    'Proxy-Authorization': {
        'definition': 'RFC 2616, Section 14.34',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.34',
    },
    'Range': {
        'definition': 'RFC 2616, Section 14.35',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.35',
    },
    'Referer': {
        'definition': 'RFC 2616, Section 14.36',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.36',
    },
    'TE': {
        'definition': 'RFC 2616, Section 14.39',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.39',
    },
    'User-Agent': {
        'definition': 'RFC 2616, Section 14.43',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.43',
    },
}


HTTP_RESPONSE_HEADERS = {
    'Accept-Ranges': {
        'definition': 'RFC 2616, Section 14.5',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.5',
    },
    'Age': {
        'definition': 'RFC 2616, Section 14.6',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.6',
    },
    'ETag': {
        'definition': 'RFC 2616, Section 14.19',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.19',
    },
    'Location': {
        'definition': 'RFC 2616, Section 14.30',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.30',
    },
    'Proxy-Authenticate': {
        'definition': 'RFC 2616, Section 14.33',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.33',
    },
    'Retry-After': {
        'definition': 'RFC 2616, Section 14.37',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.37',
    },
    'Server': {
        'definition': 'RFC 2616, Section 14.38',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.38',
    },
    'Vary': {
        'definition': 'RFC 2616, Section 14.44',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.44',
    },
    'WWW-Authenticate': {
        'definition': 'RFC 2616, Section 14.47',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.47',
    },
}


HTTP_ENTITY_HEADERS = {
    'Allow': {
        'definition': 'RFC 2616, Section 14.7',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.7',
    },
    'Content-Encoding': {
        'definition': 'RFC 2616, Section 14.11',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.11',
    },
    'Content-Language': {
        'definition': 'RFC 2616, Section 14.12',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.12',
    },
    'Content-Length': {
        'definition': 'RFC 2616, Section 14.13',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.13',
    },
    'Content-Location': {
        'definition': 'RFC 2616, Section 14.14',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.14',
    },
    'Content-MD5': {
        'definition': 'RFC 2616, Section 14.15',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.15',
    },
    'Content-Range': {
        'definition': 'RFC 2616, Section 14.16',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.16',
    },
    'Content-Type': {
        'definition': 'RFC 2616, Section 14.17',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.17',
    },
    'Expires': {
        'definition': 'RFC 2616, Section 14.21',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.21',
    },
    'Last-Modified': {
        'definition': 'RFC 2616, Section 14.29',
        'definition-url': 'http://tools.ietf.org/html/rfc2616#section-14.29',
    },
}


if __name__ == "__main__":
    print "<html><head></head><body>"
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

    # general headers
    headers = HTTP_GENERAL_HEADERS.keys()
    headers.sort()
    print "<h2>General Headers</h2>"
    print "<table><tbody>"
    for header in headers:
        info = HTTP_GENERAL_HEADERS[header]
        print ("<tr><td>%s</td><td><a href=\"%s\">%s</a></td></tr>" %
            (header, info['definition-url'], info['definition']))
    print "</tbody></table>"

    # request headers
    headers = HTTP_REQUEST_HEADERS.keys()
    headers.sort()
    print "<h2>Request Headers</h2>"
    print "<table><tbody>"
    for header in headers:
        info = HTTP_REQUEST_HEADERS[header]
        print ("<tr><td>%s</td><td><a href=\"%s\">%s</a></td></tr>" %
            (header, info['definition-url'], info['definition']))
    print "</tbody></table>"


    # response headers
    headers = HTTP_RESPONSE_HEADERS.keys()
    headers.sort()
    print "<h2>Response Headers</h2>"
    print "<table><tbody>"
    for header in headers:
        info = HTTP_RESPONSE_HEADERS[header]
        print ("<tr><td>%s</td><td><a href=\"%s\">%s</a></td></tr>" %
            (header, info['definition-url'], info['definition']))
    print "</tbody></table>"


    # entity headers
    headers = HTTP_ENTITY_HEADERS.keys()
    headers.sort()
    print "<h2>Entity Headers</h2>"
    print "<table><tbody>"
    for header in headers:
        info = HTTP_ENTITY_HEADERS[header]
        print ("<tr><td>%s</td><td><a href=\"%s\">%s</a></td></tr>" %
            (header, info['definition-url'], info['definition']))
    print "</tbody></table>"


    # finish
    print "</body></html>"