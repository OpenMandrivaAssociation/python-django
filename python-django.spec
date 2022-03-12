%define module django
%define tarname Django

Summary:	A high-level Python Web framework
Name:		python-%{module}
Version:	3.1.4
Release:	2
License:	BSD
Group:		Development/Python
Url:		http://www.djangoproject.com
Source0:	https://files.pythonhosted.org/packages/cc/bf/b9f5e4c4707bcabcd4202d78a4d23459d5de3083a7e7efde4dd215b997ac/Django-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(python)
BuildRequires:	python-babel

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

Developed and used over the past two years by a fast-moving online-news
operation, Django was designed from scratch to handle two challenges:	the
intensive deadlines of a newsroom and the stringent requirements of experienced
Web developers. It has convenient niceties for developing content-management
systems, but it's an excellent tool for building any Web site.

Django focuses on automating as much as possible and adhering to the
DRY principle.

%prep
%autosetup -n %{tarname}-%{version}
sed -i 's/^\(ez_setup.use_setuptools\)/#\1/' setup.py

%build
%py_build
make -C docs/ html

%install
%py_install

%files
%doc python3/LICENSE python3/docs/_build/html
%{_bindir}/*
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{tarname}-*.egg-info
