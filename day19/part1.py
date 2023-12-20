from tqdm import tqdm

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

wfs = {}

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
    wfs[name] = temp_wf

workflows = wfs


accepted = []
rejected = []

current_wf = 'in'
next_step = 0
rule_satisfied = False
sort = False

for part in tqdm(parts):
    # print(part)
    sort = False
    current_wf = 'in'
    while not sort:
        # print(current_wf)
        workflow = workflows[current_wf]
        rule_satisfied = False
        for rule in workflow[:-1]:
            if not rule_satisfied:
                key, operator, value, next_wf = rule
                if operator == '<':
                    delta = value - part[key]
                else:
                    delta = part[key] - value

                if delta > 0:
                    rule_satisfied = True
                    next_step = next_wf

        if not rule_satisfied:
            next_step = workflow[-1]
            rule_satisfied = True

        if next_step == 'A':
            accepted.append(part)
            sort = True

        elif next_step == 'R':
            rejected.append(part)
            sort = True
        else:
            current_wf = next_step


product = 0

for part in accepted:
    for value in part:
        product += part[value]

print(product)
