data = open('input.txt').read()

workflows, parts = data.split('\n\n')

workflows = workflows.splitlines()
parts = parts.splitlines()

print(workflows)