%define module	django
%define tarname	Django

Summary:	A high-level Python Web framework
Name:		python-%{module}
Version:	3.0.2
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://www.djangoproject.com
Source0:	https://files.pythonhosted.org/packages/c5/c1/5b901e21114b5dd9233726c2975c0aa7e9f48f63e41ec95d8777721d8aff/Django-3.0.2.tar.gz
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python-sphinx
BuildRequires:  python-devel
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
%setup -q -n %{tarname}-%{version}

# drop bundled egg-info
rm -rf Django.egg-info/

# fix shebangs
find . \( -name "*.py" -o -name "*.py-tpl" \) -exec sed -i -e '1s|#!.*python[2,3]\?|#!%{__python3}|' {} \;

# empty files
for f in \
    django/contrib/staticfiles/models.py \
    django/contrib/humanize/models.py \
; do
  echo "# just a comment" > $f
done

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/*
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{tarname}-*.egg-info

