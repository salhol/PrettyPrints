from setuptools import setup
with open("README.md",encoding="utf-8") as f:
   long_desc = f.read()
setup(
   name = "PrettyPrints",
   version = "2.0.1",
   url = "https://github.com/salhol/PrettyPrints",
   author = "Sally Holm",
   author_email = "sallymholm+github@gmail.com",
   packages = ["PrettyPrints"],
   description = "The lazy way for pretty print spacings.",
   long_description = long_desc,
   long_description_content_type='text/markdown',
   classifiers=['License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)','Programming Language :: Python :: 3.9'],
   license = "glp-3.0-or-later"
)