from distutils.core import setup

setup(name='python-tds',
        version='0.1',
        description='Python DBAPI driver for MSSQL using pure Python TDS (Tabular Data Stream) protocol implementation',
        author='Mikhail Denisenko',
        author_email='denisenkom@gmail.com',
        url='https://github.com/denisenkom/pytds',
        packages=['pytds'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
        ],
        )