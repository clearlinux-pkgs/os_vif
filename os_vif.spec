#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os_vif
Version  : 1.15.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/69/ba/321db41cb3c041d2d7c1da04231b40a144b8577818bb5cbf40f9ffef8f26/os_vif-1.15.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/ba/321db41cb3c041d2d7c1da04231b40a144b8577818bb5cbf40f9ffef8f26/os_vif-1.15.1.tar.gz
Summary  : A library for plugging and unplugging virtual interfaces in OpenStack.
Group    : Development/Tools
License  : Apache-2.0
Requires: os_vif-license = %{version}-%{release}
Requires: os_vif-python = %{version}-%{release}
Requires: os_vif-python3 = %{version}-%{release}
Requires: debtcollector
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.privsep
Requires: oslo.versionedobjects
Requires: ovsdbapp
Requires: pbr
Requires: pyroute2
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pyroute2

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/os-vif.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the os_vif package.
Group: Default

%description license
license components for the os_vif package.


%package python
Summary: python components for the os_vif package.
Group: Default
Requires: os_vif-python3 = %{version}-%{release}

%description python
python components for the os_vif package.


%package python3
Summary: python3 components for the os_vif package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os_vif package.


%prep
%setup -q -n os_vif-1.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551366157
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os_vif
cp LICENSE %{buildroot}/usr/share/package-licenses/os_vif/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os_vif/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
