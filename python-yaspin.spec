%global srcname yaspin
Name:		python-yaspin		
Version:	0.14.0
Release:	2%{?dist}
License:	MIT
URL:		https://pypi.org/project/yaspin
Source0:	https://github.com/pavdmyt/yaspin/archive/v%{version}.tar.gz
BuildArch:	noarch

Summary:	PyPi library for terminal spinners
%description
Yet Another Terminal Spinner for Python.

Yaspin provides a full-featured terminal spinner to show the progress during long-hanging operations.


%package -n python3-%{srcname}
Summary:	PyPi library for terminal spinners
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
Requires:	python3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Yet Another Terminal Spinner for Python.

Yaspin provides a full-featured terminal spinner to show the progress during long-hanging operations.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

$install
%py3_install

%check
# many tests are skipped because they are generated, some combinations are not supported use cases
#example: tests/test_in_out.py::test_compose_out_with_color[None-''-bold] SKIPPED
%{__python3} -m pytest

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Wed Jan 9 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-2
- added BuildRequires

* Tue Jan 8 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.14.0-1
- created package
