"""
maimai_score Cython 编译配置

编译:
    pip install cython
    python setup.py build_ext --inplace

使用:
    import maimai_score
    data = maimai_score.fetch(sgwcmaid="SGWCMAID...")
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="maimai_score",
    version="1.0.0",
    description="maimai DX CHN score fetcher",
    ext_modules=cythonize(
        "maimai_score.py",
        compiler_directives={"language_level": "3"},
    ),
    install_requires=["httpx", "cryptography"],
    zip_safe=False,
)
