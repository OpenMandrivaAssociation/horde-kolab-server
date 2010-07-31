%define prj Kolab_Server
%define prj Kolab_Server

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-kolab-server
Version:       0.5.0
Release:       %mkrel 3
Summary:       A package for manipulating the Kolab user database
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-framework
Requires:      horde-ldap
Requires:      horde-sessionobjects
Requires:      php-ldap
Requires:      php-pear
Requires(pre): php-pear-Net_LDAP2
Suggests:      php-pear-PHPUnit
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
This package allows read/write entries in the Kolab user
database stored in LDAP.


%prep
%setup -q -n %{prj}-%{version}
%__cp %{SOURCE0} %{prj}-%{version}.tgz

%build

%install
pear install --packagingroot %{buildroot} --nodeps --offline %{prj}-%{version}.tgz

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp %{_builddir}/package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Kolab
%dir %{peardir}/Horde/Kolab/IMAP
%dir %{peardir}/Horde/Kolab/Server
%dir %{peardir}/Horde/Kolab/Server/Object
%dir %{peardir}/Horde/Kolab/Test
%{peardir}/Horde/Kolab/IMAP.php
%{peardir}/Horde/Kolab/IMAP/cclient.php
%{peardir}/Horde/Kolab/IMAP/pear.php
%{peardir}/Horde/Kolab/IMAP/test.php
%{peardir}/Horde/Kolab/Server.php
%{peardir}/Horde/Kolab/Server/Object.php
%{peardir}/Horde/Kolab/Server/Object/address.php
%{peardir}/Horde/Kolab/Server/Object/administrator.php
%{peardir}/Horde/Kolab/Server/Object/adminrole.php
%{peardir}/Horde/Kolab/Server/Object/distlist.php
%{peardir}/Horde/Kolab/Server/Object/domainmaintainer.php
%{peardir}/Horde/Kolab/Server/Object/group.php
%{peardir}/Horde/Kolab/Server/Object/maintainer.php
%{peardir}/Horde/Kolab/Server/Object/server.php
%{peardir}/Horde/Kolab/Server/Object/sharedfolder.php
%{peardir}/Horde/Kolab/Server/Object/user.php
%{peardir}/Horde/Kolab/Server/ldap.php
%{peardir}/Horde/Kolab/Server/test.php
%{peardir}/Horde/Kolab/Session.php
%{peardir}/Horde/Kolab/Test/Server.php
%dir %{peardir}/tests/Kolab_Server/Horde/Kolab/Server
%dir %{peardir}/tests/Kolab_Server
%dir %{peardir}/tests/Kolab_Server/Horde
%dir %{peardir}/tests/Kolab_Server/Horde/Kolab
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/AddingObjectsTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/AdminTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/AllTests.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/DistListHandlingTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/GroupHandlingTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/GroupTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/ObjectTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/ServerTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/SessionTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/UserHandlingTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/UserTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/ldapTest.php
%{peardir}/tests/Kolab_Server/Horde/Kolab/Server/testTest.php

