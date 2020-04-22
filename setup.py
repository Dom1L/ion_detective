import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ion_detective',  
     version='0.1',
     author="Dominik Lemm",
     author_email="lemm92.d@gmail.com",
     description="Virtual laboratory for chemistry students to simulate qualitative ion analysis.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Dom1L/ion_detective",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU License",
         "Operating System :: OS Independent",
     ],
 )
