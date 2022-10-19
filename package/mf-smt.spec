#
# spec file for package mf-smt
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
# (c) Copyright [2019] Micro Focus or one of its affiliates.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# Licensed under the GPLv2 License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# (https://opensource.org/licenses/GPL-2.0)

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


Name:           mf-smt
BuildRequires:  apache2
BuildRequires:  apache2-mod_perl
BuildRequires:  swig
Version:        3.0.1
Release:        0
Requires(pre):  apache2 apache2-mod_perl pwdutils
Requires:	htmldoc
Requires:       createrepo_c
Requires:       gpg2
Requires:       perl-camgm
Requires:       logrotate
Requires:       ca-certificates
Requires:       perl = %{perl_version}
Requires:       perl-Config-IniFiles
Requires:       perl-DBI
Requires:       perl-Digest-SHA1
Requires:       perl-JSON 
#Conflicts:	perl-JSON > 2.90
Requires:       perl-MIME-Lite 
Conflicts:      perl-MIME-Lite > 3.030
Requires:       perl-Text-ASCIITable 
Requires:       perl-TimeDate
Requires:       perl-URI
Requires:       perl-WWW-Curl
Requires:       perl-XML-Parser
Requires:       perl-XML-Simple
Requires:       perl-XML-Writer
Requires:       perl-XML-XPath
Requires:       perl-gettext
Requires:       perl-libwww-perl
Requires:	perl-solv
Requires:	perl-DateTime
Requires:     mariadb
Requires:     perl-DBD-mysql
Recommends:     yast2-mf-smt
Conflicts:      slms-registration
Conflicts:      mf-smt-client <= 0.0.14
Summary:        Micro Focus Subscription Management Tool
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Proxy
Source0:         %{name}-%{version}.tar.bz2
Source1:        mf-smt-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:	smt 
Conflicts:	smt-support 
obsoletes:	smt 
Obsoletes:	smt-support
Conflicts:	rmt-server
Conflicts:	rmt-server-config
Conflicts:	rmt-server-pubcloud


%description
This package provide everything you need to get a local NU and
registration proxy.



Authors:
--------
    Authors:
    --------
        dmacvicar@suse.de
        mc@suse.de
        jdsn@suse.de
        locilka@suse.cz

%package -n res-signingkeys

Summary:        Signing Key for RES
Group:          Productivity/Security
PreReq:         mf-smt = %version

%description -n res-signingkeys
This package contain the signing key for RES.



Authors:
--------
    Authors:
    --------
        dmacvicar@suse.de
        mc@suse.de
        jdsn@suse.de
        locilka@suse.cz

%package support

Summary:        Micro Focus SMT support proxy
Group:          Productivity/Networking/Web/Proxy
PreReq:         mf-smt = %version

%description support
This package contains proxy for Novell Support Link



Authors:
--------
    Authors:
    --------
        dmacvicar@suse.de
        mc@suse.de
        jdsn@suse.de
        locilka@suse.cz

%prep
%setup -n %{name}-%{version}
# ---------------------------------------------------------------------------

%build
make
mkdir man
cd script

#processes *.pod twice, but this way they are processed after the real scripts and their data does not get rewritten
for prog in smt* smt*.pod; do
    progfile=`echo "$prog" | sed 's/\(.*\)\.pod/\1/'`
    if pod2man --center=" " --release="%{version}-%{release}" --date="$(date)" $prog > $prog.$$$$ ; then
        perl -p -e 's/.if n .na/.\\\".if n .na/;' $prog.$$$$ > ../man/$progfile.1;
    fi
    rm -f $prog.$$$$
done
rm smt*.pod #don't package .pod-files
# BNC #511168 (smt-catalogs is a symlink to smt-repos)
ln -s smt-repos.1 ../man/smt-catalogs.1
cd -
progfile="SMT::RESTService"
if pod2man --center=" " --release="%{version}-%{release}" --date="$(date)" www/perl-lib/SMT/RESTService.pm > www/perl-lib/SMT/RESTService.pm.$$$$ ; then
    perl -p -e 's/.if n .na/.\\\".if n .na/;' www/perl-lib/SMT/RESTService.pm.$$$$ > man/$progfile.3pm;
fi
rm -f www/perl-lib/SMT/RESTService.pm.$$$$
#make test
# ---------------------------------------------------------------------------

%install

/usr/sbin/useradd -r -g www -s /bin/false -c "User for SMT" -d /var/lib/empty smt 2> /dev/null || :
/usr/sbin/usermod -a -G wwwrun smt 2> /dev/null || :

make DESTDIR=$RPM_BUILD_ROOT DOCDIR=%{_docdir} install
make DESTDIR=$RPM_BUILD_ROOT install_conf

#ln -sf service %{buildroot}/%{_sbindir}/rcsmt

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
cd man
for manp in smt*.1; do
    install -m 644 $manp    $RPM_BUILD_ROOT%{_mandir}/man1/$manp
done
for manp in *.3pm; do
    install -m 644 $manp    $RPM_BUILD_ROOT%{_mandir}/man3/$manp
done
mkdir -p $RPM_BUILD_ROOT/var/run/smt
mkdir -p $RPM_BUILD_ROOT/var/log/smt/schema-upgrade
mkdir -p $RPM_BUILD_ROOT%{_docdir}/smt/
mkdir -p $RPM_BUILD_ROOT/var/lib/smt

ln -s /srv/www/htdocs/repo/tools/clientSetup4SMT.sh $RPM_BUILD_ROOT%{_docdir}/smt/clientSetup4SMT.sh

# ---------------------------------------------------------------------------

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%pre
if ! /usr/bin/getent passwd smt >/dev/null; then
  /usr/sbin/useradd -r -g www -s /bin/false -c "User for SMT" -d /var/lib/smt smt 2> /dev/null || :
fi
/usr/sbin/usermod -a -G wwwrun smt 2> /dev/null || :

%post
sysconf_addword /etc/sysconfig/apache2 APACHE_MODULES perl
sysconf_addword /etc/sysconfig/apache2 APACHE_SERVER_FLAGS SSL
#usr/bin/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
echo "d /var/run/smt 755 smt www" > /usr/lib/tmpfiles.d/mf-smt.conf

%preun
%service_del_preun smt-schema-upgrade.service
%service_del_preun smt.service
%service_del_preun smt.target

# no postun service handling for target or schema-upgrade, we don't want them to be restarted on upgrade
%postun

%service_del_postun smt.service


%files
%defattr(-,root,root)
%dir %{perl_vendorlib}/SMT/
%dir %{perl_vendorlib}/SMT/Job
%dir %{perl_vendorlib}/SMT/Utils
%dir %{perl_vendorlib}/SMT/Mirror
%dir %{perl_vendorlib}/SMT/Parser
%dir %{perl_vendorlib}/SMT/Rest
%dir %{perl_vendorarch}/Sys
%dir %{perl_vendorarch}/auto/Sys/
%dir %{perl_vendorarch}/auto/Sys/GRP
%dir /etc/smt.d
%dir /etc/slp.reg.d
%dir %attr(755, smt, www)/srv/www/htdocs/repo/
%dir %attr(755, smt, www)/srv/www/htdocs/repo/tools
%dir %attr(755, smt, www)/srv/www/htdocs/repo/keys
%dir %attr(755, smt, www)/srv/www/htdocs/repo/testing
%dir %attr(755, smt, www)/srv/www/htdocs/repo/full
%dir /srv/www/perl-lib/NU/
%dir /srv/www/perl-lib/SMT/
%dir /srv/www/perl-lib/SMT/Client
%dir /usr/lib/SMT/
%dir /usr/lib/SMT/bin/
%dir %{_datadir}/schemas/
%dir %{_datadir}/schemas/smt
%dir %{_docdir}/smt/
%dir %attr(755, smt, www)/var/run/smt
%dir %attr(755, smt, www)/var/log/smt
%dir %attr(755, smt, www)/var/log/smt/schema-upgrade
%dir %attr(755, smt, www)/var/lib/smt
%config(noreplace) %attr(640, root, www)/etc/smt.conf
%config /etc/apache2/*.pl
%config /etc/apache2/conf.d/*.conf
%config (noreplace) /etc/apache2/vhosts.d/vhost-ssl.conf
%config /etc/smt.d/*.conf
%config /etc/slp.reg.d/smt.reg
%exclude /etc/apache2/conf.d/smt_support.conf
%config /etc/cron.d/novell.com-smt
%config /etc/logrotate.d/smt
%{perl_vendorlib}/SMT.pm
%{perl_vendorlib}/SMT/*.pm
%{perl_vendorlib}/SMT/Job/*.pm
%{perl_vendorlib}/SMT/Utils/*.pm
%{perl_vendorlib}/SMT/Mirror/*.pm
%{perl_vendorlib}/SMT/Parser/*.pm
%{perl_vendorlib}/SMT/Rest/*.pm
%{perl_vendorarch}/Sys/*.pm
%{perl_vendorarch}/auto/Sys/GRP/*.so
/srv/www/perl-lib/NU/*.pm
/srv/www/perl-lib/SMT/*.pm
/srv/www/perl-lib/SMT/Client/*.pm
%exclude /srv/www/perl-lib/SMT/Support.pm
/usr/sbin/smt-*
#/usr/sbin/rcsmt
%exclude /usr/sbin/smt-support
/usr/sbin/smt
/usr/lib/SMT/bin/*
/usr/bin/smt*
%{_libexecdir}/systemd/system/smt.service
%{_libexecdir}/systemd/system/smt-schema-upgrade.service
/srv/www/htdocs/repo/tools/*
%{_datadir}/schemas/smt/*
/usr/bin/smt-*
%attr(644, root, root) /usr/lib/systemd/system/smt.target
%doc %attr(644, root, root) %{_mandir}/man3/*
%doc %attr(644, root, root) %{_mandir}/man1/*
%exclude %{_mandir}/man1/smt-support.1.gz
%doc %{_docdir}/smt/*

%files -n res-signingkeys
%defattr(-,root,root)
%dir %attr(755, smt, www)/srv/www/htdocs/repo/keys
/srv/www/htdocs/repo/keys/res-signingkeys.key

%files support
%defattr(-,root,root)
/usr/sbin/smt-support
/srv/www/perl-lib/SMT/Support.pm
%config /etc/apache2/conf.d/smt_support.conf
%dir %attr(775, smt, www)/var/spool/smt-support
%doc %attr(644, root, root) %{_mandir}/man1/smt-support.1.gz

%changelog
