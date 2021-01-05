import os
import fnmatch
import argparse
from collections import defaultdict

template ='''\
{p} module
{l}

.. automodule:: {p}
    :members:
    :undoc-members:
    :exclude-members: {exclude}
'''

index_template = '''\
{title}
{l}

.. toctree::
    :maxdepth: 1

    {index}

'''


exclude = 'RUNNER,aborted,apply_data,blocked,description,errored,failed,'\
          'id,parameters,parent,passed,passx,skipped,source,uid'
ignores = ['__pycache__', '.git']

class CreateApiDoc(object):
    def __init__(self, package, location, save, title):

        self.package = package
        self.location = location
        self.save = save
        self.title = title

        self.directories = defaultdict(list)

        # Make sure the save directory is created
        os.makedirs(save, exist_ok=True)

    def right_location(self, dct, path):
        for p in path.split('/'):
            if p not in dct:
                dct[p] = {}
            dct = dct[p]
        return dct

    def organize_file(self):
        for root, dirnames, filenames in os.walk(self.location):
            to_ignore = [ignore for ignore in ignores if ignore in root]
            if to_ignore:
                continue

            for filename in fnmatch.filter(filenames, '*.py'):
                # To save some time
                # Only do trigger
                #if 'trigger' not in root:
                #    continue

                # Remove ext
                # Remove location from filename
                temp_root = root.replace(self.location, '')
                dct_loc = self.right_location(self.directories, temp_root)

                # Add value
                if 'value' not in dct_loc:
                    dct_loc['value'] = []

                dct_loc['value'].append(filename)

    def create_dir(self, directory=None, title=None, path=None, module=None):

        # Get default values
        directory = directory or self.directories
        title = title or self.title
        path = path or self.save
        module = module or self.package

        # Create index for this directory
        index = []
        if isinstance(directory, list):
            return
        for key, value in sorted(directory.items()):
            if key == '':
                # Same level, only for first key
                key = '__init__'
                continue

            if key == 'value':
                # Now at some leaves
                for val in value:
                    if val == '__init__.py':
                        continue
                    # Remove the py
                    val = os.path.splitext(os.path.basename(val))[0]
                    index.append(val)

                    cur_module = '{m}.{v}'.format(m=module, v=val)
                    # And also populate the file
                    apidoc = template.format(p=cur_module,
                                             l='='*(len(cur_module)+7),
                                             exclude=exclude)

                    save_loc = os.path.join(path, val+'.rst')
                    with open(save_loc, 'a') as f:
                        f.write(apidoc)
                continue

            cur_module = '{m}.{k}'.format(m=module, k=key)

            os.makedirs(os.path.join(path, key), exist_ok=True)
            index.append(key+'/index')
            self.create_dir(directory=value, title=cur_module,
                            path=os.path.join(path, key),
                            module=cur_module)

        # Save Index
        index_str = '\n    '.join(index)
        with open(os.path.join(path, 'index.rst'), 'a') as f:
            f.write(index_template.format(title=title, l='='*(len(title)),
                                            index=index_str))

    ## now..we got to create those directories
    #create_dir(directory=directories, title=title,
    #           path=save, module=module)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--title',
                    help='Title of apidoc')
    parser.add_argument('--package',
                    help='Package name')
    parser.add_argument('--location',
                    help='Package location')
    parser.add_argument('--save',
                    help='Where to save the apidoc')
    custom_args = parser.parse_known_args()[0]


    package = custom_args.package
    location = custom_args.location
    save = custom_args.save
    title = custom_args.title

    api = CreateApiDoc(package=package, location=location, save=save,
                       title=title)
    api.organize_file()
    api.create_dir()
