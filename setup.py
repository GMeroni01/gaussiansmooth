from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name="gaussiansmooth_giorgiom",
      version="0.0.5",
      description="Gaussian smoothing for noisy signals",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="Giorgio M.",
      packages=find_packages(),
      install_requires=["numpy", "scipy", "matplotlib"])