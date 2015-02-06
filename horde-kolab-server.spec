%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: 	A package for manipulating the Kolab user database
Name:		horde-kolab-server
Version:		0.5.0
Release: 	11
License: 	LGPLv2.1
Group:		Networking/Mail
Source0:		http://pear.horde.org/get/Kolab_Server-%{version}.tgz
URL:		http://pear.horde.org/package/Kolab_Server
BuildRequires: 	php-pear  >= 1.4.7
BuildRequires:	php-pear-channel-horde
Requires: 	horde-auth, 
Requires:	php-pear-Net_LDAP2 
Requires:	php-pear >= 1.4.0b1
Requires:	php-pear-channel-horde
BuildArch:	noarch

%description
This package allows to read/write entries in the Kolab user
 database stored in LDAP.

%prep
%setup -c -T
pear -v -c pearrc \
        -d php_dir=%{peardir} \
        -d doc_dir=/docs \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{peardir}/data \
        -d test_dir=%{peardir}/tests \
        -d ext_dir=%{_libdir} \
        -s

%build

%install
rm -rf %{buildroot}
pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
        
# Clean up unnecessary files
rm pearrc
rm %{buildroot}/%{peardir}/.filemap
rm %{buildroot}/%{peardir}/.lock
rm -rf %{buildroot}/%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock



# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/Kolab_Server.xml

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/Kolab_Server.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/Kolab_Server
fi

%files
%defattr(-,root,root)

%{peardir}/*
%{xmldir}/Kolab_Server.xml


%changelog
* Sat Apr 14 2012 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-9mdv2012.0
+ Revision: 791020
+ rebuild (emptylog)

* Sun Feb 26 2012 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-8
+ Revision: 780940
+ rebuild (emptylog)

* Sun Feb 26 2012 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-7
+ Revision: 780774
+ rebuild (emptylog)

* Sat Feb 25 2012 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-6
+ Revision: 780757
+ rebuild (emptylog)

* Wed Dec 28 2011 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-5
+ Revision: 745833
+ rebuild (emptylog)

* Sat Dec 24 2011 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-4
+ Revision: 744944
- added %%define _requires_exceptions pear(PHPUnit/Framework.php)

* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-3mdv2011.0
+ Revision: 564074
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-2mdv2010.1
+ Revision: 523075
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Sun Feb 28 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 512771
- replaced PreReq with Requires(pre)
- removed BuildRequires: horde-framework
- import horde-kolab-server


