# TODO:
# - fix objects.inv paths
Summary:	Clean customizable Sphinx documentation theme
Summary(pl.UTF-8):	Czysty, konfigurowalny motyw dokumentacji Sphinksa
Name:		python3-furo
Version:	2024.8.6
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/furo/
Source0:	https://files.pythonhosted.org/packages/source/f/furo/furo-%{version}.tar.gz
# Source0-md5:	f3097240959189473d67d001bb2ddd71
Source1:	https://src.fedoraproject.org/repo/pkgs/python-furo/furo-2024.08.06-vendor.tar.xz/sha512/4a4313b30aff8dcb12ca857064bf73a18e3287e1fdd9e5ca55b277519628b8401b287f48195271d09e88249c431d390f3710f10b82b498f0176c4c40a415bb39/furo-2024.08.06-vendor.tar.xz
# Source1-md5:	685e508601d03c86281ea8fb65f1d844
URL:		https://pypi.org/project/furo/
BuildRequires:	npm
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-nodeenv
BuildRequires:	python3-sphinx_theme_builder
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildRequires:	yarn
Requires:	python3-modules >= 1:3.6
ExcludeArch:	x32
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	nodejs_version	%(nodejs -v | sed s/v//)

%description
Clean customizable Sphinx documentation theme.

%description -l pl.UTF-8
Czysty, konfigurowalny motyw dokumentacji Sphinksa.

%prep
%setup -q -n furo-%{version} -a1

# Substitute the installed nodejs version for the requested version
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%build
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv
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
