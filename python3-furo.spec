Summary:	Clean customizable Sphinx documentation theme
Summary(pl.UTF-8):	Czysty, konfigurowalny motyw dokumentacji Sphinksa
Name:		python3-furo
Version:	2024.8.6
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/furo/
Source0:	https://files.pythonhosted.org/packages/source/f/furo/furo-%{version}.tar.gz
# Source0-md5:	f3097240959189473d67d001bb2ddd71
URL:		https://pypi.org/project/furo/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-sphinx_theme_builder
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clean customizable Sphinx documentation theme.

%description -l pl.UTF-8
Czysty, konfigurowalny motyw dokumentacji Sphinksa.

%prep
%setup -q -n furo-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/furo
%{py3_sitescriptdir}/furo-%{version}.dist-info
