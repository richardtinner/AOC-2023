lines = []
workflows = dict()
parts = []
accepted_parts = []
total_A = 0
total_R = 0

char_to_index = {'x': 0, 'm': 1, 'a': 2, 's': 3}
reverse_equality = {'>': '<', '<': '>'}
offset = {'>': 1, '<': -1}


def process_branch(action, branch):
    global total_A
    global total_R
    xmas = {'x': [], 'm': [], 'a': [], 's': []}
    for leaf in branch:
        xmas[leaf[0]].append((leaf[2], leaf[1]))

    for value in xmas.values():
        value.sort()

    xmas_total = {'x': 0, 'm': 0, 'a': 0, 's': 0}
    for key, value in xmas.items():
        if len(value) == 0:
            xmas_total[key] = 4000
        else:
            max_lt = 4001
            min_gt = 0
            for index, ineq in enumerate(value):
                if ineq[1] == '>' and ineq[0] > min_gt:
                    min_gt = ineq[0]
                elif ineq[1] == '<' and ineq[0] < max_lt:
                    max_lt = ineq[0]
            xmas_total[key] = max_lt - min_gt - 1

    final_total = 1
    for value in xmas_total.values():
        final_total *= value

    print(final_total)

    if action == 'A':
        total_A += final_total
    else:
        total_R += final_total

    return


def process_tree(workflow, branch):
    cnt = 0
    for step in workflows[workflow]:
        if step == 'A':
            print('A- ', branch)
            process_branch('A', branch)
        elif step == 'R':
            print('R- ', branch)
            process_branch('R', branch)
        elif step[1:2] == '>':
            next_workflow = step[2:].split(':')[1]
            # Process as if True, but do not return as the false case will be the next step in the workflow
            if next_workflow == 'A':
                branch.append((step[0:1], step[1:2], int(step[2:].split(':')[0])))
                print('A> ', branch)
                process_branch('A', branch)
                branch.pop()
            elif next_workflow == 'R':
                branch.append((step[0:1], step[1:2], int(step[2:].split(':')[0])))
                print('R> ', branch)
                process_branch('R', branch)
                branch.pop()
            else:
                branch.append((step[0:1], step[1:2], int(step[2:].split(':')[0])))
                process_tree(next_workflow, branch)
                branch.pop()
            # Now in the False case, so add the false branch to the workflow
            cnt += 1
            branch.append((step[0:1], reverse_equality[step[1:2]], int(step[2:].split(':')[0]) + offset[step[1:2]]))

        elif step[1:2] == '<':
            next_workflow = step[2:].split(':')[1]
            # Process as if True, but do not return as the false case will be the next step in the workflow
            if next_workflow == 'A':
                branch.append((step[0:1], step[1:2], int(step[2:].split(':')[0])))
                print('A< ', branch)
                process_branch('A', branch)
                branch.pop()
            elif next_workflow == 'R':
                branch.append((step[0:1], step[1:2], int(step[2:].split(':')[0])))
                print('R< ', branch)
                process_branch('R', branch)
                branch.pop()
            else:
                branch.append((step[0:1], step[1:2], int(step[2:].split(':')[0])))
                process_tree(next_workflow, branch)
                branch.pop()
            # Now in the False case, so add the false branch to the workflow
            cnt += 1
            branch.append((step[0:1], reverse_equality[step[1:2]], int(step[2:].split(':')[0]) + offset[step[1:2]]))
        else:
            process_tree(step, branch)

    # need to pop off the < or > that were added
    for i in range(0, cnt):
        branch.pop()
    return


def process_part(part, workflow):
    for step in workflows[workflow]:
        if step in 'AR':
            return step
        elif step[1:2] == '>':
            if part[char_to_index[step[0:1]]] > int(step[2:].split(':')[0]):
                next_workflow = step[2:].split(':')[1]
                if next_workflow in 'AR':
                    return next_workflow
                else:
                    return process_part(part, next_workflow)
        elif step[1:2] == '<':
            if part[char_to_index[step[0:1]]] < int(step[2:].split(':')[0]):
                next_workflow = step[2:].split(':')[1]
                if next_workflow in 'AR':
                    return next_workflow
                else:
                    return process_part(part, next_workflow)
        else:
            return process_part(part, step)


with open("input19.txt") as my_file:
    # read file
    for line in my_file:
        lines.append(line.strip())
        l = line.strip().split('{')
        if l[0] != '':
            workflows[l[0]] = l[1][:-1].split(',')
        elif len(l) > 1:
            parts.append([int(x[2:]) for x in l[1][:-1].split(',')])

    for part in parts:
        if process_part(part, 'in') == 'A':
            accepted_parts.append(part)

    total = 0
    for part in accepted_parts:
        total += sum(part)

    print("Part1 = ", total)

    process_tree('in', [])
    print("A = ", total_A, "R = ", total_R, "total = ", total_A + total_R)
