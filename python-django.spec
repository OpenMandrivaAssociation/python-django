%define module django
%define oname Django

Name:		python-django
Summary:	A high-level Python Web framework
Version:	6.0.2
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://www.djangoproject.com
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildSystem:	python
BuildRequires:	make
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(asgiref)
BuildRequires:	python%{pyver}dist(argon2-cffi)
BuildRequires:	python%{pyver}dist(babel)
BuildRequires:	python%{pyver}dist(bcrypt)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pytz)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sqlparse)
BuildRequires:	python%{pyver}dist(tzdata)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(asgiref)
Requires:	python%{pyver}dist(sqlparse)
Recommends:	python%{pyver}dist(argon2-cffi)
Recommends:	python%{pyver}dist(bcrypt)
Recommends:	python%{pyver}dist(jinja2)
Recommends:	python%{pyver}dist(pillow)
Recommends:	python%{pyver}dist(pyyaml)

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

%prep -a
export LC_ALL=C.utf-8
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build -a
make -C docs/ html

%install -a
install -D -m 0644 extras/django_bash_completion %{buildroot}%{_datadir}/bash-completion/completions/django_bash_completion
# Fix wrong script interpeter
sed -i "s|^#!%{_bindir}/env python$|#!%{__python}|" %{buildroot}%{python_sitelib}/django/conf/project_template/manage.py-tpl

mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

%files
%doc README.rst
%license LICENSE LICENSE.python
%{_bindir}/django-admin
%{_datadir}/bash-completion/completions/django_bash_completion
%{_mandir}/man1/django-admin.1*
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
