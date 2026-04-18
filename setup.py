from setuptools import setup, find_packages

setup(
    name="icon_color_override",
    version="0.0.1",
    description="Override ERPNext icon colors to custom color",
    author="Your Company",
    author_email="your@email.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
