#
# spec file for package yast2-smt
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

Name:           yast2-mf-smt
Version:        3.1.0
Release:        0
License:        GPL-2.0
Group:          System/YaST
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-mf-smt-%{version}.tar.bz2

Prefix:         /usr

Requires:	yast2
# FATE 305541: Creating NCCcredentials file using yast2-registration
#Requires:	yast2-oes-registration
Requires:	/usr/bin/curl
Requires:	/usr/bin/grep
Requires:	/bin/hostname
# For adjusting the NCCcredentials file permissions
Requires:	/usr/bin/setfacl
Requires:	/bin/chown
Requires:	/bin/chmod
# For checking whether the DB->user is available on the system
Requires:	/usr/bin/getent
Requires:       sudo
# Modified smt-catalogs (added --batch-mode)
# SMT::Client::getPatchStatusLabel returning two values
# require smt version having SMT::Curl
Requires:	mf-smt >= 1.1.23
# Icons
Requires:	hicolor-icon-theme
# any YaST theme
#Requires:	yast2-theme-OES
# 'current'
#PreReq:		yast2-branding-OES

# This YaST tool configures SMT (cron, apache2)
Recommends:	mysql
Recommends:	cron
Recommends:	apache2
Obsoletes:      yast2-smt <= 3.0.0

# If CA is missing, SMT offers to create one
%if 0%{?sle_version} < 0150000
Recommends:	yast2-ca-management
%endif
BuildRequires:	automake perl-XML-Writer update-desktop-files yast2 yast2-devtools yast2-testsuite
BuildRequires:	hicolor-icon-theme
# any YaST theme
BuildRequires:	yast2-theme-SLE

BuildArchitectures:	noarch
Obsoletes:	yast2-smt <= 3.0.0

Summary:	Configuration of Micro Focus Subscription Management Tool for SUSE Linux Enterprise

%description
Provides the YaST module for Micro Focus SMT configuration.

%prep
%setup -n yast2-mf-smt-%{version}

%build
%yast_build

%install
%yast_install

for f in `find $RPM_BUILD_ROOT/%{prefix}/share/applications/YaST2/ -name "*.desktop"` ; do
    d=${f##*/}
    %suse_update_desktop_file -d ycc_${d%.desktop} ${d%.desktop}
done

mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps

cd $RPM_BUILD_ROOT//usr/share/YaST2/theme/current/icons
for dir in 16x16 22x22 32x32 48x48; do
    cd $RPM_BUILD_ROOT/usr/share/icons/hicolor/$dir/apps
    rm -rf yast-smt.png
    ln -s /usr/share/YaST2/theme/current/icons/$dir/apps/yast-smt.png .
done

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%dir /usr/share/YaST2/include/smt
/usr/share/YaST2/include/smt/*
/usr/share/YaST2/clients/*.rb
/usr/share/YaST2/modules/SMT*.*
%{prefix}/share/applications/YaST2/smt*.desktop
/usr/share/YaST2/scrconf/smt*.scr
%{prefix}/lib/YaST2/servers_non_y2/ag_*
%{prefix}/lib/YaST2/bin/regsrv-check-creds
%doc %{prefix}/share/doc/packages/yast2-mf-smt
%dir /usr/share/YaST2/control
/usr/share/YaST2/control/smt_control.xml

# ... and icons (again)
%dir /usr/share/YaST2/theme/current/icons
%dir /usr/share/YaST2/theme/current/icons/16x16/
%dir /usr/share/YaST2/theme/current/icons/16x16/apps/
%dir /usr/share/YaST2/theme/current/icons/22x22/
%dir /usr/share/YaST2/theme/current/icons/22x22/apps/
%dir /usr/share/YaST2/theme/current/icons/32x32/
%dir /usr/share/YaST2/theme/current/icons/32x32/apps/
%dir /usr/share/YaST2/theme/current/icons/48x48/
%dir /usr/share/YaST2/theme/current/icons/48x48/apps/

/usr/share/YaST2/theme/current/icons/16x16/apps/yast-smt.png
/usr/share/YaST2/theme/current/icons/22x22/apps/yast-smt.png
/usr/share/YaST2/theme/current/icons/32x32/apps/yast-smt.png
/usr/share/YaST2/theme/current/icons/48x48/apps/yast-smt.png

%dir /usr/share/icons/hicolor/16x16/apps/
%dir /usr/share/icons/hicolor/22x22/apps/
%dir /usr/share/icons/hicolor/32x32/apps/
%dir /usr/share/icons/hicolor/48x48/apps/

/usr/share/icons/hicolor/16x16/apps/yast-smt.png
/usr/share/icons/hicolor/22x22/apps/yast-smt.png
/usr/share/icons/hicolor/32x32/apps/yast-smt.png
/usr/share/icons/hicolor/48x48/apps/yast-smt.png

# client status icons
%dir /usr/share/icons/hicolor/16x16/status
/usr/share/icons/hicolor/16x16/status/client-*.xpm
/usr/share/icons/hicolor/16x16/status/repo-*.xpm
/usr/share/icons/hicolor/16x16/status/patch-*.xpm
