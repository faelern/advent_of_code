data = open('input.txt').read()

workflows, parts = data.split('\n\n')

workflows = workflows.splitlines()
parts = parts.splitlines()

parts_dicts = []

for i, part in enumerate(parts):
    parts_dicts.append({})
    part = part[1:-1].split(',')
    for cat in part:
        key = cat[0]
        value = int(cat[2:])
        parts_dicts[i][key] = value

parts = parts_dicts

wfs = []

for i, workflow in enumerate(workflows):
    name, workflow = workflow.split('{')
    workflow = workflow[:-1].split(',')
    temp_wf = []
    for rule in workflow:
        if '<' not in rule and '>' not in rule:
            next_wf = rule
            temp_rule = next_wf
        else:
            key = rule[0]
            operator = rule[1]
            temp = rule[2:].split(':')
            value = int(temp[0])
            next_wf = temp[1]
            temp_rule = [key, operator, value, next_wf]
        temp_wf.append(temp_rule)
    wfs.append(temp_wf)

