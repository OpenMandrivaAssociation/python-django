%define oname django
%define Oname Django
%define name python-%oname
%define version 1.1.1
%define rel 2

Summary: A high-level Python Web framework
Name: %{name}
Version: %{version}
Release: %mkrel %rel
Source0: http://media.djangoproject.com/releases/%{version}/%Oname-%{version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Url: http://www.djangoproject.com
%py_requires -d
BuildRequires: python-setuptools

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

Developed and used over the past two years by a fast-moving online-news
operation, Django was designed from scratch to handle two challenges: the
intensive deadlines of a newsroom and the stringent requirements of experienced
Web developers. It has convenient niceties for developing content-management
systems, but it's an excellent tool for building any Web site.

Django focuses on automating as much as possible and adhering to the
DRY principle.

%prep
%setup -q -n %Oname-%version
perl -pi -e 's/^(ez_setup.use_setuptools)/#$1/' setup.py

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE  README docs/*
%_bindir/*
%py_puresitedir/%{oname}
%py_puresitedir/%{Oname}-*.egg-info
