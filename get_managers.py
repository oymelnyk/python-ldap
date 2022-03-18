import pyad.adquery

username = ''  # usename
q = pyad.adquery.ADQuery()


def get_manager_name(username):

    q.execute_query(
        attributes=["manager", ],
        where_clause="sAMAccountName = '{}'".format(username),
        base_dn="OU=Users,OU=HO,DC=XXX,DC=ua,DC=loc"
    )

    for row in q.get_results():
        manager = row["manager"]
        # print(row["manager"])
        manager = manager.split(",")
        manager_name = manager[0].replace("CN=", "")

    def get_manager_login(manager_name):

        q.execute_query(
            attributes=["sAMAccountName", ],
            where_clause="cn = '{}'".format(manager_name),
            base_dn="OU=Users,OU=HO,DC=XXX,DC=ua,DC=loc"
        )

        for row1 in q.get_results():
            manager_login = row1["sAMAccountName"]
            # print(row1["sAMAccountName"])

        return manager_login
    manager_login = get_manager_login(manager_name)

    return manager_login, manager_name


print(get_manager_name(username))
