from setuptools import setup
import re

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('discord/ext/colours/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version = version + out.decode('utf-8').strip()
    except Exception:
        pass

with open('README.md') as f:
    readme = f.read()

setup(name='discord-ext-colours',
      author='MGardne8',
      url='https://github.com/MGardne8/DiscordPyColours',
      version=version,
      packages=['discord.ext.colours', 'discord.ext.colors'],
      license='GPLv3',
      description='An Extension Package for Discord.py with additional colour packages',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      extras_require=None,
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)