from setuptools import setup, find_packages

setup(
    name="NovaAI",
    version="0.1.0",  # Initial version for development
    description="NovaAI: A scripturally aligned AI framework powered by OmniCode",
    author="CreativeWorkzStudio LLC",
    author_email="",  # Replace with actual contact email
    url="",  # Replace with your company website
    packages=find_packages(),  # Automatically finds all packages (requires __init__.py files)
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    entry_points={
        "console_scripts": [
            "novaai=main:run_nova_ai",  # Command to run NovaAI
        ]
    },
    install_requires=[],  # Add Python dependencies here, if any
    python_requires=">=3.6",  # Ensure compatibility with Python 3.6+
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",  # Current stage of development
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Adjust license as needed
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    keywords="NovaAI AI framework OmniCode scripture-based AI",
)
