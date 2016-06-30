%define upstream_name PyGithub

Name:           python-pygithub
Version:        1.26.0
Release:        %mkrel 2
Summary:        Use the full Github API v3
Group:          Development/Python
License:        LGPLv3+
URL:            https://pypi.python.org/pypi/PyGithub
Source0:        https://pypi.python.org/packages/source/P/PyGithub/%{upstream_name}-%{version}.tar.gz
Patch0:         0001-fix-wrong-expectance-on-requestJsonAndCheck-returnin.patch
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(2)(setuptools)

%description
PyGithub is a Python (2 and 3) library to use the Github API v3. With it, you
can manage your Github resources (repositories, user profiles, organizations,
etc.) from Python scripts.

%package -n     python3-pygithub
Summary:        Use the full Github API v3
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  pythonegg(3)(setuptools)

%description -n python3-pygithub
PyGithub is a Python (2 and 3) library to use the Github API v3. With it, you
can manage your Github resources (repositories, user profiles, organizations,
etc.) from Python scripts.

This is the Python 3 version of the package.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0 -p1

# Remove bundled egg-info
rm -rf %{upstream_name}.egg-info

cp -a . %{py3dir}

%build
%py2_build

pushd %{py3dir}
%py3_build
popd

%install
pushd %{py3dir}
%py3_install
popd

%py2_install

%files
%doc README.rst
%{python2_sitelib}/github
%{python2_sitelib}/PyGithub-%{version}-*.egg-info

%files -n python3-pygithub
%doc README.rst
%{python3_sitelib}/github
%{python3_sitelib}/PyGithub-%{version}-*.egg-info
