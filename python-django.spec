%define module	django
%define tarname	Django

%bcond_with python2

Summary:	A high-level Python Web framework
Name:		python-%{module}
Version:	3.0.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://www.djangoproject.com
Source0:	https://files.pythonhosted.org/packages/44/e8/4ae9ef3d455f4ce5aa22259cb6e40c69b29ef6b02d49c5cdfa265f7fc821/Django-3.0.1.tar.gz
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python-sphinx
BuildRequires:  python-devel
BuildRequires:	python-babel
%if %{with python2}
BuildRequires:	python2-distribute
BuildRequires:	python2-sphinx
BuildRequires:  python2-devel
BuildRequires:	python2-babel
%endif

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

%if %{with python2}
%package -n python2-django
Summary:	A high-level Python Web framework
Group:		Development/Python

%description -n python2-django
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

Developed and used over the past two years by a fast-moving online-news
operation, Django was designed from scratch to handle two challenges:	the
intensive deadlines of a newsroom and the stringent requirements of experienced
Web developers. It has convenient niceties for developing content-management
systems, but it's an excellent tool for building any Web site.

Django focuses on automating as much as possible and adhering to the
DRY principle.
%endif

%prep
%setup -qc
sed -i 's/^\(ez_setup.use_setuptools\)/#\1/' %{tarname}-%{version}/setup.py

mv %{tarname}-%{version} python3

%if %{with python2}
cp -a python3 python2
%endif

%build
%if %{with python2}
cd python2
PYTHONDONTWRITEBYTECODE=1 %__python2 setup.py build
make -C docs/ html
cd ..
%endif

cd python3
PYTHONDONTWRITEBYTECODE=1 %__python setup.py build
make -C docs/ html
cd ..

%install
%if %{with python2}
cd python2
PYTHONDONTWRITEBYTECODE=1 %__python2 setup.py install --root=%{buildroot}
cd ..
cd %{buildroot}%{_bindir}
for i in *; do
	mv $i $i-2
done
cd -
%endif

cd python3
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%files
%doc python3/LICENSE python3/docs/_build/html
%{_bindir}/*
%if %{with python2}
%exclude %{_bindir}/*-2
%endif
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{tarname}-*.egg-info

%if %{with python2}
%files -n python2-django
%doc python2/LICENSE python2/docs/_build/html
%{_bindir}/*-2
%{py2_puresitedir}/%{module}
%{py2_puresitedir}/%{tarname}-*.egg-info
%endif
