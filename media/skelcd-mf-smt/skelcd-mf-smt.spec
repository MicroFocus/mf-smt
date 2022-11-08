#
# spec file for package skelcd-smt
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           skelcd-mf-smt
BuildRequires:  recode suse-build-key zip
License:        GPL-2.0+
Group:          Metapackages
AutoReqProv:    off
Version:        2022.11.4
Release:        0.<RELEASE5>
Summary:        CD skeleton for Micro Focus SMT add on product
Conflicts:      skelcd-SUSE_Linux skelcd skelcd-SUSE_Linux-Addon skelcd-sles 
Conflicts:      skelcd-openSUSE-CD skelcd-sletc skelcd-ISSLE-Addon
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         smt-docu.tar.bz2
Source1:        micro-focus-smt-2.0-license
Source6:        autorun.sh
Source10:       autorun.inf
Source11:       SuSEgo.ico
Url:		http://www.microfocus.com
#Source12:       installation.xml
Source100:      skelcd-mf-smt-rpmlintrc
%define         build_distribution_version "SLES 15"

%description
This package contains:  

* Documentation for SMT

* autorun.sh file



%prep
%setup  -n skelcd 

%build

%install
# create needed directories first
install -d 755 $RPM_BUILD_ROOT/CD1/docu
#install -d 755 $RPM_BUILD_ROOT/CD1/license
install -d 755 $RPM_BUILD_ROOT/CD1/media.1
# now copy the sources
install docu/*       $RPM_BUILD_ROOT/CD1/docu
#install license-smt/*  $RPM_BUILD_ROOT/CD1/license

cp $RPM_SOURCE_DIR/autorun.inf $RPM_BUILD_ROOT/CD1/ 
cp $RPM_SOURCE_DIR/SuSEgo.ico $RPM_BUILD_ROOT/CD1/ 
cp $RPM_SOURCE_DIR/micro-focus-smt-2.0-license $RPM_BUILD_ROOT/CD1/
# installation.xml
%if ! 0%{?sles_version}
# be shure, that autorun.inf is in dos format:
# using unix2dos for poor:
sed -i 's/$/\r/' $RPM_BUILD_ROOT/CD1/autorun.inf
%endif
#
# adapt READMEs and License files
#
DATE_ENG=`date +"%%Y/%%m/%%d"`
BUILD_DISTRIBUTION_VERSION=%{build_distribution_version}
#for i in README ; do
# sed -e "s@DATE@$DATE_ENG@" \
#     -e "s@#VERSION#@$BUILD_DISTRIBUTION_VERSION@" $RPM_SOURCE_DIR/$i \
#    > $RPM_BUILD_ROOT/CD1/$i
#done
#
# Copy licenses
#
#for i in $RPM_BUILD_ROOT/CD1/license/license* ; do
# sed -e "s@#DATE#@$DATE_ENG@" \
#     -e "s@#VERSION#@$BUILD_DISTRIBUTION_VERSION@" $i \
#    > $i.new
#    mv $i.new $i
#done
#cd $RPM_BUILD_ROOT/CD1/license
#ls -1 > directory.yast
#tar -cvzf license.tar.gz *txt *.yast
#cp license.tar.gz $RPM_BUILD_ROOT/CD1/
# rm $RPM_BUILD_ROOT/CD1/license/license.tar.gz
#rm -rf $RPM_BUILD_ROOT/CD1/license
#
# install autorun.sh
#
cp $RPM_SOURCE_DIR/autorun.sh $RPM_BUILD_ROOT/CD1/
#
# copy gpg-keys
#
#test -s /usr/lib/rpm/gnupg/pubring.gpg || exit 1
#cp -v /usr/lib/rpm/gnupg/pubring.gpg $RPM_BUILD_ROOT/CD1/
#(cd $RPM_BUILD_ROOT/CD1 ; /usr/lib/rpm/gnupg/dumpsigs ./pubring.gpg >/dev/null 2>&1 ; /usr/lib/rpm/gnupg/dumpsigs ./pubring.gpg )

%clean 
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(644,root,root,755)
/CD1

%changelog
