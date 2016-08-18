%define oname   PyGithub

Name:           python-pygithub
Version:        1.27.1
Release:        %mkrel 1
Summary:        Use the full Github API v3
Group:          Development/Python
License:        LGPLv3+
URL:            https://pypi.python.org/pypi/%{oname}
Source0:        https://github.com/%{oname}/%{oname}/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(2)(setuptools)

%description
%{oname} is a Python (2 and 3) library to use the Github API v3. With it, you
can manage your Github resources (repositories, user profiles, organizations,
etc.) from Python scripts.

%package -n     python3-pygithub
Summary:        Use the full Github API v3
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  pythonegg(3)(setuptools)

%description -n python3-pygithub
%{oname} is a Python (2 and 3) library to use the Github API v3. With it, you
can manage your Github resources (repositories, user profiles, organizations,
etc.) from Python scripts.

This is the Python 3 version of the package.

%prep
%setup -q -n %{oname}-%{version}

# Remove bundled egg-info
rm -rf %{oname}.egg-info

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
%doc README.md
%{python2_sitelib}/github
%{python2_sitelib}/%{oname}-%{version}-*.egg-info

%files -n python3-pygithub
%doc README.md
%{python3_sitelib}/github
%{python3_sitelib}/%{oname}-%{version}-*.egg-info
