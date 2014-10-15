%define upstream_name PyGithub

Name:           python-pygithub
Version:        1.17.0
Release:        %mkrel 7
Summary:        Use the full Github API v3
Group:          Development/Python
License:        LGPL
URL:            https://pypi.python.org/pypi/PyGithub
Source0:        https://pypi.python.org/packages/source/P/PyGithub/PyGithub-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
PyGithub is a Python (2 and 3) library to use the Github API v3. With it, you
can manage your Github resources (repositories, user profiles, organizations,
etc.) from Python scripts.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%files
%doc README.rst
%{python_sitelib}/github
%{python_sitelib}/PyGithub-%{version}-*.egg-info
