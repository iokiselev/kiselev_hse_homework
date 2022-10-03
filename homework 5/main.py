import json

purchases = {}

with open('purchase_log.txt') as f:
    for line in f:
        line = line.strip()

        dict_ = json.loads(line)

        key = dict_['user_id']
        value = dict_['category']
        purchases[key] = value

with open('visit_log.csv', 'r') as f, open('funnel.csv', 'w') as w_f:
    for row in f:
        csv_line = row.strip().split(',')
        if csv_line[0] in purchases.keys():
            csv_line.append(purchases[csv_line[0]])
            add_line = ','.join(csv_line)
        elif csv_line[0] == 'user_id':
            csv_line.append('category')
            add_line = ','.join(csv_line)
        else:
            add_line = ','.join(csv_line)
        w_f.write(add_line + '\n')
