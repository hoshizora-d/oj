import setuptools

setuptools.setup(
    name="hoshizora.oj", # Replace with your own username
    version="0.0.1",
    author="hoshizora.d",
    author_email="hoshizora.ding@gmail.com",
    description="A simple oj system",
    #url="https://github.com/hoshizora-d/oj",
    packages=setuptools.find_packages(include=("problems", "oj")),
    python_requires='>=3.8',
)
