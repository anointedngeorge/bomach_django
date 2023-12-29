from django.contrib.auth.models import Group


def checkCodenameInPermGroup(group_name='',permission_codename=''):
    if group_name != None:
        group_permissions = Group.objects.get(name=group_name).permissions.all()
        flag = False
        permission_container = [x.codename for x in group_permissions]
        if permission_codename in permission_container:
            flag = True
        else:
            flag = False
        return flag
    else:
        return True

