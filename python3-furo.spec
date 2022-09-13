Summary:	Clean customizable Sphinx documentation theme
Summary(pl.UTF-8):	Czysty, konfigurowalny motyw dokumentacji Sphinksa
Name:		python3-furo
# 2021.11.12+ requires sphinx-theme-builder
Version:	2021.10.9
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/furo/
Source0:	https://files.pythonhosted.org/packages/source/f/furo/furo-%{version}.tar.gz
# Source0-md5:	0ebcd2d672b60689d89ae1affafbe418
Patch0:		%{name}-setuptools.patch
URL:		https://pypi.org/project/furo/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clean customizable Sphinx documentation theme.

%description -l pl.UTF-8
Czysty, konfigurowalny motyw dokumentacji Sphinksa.

%prep
%setup -q -n furo-%{version}
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/furo
%{py3_sitescriptdir}/furo-%{version}-py*.egg-info
