# Created by pyp2rpm-3.3.5
%global pypi_name xxh-xxh

Name:           python-%{pypi_name}
Version:        0.8.6
Release:        2%{?dist}
Summary:        Bring your favorite shell wherever you go through the ssh

License:        BSD
URL:            https://github.com/xxh/xxh
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
<p align"center">You stuffed command shell with aliases, tools and colors but
you lose it all when using ssh. The mission of xxh is to bring your favorite
shell wherever you go through the ssh without root access and system
installations.</p><p align"center"> If you like the idea of xxh click ⭐ on the
repo and stay tuned. <a href' alt'[xxh demo]' src' border"0" width"100%">
<col...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pexpect) >= 4.8
Requires:       python3dist(pyyaml)
# Let users just install "xxh"
Provides:       xxh = %{version}-%{release}
%description -n python3-%{pypi_name}
<p align"center">You stuffed command shell with aliases, tools and colors but
you lose it all when using ssh. The mission of xxh is to bring your favorite
shell wherever you go through the ssh without root access and system
installations.</p><p align"center"> If you like the idea of xxh click ⭐ on the
repo and stay tuned. <a href' alt'[xxh demo]' src' border"0" width"100%">
<col...

%package -n xxh-bash
Summary:        Bash seamless script for xxh
Requires:       xxh = %{version}-%{release}
%description -n xxh-bash
<p align"center">You stuffed command shell with aliases, tools and colors but
you lose it all when using ssh. The mission of xxh is to bring your favorite
shell wherever you go through the ssh without root access and system
installations.</p><p align"center"> If you like the idea of xxh click ⭐ on the
repo and stay tuned. <a href' alt'[xxh demo]' src' border"0" width"100%">
<col...

%package -n xxh-zsh
Summary:        ZSH seamless script for xxh
Requires:       xxh = %{version}-%{release}
%description -n xxh-zsh
<p align"center">You stuffed command shell with aliases, tools and colors but
you lose it all when using ssh. The mission of xxh is to bring your favorite
shell wherever you go through the ssh without root access and system
installations.</p><p align"center"> If you like the idea of xxh click ⭐ on the
repo and stay tuned. <a href' alt'[xxh demo]' src' border"0" width"100%">
<col...

%package -n xxh-xonsh
Summary:        Xonsh seamless script for xxh
Requires:       xxh = %{version}-%{release}
%description -n xxh-xonsh
<p align"center">You stuffed command shell with aliases, tools and colors but
you lose it all when using ssh. The mission of xxh is to bring your favorite
shell wherever you go through the ssh without root access and system
installations.</p><p align"center"> If you like the idea of xxh click ⭐ on the
repo and stay tuned. <a href' alt'[xxh demo]' src' border"0" width"100%">
<col...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/xxh
%{python3_sitelib}/xxh_xxh
%{python3_sitelib}/xxh_xxh-%{version}-py%{python3_version}.egg-info

%files -n xxh-bash
%{_bindir}/xxh.bash

%files -n xxh-zsh
%{_bindir}/xxh.zsh

%files -n xxh-xonsh
%{_bindir}/xxh.xsh


%changelog
* Fri Jan 15 2021 Jerzy Drozdz <jerzy.drozdz@jdsieci.pl> - 0.8.6-2
- Seamless scripts moved to seperate packages

* Tue Jan 12 2021 mockbuilder - 0.8.6-1
- Initial package.

