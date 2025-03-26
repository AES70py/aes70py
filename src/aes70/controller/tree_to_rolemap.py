import asyncio

async def tree_to_rolemap(tree, s='/'):
    roles = {}

    tasks = []

    def fetch_role(o):
        if isinstance(o, list):
            for item in o:
                fetch_role(item)
        else:
            async def process():
                role = await o.GetRole()
                roles[o] = role
            tasks.append(asyncio.create_task(process()))

    for item in tree:
        #print(roles)
        fetch_role(item)

    await asyncio.gather(*tasks)

    rolemap = {}

    def build_paths(a, prefix):
        p = (prefix + s) if (prefix is not None) else ''
        local_roles = {}

        for i, o in enumerate(a):
            if isinstance(o, list):
                continue
            role = roles.get(o)
            if role in local_roles:
                tmp = local_roles[role]
                if isinstance(tmp, list):
                    tmp.append(o)
                else:
                    local_roles[role] = [tmp, o]
            else:
                local_roles[role] = o

        for role, value in list(local_roles.items()):
            if isinstance(value, list):
                n = 1
                for obj in value:
                    while (role + str(n)) in local_roles:
                        n += 1
                    nrole = role + str(n)
                    local_roles[nrole] = obj
                    local_roles[obj] = nrole
                del local_roles[role]
            else:
                local_roles[value] = role

        for i, o in enumerate(a):
            if isinstance(o, list):
                prev = a[i - 1] if i > 0 and not isinstance(a[i - 1], list) else None
                new_prefix = p + str(local_roles.get(prev))
                build_paths(o, new_prefix)
            else:
                path = p + str(local_roles.get(o))
                rolemap[path] = o

    build_paths(tree, None)

    return rolemap

#default = tree_to_rolemap
