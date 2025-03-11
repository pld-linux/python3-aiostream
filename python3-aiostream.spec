Summary:	Generator-based operators for asynchronous iteration
Name:		python3-aiostream
Version:	0.4.5
Release:	3
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/a/aiostream/aiostream-%{version}.tar.gz
# Source0-md5:	a61ca6b2586df89d9596a2342ad8f205
URL:		https://github.com/vxgmichel/aiostream
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aiostream provides a collection of stream operators that can be
combined to create asynchronous pipelines of operations.

It can be seen as an asynchronous version of itertools, although some
aspects are slightly different. Essentially, all the provided
operators return a unified interface called a stream.

%prep
%setup -q -n aiostream-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitescriptdir}/aiostream
%{py3_sitescriptdir}/aiostream/*.py
%{py3_sitescriptdir}/aiostream/__pycache__
%dir %{py3_sitescriptdir}/aiostream/stream
%{py3_sitescriptdir}/aiostream/stream/*.py
%{py3_sitescriptdir}/aiostream/stream/__pycache__
%{py3_sitescriptdir}/aiostream-%{version}-py*.egg-info
