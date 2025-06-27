import os
import json

queries = list()
for filename in os.listdir('queries/'):
    with open('queries/' + filename, 'r') as f:
        lines = f.readlines()
        # find the line starting with '#title:'
        title = None
        tags = []
        body = ''
        for line in lines:
            if line.startswith('#title:'):
                title = line[len('#title:'):].strip()
            elif line.startswith('#tags:'):
                tags = [tag.strip() for tag in line[len('#tags:'):].split(',')]

            # finally, the body should consist of everything minus the line starting with '#tags:'
            if not line.startswith('#tags:'):
                body += line

        query = {}
        query['title'] = title
        query['tags'] = tags
        query['body'] = body

        queries.append(query)

with open('queries.json', 'w') as outfile:
    json.dump(queries, outfile)

print('Done generating JSON')
