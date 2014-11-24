%define module	django
%define tarname	Django

Summary:	A high-level Python Web framework



Name:		python-%{module}
Version:	1.7.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://www.djangoproject.com
Source0:	https://pypi.python.org/packages/source/D/Django/Django-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python-sphinx
BuildRequires:  python-devel

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
%setup -qn %{tarname}-%{version}
sed -i 's/^\(ez_setup.use_setuptools\)/#\1/' setup.py

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
make -C docs/ html

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc LICENSE  docs/_build/html
%{_bindir}/*
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{tarname}-*.egg-info
