"""Perform introspection tests."""
from lib.utils import graph_query


def introspection(url, proxy, headers):
  """Run introspection."""
  result = False

  q = 'query { __schema { types { name fields { name } } } }'

  gql_response = graph_query(url, proxies=proxy, headers=headers, payload=q)
  try:
    if gql_response['data']['__schema']['types']:
      result = True
  except:
    pass

  return result
