class File(object):

    FILE_PERMISSIONS = 'rwx'

    def __init__(self, name, owner, size=0, permissions=''):
        self.name = name
        self.owner = owner
        self.size = int(size)
        self.permissions = permissions

    def __str__(self):
        l = []
        l.append('File: {:s}'.format(self.name))
        l.append('Owner: {:s}'.format(self.owner))
        if self.permissions == '':
            x = 'null'
        else:
            x = self.permissions
        l.append('Permissions: {:s}'.format(x))
        l.append('Size: {:d} bytes'.format(self.size))
        return '\n'.join(l)

    def has_access(self, name, per):
        if name == self.owner:
            return True
        elif per in self.permissions:
            return True
        return False

    def enable_permission(self, name, per):
        if name != self.owner:
            print('Access denied')
        elif name == self.owner and per not in self.permissions and per in self.FILE_PERMISSIONS:
            self.permissions = ''.join(sorted(self.permissions + per))

    def disable_permission(self, name, per):
        if name != self.owner:
            print('Access denied')
        elif name == self.owner and per in self.permissions:
            self.permissions = self.permissions.replace(per, '')

    def get_permissions(self):
        return self.permissions
