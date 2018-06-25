from six.moves import urllib
import json


class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def executeMultiple(self, queryfn, variables=None):
        mutationQuery = 'mutation {'
        for (i, var) in enumerate(variables):
            inserted = queryfn(var)
            mutationQuery += f'mut{i}:{inserted}'
        mutationQuery += '}'
        return self._send(mutationQuery, None)

    def inject_token(self, token):
        self.token = token

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers['Authorization'] = '{}'.format(self.token)

        req = urllib.request.Request(
            self.endpoint, json.dumps(data).encode('utf-8'), headers)

        try:
            response = urllib.request.urlopen(req)
            return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e