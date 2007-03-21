from setuptools import setup, find_packages

setup(
    name='sookti',
    version="",
    #description="",
    #author="",
    #author_email="",
    #url="",
    install_requires=["Pylons>=0.9.4","FormBuild>=0.1.5b,<0.2", "FormEncode>=0.4"],
    packages=find_packages(),
    include_package_data=True,
    test_suite = 'nose.collector',
    package_data={'sookti': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [paste.app_factory]
    main=sookti:make_app
    [paste.app_install]
    main=pylons.util:PylonsInstaller
    """,
)
