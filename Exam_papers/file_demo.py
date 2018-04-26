from file import File


def main():
    # Display available permissions
    print('-----File permissions: {}'.format(File.FILE_PERMISSIONS))

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 1000, 'r')
    f3 = File('secret.txt', 'fred', 100)

    # Display file details
    print('-----File details...')
    print(f1)
    print(f2)
    print(f3)

    # Check access rights
    print('-----Access rights...')
    print(f3.has_access('fred', 'r'))
    print(f3.has_access('mary', 'x'))

    # Enable permissions
    print('-----Enabling permissions...')
    f3.enable_permission('fred', 'x')
    f3.enable_permission('mary', 'w')

    # Check access rights
    print('-----Access rights...')
    print(f3.has_access('mary', 'x'))

    # Disable permissions
    print('-----Disabling permissions...')
    f3.disable_permission('fred', 'x')
    f3.disable_permission('mary', 'w')

    # Check access rights
    print('-----Access rights...')
    print(f3.has_access('mary', 'x'))
    print(f3.has_access('vera', 'w'))

    # Enable permissions
    print('-----Enabling permissions...')
    f3.enable_permission('fred', 'r')
    f3.enable_permission('fred', 'x')
    f2.enable_permission('max', 'w')
    f2.enable_permission('max', 'x')

    # Display permissions
    print('-----Permissions: {}'.format(f3.get_permissions()))
    print('-----Permissions: {}'.format(f2.get_permissions()))

    # Display file details
    print('-----File details...')
    print(f3)


if __name__ == '__main__':
    main()
