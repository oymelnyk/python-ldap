#from pyad import *
import pyad.adquery


def main():
    q = pyad.adquery.ADQuery()

    q.execute_query(
        attributes=["distinguishedName", "description"],
        where_clause="objectClass = '*'",
        base_dn="OU=Users,OU=HO,DC=XXX,DC=ua,DC=loc"
    )

    for row in q.get_results():
        print(row["distinguishedName"])


main()
