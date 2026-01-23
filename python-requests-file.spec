Name:		python-requests-file
Version:	3.0.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/requests-file/requests_file-%{version}.tar.gz
Summary:	File transport adapter for Requests
URL:		https://pypi.org/project/requests-file/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(six)

BuildSystem:	python

BuildArch:	noarch

%patchlist 
python-requests-file-3.0.1-fix_version.patch

%description
Requests-File is a transport adapter for use with the Requests Python
library to allow local filesystem access via file:\/\/ URLs.

%prep
%autosetup -p1 -n requests_file-%{version}
sed -i -e "s,@VERSION@,%{version}," pyproject.toml

%files
%license LICENSE
%doc README.rst
%{py_sitedir}/requests_file
%{py_sitedir}/requests_file-*.*-info
